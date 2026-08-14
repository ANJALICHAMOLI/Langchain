import os 
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


vector_store = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever=vector_store.as_retriever(search_type='similarity',search_kwargs={"k":4})

# data=retriver.invoke("what is gradient boosting")
# for i,doc in enumerate(data,1):
#     print(f"\n--- Document {i} ---")
#     print(doc.page_content)