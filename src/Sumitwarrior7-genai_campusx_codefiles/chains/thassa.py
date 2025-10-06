from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from typing import Annotated, Literal
from langchain_ollama import ChatOllama
from langchain_ollama.llms import OllamaLLM

load_dotenv()

# Mistral Model
# model = ChatMistralAI(
#     model="mistral-large-latest"
# )


# model = ChatOllama(
#     model="llama3.2",
#     temperature=0,
# )

model = OllamaLLM(model="llama3.2")


# The Pydantic output we want from the model response
class Feedback(BaseModel):
    sentiment: Annotated[Literal["positive", "negative"], "Return sentiment of the review either positive or negative"]

pydantic_output_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt_initial = PromptTemplate(
    template="Given below is feedback, analyze it and based on that tell if it is positive or negative. \n{format_instructions}\n{feedback}\n",
    input_variables=["feedback"],
    partial_variables={'format_instructions': pydantic_output_parser.get_format_instructions()}
)

# Chain which will classify the feedback to be positive or negative
classifier_chain = prompt_initial | model | pydantic_output_parser


prompt_pos = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"]
)
prompt_neg = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)
str_parser = StrOutputParser()

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt_pos | model | str_parser),
    (lambda x:x.sentiment == 'negative', prompt_neg | model | str_parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain
resp = chain.invoke({"feedback":"I want to give positive feedback to the product"})
print(resp)
# chain.get_graph().print_ascii()