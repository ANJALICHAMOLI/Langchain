
from langchain_groq import ChatGroq
from langchain_core.tools import tool
import requests
from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_community.tools import DuckDuckGoSearchRun
import os
load_dotenv()

api=os.getenv('weather_api')
search_tool = DuckDuckGoSearchRun()
#buling the tools
@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key={api}={city}'

  response = requests.get(url)

  return response.json()


llm= ChatGroq(model=os.getenv("groq_model"),groq_api_key=os.getenv('groq_api_key'))

# Step 2: Pull the ReAct prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")  # pulls the standard ReAct agent prompt


# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)
# Step 4: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True #lets us see what agent is thinking
)

# Step 5: Invoke
response = agent_executor.invoke({"input": "Find the capital of India, then find it's current weather condition"})
print(response)

response['output']