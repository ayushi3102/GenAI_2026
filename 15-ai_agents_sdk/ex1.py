from google import genai
from datetime import datetime
from dotenv import load_dotenv

def get_gemini_ai_client():
    load_dotenv()
    client = genai.Client()
    return client




def get_current_time():
    print("Tool called...")
    """
        Returns the current date and time
    """
    return datetime.now().strftime("%d %B %Y, %I:%M:%S %p")

client = get_gemini_ai_client()

user_ques = input("Question : ")
response = client.models.generate_content(
    model ='gemini-2.5-flash',
    contents = user_ques,
    config={'tools':[get_current_time]}
)

print("\n Agent Response",response.text)


#agent_sdk - gemini we have used now 
#responses api - openai is being used till previous examples,but from next example we will use aget sdk of openai.