from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

text="Delhi is the capital of India"

vector= embedding.embed_documents([text])

print(str(vector))
print(len(vector[0]))