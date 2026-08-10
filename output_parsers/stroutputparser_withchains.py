#simplest parser .extracts rawt text content form the models response removing meta data


from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(repo_id='Qwen/Qwen2.5-1.5B-Instruct',task="text_genration")

model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(template='Write a detailed paragraph on {topic}',input_variables=['topic'])

template2=PromptTemplate(template='Write 5 line summary on the following text {text}',input_variables=['text'])

prompt1=template1.invoke({'topic':'black hole'})

parser=StrOutputParser()
chain= template1 | model | parser| template2 |model |parser

result=chain.invoke({'topic':'black hole'})

print(result)

