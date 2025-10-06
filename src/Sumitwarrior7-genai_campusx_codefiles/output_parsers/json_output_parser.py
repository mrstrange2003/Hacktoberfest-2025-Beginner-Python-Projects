from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)

json_output_parser = JsonOutputParser()
template = PromptTemplate(
    template = "Give me the name, age, city of a fictinal person \n {format_instruction}", 
    input_variables=[],
    partial_variables={'format_instruction': json_output_parser.get_format_instructions()}
)
# Chain Approach
chain = template | model | json_output_parser
resp = chain.invoke({})
print(resp)

# Normal Approach
# prompt = template.format()
# resp = model.invoke(prompt)
# final_resp = json_output_parser.parse(resp.content)
