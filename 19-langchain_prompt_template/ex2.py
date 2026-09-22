from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
prompt = PromptTemplate.from_template("Write  a {adjective} summary of {topic} in {language}")
formatted_prompt = prompt.format(adjective = 'short',
              topic='GENAI',
              language ='english')

print(formatted_prompt)

llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
res = llm.invoke(formatted_prompt)
print(res.content)