from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()


# Temperature is a parameter that controls the randomness of a language model's output. 
# It affects how creative or deterministic the responses are.

# * Lower values (0.0 - 0.3) → More deterministic and predictable.
# * Higher values (0.7 - 1.5) → More random, creative, and diverse.
# Use Case	Recommended Temperature :-
# -->  Factual answers (math, code, facts)	            0.0 - 0.3
# -->  Balanced response (general QA, explanations)     0.5 - 0.7
# -->  Creative writing, storytelling, jokes	        0.9 - 1.2
# -->  Maximum randomness (wild ideas, brainstorming)   1.5+
chat_model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2,
)

result = chat_model.invoke("What is the capital of India?")
print(result.content)