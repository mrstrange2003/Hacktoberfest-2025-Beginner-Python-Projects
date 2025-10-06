from langchain_community.document_loaders import TextLoader

loader = TextLoader("../data/text.txt", encoding="utf-8")
documents = loader.load()
print(len(documents))
print(documents[0])
print(documents[0].page_content)
print(documents[0].metadata)