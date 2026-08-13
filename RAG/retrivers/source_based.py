#wikipedia Retriver is a retriver that retrives queries the wikipedia api to fetch relevlent contet for a given query 

#setting up wikipedia api 

import requests
import wikipedia

# Set User-Agent for the requests module used by wikipedia
original_get = requests.get

def custom_get(*args, **kwargs):
    headers = kwargs.setdefault("headers", {})
    headers["User-Agent"] = "MyLangChainLearningBot/1.0 (extrakeep825@gmail.com)"
    return original_get(*args, **kwargs)

requests.get = custom_get

# maincode--------------

from langchain_community.retrievers import WikipediaRetriever

#Initialize the retriever (optional: set language and top_k)

retriever = WikipediaRetriever(top_k_results=2, lang="en")


# Define query
query = "the akbar"

# getting relevant Wikipedia documents
docs = retriever.invoke(query)
print(docs)

#contnet form doctument pages form wikipedia articles
for doc in docs:
    print("PAGE CONTENT:")
    print(doc.page_content)

    print("METADATA:")
    print(doc.metadata)

    print("----------------")