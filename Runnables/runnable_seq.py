#runnables :Runnables are a standardized approach designed to simplify the creation of AI workflows
#runnables are of 2 types
#a sequantial chain of runnables in langchain that execute each step after another passing the output of one step as the input to next 
#this happened as the shift from disparate, non standardized components to a unified approach using the invoke method. This standardization via the Runnable abstract class allows different components (like LLMs, prompts, and parsers) to connect seamlessly 

#Categorization of Runnables:
# Task-Specific Runnables: These are core LangChain components that perform a distinct, functional job Eg:
    # ChatOpenAI (for interacting with LLMs).
    # PromptTemplate (for structuring input prompts).
    # Retrievers (for accessing external data).
# Runnable Primitives: These are building blocks used to orchestrate how tasks interact with each other. They help define complex execution logic, EG:

    # RunnableSequence: Chains components to execute one after another 
    # RunnableParallel: Runs multiple components simultaneously using the same input 
    # RunnablePassthrough: Passes input through without modification, useful for maintaining context 
    # RunnableLambda: Converts custom Python functions into runnables 
    # RunnableBranch: Implements conditional "if-else" logic for decision making flows 

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
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

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic':'AI'}))