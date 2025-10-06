
# -----------------------------------------------: Approach 1 :-----------------------------------------------
from langchain_core.tools import tool

# Step 1 - create a function
# def multiply(a, b):
#     """Multiply two numbers"""
#     return a*b

# Step 2 - add type hints
# def multiply(a: int, b:int) -> int:
#     """Multiply two numbers"""
#     return a*b

# Step 3 - add tool decorator
@tool
def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a":3, "b":5})
print(result)


# -----------------------------------------------: Approach 2 :-----------------------------------------------
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to add")
    b: int = Field(required=True, description="The second number to add")

def multiply_func(a: int, b: int) -> int:
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({'a':3, 'b':3})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)