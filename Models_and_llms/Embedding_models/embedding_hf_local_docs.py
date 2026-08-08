from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

docs=["Delhi is the capital of India",
      "India is a country in South Asia"]

vector= embedding.embed_documents(docs)

print(str(vector))
print(len(vector[0]))