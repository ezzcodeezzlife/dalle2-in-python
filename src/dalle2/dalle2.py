import json
import os
import requests
import time
import urllib
import urllib.request

class Dalle2():
    def __init__(self, bearer):
        self.bearer = bearer
        self.batch_size = 4

    def generate(self, prompt):
        url = "https://labs.openai.com/api/labs/tasks"
        headers = {
            'Authorization': "Bearer " + self.bearer,
            'Content-Type': "application/json",
        }
        body = {
            "task_type": "text2im",
            "prompt": {
                "caption": prompt,
                "batch_size": self.batch_size,
            }
        }

        response = requests.post(url, headers=headers, data=json.dumps(body))
        if response.status_code != 200:
            print(response.text)
            return None
        data = response.json()
        print("✔️  Task created with ID:", data["id"], "and PROMPT:", prompt)
        print("⌛ Waiting for task to finish...")

        while True:
            url = "https://labs.openai.com/api/labs/tasks/" + data["id"]
            response = requests.get(url, headers=headers)
            data = response.json()
            if data["status"] == "succeeded":
                print("🙌 Task completed!")
                generations = data["generations"]["data"]
                return generations

            time.sleep(3)

    def generate_and_download(self, prompt):
        generations = self.generate(prompt)
        if not generations:
            return None

        print("Download to directory: " + os.getcwd())
        for generation in generations:
            image_url = generation["generation"]["image_path"]
            image_id = generation["id"]

            urllib.request.urlretrieve(image_url, image_id +".jpg")
            print("✔️ Downloaded: ", image_id + ".jpg")

        return generations

    def generate_amount(self, prompt, amount):
        url = "https://labs.openai.com/api/labs/tasks"
        headers = {
            'Authorization': "Bearer " + self.bearer,
            'Content-Type': "application/json",
        }
        body = {
            "task_type": "text2im",
            "prompt": {
                "caption": prompt,
                "batch_size": self.batch_size,
            }
        }

        all_generations = []
        for i in range(1, int(amount / self.batch_size +1)):
            url = "https://labs.openai.com/api/labs/tasks"
            response = requests.post(url, headers=headers, data=json.dumps(body))
            if response.status_code != 200:
                print(response.text)
                return None
            data = response.json()
            print("✔️ Task created with ID:", data["id"], "and PROMPT:", prompt, "OVERALL:", str(i) + "/", int(amount / self.batch_size))
            print("⌛ Waiting for task to finish...")

            while True:
                url = "https://labs.openai.com/api/labs/tasks/" + data["id"]
                response = requests.get(url, headers=headers)
                data = response.json()
                if data["status"] == "succeeded":
                    generations = data["generations"]["data"]
                    print("➕ Appended new generations to all_generations")
                    all_generations.append(generations)
                    break

                time.sleep(3)
        print("🙌 Task completed!")
        print(all_generations)
        return all_generations
