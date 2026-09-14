from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # This will load the .env in out environment

client = OpenAI()  # OpeniAI says if you keep api key name as OPENAI_API_KEY in env, then you don't need to call it explicity
resp =client.responses.create(model="gpt-5.1",input = "Hello I am Ayushi. What about u ?")
print(resp.output_text)