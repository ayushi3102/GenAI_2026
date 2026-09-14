from openai import OpenAI
from dotenv import load_dotenv
import base64 
import os

def get_openai_client():
    load_dotenv()
    client = OpenAI()
    return client

client = get_openai_client()
result = client.images.generate(
    model = "gpt-image-1",
    prompt = "A cute smiling baby",
    size="1024X1024",
    n=3)

os.makedirs("generated",exist_ok=True)
for idx,img in enumerate(result.data):
    img_b64 = img.b64_json
    img_bytes = base64.b64decode(img_b64)
    with open(f"generated/baby{idx}.png","wb") as f:
        f.write(img_bytes)
print("Image saved!")