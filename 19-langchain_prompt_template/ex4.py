from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
prompt = ChatPromptTemplate.from_messages([('system','you are helpful assistant'),
                                           ('human','Explain {topic} in simple terms')
                                           ])
message = prompt.format_messages(topic= 'LangGraph')

print(message)

llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
res = llm.invoke(message)
print(res.content)