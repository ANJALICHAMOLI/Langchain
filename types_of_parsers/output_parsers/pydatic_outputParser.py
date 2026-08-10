#helps do data validation 
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel ,Field

load_dotenv()
llm=HuggingFaceEndpoint(repo_id='Qwen/Qwen2.5-1.5B-Instruct',task="text_generation")

model=ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str=Field(description='Name of the person')
    age:int=Field(description='age of the person')
    city:str=Field(description='Name of the city')

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='generate the name age and city of a fictional {place} perosn \n {format_instructions}',input_variables=['place'],partial_variables={'format_instructions':parser.get_format_instructions()}
)
chain= template|model|parser

result=chain.invoke({'place':'africa'})

print(result)