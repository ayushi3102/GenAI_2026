from google import genai
from dotenv import load_dotenv
from google.genai import types

SYSTEM_PROMPT = "You are a helpful python tutor. Please answer questions related to python only in a concise way. For any other questions do not answer and give a polite reply"

def get_gemini_api_key():
    load_dotenv() # This will load the .env in our environment
    client = genai.Client() 
    return client

def chat_with_ai(content_list):
    
    resp = client.models.generate_content(model ="gemini-2.5-flash",
    config = types.GenerateContentConfig(system_instruction =  SYSTEM_PROMPT),
    contents = content_list)
    return resp.text

try:
    client = get_gemini_api_key()
    content_list=[]
    print("I am python tutor.You can ask anything to me ")
    while True:
        user_input = input("YOU:")
        if user_input.lower() == 'exit':
            break
        content_list.append(types.Content(role="user",parts=[types.Part(text = user_input)]))

        ai_reply = chat_with_ai(content_list)
        content_list.append(types.Content(role="model",parts=[types.Part(text = ai_reply)]))
        print("AI:",ai_reply)
except Exception as ex:
    print("Error",ex)
