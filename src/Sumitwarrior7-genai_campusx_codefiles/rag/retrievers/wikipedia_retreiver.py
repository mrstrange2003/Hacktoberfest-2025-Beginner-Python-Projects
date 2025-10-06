from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

docs = retriever.invoke("The real problems in India which no one is talking about?")
# print(docs)

cnt = 1
for doc in docs:
    print("Doc " + str(cnt) + " :-")
    print("doc metadata :", doc.metadata)
    print("doc page content :", doc.page_content)
    cnt += 1