from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
import os 

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-flash-latest",google_api_key=os.getenv("GOOGLE_API_KEY"),temperature=0)

chat_history=[SystemMessage(content="you are a helpful Ai assistant")] #to keep the record of context 

while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input)) #adding user input from chat to the list
    if user_input=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content)) #adding ai response(model reply) from chat to list to save the convo 
    print("AI: ",result.content)

print(chat_history)   #printing whole convo 