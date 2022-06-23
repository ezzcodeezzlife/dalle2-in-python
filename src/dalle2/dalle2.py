from tokenize import String
import requests
import json
import time 
import urllib
import urllib.request
import os

class Dalle2():
    def __init__(self, bearer):
        self.bearer = bearer
        self.batch_size = 6

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
                "batch_size": self.batch_size,
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
            print("✔️ Downloaded: " , id + ".jpg")

    def generate_amount(self, promt, amount):
        url = "https://labs.openai.com/api/labs/tasks"
        headers = {
            'Authorization': "Bearer " + self.bearer,
            'Content-Type': "application/json"
        }
        body = {
            "task_type": "text2im",
            "prompt": {
                "caption": promt,
                "batch_size": self.batch_size,
            }
        }
        
        
        all_generations = []
        for i in range(1,int(amount / self.batch_size +1)):
            url = "https://labs.openai.com/api/labs/tasks"
            response = requests.post(url, headers=headers, data=json.dumps(body))
            if response.status_code != 200:
                print(response.text)
                return None
            data = response.json()
            print("✔️ Task created with ID:", data["id"], "and PROMT:", promt, "OVERALL:" , str(i)  + "/" , int(amount / self.batch_size ))
            print("⌛ Waiting for task to finish .. ")

            while True:
                url = "https://labs.openai.com/api/labs/tasks/" + data["id"]
                response = requests.get(url, headers=headers)
                data = response.json()
                if data["status"] == "succeeded":
                    
                    generations = data["generations"]["data"]
                    print("➕ Appended new generations to all_generations")
                    all_generations.append(generations)
                    break
                else:
                    # print("Task not completed yet")
                    time.sleep(3)
                    continue
        print("🙌 Task completed!")
        print(all_generations)
        return all_generations