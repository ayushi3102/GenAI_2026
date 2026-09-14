from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client = OpenAI()
    return client

client = get_open_ai_client()

def get_current_time():
    print("Tool called...")
    """
        Returns the current date and time
    """
    return datetime.now().strftime("%d %B %Y, %I:%M:%S %p")

tools =[
    {
        "type":"function",
        "name":"get_current_time",
        "description":"Returns the current date and time",
        "parameters":{
            "type":"object",
            "properties":{},
            "required":[],
            "additionalProperties":False
        },
        "strict":True
    }]

system_prompt = "You are helpful assistant. Use the get_current_time toom wheneever user asks for the current date or time."

user_ques = input("Question : ")
response = client.responses.create(
    model='gpt-5-mini',
    instructions = system_prompt,
    input=user_ques,
    tools=tools
)

for item in response.output:
    if item.type == 'function_call':
        tool_name = item.name
        if tool_name == 'get_current_time':
            result = get_current_time()
            tool_output = {
                'type':"fucntion_call_output",
                "call_id":item.call_id,
                "output":result
            }
            response = client.responses.create(model='gpt-5-mini',
            input = tool_output,
            previous_response_id=response.id,
            tools=tools
            )

print("\n Agent Response",response.output_text)