from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

emb = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

v1 = emb.embed_query("cheap phone")
v2 = emb.embed_query("budget phone")

print(len(v1))
print(len(v2))