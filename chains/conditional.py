from langchain_google_genai import GoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
import os

load_dotenv()

parser1= StrOutputParser()
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

model1=ChatGroq(model=os.getenv("groq_model"))

parser =PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(template="classify the sentimet of the following feedback text into positive or negative \n {feedback}\n {format_instruction}",input_variables=(['feedback']),partial_variables={'format_instruction':parser.get_format_instructions()})


classifier_chain=prompt1|model1|parser


prompt2=PromptTemplate(template="write an appropriate reponse to this positive feedback \n {feedback}",input_variables=(['feedback']))

prompt3=PromptTemplate(template="write an appropriate reponse to this negative feedback \n {feedback}",input_variables=(['feedback']))




branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2|model1|parser1),
    (lambda x:x.sentiment=='negative',prompt3|model1|parser1),
    RunnableLambda(lambda x :"Cound not understand what you mean")
)


chain=classifier_chain|branch_chain

print(chain.invoke({'feedback':'the food they served was very bad i hated the ambience'}))

chain.get_graph().print_ascii()