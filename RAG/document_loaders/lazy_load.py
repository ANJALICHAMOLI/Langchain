#LAZY LOADER LOADS ONE DOCUMENT AT AT TIME IN MEMOMY USING GENREATOR HENCE FASTER THAN LOAD 

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='eg.pdf',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)