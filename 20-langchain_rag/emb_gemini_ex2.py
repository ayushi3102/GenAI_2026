from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import numpy as np

load_dotenv()

emb = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

v1 = emb.embed_query("cheap phone")
v2 = emb.embed_query("budget phone")

similarity = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
print(similarity)