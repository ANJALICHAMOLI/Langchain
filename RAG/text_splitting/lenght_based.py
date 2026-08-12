#The simplest method where text is split by a fixed number of characters or tokens. while fast and easy to implement, it risks cutting words or sentences in the middle, which can lose context.

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


splitter =CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

loader = PyPDFLoader('/Users/data/Desktop/lagchain models /RAG/document_loaders/langchain_learning_notes.pdf')

docs= loader.load()

result=splitter.split_documents(docs)

print(result[0].page_content)