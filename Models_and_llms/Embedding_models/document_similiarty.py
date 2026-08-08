from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2",google_api_key=os.getenv("GOOGLE_API_KEY"),output_dimensionality=128)

documents=["Andrew Ng is an AI researcher known for his work in machine learning.",
    "Geoffrey Hinton is known for his work on neural networks and deep learning.",
    "Yann LeCun is known for his work on convolutional neural networks.",
    "Fei-Fei Li is an AI researcher known for her work in computer vision."]

query="who is known for his work in deep learning?"

query_embedding=embedding.embed_query(query,output_dimensionality=128)
doc_embeddings=embedding.embed_documents(documents,output_dimensionality=128)

scores=cosine_similarity([query_embedding], doc_embeddings)[0] #both has to be 2d list 

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score",score)