from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from youtube_transcript_api import YouTubeTranscriptApi 
from youtube_transcript_api._errors import TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
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
#FETCHING TRANSCRIPT
vid_id ='E0Hmnixke2g'
try:
    yt_api=YouTubeTranscriptApi()
    # If you don’t care which language, this returns the “best” one
    transcript_list = yt_api.fetch(vid_id, languages=["en"])

    # Flatten it to plain text
    transcript = " ".join(chunk.text for chunk in transcript_list)
    # print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")

#SPLITTING TEXT  
splitter=RecursiveCharacterTextSplitter(chunk_size=1500,chunk_overlap=300)  
chunks=splitter.create_documents([transcript])
# print(len(chunks))
# print(chunks[10])

#INDEXING(EMBEDDING GENERATION AND STORING)
vector_store=FAISS.from_documents(chunks,embedding_model)
# id=vector_store.index_to_docstore_id
# print(id)
# vector_store.save_local("vectorstore")