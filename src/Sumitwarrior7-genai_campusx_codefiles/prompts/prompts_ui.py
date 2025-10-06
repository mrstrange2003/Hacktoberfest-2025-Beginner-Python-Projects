from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
import asyncio


load_dotenv()

chat_model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2,
)

async def main():
    st.header("Research Tool")
    user_inp = st.text_input("Enter your prompt")
    style_input = st.selectbox("Select Selection style :", ["Beginner Friendly", "Technical", "Mathematical"])
    length_input = st.selectbox("Select Explanation length :", ["Short", "Medium", "Long"])

    # Template
    template = load_prompt('template.json')
    if st.button("Summarize"):
        # -------Standard Approach-------
        # prompt = template.invoke({
        #     'paper_input':user_inp,
        #     'style_input':style_input,
        #     'length_input':length_input
        # })
        # resp = chat_model.invoke(prompt)

        # -------Chain Approach-------
        chain = template | chat_model
        resp = chain.invoke({
            'paper_input':user_inp,
            'style_input':style_input,
            'length_input':length_input
        })
        st.write(resp.content)

if __name__ == "__main__":
    asyncio.run(main())