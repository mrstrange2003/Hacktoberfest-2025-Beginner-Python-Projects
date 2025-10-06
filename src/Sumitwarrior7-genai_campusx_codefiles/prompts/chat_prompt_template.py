from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate([
    ("system", "You are helpful {domain} expert"),
    ("human", "Explain in simpler terms , what is {topic}")
])

prompt = chat_template.invoke({"domain":"cricket", "topic":"Killer Miller"})
print(prompt)