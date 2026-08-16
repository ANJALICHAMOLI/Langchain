# tool create
#process of connecting a tool with llm is toobinding
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv
import os
from langchain_core.tools import InjectedToolArg
from typing import Annotated

load_dotenv()


@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
  """
  This function fetches the currency conversion factor between a given base currency and a target currency
  """
  api_key=os.getenv("exchange")
  url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}'

  response = requests.get(url)

  return response.json()

get_conversion_factor.invoke({'base_currency':'USD','target_currency':'INR'})


@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
  """
  given a currency conversion rate this function calculates the target currency value from a given base currency value
  """

  return base_currency_value * conversion_rate


# convert.invoke({'base_currency_value':10,'conversion_rate':85.16})

#tool binding
llm=ChatGroq(model=os.getenv("groq_model"),groq_api_key=os.getenv("GROQ_API_KEY"))

llm_tools=llm.bind_tools([get_conversion_factor,convert])

messages = [HumanMessage('What is the conversion factor between INR and USD, and based on that can you convert 10 inr to usd')]

ai_message = llm_tools.invoke(messages)
messages.append(ai_message)

# print(ai_message.tool_calls)

import json

for tool_call in ai_message.tool_calls:
  # execute the 1st tool and get the value of conversion rate
  if tool_call['name'] == 'get_conversion_factor':
    tool_message1 = get_conversion_factor.invoke(tool_call)
    # fetch this conversion rate
    conversion_rate = json.loads(tool_message1.content)['conversion_rate']
    # append this tool message to messages list
    messages.append(tool_message1)
  # execute the 2nd tool using the conversion rate from tool 1
  if tool_call['name'] == 'convert':
    # fetch the current arg
    tool_call['args']['conversion_rate'] = conversion_rate
    tool_message2 = convert.invoke(tool_call)
    messages.append(tool_message2)

final_msg=llm_tools.invoke(messages).content

print(final_msg)