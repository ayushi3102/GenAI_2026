import json

person = {"name":"ayushi","age":34}
with open("data.json","w") as file_obj:
    json.dump(person,file_obj)
print("Data saved")