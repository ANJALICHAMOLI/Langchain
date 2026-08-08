from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os 

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", google_api_key=os.getenv("GOOGLE_API_KEY"),output_dimensionality=128)

doc=[
    "delhi the capital of India",
    "paris the capital of France",
]

result=embeddings.embed_documents(doc, output_dimensionality=128)

print(str(result))
print(len(result))