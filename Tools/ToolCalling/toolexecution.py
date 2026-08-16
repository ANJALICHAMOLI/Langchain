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

llm=ChatGroq(model=os.getenv("groq_model"),groq_api_key=os.getenv("GROQ_API_KEY"))

#tool binding
llm_tool=llm.bind_tools([multiply])


#user query
query=HumanMessage("can you multiply 3 with 10")
#toolcalling

messages=[query]

#llm produces an ai message contianing a tool call
result=llm_tool.invoke(messages)


# print(result.tool_calls[0]) 

#appending ai msg into the messages
messages.append(result)
print(messages)
# tool call args
# print(result.tool_calls[0]['args'])
#PRINTS TOOL MESSAGE    
# print(multiply.invoke({'name': 'multiply', 'args': {'a': 58, 'b': 68}, 'id': 'czw18jeh2', 'type': 'tool_call'}
# ))

#therfore tool execution
result_tool=multiply.invoke(result.tool_calls[0]) #fucntion or tool exectues

messages.append(result_tool)

print(messages)
print(llm_tool.invoke(messages).content) #2nd llm call to produce final response with the ans