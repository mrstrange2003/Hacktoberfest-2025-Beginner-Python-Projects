from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

chat_model = ChatHuggingFace(
    llm=llm,
)

# We are interacting with open source llm through hugging face apis 
result = chat_model.invoke("Which is the oldest religion of world?")
print(result.content)