# subhashkumar_module5_2.py
# make UI using streamlit to interact with LLM to get user question and return the result. 
# What is streamlit ? 
'''
What is Streamlit?

Streamlit is useful for turning a Python script into an interactive web application.

For example, this:
name = st.text_input("Enter your name")
st.write("Hello", name)

creates a textbox and displays the result in a browser.

You can use Streamlit for:

Chatbots
LLM applications
Data dashboards
Machine-learning demos
AI prototypes
Data visualization
Internal tools

'''
#python -m pip install streamlit

import streamlit as st
import urllib.request
import json


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"


st.title("🤖 Ollama LLM Chat")

st.write("Ask a question and get an answer from the LLM.")

# User input
question = st.text_area(
    "Enter your question:",
    height=100
)

# Temperature
temperature = st.slider(
    "Temperature",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.1
)

# Context window
context_window = st.selectbox(
    "Context Window",
    [2048, 4096, 8192, 16384],
    index=2
)


if st.button("Ask LLM"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        data = {
            "model": MODEL,
            "prompt": question,
            "stream": False,
            "options": {
                "num_ctx": context_window,
                "temperature": temperature
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

        try:

            with st.spinner("LLM is thinking..."):

                with urllib.request.urlopen(
                    request,
                    timeout=120
                ) as response:

                    response_data = response.read().decode("utf-8")

                    result = json.loads(response_data)

            st.subheader("LLM Response")

            st.write(result["response"])

        except urllib.error.URLError as e:

            st.error(
                "Could not connect to Ollama. "
                "Make sure Ollama is running."
            )

            st.error(str(e))

        except Exception as e:

            st.error("An error occurred.")

            st.error(str(e))

# Run the application
# python -m streamlit run subhashkumar_module5_6.py