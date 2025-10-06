# PyPDFLoader is a document loader in LangChain used to load content from PDF files and convert each page into a Document object. 

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("../data/content.pdf")

docs = loader.load()

print(len(docs))

print(docs[1].page_content)
print(docs[1].metadata)