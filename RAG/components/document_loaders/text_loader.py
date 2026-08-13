from langchain_community.document_loaders import TextLoader

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

model=ChatGroq(model=os.getenv("groq_model"))
parser=StrOutputParser()

loader = TextLoader('/Users/data/Desktop/lagchain models /RAG/rag.txt',encoding='utf-8')



prompt = PromptTemplate(
    template='Summarize the following text \n {text} in approx 200 words',input_variables=['text'])
docs=loader.load()

chain= prompt | model | parser
result= chain.invoke({'text':docs[0].page_content})

# print(docs)

print("PAGE CONTENT Summarized",result)
