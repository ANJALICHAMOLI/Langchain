from retrieving import retriever
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
import os
load_dotenv()

#init embedding
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

llm = ChatGoogleGenerativeAI(
    model=os.getenv("gemini_model"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

question= "is the topic of linear regression discussed in this video? if yes then what was discussed"
retrieved_docs= retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

# print(context_text)

final_prompt = prompt.invoke({"context": context_text, "question": question})

# print(final_prompt)
answer = llm.invoke(final_prompt)
print(answer.content)