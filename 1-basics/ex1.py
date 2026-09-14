from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() #this will load the .env in out environment
my_api_key = os.getenv("OPENAI_API_KEY")

if my_api_key is None:
    print("API key not found!")
else:
    client = OpenAI(api_key = my_api_key)
    resp =client.responses.create(model="gpt-5.1",input = "Hello I am Ayushi. What about u ?")
    print(resp.output_text)