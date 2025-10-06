from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


# 🔹 What is PydanticOutputParser in LangChain?
# PydanticOutputParser is a structured output parser in LangChain that uses Pydantic models to enforce schema validation when processing LLM responses.

# 🎯 Why Use PydanticOutputParser?
# ✅ Strict Schema Enforcement → Ensures that LLM responses follow a well-defined structure.
# ✅ Type Safety → Automatically converts LLM outputs into Python objects.
# ✅ Easy Validation → Uses Pydantic’s built-in validation to catch incorrect or missing data.
# ✅ Seamless Integration → Works well with other LangChain components.

load_dotenv()

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.9
)


# The Pydantic output we want from the model response
class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Name of the person")
    city: str = Field(description="Name of the city person belongs to")
pydantic_output_parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = "Give me the name, age, city of a fictinal {place} person \n {format_instruction}", 
    input_variables=["place"],
    partial_variables={'format_instruction': pydantic_output_parser.get_format_instructions()}
)


# Chain Approach
chain = template | model | pydantic_output_parser
resp = chain.invoke({"place": "Indian"})
print(resp)

# Normal Approach
# prompt = template.format()
# resp = model.invoke(prompt) 
# final_resp = json_output_parser.parse(resp.content)
