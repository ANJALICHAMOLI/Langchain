from typing import TypedDict,Annotated
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

#this schema is made to tell the types 
class Review(TypedDict):
    summary: Annotated[str,"A breif summary of the review"]
    sentiment:Annotated[str,"sentiment of the review either positive,negetive or nurtral"]
#to guide llm if ambiguity crub it 

#this schema is converted into a system prompt which leads to the seggregation of sentimet and summary without explicitly mentioning so in a json formula beacuse llm is  trained to return a json output 

struct_model=model.with_structured_output(Review) #invoke the model witch is struct model now which ha sthe defination of the class (review ) 

result= struct_model.invoke("""the cloth was not the same colour as shown in the picture and i recived it in an already opened package""")
#returs a json output with summary and sentiment 

print(result)
print(result['summary'])