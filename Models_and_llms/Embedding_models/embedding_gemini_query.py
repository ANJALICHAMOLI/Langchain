from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os 

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", google_api_key=os.getenv("GOOGLE_API_KEY"),output_dimensionality=128)

result=embeddings.embed_query("delhi the capital of India", output_dimensionality=128)

print(str(result))
print(len(result))