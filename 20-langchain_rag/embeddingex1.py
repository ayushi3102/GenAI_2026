from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

emb = OpenAIEmbeddings()
v1  = emb.embed_query("cheap phone")
v2  = emb.embed_query("budget phone")
print(len(v1))
print(len(v2))