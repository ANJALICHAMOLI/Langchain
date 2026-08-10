from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

llm=HuggingFaceEndpoint(repo_id='Qwen/Qwen2.5-1.5B-Instruct',task="text_genration")

model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(template='Write a detailed paragraph on {topic}',input_variables=['topic'])

template2=PromptTemplate(template='Write 5 line summary on the following text {text}',input_variables=['text'])

prompt1=template1.invoke({'topic':'black hole'})

result1=model.invoke(prompt1)

prompt2=template2.invoke({'text':result1.content})

result2=model.invoke(prompt2)

print(result2.content)

