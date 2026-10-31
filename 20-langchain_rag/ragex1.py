from langchain_openai import ChatOpenAI, OpenAIEmbeddings 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()

#step 1 - convert pdf to docs
loader = PyPDFLoader('Ayushi_4YOE_2026.pdf')
docs = loader.load()

#step 2 - split docs into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
chunks = splitter.split_documents(docs)

#step 3 - create embedding engine
embeddings = OpenAIEmbeddings()

#step 4 - create embeddings, store them in vector
vectordb = FAISS.from_documents(chunks,embeddings)

#step 5 - create retriver
retriever = vectordb.as_retriever()

#step 6 - prompt template
prompt = ChatPromptTemplate.from_template("Answer the questions only on the context provided : {context}, Question : {question}")

#step 7 - create llm 
llm = ChatOpenAI(model = "gpt-$o-mini")

# step 8 - create the rag pipeline

while True:
    query = input("Type your ques regarding your resume. Type exit to quit")
    if query.lower().trim()=='exit':
        break
    retrieved_docs = retriever.invoke(query)
    
    #combine all docs(context) 
    context = '\n'.join([doc.page_context for doc in retrieved_docs])
    
    #create final prompt
    final_prompt = prompt.format(context ={context},question = {query})
    
    #generate the answer 
    res = llm.invoke(final_prompt)
    print('\nAnswer: ', res.content)
    
    
    



