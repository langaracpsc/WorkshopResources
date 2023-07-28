import json
import requests

"""
'{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
"""

key = "Bearer YOUR_TOKEN"

url = "https://api.openai.com/v1/chat/completions"

def getContentFromResponse(response):
    choices = response["choices"]

    choice = choices[0]

    message = choice["message"]

    return message["content"]

def Prompt(prompt):
    requestObject = {
        "model": "gpt-3.5-turbo",
        "messages": [
        {
            "role": "user",
            "content": prompt
        }
        ]
    }

    requestObjectJson = json.dumps(requestObject)

    response = requests.post(url, headers={"Content-Type": "application/json", 
                                "Authorization": key},
                                data=requestObjectJson)


    return getContentFromResponse(response.json())

def Run():
    running = True
    while (running):
        inp = input("Your prompt: ")

        if (inp.lstrip() == "end"):
            running = False
            break

        print(f"AI: {Prompt(inp)}")

Run()
