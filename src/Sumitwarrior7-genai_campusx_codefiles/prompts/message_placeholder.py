from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


chat_template = ChatPromptTemplate([
    ("system", "You are helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"), # Loading the previous chat history
    ("human", "Here is the user query : {query}")
])

# Getting the chat history
chat_history = []
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = chat_template.invoke({"chat_history":chat_history, "query":"Where is my refund?"})
print(prompt)