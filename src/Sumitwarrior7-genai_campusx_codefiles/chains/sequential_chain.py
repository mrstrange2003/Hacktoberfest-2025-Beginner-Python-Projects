from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

load_dotenv()

# model = ChatMistralAI(
#     model="mistral-large-latest"
# )

model = ChatOllama(
    model="llama3.2",
    temperature=0,
    # other params...
)

prompt1 = PromptTemplate(
    template="Write the question in a more refined way and correcting the grammatical errors. \n {question}",
    input_variables=["question"]
)

prompt2 = PromptTemplate(
    template="Answer the question in brief way \n {refined_question}",
    input_variables=["refined_question"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

resp = chain.invoke({
    "question":"assplain me fom where alllllll thus browsers get      data which we c on itrnet?"
})

print(resp)
# chain.get_graph().print_ascii()