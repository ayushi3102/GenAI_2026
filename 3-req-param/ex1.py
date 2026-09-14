from openai import OpenAI
from dotenv import load_dotenv
import json
import os

CHAT_FILE= "chat_histort.json"

def save_chat_history(messages):
    with open(CHAT_FILE,"w") as file_obj:
        json.dump(messages,file_obj)
    
def load_chat_history():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE,"r") as file_obj:
          return json.load(file_obj),False
    else :
        messages = [{"role":"system",
        "content":("You are a helpful python tutor."
        "Please answer questions related to python only in a concise way."
        "For any other questions do not answer and give a polite reply."
          )}]
        return messages,True
    
def get_openai_api_key():
    load_dotenv() # This will load the .env in out environment
    client = OpenAI()  # OpenAI says if you keep api key name as OPENAI_API_KEY in env, then you don't need to call it explicity
    return client

def chat_with_ai(messages,temp):
    resp = client.responses.create(model="gpt-5.1",input = messages,temperature = temp)
    return resp

try:
    client = get_openai_api_key()
    messages,is_new = load_chat_history()
    if is_new:
            print("Welcome to pyMentor!")
            print("You can ask any question to me")
            print("Type 'exit' to quit")
    else:
            print("Chat resumed! Type 'exit' to quit")
    while True:
        
        question = input("YOU:")
        if question.lower() == 'exit':
            save_chat_history(messages)
            break
        messages.append({"role":"user","content":question})
        ai_response = chat_with_ai(messages,0.2)
        messages.append({"role":"model","content":ai_response.output_text})
        print("AI:",ai_response.output_text)
except Exception as ex:
    print("Error",ex)
