# ------------------------------------------------------------------------------------------------------------------------------------
# 📄 Multi-Query Retriever - Summary from reference material

# 🧠 Concept:
# Sometimes a single query might not capture all the ways 
# information is phrased in your documents.

# 📌 Example:
# Query: "How can I stay healthy?"
# This could imply sub-questions like:
#   - What should I eat?
#   - How often should I exercise?
#   - How can I manage stress?

# ⚠️ Issue:
# A basic similarity search might *miss documents* that cover 
# these topics but don’t use the word “healthy.”

# ✅ Multi-Query Retriever Workflow:
# 1. Takes your original query
# 2. Uses an LLM (e.g., GPT-3.5) to generate multiple 
#    semantically different versions of that query
# 3. Performs retrieval for each sub-query
# 4. Combines and deduplicates the results
# ------------------------------------------------------------------------------------------------------------------------------------


from langchain_community.vectorstores import FAISS
from langchain_mistralai import ChatMistralAI
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv

load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

chat_model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2,
)


# Relevant health & wellness documents
all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]

vectorstore = FAISS.from_documents(
    documents=all_docs,
    embedding=embedding_model,
)

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    llm=chat_model
)

multiquery_results = multiquery_retriever.invoke("How to improve energy levels and maintain balance?")

for i, doc in enumerate(multiquery_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)