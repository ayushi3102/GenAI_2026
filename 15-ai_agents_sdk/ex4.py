from agents import Agent,Runner,function_tool
from dotenv import load_dotenv

load_dotenv()

@function_tool
def get_course_fee(course_name : str)->str:   # -> tells return type
    """
    Return the fee for a course.
    """
    courses={
        'mern':'Rs35000',
        'java':'Rs30000',
        'python':'Rs28000',
    }

    return courses.get(course_name,'course not found')

agent = Agent(name = 'shopkeeper',
instructions = "you are shopkeeper who sell his products",
tools=[get_course_fee])

user_ques = input("Enter your question : ")
result = Runner.run_sync(agent,user_ques)
print("\nAgent response :",result.final_output)