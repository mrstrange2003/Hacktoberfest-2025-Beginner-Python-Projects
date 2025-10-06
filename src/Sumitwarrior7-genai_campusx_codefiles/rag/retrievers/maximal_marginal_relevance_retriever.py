# Maximal Marginal Relevance (MMR)
# "How can we pick results that are not only relevant to the query but also different from each other?"

# MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved results while maintaining high relevance to the query.

# 🤔 Why MMR Retriever?

# In regular similarity search, you may get documents that are:
# - All very similar to each other
# - Repeating the same info
# - Lacking diverse perspectives

# MMR Retriever avoids that by:
# - Picking the most relevant document first
# - Then picking the next most relevant and least similar to already selected docs
# - And so on...

# This helps especially in RAG pipelines where:
# - You want your context window to contain diverse but still relevant information
# - Especially useful when documents are semantically overlapping
#----------------------------------------------------------------------------------------------------------------------------------------------------------

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

# Initialising Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model,
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3, "lambda_mult": 0.5}
)

result = retriever.invoke("What is chroma used for?")

cnt = 1
for doc in result:
    print("Doc " + str(cnt) + " :-")
    print("doc metadata :", doc.metadata)
    print("doc page content :", doc.page_content)
    cnt += 1