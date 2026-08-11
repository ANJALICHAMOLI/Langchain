#is a runnable primitive that allows multiple runnables to execture in parallel. 
#each runnable recevie the same inputs 

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel
import os 


load_dotenv()

prompt1=PromptTemplate(
    template='generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='generate a linkdin post about {topic}',
    input_variables=['topic']
)

model=ChatGroq(model=os.getenv("groq_model"))

parser=StrOutputParser()

#2 runnable seq inside runnable parallels
parallel_chain=RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})
result=parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])
print(result['linkedin'])