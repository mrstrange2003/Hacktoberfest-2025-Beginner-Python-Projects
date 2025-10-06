from langchain_core.tools import tool

# Custom tools
@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


class MathToolkit:
    def get_tools(self):
        return [add, multiply]
    

toolkit = MathToolkit()
tools = toolkit.get_tools()
for tool in tools:
    print(tool.name, "=>", tool.description)
