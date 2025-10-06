from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from langchain_ollama import ChatOllama

load_dotenv()

# Mistral Model
# model = ChatMistralAI(
#     model="mistral-large-latest"
# )


model = ChatOllama(
    model="llama3.2",
    temperature=0,
)

prompt_summary = PromptTemplate(
    template="Generate a detailed summary on the topic give below : \n {topic}",
    input_variables=["topic"]
)

prompt_quiz = PromptTemplate(
    template="Generate a quiz consisting of 5 questions and answets on the topic give below : \n {topic}",
    input_variables=["topic"]
)

prompt_final = PromptTemplate(
    template="Merge the below summary and quiz in a better readable way : \n summary :{summary} \n\n quiz: {quiz}",
    input_variables=["summary", "quiz"]
)

parser = StrOutputParser()

# Parallel Chaining
# chain = prompt1 | model | parser | prompt2 | model | parser
parallel_chain = RunnableParallel({
    "summary": prompt_summary | model | parser,
    "quiz": prompt_quiz | model | parser,
})
merger_chain = prompt_final | model | parser
chain = parallel_chain | merger_chain

resp = chain.invoke({
    "topic":"destiny"
})

print(resp)
# chain.get_graph().print_ascii()