import langchain
print(langchain.__version__)

import torch

print(torch.__version__)
print(torch.backends.mps.is_available())


import langchain_google_genai
print(langchain_google_genai.__version__)

from inspect import signature
from langchain_google_genai import GoogleGenerativeAIEmbeddings

print(signature(GoogleGenerativeAIEmbeddings))