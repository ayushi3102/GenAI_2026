from openai import OpenAI
from dotenv import load_dotenv
import json
import os


def get_openai_api_key():
    load_dotenv() # This will load the .env in out environment
    client = OpenAI()  # OpenAI says if you keep api key name as OPENAI_API_KEY in env, then you don't need to call it explicity
    return client

def chat_with_ai(question):
    stream = client.responses.create(model="gpt-5.1",input = question,stream=True)

    for event in stream:
        if event.type == 'response.output_text.delta':
            print(event.delta,end="")

try:
    client = get_openai_api_key()
    
    while True:
        
        question = input("YOU:")
        if question.lower() == 'exit':
            break
        
        chat_with_ai(question)
        
        
except Exception as ex:
    print("Error",ex)
