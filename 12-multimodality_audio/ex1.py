from openai import OpenAI
from dotenv import load_dotenv

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
        prompt = 'it is about myself',
        response_format = 'srt',
        temperature = 1.2
        )
        return response.text

client =  get_openai_client()
audio_path = input("Enter your path:")
transcribed_audio= transcribe_audio(audio_path)
print(transcribed_audio)
