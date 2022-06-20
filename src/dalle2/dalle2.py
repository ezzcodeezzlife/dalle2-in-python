import requests
import json
import time 

class Dalle2():
    def __init__(self, bearer):
        self.bearer = bearer

    def generate(self, promt):
        # make post request to https://labs.openai.com/api/labs/tasks with header: authorization: "Bearer asdasdasdas" and data: data: { task_type: "text2im", prompt: {caption: promt,batch_size: 6,},}
        url = "https://labs.openai.com/api/labs/tasks"
        headers = {
            'Authorization': "Bearer " + self.bearer,
            'Content-Type': "application/json"
        }
        body = {
            "task_type": "text2im",
            "prompt": {
                "caption": promt,
                "batch_size": 10,
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
            
