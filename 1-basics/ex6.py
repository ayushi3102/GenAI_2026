from openai import OpenAI
from dotenv import load_dotenv

def get_openai_api_key():
    load_dotenv() # This will load the .env in out environment
    client = OpenAI()  # OpenAI says if you keep api key name as OPENAI_API_KEY in env, then you don't need to call it explicity
    return client

def chat_with_ai():
    resp =client.responses.create(model="gpt-5.1",input = "Hello I am Ayushi. What about u ?")
    print(resp.output_text)

try:
    client = get_openai_api_key()
    chat_with_ai()
except Exception as ex:
    print("Error",ex)