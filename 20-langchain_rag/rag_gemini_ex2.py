from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Step 1 - Convert PDF to documents
loader = PyPDFLoader("Ayushi_4YOE_2026.pdf")
docs = loader.load()

# Step 2 - Split documents into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# Step 3 - Create Gemini embedding engine
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

# Step 4 - Create embeddings and store in Chroma
vectordb = Chroma.from_documents(documents = chunks,embedding=  embeddings,persist_directory = './resumeDb')

# Step 5 - Create retriever
retriever = vectordb.as_retriever(
    search_kwargs={"k": 4}
)

# Step 6 - Create prompt template
prompt = ChatPromptTemplate.from_template(
    """Answer the question using only the provided context.
    If the answer is not available in the context, say
    "I couldn't find that information in the resume."

    Context:
    {context}

    Question:
    {question}
    """
)

# Step 7 - Create Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
    
)

# Step 8 - Combine all the retrieved chunks
def format_doc(docs):
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    return context

# Step 9 - Create the RAG pipeline
while True:
    query = input(
        "Ask a question about your resume (type exit to quit): "
    )

    if query.strip().lower() == "exit":
        break

    # Retrieve relevant documents
    retrieved_docs = retriever.invoke(query)

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