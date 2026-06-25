from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

texts = ["Helloo i am Pratibha Banerjee", "Hi i am learning GenAI", "I am enjoying it."]

vector = embeddings.embed_documents(texts)
print(vector)
