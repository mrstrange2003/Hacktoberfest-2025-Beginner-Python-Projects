# Tool Calling is the process where the LLM decides, during a conversation or task, that it needs to use a specific tool (function) - and generates a structured output with:
# * the name of the tool
# * and the arguments to call it with

# ⚠️ The LLM does not actually run the tool - it just suggests the tool and the input arguments. The actual execution is handled by LangChain or you.
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

all_messages = []
all_messages.append(HumanMessage("what is the product for 2 and 8"))

# Tool Creation
@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b


# Tool Binding
tools = [multiply]
llm_with_tools = llm.bind_tools(tools)

# LLM inference
result = llm_with_tools.invoke(all_messages)
all_messages.append(result)


# Tool Calling
if len(result.tool_calls) != 0:
    tool_result = multiply.invoke(result.tool_calls[0])
    all_messages.append(tool_result)

# print(all_messages)


final_result = llm_with_tools.invoke(all_messages).content
print(final_result)