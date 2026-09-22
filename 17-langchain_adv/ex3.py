from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
for chunk in llm.stream('Explain artificial intellegence'):
    print(chunk.content,flush = True,end="") 
    #print has its own buffer, and until it fill it doesn't dislay anything so that why flush = True helps print to know that dont wait for buffer to fill, print it as u get response.