from openai import OpenAI
from dotenv import load_dotenv

def get_openai_api_key():
    load_dotenv() # This will load the .env in out environment
    client = OpenAI()  # OpenAI says if you keep api key name as OPENAI_API_KEY in env, then you don't need to call it explicity
    return client

def chat_with_ai(messages):
    resp = client.responses.create(model="gpt-5.1",input = messages)
    return resp

try:
    client = get_openai_api_key()
    messages = [{"role":"system","content":"You are a helpful python tutor. Please answer questions related to python only in a concise way. For any other questions do not answer and give a polite reply."}]
    while True:
        question = input("YOU:")
        if question.lower() == 'exit':
            break
        messages.append({"role":"user","content":question})
        ai_response = chat_with_ai(messages)
        messages.append({"role":"model","content":ai_response.output_text})
        print("AI:",ai_response.output_text)
except Exception as ex:
    print("Error",ex)
