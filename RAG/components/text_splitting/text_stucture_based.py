#techinque used to work on the hirarchy of the structure .
#uses the Recursive Character Text Splitter, which attempts to keep text segments logically grouped by paragraphs, sentences, or words rather than just cutting mid word
#eg \n\n-means para ,\n-line ,_ word ,''- char 
# so it first tries to chunk by para then line etc it decides so by given constraints
from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
techinque used to work on the hirarchy of the structure .
uses the Recursive Character Text Splitter, which attempts to keep text segments logically grouped by paragraphs, sentences, or words rather than just cutting mid word.
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)