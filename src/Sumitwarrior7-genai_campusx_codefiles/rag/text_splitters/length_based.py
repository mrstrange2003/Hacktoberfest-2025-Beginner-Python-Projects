from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

splitter = CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=5,
    separator=""
)

# text = """
# The power of focus is straight-up underrated. When you lock in on one goal, blocking out distractions, you unlock a whole new level of potential. Focus channels your energy, sharpens your mind, and helps you move with purpose. In a world full of noise and constant notifications, staying focused is a superpower. It’s not about doing a million things—it's about doing the right thing with full intent. Whether you’re chasing grades, goals, or greatness, focus keeps you grounded and on track. Master it, and there’s literally no limit to what you can achieve.
# """
# result = splitter.split_text(docs)
# print("result :", result)

loader = PyPDFLoader("../data/content.pdf")
docs = loader.load()
result = splitter.split_documents(docs)
print("result :", result[0])