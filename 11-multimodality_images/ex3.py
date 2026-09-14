from openai import OpenAI
from dotenv import load_dotenv
import base64 


def get_openai_client():
    load_dotenv()
    client = OpenAI()
    return client



def encode_image(image_path):
    with open(image_path,"rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def chat_with_ai(image_path,user_ques):
    img_b64 = encode_image(image_path)
    response = client.responses.create(
        model="gpt-4.1",
        input = [
            {
                'role':'user',
                'content':[{
                    'type':'input_text',
                    'text':user_ques
                    },
                    {
                    'type':'input_image',
                    'image_url':f"data:image/jpg;base64,{img_b64}"
                    }
                    ]
            }
        ])
    return response.output_text

client = get_openai_client()
image_path = input("Enter image path:")
user_question = input("Type your question:")
ai_reply=chat_with_ai(image_path,user_question)
print("\nResponse")
print(ai_reply)




