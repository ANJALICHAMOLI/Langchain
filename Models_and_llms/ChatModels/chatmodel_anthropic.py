from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()
# eg (requires an Anthropic API key)

model = ChatAnthropic(
    model="claude-sonnet-4",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    temperature=0
)
result =model.invoke('what is the capital of france')