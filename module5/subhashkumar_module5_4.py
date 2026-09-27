# subhashkumar_module5_4.py
# make python code to answer the result from user but give the LLM a persona using system prompt. 
# What is system prompt? 
'''
What is a system prompt?

A system prompt is an instruction given to the LLM that tells it how it should behave or respond.
For example:
You are a helpful Python teacher.
Explain Python concepts in simple language.
Give examples when appropriate.

Then the user can ask:
What is a Python function?
The LLM uses both:
System prompt
      +
User question
      ↓
     LLM
      ↓
Response following the requested persona

'''
import urllib.request
import json


def call_ollama(user_text):
    """Send user text to Ollama using a Python teacher persona."""

    # Ollama API URL.
    api_url = "http://localhost:11434/api/chat"

    # Define the persona and behavior of the LLM.
    system_prompt = """
    You are a friendly Python teacher.

    Explain Python concepts in simple language.
    Assume the user is a beginner.
    Give a simple example when useful.
    Do not use unnecessarily complicated technical terms.
    """

    # Create the request data.
    request_data = {
        "model": "llama3.2",

        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_text
            }
        ],

        "stream": False
    }

    # Convert the Python dictionary into JSON.
    json_data = json.dumps(request_data).encode("utf-8")

    # Create the HTTP POST request.
    request = urllib.request.Request(
        api_url,
        data=json_data,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    # Send the request to Ollama.
    with urllib.request.urlopen(request) as response:

        # Read the response.
        response_data = response.read()

        # Convert JSON into a Python dictionary.
        result = json.loads(response_data)

    # Return the LLM's response.
    return result["message"]["content"]


def main():
    """Get a question from the user and display the LLM response."""

    # Ask the user for a question.
    user_text = input("Ask a Python question: ")

    # Send the question to Ollama.
    answer = call_ollama(user_text)

    # Display the answer.
    print("\nLLM Response:")
    print(answer)


if __name__ == "__main__":
    main()