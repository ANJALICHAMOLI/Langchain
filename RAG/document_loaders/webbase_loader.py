#used to laod and extract text content form web pages
#uses beautiful soup
#for blogs news articles or public websites where the content is primarily text based and static 
#cnat handel js heavy web pages well 
#loads only static contcnt 

from langchain_community.document_loaders import WebBaseLoader

url='https://www.amazon.in/realme-6300mAh-Segments-Biggest-Battery/dp/B0H6HY2C29/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.042d46f5-694e-468c-9cb3-67fb658627a2&dib=eyJ2IjoiMSJ9.pPxABEcWlS-NcpgSX-VCHAiNmmA4TYP1m_VtGZ2pMWiekTvrlRG2RlyCbijnomaBdgoyToG3eVXx0XgB7OyP17yt_BOE7hv_pPzICiF79xRnW39gdIae1StfUqZCj4GPQ9A7i3IYQbQcAeeo1yHxAKIsQF5c7TMdbdBArDfCpMafAIu-hau5fnSH7qhOdQ2TrwqozD0Wpm7FvmditAVFshQ_plZiEvShZWF0bLs_5XWvmrksRdOJ-iQH734glcpLv-bUz7tKCpIeQrcf4v6l6j1-WlT7IHNePY94hpi5RXs.W809T-RYTYSqMUiOa63kq5Y9tIoi25L2fSawBj3lXj8&dib_tag=se&pd_rd_r=85b5e414-b899-4243-a227-0de122d2fee7&pd_rd_w=qkXLS&pd_rd_wg=uljFX&qid=1786548205&refinements=p_36%3A500000-1540000&rnid=1318502031&s=electronics&sr=1-1&th=1'

loader = WebBaseLoader(url)

docs=loader.load()
print(len(docs))
print(docs[0].page_content)