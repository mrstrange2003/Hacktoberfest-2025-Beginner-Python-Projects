from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)


template1 = PromptTemplate(
    template = "Generate a detailed description of the topic :{topic}", 
    input_variables=['topic']
)
template2 = PromptTemplate(
    template = "Generate a short summary of below description :\n {text}", 
    input_variables=['text']
)

str_output_parser = StrOutputParser()

chain = template1 | model | str_output_parser | template2 | model | str_output_parser
resp = chain.invoke("Rat Race")
print(resp)
