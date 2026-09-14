from openai import OpenAI
from dotenv import load_dotenv

def get_openai_client():
    load_dotenv()
    client = OpenAI()
    return client


client =  get_openai_client()
response = client.audio.speech.create(model="gpt-4o-mini-tts",voice="marin",input="HEllo everyone welcome to the generative ai class")
os.makedirs("audio",exists=True)
audio_bytes= response.read()
with open("audio/output.mp3","wb") as f:
    f.write(audio_bytes)

print("Audio saved as audio/output.mp3")
