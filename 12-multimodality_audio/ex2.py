from openai import OpenAI
from dotenv import load_dotenv

def get_openai_client():
    load_dotenv()
    client = OpenAI()
    return client

def translate_audio(audio_path):
    
    with open(audio_path,'rb') as audio_file:
        response = client.audio.transcriptions.create(
        model='whisper-1',
        file = audio_file,
        language='en',
        prompt = 'it is about myself',
        response_format = 'srt',
        temperature = 1.2
        )
        return response.text

client =  get_openai_client()
audio_path = input("Enter your path:")
translated_audio= translate_audio(audio_path)
print(translated_audio)
