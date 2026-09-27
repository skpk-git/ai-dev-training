# subhashkumar_module5_2.py
# make a streamlit code to chat with an LLM 
# and it remembers all information in same chat 


import streamlit as st
import urllib.request
import json


# --------------------------------------------------
# Configuration
# --------------------------------------------------

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Ollama Chat",
    page_icon="🤖"
)

st.title("🤖 Ollama Chat")

st.caption(
    "Chat with your local LLM. "
    "The conversation is remembered during this session."
)


# --------------------------------------------------
# Initialize conversation history
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# --------------------------------------------------
# Display previous messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# User enters a question
# --------------------------------------------------

prompt = st.chat_input("Ask the LLM something...")


if prompt:

    # ----------------------------------------------
    # Display user message
    # ----------------------------------------------

    with st.chat_message("user"):

        st.markdown(prompt)


    # ----------------------------------------------
    # Save user message
    # ----------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # ----------------------------------------------
    # Send entire conversation to Ollama
    # ----------------------------------------------

    data = {
        "model": MODEL,
        "messages": st.session_state.messages,
        "stream": False,

        "options": {
            "temperature": 0.7,
            "num_ctx": 8192
        }
    }


    json_data = json.dumps(data).encode("utf-8")


    request = urllib.request.Request(
        OLLAMA_URL,
        data=json_data,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )


    # ----------------------------------------------
    # Call Ollama
    # ----------------------------------------------

    try:

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                with urllib.request.urlopen(
                    request,
                    timeout=120
                ) as response:

                    response_data = (
                        response
                        .read()
                        .decode("utf-8")
                    )


            result = json.loads(response_data)

            answer = result["message"]["content"]

            st.markdown(answer)


        # ------------------------------------------
        # Save assistant response
        # ------------------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


    except urllib.error.URLError as e:

        st.error(
            "Could not connect to Ollama. "
            "Make sure Ollama is running."
        )

        st.error(str(e))


    except Exception as e:

        st.error("An error occurred.")

        st.error(str(e))


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("Chat Controls")

    if st.button("🗑️ Clear Conversation"):

        st.session_state.messages = []

        st.rerun()


    st.write(
        f"Messages in conversation: "
        f"{len(st.session_state.messages)}"
    )


# Run the application
# python -m streamlit run subhashkumar_module5_7.py