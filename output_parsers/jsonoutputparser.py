#forces an llm or model  to give output in json format 

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(repo_id='Qwen/Qwen2.5-1.5B-Instruct',task="text_genration")

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template1=PromptTemplate(template='give me the name,age and city of a frictional peroson \n{format_instructions}',input_variables=[],partial_variables={'format_instructions':parser.get_format_instructions()})



# prompt1=template1.format()

# result=model.invoke(prompt1)

# result_final=parser.parse(result.content)
#intead of this we cna make a chain 
chain = template1|model|parser

result=chain.invoke({})
print(result)
print(type(result))

#but we cannot enforce a schema say we want 5 facts but like fact1-... fact 2.. so on that we cannot customise while formating to json
#hence we use stuctured output parser