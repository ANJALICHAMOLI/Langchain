from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-flash-latest",google_api_key=os.getenv("GOOGLE_API_KEY"),temperature=0)


while True:
    user_input=input('You: ')
    if user_input=='exit':
        break
    result=model.invoke(user_input)
    print("AI: ",result.content)