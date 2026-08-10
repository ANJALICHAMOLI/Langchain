#helps extract structured json data from llm repsonse based on predefined feild schema(class)

#we have the advantge or option to enforce schema here unlike jsonoutputparser

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

llm=HuggingFaceEndpoint(repo_id='Qwen/Qwen2.5-1.5B-Instruct',task="text_generation")

model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact_1',description='fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='fact 2 about the topic')
]
parser=StructuredOutputParser()

template=PromptTemplate(
    template='give 2 facts about {topic}\n {format_intructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain=template|model|parser

result= chain.invoke({'topic':'black hole'})

print(result)

#it doest give data validation hence we use pydantic output parser 