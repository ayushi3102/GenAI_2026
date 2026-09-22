from langchain_core.prompts import ChatPromptTemplate,PromptTemplate,FewShotChatMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()



examples = [{'input':'Hello friend','output':'hola amigo'},
            {'input':'my name is ayushi','output':'mi nombra es Sachin'}]

example_prompt = ChatPromptTemplate.from_messages([
    ('human',"{input}"),
    ('ai',"{output}")
])

user_input = input("Type a sentence : ") 
target = input("Enter the target language : ") 
few_shot_prompt = FewShotChatMessagePromptTemplate(examples=examples,example_prompt=example_prompt)

final_prompt = ChatPromptTemplate.from_messages([('system',f'you translate english to {target}'),few_shot_prompt,('human',"{input}")])



message = final_prompt.format(input = user_input)

llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
response = llm.invoke(message)
print(response.content)