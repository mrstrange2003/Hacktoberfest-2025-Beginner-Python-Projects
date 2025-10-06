from langchain_community.retrievers import WikipediaRetriever
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# Initialising Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

# Step 3: Creating in-memory vector store for chromadb
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="sample-collection"
)

# Step 4: Convert vectorstore into a retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k":2}
)

result = retriever.invoke("What is chroma used for?")

cnt = 1
for doc in result:
    print("Doc " + str(cnt) + " :-")
    print("doc metadata :", doc.metadata)
    print("doc page content :", doc.page_content)
    cnt += 1