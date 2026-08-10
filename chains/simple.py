from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
import os
prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatGroq(model=os.getenv("groq_model"))

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'llm'})

print(result)

chain.get_graph().print_ascii()