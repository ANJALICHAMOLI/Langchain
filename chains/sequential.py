from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()


prompt1 = PromptTemplate(
    template='Generate a detailed paragraph about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Generate a 3 pointer summary from the following text\n {text}',
    input_variables=['text']
)

model = ChatGroq(model=os.getenv("groq_model"))

parser = StrOutputParser()

chain = prompt1 | model | parser |prompt2 |model |parser

result = chain.invoke({'topic':'chains in langchain'})

print(result)

chain.get_graph().print_ascii()