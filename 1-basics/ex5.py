from google import genai
from dotenv import load_dotenv

def get_gemini_api_key():
    load_dotenv() # This will load the .env in out environment
    client = genai.Client() # Gemini says if you keep api key name as GEMINI_API_KEY in env, then you don't need to call it explicity
    return client

def chat_with_ai():
    
    resp = client.models.generate_content(model ="gemini-3.5-flash",contents = "who is the cm of up ?")
    print(resp.text)

client = get_gemini_api_key()
chat_with_ai()


