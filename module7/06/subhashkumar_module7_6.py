# subhashkumar_module7_6.py

# make python code python code to launch chat with ollama UI using streamlit. Make the docker images using MAKEFILE. 

# insert docker Environment variable to choose either launch chat with persona or without. Why we use Environment variable? 

import os
import streamlit as st
from langchain_ollama import ChatOllama


# =========================================================
# Read environment variable
# =========================================================

persona_enabled = os.getenv(
    "PERSONA_ENABLED",
    "false"
).lower() == "true"


# =========================================================
# Ollama configuration
# =========================================================

llm = ChatOllama(
    model="llama3.2",
    base_url="http://host.docker.internal:11434",
    temperature=0
)


# =========================================================
# Streamlit page
# =========================================================

st.set_page_config(
    page_title="Ollama Chat",
    page_icon="🤖"
)

st.title("🤖 Ollama Chat")


# Display current mode

if persona_enabled:

    st.info("Persona mode is enabled.")

else:

    st.info("Normal chat mode is enabled.")


# =========================================================
# Chat history
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =========================================================
# User input
# =========================================================

user_input = st.chat_input(
    "Ask something..."
)


if user_input:

    # ---------------------------------------------
    # Display user message
    # ---------------------------------------------

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):

        st.markdown(user_input)


    # ---------------------------------------------
    # Create prompt
    # ---------------------------------------------

    if persona_enabled:

        system_prompt = """
You are a helpful senior Python developer.

Your responsibilities:

- Explain concepts clearly.
- Provide practical examples.
- Prefer simple and readable Python code.
- Explain why something works.
- Help the user learn rather than simply giving an answer.
"""

    else:

        system_prompt = """
You are a helpful AI assistant.
Answer the user's questions clearly and accurately.
"""


    # ---------------------------------------------
    # Send conversation to Ollama
    # ---------------------------------------------

    messages = [
        ("system", system_prompt)
    ]

    for message in st.session_state.messages:

        messages.append(
            (
                message["role"],
                message["content"]
            )
        )


    # ---------------------------------------------
    # Call Ollama
    # ---------------------------------------------

    with st.chat_message("assistant"):

        try:

            response = llm.invoke(messages)

            answer = response.content

            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:

            st.error(
                f"Unable to connect to Ollama: {e}"
            )
