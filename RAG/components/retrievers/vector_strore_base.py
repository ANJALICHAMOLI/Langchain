#most common type of retriver that lets one search and fetch documents form a  vector database on semantic similiarity using vector embbedings
#how?--> documents are stored in vector store ,each document is converted into a dense vector using embedding model,the user returns the embbedings for the query given ,the retriver compares the query vector with the stored vector,it receives the top k most similar ones

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain.schema import Document
from langchain_chroma import Chroma
import os 
from dotenv import load_dotenv

load_dotenv()


documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# Step 2: Initialize embedding model
embedding_model = embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", google_api_key=os.getenv("GOOGLE_API_KEY"))



# Step 3: Create Chroma vector store in memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

retriever=vectorstore.as_retriever(search_kwargs={"k":2})

query="what is chroma in langchain"

results=retriever.invoke(query)

for i,doc in enumerate(results):
    print(f"\n.....Result {i+1}.......")
    print(doc.page_content)
