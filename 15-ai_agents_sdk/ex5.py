from agents import Agent,Runner,function_tool
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

@function_tool
def get_current_time():
    print("get_current_time()Tool called...")
    """
        Returns the current date and time
    """
    return datetime.now().strftime("%d %B %Y, %I:%M:%S %p")

@function_tool
def get_weather(city:str)->str:           #city:str --> type annotation
    print("get_weather(city:str) Tool called...")
    """
        Returns the current weather from the city.
        Args:
            city
    """
    weather_data={'delhi':'25 Sunny','mumbai':'30 humid'}

    return weather_data.get(city,'details not found')


agent = Agent(name = 'My asistant',
instructions = "you are helpful agent. use tools whenever necessary",
tools=[get_current_time,get_weather])

user_ques = input("Enter your question : ")
result = Runner.run_sync(agent,user_ques)
print("\nAgent response :",result.final_output)