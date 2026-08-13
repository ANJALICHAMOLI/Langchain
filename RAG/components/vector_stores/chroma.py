from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema import Document
from langchain_chroma import Chroma
import os 


load_dotenv()



# Create LangChain documents for IPL players

doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )

vector_store=Chroma(embedding_function=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001',google_api_key=os.getenv('GOOGLE_API_KEY')),persist_directory='my_chroma_db',collection_name='sample')

docs = [doc1, doc2, doc3, doc4, doc5]

if not os.path.exists("my_chroma_db"):
    vector_store.add_documents(docs)

#for viweing document
view_doc=vector_store.get(include=['embeddings','documents', 'metadatas'])

#for eaching similarity score with doctumens 
result=vector_store.similarity_search_with_score(query='who among these is a bowler?',k=1)

#filtering of meta data
meta_data=vector_store.get(
    where={"team": "Chennai Super Kings"}
)
print("VIEW DOCUMENTS",view_doc)
print("SIMILIARITY SCORE",result[0][1])
print("DOCUMENT:", result[0][0])

print(vector_store._collection.count())

print("META DATA FILTERING",meta_data)

#updating doctument

# update_doc3=Document(page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
#     metadata={"team": "Royal Challengers Bangalore"})


# vector_store.update_document(document_id='4519c988-5322-4a2f-9ded-7cf79e08cf87', document=update_doc3)

#deleting doc 
# vector_store.delete(ids=['4519c988-5322-4a2f-9ded-7cf79e08cf87'])

data = vector_store.get(
    include=["documents", "metadatas"]
)

for id, doc, metadata in zip(
    data["ids"],
    data["documents"],
    data["metadatas"]
):
    print("ID:", id)
    print("DOCUMENT:", doc)
    print("METADATA:", metadata)
    print("----------------")

