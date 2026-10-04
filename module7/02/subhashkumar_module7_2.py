# subhashkumar_module7_2.py

# make python program to get user input then connect to ollama and show result in terminal or using streamlit. Use (yml) file for docker compose up

import streamlit as st
from langchain_ollama import ChatOllama


# --------------------------------------------------
# Connect to Ollama
# --------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    base_url="http://host.docker.internal:11434",
    temperature=0
)


# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------

st.title("Ollama Chat Application")

st.write("Enter a question and ask the local LLM.")


user_input = st.text_input(
    "Enter your question:"
)


if st.button("Ask LLM"):

    if not user_input.strip():

        st.warning("Please enter a question.")

    else:

        try:

            response = llm.invoke(user_input)

            st.subheader("LLM Response")

            st.write(response.content)

        except Exception as e:

            st.error(f"Error connecting to Ollama: {e}")

            #docker compose up --build
