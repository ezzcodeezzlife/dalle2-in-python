import base64
import json
import math
import os
import requests
import time
import urllib
import urllib.request

from pathlib import Path

class Dalle2():
    def __init__(self, bearer):
        self.bearer = bearer
        self.batch_size = 4
        self.inpainting_batch_size = 3
        self.task_sleep_seconds = 3

    def generate(self, prompt):
        body = {
            "task_type": "text2im",
            "prompt": {
                "caption": prompt,
                "batch_size": self.batch_size,
            }
        }

        return self.get_task_response(body)

    def generate_and_download(self, prompt, image_dir=os.getcwd()):
        generations = self.generate(prompt)
        if not generations:
            return None

        return self.download(generations, image_dir)

    def generate_amount(self, prompt, amount):
        if amount < self.batch_size:
            raise ValueError(f"passed amount of {amount} cannot be smaller than the batch size of {self.batch_size}")

        return [self.generate(prompt) for _ in range(math.ceil(amount / self.batch_size))]

    def generate_from_masked_image(self, prompt, image_path):
        with open(image_path, "rb") as f:
            image_base64 = base64.b64encode(f.read())

        body = {
            "task_type": "inpainting",
            "prompt": {
                "caption": prompt,
                "batch_size": self.inpainting_batch_size,
                "image": image_base64.decode(),
                "masked_image": image_base64.decode(), # identical since already masked
            }
        }

        return self.get_task_response(body)

    def get_task_response(self, body):
        url = "https://labs.openai.com/api/labs/tasks"
        headers = {
            'Authorization': "Bearer " + self.bearer,
            'Content-Type': "application/json",
        }

        response = requests.post(url, headers=headers, data=json.dumps(body))
        if response.status_code != 200:
            print(response.text)
            return None
        data = response.json()
        print(f"✔️ Task created with ID: {data['id']}")
        print("⌛ Waiting for task to finish...")

        while True:
            url = f"https://labs.openai.com/api/labs/tasks/{data['id']}"
            response = requests.get(url, headers=headers)
            data = response.json()

            if not response.ok:
                print(f"Request failed with status: {response.status_code}, data: {response.json()}")
                return None
            if data["status"] == "failed":
                print(f"Task failed: {data['status_information']}")
                return None
            if data["status"] == "succeeded":
                print("🙌 Task completed!")
                return data["generations"]["data"]

            print("...task not completed yet")
            time.sleep(self.task_sleep_seconds)

    def download(self, generations, image_dir=os.getcwd()):
        if not generations:
            raise ValueError("generations is empty!")

        file_paths = []
        for generation in generations:
            image_url = generation["generation"]["image_path"]
            file_path = Path(image_dir, generation['id']).with_suffix('.png')
            file_paths.append(str(file_path))
            urllib.request.urlretrieve(image_url, file_path)
            print(f"✔️ Downloaded: {file_path}")

        return file_paths
