

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnableBranch,RunnablePassthrough
from pydantic import BaseModel
import os 


load_dotenv()

model = ChatGroq(model=os.getenv("groq_model"))


class Summary(BaseModel):
    summary: str
    key_points: list[str]
    word_count: int

parser = StrOutputParser()
summary_parser = PydanticOutputParser(pydantic_object=Summary)    

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text} in approx 200 words Return the result according to the format instruction\n {format_instruction}  ',
    input_variables=['text'],
    partial_variables={ "format_instruction": summary_parser.get_format_instructions()}
)


report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>200,RunnableSequence(prompt2 | model | summary_parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print("RESULT:")
print(final_chain.invoke({'topic':'Ai'}))

