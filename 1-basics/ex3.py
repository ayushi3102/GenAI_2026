from google import genai
from dotenv import load_dotenv

load_dotenv() # This will load the .env in out environment

client = genai.Client() # Gemini says if you keep api key name as GEMINI_API_KEY in env, then you don't need to call it explicity
resp = client.models.generate_content(
    model ="gemini-3.5-flash",
    contents = "Upto till data you are trained ?"
)
print(resp.text)