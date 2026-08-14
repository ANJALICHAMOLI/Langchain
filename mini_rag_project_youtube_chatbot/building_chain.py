from aug_and_generation import prompt
from retrieving import retriever
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

# format docs for context
def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

Parallel_chain=RunnableParallel({
  'context':retriever|RunnableLambda(format_docs),
  'question':RunnablePassthrough()
})
question=input("Ask a question:")
# result=Parallel_chain.invoke(question)
# print(result['context'])
# print(result["question"])

#connecting for final ans
parser=StrOutputParser()

llm = ChatGoogleGenerativeAI(
    model=os.getenv("gemini_model"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

main_chain=Parallel_chain|prompt|llm |parser

final_answer=main_chain.invoke(question)

print(final_answer)