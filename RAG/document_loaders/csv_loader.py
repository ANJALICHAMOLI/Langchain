from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='/Users/data/Desktop/lagchain models /RAG/document_loaders/iris.numbers.csv',encoding='utf-8')

docs = loader.load()

print(len(docs))
print(docs[1])