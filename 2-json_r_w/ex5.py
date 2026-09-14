import json


with open("data.json","r") as file_obj:
    messages = json.load(file_obj)
print(type(messages),messages)