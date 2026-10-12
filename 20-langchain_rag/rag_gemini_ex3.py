from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

PDF_PATH = 'Ayushi_4YOE_2026.pdf'
DB_DIR = './resumeDb'

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
    )

def create_vector_db():

    # Step 1 - Convert PDF to documents
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()
    
    # Step 2 - Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
    )
    
    chunks = splitter.split_documents(docs)
    
    vectordb = Chroma.from_documents(documents = chunks,
                                 embedding=  embeddings,
                                 persist_directory = DB_DIR)

def load_vector_db():
    return Chroma(persist_directory = DB_DIR,embedding_function = embeddings)   

def get_or_create_db():
    if os.path.exists(DB_DIR) and len(os.listdir(DB_DIR))>0 :
        print("n Loading existing vector DB...")
        return load_vector_db()
    create_vector_db()
    return load_vector_db()

def get_retriever():
    return vectordb.as_retriever(
    search_kwargs={"k": 4}
)

def get_prompt():
    return ChatPromptTemplate.from_template(
    """Answer the question using only the provided context.
    If the answer is not available in the context, say
    "I couldn't find that information in the resume."

    Context:
    {context}

    Question:
    {question}
    """
)

def format_doc(docs):
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    return context

vectordb = get_or_create_db()
retriever = get_retriever()
prompt = get_prompt()

# Create Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
    )

while True:
    query = input(
        "Ask a question about your resume (type exit to quit): "
    )

    if query.strip().lower() == "exit":
        break

    # Retrieve relevant documents
    retrieved_docs = retriever.invoke(query)
    if not retrieved_docs:
        print('\n no relevant data found for your query')
        continue

    # Combine retrieved documents into context
    context = format_doc(retrieved_docs)

    # Create final prompt
    final_prompt = prompt.format(
        context=context,
        question=query
    )

    # Generate the answer
    res = llm.invoke(final_prompt)

    print("\nAnswer:", res.content)