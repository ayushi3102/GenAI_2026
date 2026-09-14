from openai import OpenAI
from dotenv import load_dotenv
import os

def get_openai_client():
    load_dotenv()
    client = OpenAI()
    return client

def transcribe_audio(audio_path):
    
    with open(audio_path,'rb') as audio_file:
        response = client.audio.transcriptions.create(
        model='gpt-4o-transcribe',
        file = audio_file,
        language='en',
        )
        return response.text
def chat_with_ai(transcribed_text,question):
    response = responses.create(model="gpt-4o-mini",input=[
        {
            "role":"user",
            "content":f"Here is the transcribe audio:{transcribed_text} User question:{question}"
        }
        
    ])
    return response.output_text



client =  get_openai_client()
audio_path = input("Enter your audio file path:").strip()
if not os.path.exists(audio_path):
    print("Audio file not found")
else:
    transcribe_text = transcribe_audio(audio_path)
    print("Type exit to quit")
    while True:
        question = input("Enter your question:").strip()
        if question == "exit":
            break
        else:
            ans = chat_with_ai(transcribe_text,question)
            print(f"\n AI:{ans}")


print("Type exit to quit")


transcribed_audio= transcribe_audio(audio_path)
print(transcribed_audio)
