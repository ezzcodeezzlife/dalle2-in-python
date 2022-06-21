import requests
import json
import time 
import urllib
import urllib.request
import os

class Dalle2():
    def __init__(self, bearer):
        self.bearer = bearer

    def generate(self, promt):
        url = "https://labs.openai.com/api/labs/tasks"
        headers = {
            'Authorization': "Bearer " + self.bearer,
            'Content-Type': "application/json"
        }
        body = {
            "task_type": "text2im",
            "prompt": {
                "caption": promt,
                "batch_size": 6,
            }
        }

        response = requests.post(url, headers=headers, data=json.dumps(body))
        if response.status_code != 200:
            print(response.text)
            return None
        data = response.json()
        print("✔️  Task created with ID:", data["id"], "and PROMT:", promt)
        print("⌛ Waiting for task to finish .. ")

        while True:
            url = "https://labs.openai.com/api/labs/tasks/" + data["id"]
            response = requests.get(url, headers=headers)
            data = response.json()
            if data["status"] == "succeeded":
                print("🙌 Task completed!")
                generations = data["generations"]["data"]
                return(generations)
            else:
                # print("Task not completed yet")
                time.sleep(3)
                continue

    def generate_and_download(self, promt):
        generations = self.generate(promt)
        if generations is None:
            return None
        
        print("Download to directory: " + os.getcwd())
        #print(generations)
        for generation in generations:
            imageurl = generation["generation"]["image_path"]
            id = generation["id"]

            urllib.request.urlretrieve(imageurl, id +".jpg")
            print("✔️  Downloaded: " , id + ".jpg")
        

            
