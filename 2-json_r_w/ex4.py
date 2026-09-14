import json

messages = [{"role":"user","content":"what is for loop"},
{"role":"assistant","content":"for loop is popular way of interating."}
]
with open("data.json","w") as file_obj:
    json.dump(messages,file_obj)
print("Data saved!")