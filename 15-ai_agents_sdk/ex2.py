#using openai-agents sdk
from agents import Agent,Runner,function_tool
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

@function_tool
def get_current_time():
    print("Tool called...")
    """
        Returns the current date and time
    """
    return datetime.now().strftime("%d %B %Y, %I:%M:%S %p")




agent = Agent(
    name = "My assistant",
    instructions = "you are helpful assistant",
    tools=[get_current_time]
    )

user_ques = input("Question : ")
response = Runner.run_sync(agent,user_ques)


print("\n Agent Response",response.final_output)