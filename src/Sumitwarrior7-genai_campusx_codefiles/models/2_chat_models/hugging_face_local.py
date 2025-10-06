from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

chat_model = ChatHuggingFace(
    llm=llm,
)

# We are interacting with open source llm through hugging face apis 
# result = chat_model.invoke("Which is the oldest religion of world?")
# print(result.content)