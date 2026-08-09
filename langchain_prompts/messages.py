from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import os
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-flash-latest",google_api_key=os.getenv("GOOGLE_API_KEY"),temperature=0)

messages=[
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content='Tell me about LangChain')
]
result=model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)