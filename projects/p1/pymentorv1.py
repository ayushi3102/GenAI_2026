from google import genai
from dotenv import load_dotenv

def get_gemini_api_key():
    load_dotenv() # This will load the .env in out environment
    client = genai.Client() 
    return client

def chat_with_ai(question):
    
    resp = client.models.generate_content(model ="gemini-2.5-flash",contents = question)
    print("AI:",resp.text)

try:
    client = get_gemini_api_key()
    while True:
        question = input(" YOU:")
        if question.lower() == 'exit':
            break
        chat_with_ai(question)
except Exception as ex:
    print("Error",ex)
