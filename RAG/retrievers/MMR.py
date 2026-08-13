#MMR is an information retrival algorithm designed to reduce redundancy in the retrived results while maintaning high relevance to the query
# why do we need it - regular similarity serches may get you document which are all very similar to each other ,repeating the sam einfo and lacking diversity.
#MMR solves it by picking most relevent document first ,then picking the next most relevant and the least similar to already selected docs 
#helps pick results which are not just relevent to the query but also distinct

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
import os 
from dotenv import load_dotenv

load_dotenv()

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

#embedding
embedding_model = embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", google_api_key=os.getenv("GOOGLE_API_KEY"))

#create faiss vector store
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model,
    
)

#enable mmr retriver
# Enable MMR in the retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",                   # this enables MMR
    search_kwargs={"k": 3, "lambda_mult": 0.5}  # k = top results, lambda_mult = relevance diversity balance -lambda mult has values between 0-1
)
query = "What is langchain?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)