import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-flash-latest",google_api_key=os.getenv("GEMINI_API_KEY"),temperature=0)

result =llm.invoke("whats the capital of india")
print(result.content)
