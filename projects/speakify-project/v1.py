from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

def get_openai_api_key():
    load_dotenv() # This will load the .env in out environment
    client = OpenAI()  # OpenAI says if you keep api key name as OPENAI_API_KEY in env, then you don't need to call it explicity
    return client

def transcribe_audio(audio_path):
    
    with open(audio_path,'rb') as audio_file:
        response = client.audio.transcriptions.create(
        model='gpt-4o-transcribe',
        file = audio_file)
        return response.text

def get_ai_response(user_text):
    res = client.responses.create(model="gpt-4o-mini",input=[
        {"role":"system",
        "content" : "You are helpful assistants"},
        {"role":"user",
        "content" : user_text
        },
    ])
    return res.output_text

def convert_text_to_audio(ai_reply):
    res= client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=ai_reply)
    audio_bytes = res.read()
    audio_file_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"/audio/{audio_file_name}.mp3",'wb') as f:
        f.write(audio_bytes)
    print(f"Audio saved as audio/{audio_file_name}.mp3")


client = get_openai_api_key()
print("AI voice assistant")
print("Type exit to quit")
os.makedirs('/audio',exist_ok=True)

while True:
    audio_path=input("Audio file path:").strip()
    if(audio_path =='exit'):
        break
    if not os.path.exists(audio_path):
        print("Audio file not found")
        continue
    try:
        print("\n Transcribing...")
        user_text = transcribe_audio(audio_path)
        print("\n Thinking...")
        ai_reply = get_ai_response(user_text)
        print(f"\n AI reply :{ ai_reply}")
        print("\n Converting to audio")
        convert_text_to_audio(ai_reply)
    except Exception as ex:
        print("Error",ex)
        







