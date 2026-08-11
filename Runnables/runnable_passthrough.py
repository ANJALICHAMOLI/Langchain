#runable passthough passes whatever it recivied as input  as it is without modifying

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
import os 


load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
model = ChatGroq(model=os.getenv("groq_model"))

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_generator_chain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanantion':RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_generator_chain,parallel_chain)

print(final_chain.invoke({'topic':'llm'}))