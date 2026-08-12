#is. adocument loader that is used to load contet from pdf files and converts each page into a document object hence each containing thier own meta data and cotent

# there is one limilitation that pypdf loader internally uses PyPDF lib interanlly whihc is not that great with scanned pdf complex layouts  

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('langchain_learning_notes.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)