from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# StructuredOutputParser is an output parser in LangChain that helps extract structured JSON data from LLM responses based on predefined field schemas.
# It works by defining a list of fields (ResponseSchema) that the model should return, ensuring the output follows a structured format.
# We cant do Schema validation
load_dotenv()

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)

# The strctured output we want from the model response
schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic")
]

structured_output_parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template = "Give me 3 facts about this topic :{topic} \n {format_instruction}", 
    input_variables=["topic"],
    partial_variables={'format_instruction': structured_output_parser.get_format_instructions()}
)


# Chain Approach
chain = template | model | structured_output_parser
resp = chain.invoke({"topic": "Rat Race"})
print(resp)

# Normal Approach
# prompt = template.format()
# resp = model.invoke(prompt)
# final_resp = json_output_parser.parse(resp.content)
