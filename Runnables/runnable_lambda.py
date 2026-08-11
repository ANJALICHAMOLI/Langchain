#runnable primitive -can convert a python function into runnables
#i.e allows you to apply custom pytho functions within an Ai pipeline
#acts as a middleware between diffrent AI components,,enabling preprocessing ,transformation,api calls.filtering and post processing in langchain workflow

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough
import os 


load_dotenv()

model = ChatGroq(model=os.getenv("groq_model"))

parser = StrOutputParser()


prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

# def word_count(text):
#     return len(text.split())

joke_generator_chain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(lambda x:len(x.split()))
})

final_chain=RunnableSequence(joke_generator_chain,parallel_chain)

result=final_chain.invoke({'topic':'AI'})

final_result="""{}\n word_count - {}""".format(result['joke'],result['word_count'])

print(final_result)