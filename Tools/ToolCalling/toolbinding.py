#process of connecting a tool with llm is toobinding
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv
import os
load_dotenv()

# tool create

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

print(multiply.invoke({"a":10,"b":30}))


llm=ChatGroq(model=os.getenv("groq_model"),groq_api_key="GROQ_API_KEY")

llm_tool=llm.bind_tools([multiply])

