import os
from langchain_google_genai import ChatGoogleGenerativeAI #would have been diffrent if it was open ai beacuse open ai originally had llms (text completion models) hence langchain has both openAI (LLM) and chatopenAI (chat model) classes but gemini was introduced after  chatbased models so langchain provides the chatgooglegenai class in langchain for ginimi direclty wokring with it hence using messsgaes ->chatmodels which oprates on HumanMessage, SystemMessage, AIMessage etc.therefore langchain_google_genai has only ChatGoogleGenerativeAI class and not GoogleGenerativeAI class and impicitly converts text to message only  
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-flash-latest",google_api_key=os.getenv("GOOGLE_API_KEY"),temperature=0,max_output_tokens=10)

result=model.invoke("what is the capital of India")