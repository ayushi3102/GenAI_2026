from google import genai
from dotenv import load_dotenv
import os

load_dotenv() # This will load the .env in out environment
my_api_key = os.getenv("GEMINI_API_KEY")

if my_api_key is None:
    print("API key not found!")
else:
    client = genai.Client(api_key="")
    resp = client.models.generate_content(
    model ="gemini-3.5-flash",
    contents = "What is capital of India "
    )
    print(resp.text)