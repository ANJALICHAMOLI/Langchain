from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAI
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()

model1=ChatGroq(model=os.getenv("groq_model"))

model2=GoogleGenerativeAI(model=os.getenv("gemini_model"),google_api_key=os.getenv("GOOGLE_API_KEY"))

prompt1=PromptTemplate(template="generate simple and short notes from the following text \n {text}",input_variables=(['text']))

prompt2=PromptTemplate(template="generate 5 quiz type questions from the given text \n{text}",input_variables=(['text']))

prompt3=PromptTemplate(template="Merge the provided notes and quiz into single document\n notes ->{notes} and quiz->{quiz}",input_variables=(['notes','quiz']))

parser =StrOutputParser()

#parallel chain 
parallel_chain=RunnableParallel({
    'notes':prompt1|model1|parser,
    'quiz':prompt2|model2|parser
})

#mergeing chains

merge_chains=prompt3|model1|parser

chain = parallel_chain|merge_chains

text="""Traditional models like decision trees and random forests are easy to interpret but may lack accuracy on complex data. XGBoost (eXtreme Gradient Boosting) is an optimized gradient boosting algorithm that combines multiple weak models into a stronger, high-performance model.

It uses decision trees as base learners, building them sequentially so each tree corrects errors from the previous one and it is known as boosting.
It features parallel processing for faster training on large datasets and allows parameter customization to optimize performance for specific problems.

How XGBoost Works?
It builds decision trees sequentially with each tree attempting to correct the mistakes made by the previous one. The process can be broken down as follows:

Start with a base learner: The first model decision tree is trained on the data. In regression tasks this base model simply predicts the average of the target variable.
Calculate the errors: After training the first tree the errors between the predicted and actual values are calculated.
Train the next tree: The next tree is trained on the errors of the previous tree. This step attempts to correct the errors made by the first tree.
Repeat the process: This process continues with each new tree trying to correct the errors of the previous trees until a stopping criterion is met.
Combine the predictions: The final prediction is the sum of the predictions from all the trees.
"""
result =chain.invoke({'text':text})

print(result)
chain.get_graph().print_ascii()