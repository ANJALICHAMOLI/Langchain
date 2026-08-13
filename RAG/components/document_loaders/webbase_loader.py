#used to laod and extract text content form web pages
#uses beautiful soup
#for blogs news articles or public websites where the content is primarily text based and static 
#cnat handel js heavy web pages well 
#loads only static contcnt 

from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os 

load_dotenv()

model = ChatGroq(model=os.getenv('groq_model'))

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://amzn.in/d/05yylWGp'
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))

