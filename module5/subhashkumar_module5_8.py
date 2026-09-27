# subhashkumar_module5_2.py
# adjust the previous code to remember all past interactions and store them. 
# If I open the UI, the results from previous chat should exist. 


import streamlit as st
import urllib.request
import urllib.error
import json
import os


# ==================================================
# Configuration
# ==================================================

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

# File where the conversation will be permanently stored
CHAT_FILE = "chat_history.json"

CONTEXT_WINDOW = 8192
TEMPERATURE = 0.7


# ==================================================
# Page configuration
# ==================================================

st.set_page_config(
    page_title="Ollama Chat",
    page_icon="🤖"
)

st.title("🤖 Ollama Chat")

st.caption(
    "Persistent chat - previous conversations are saved locally."
)


# ==================================================
# Load conversation from file
# ==================================================

def load_chat_history():

    if not os.path.exists(CHAT_FILE):
        return []

    try:

        with open(
            CHAT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception as e:

        st.warning(
            f"Could not read chat history: {e}"
        )

        return []


# ==================================================
# Save conversation to file
# ==================================================

def save_chat_history(messages):

    try:

        with open(
            CHAT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                messages,
                file,
                indent=4,
                ensure_ascii=False
            )

    except Exception as e:

        st.error(
            f"Could not save chat history: {e}"
        )


# ==================================================
# Initialize session state
# ==================================================

if "messages" not in st.session_state:

    st.session_state.messages = load_chat_history()


# ==================================================
# Display previous conversation
# ==================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ==================================================
# Chat input
# ==================================================

prompt = st.chat_input(
    "Ask the LLM something..."
)


if prompt:

    # ----------------------------------------------
    # Display user question
    # ----------------------------------------------

    with st.chat_message("user"):

        st.markdown(prompt)


    # ----------------------------------------------
    # Store user question
    # ----------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # Save immediately
    save_chat_history(
        st.session_state.messages
    )


    # ----------------------------------------------
    # Prepare request for Ollama
    # ----------------------------------------------

    data = {

        "model": MODEL,

        # Send entire conversation
        "messages": st.session_state.messages,

        "stream": False,

        "options": {

            "temperature": TEMPERATURE,

            "num_ctx": CONTEXT_WINDOW
        }
    }


    json_data = json.dumps(
        data
    ).encode("utf-8")


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


            result = json.loads(
                response_data
            )


            answer = result["message"]["content"]


            # Display answer
            st.markdown(answer)


        # ------------------------------------------
        # Store assistant response
        # ------------------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        # ------------------------------------------
        # Permanently save conversation
        # ------------------------------------------

        save_chat_history(
            st.session_state.messages
        )


    except urllib.error.URLError as e:

        st.error(
            "Could not connect to Ollama."
        )

        st.error(
            "Make sure Ollama is running."
        )

        st.error(str(e))


    except Exception as e:

        st.error(
            "An error occurred."
        )

        st.error(str(e))


# ==================================================
# Sidebar
# ==================================================

with st.sidebar:

    st.header("Chat Controls")


    # ----------------------------------------------
    # Conversation information
    # ----------------------------------------------

    st.write(
        f"Messages stored: "
        f"{len(st.session_state.messages)}"
    )


    # ----------------------------------------------
    # Clear conversation
    # ----------------------------------------------

    if st.button(
        "🗑️ Clear Conversation"
    ):

        st.session_state.messages = []

        save_chat_history([])

        st.rerun()


    # ----------------------------------------------
    # Show storage location
    # ----------------------------------------------

    st.divider()

    st.write("Chat history file:")

    st.code(CHAT_FILE)



# Run the application
# python -m streamlit run subhashkumar_module5_8.py