import streamlit as st 

DB_DIR = './chatDB'
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
        

st.title("Chat bot")
file = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if file :
    st.write("Uploaded:", file.name)

def create_vectordb():
        
        pdf = PyPDFLoader(file)
        docs= pdf.load()
        
        splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap =50)
        chunks = splitter.split_documents(docs)
        
        
        vectordb = Chroma.from_documents(documents=chunks,embeddings=embeddings,persist_drectory = DB_DIR)
def load_vector_db():
    return Chroma(persist_directory = DB_DIR,embedding_function = embeddings)   
       
        
        
        
        
    