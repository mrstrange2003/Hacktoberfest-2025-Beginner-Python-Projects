from langchain_core.prompts import PromptTemplate

# Template
template = PromptTemplate(
    template="""
        Please summarize the research paper titled "{paper_input}" with the following specifications:
        Explanation Style: {style_input}
        Explanation Length: {length_input}

        Mathematical Details:

        Include relevant mathematical equations if present in the paper.

        Explain the mathematical concepts using simple, intuitive code snippets where applicable.

        Analogies:

        Use relatable analogies to simplify complex ideas.

        If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
        Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,
    input_variables=['paper_input', 'style_input', 'length_input']
)

template.save("template.json")