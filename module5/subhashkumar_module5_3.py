# subhashkumar_module5_3.py
# make python code to call ollama API and get result. The text input will be from user   

# ollama pull llama3.2

'''
Available endpoints
localhost:11434
       |
       +-- /api/generate
       +-- /api/chat
       +-- /api/tags
       +-- /api/show
       +-- /api/pull
       +-- /api/delete
       +-- /api/copy
       +-- /api/ps
       +-- /api/embed
       +-- /api/version
       
'''
import urllib.request
import json


def call_ollama(user_text):
    """Send user text to Ollama and return the generated response."""

    # Ollama's local API URL.
    api_url = "http://localhost:11434/api/generate"

    # Create the data that will be sent to Ollama.
    request_data = {
        "model": "llama3.2",
        "prompt": user_text,
        "stream": False
    }

    # Convert the Python dictionary to JSON.
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

        # Read the response from Ollama.
        response_data = response.read()

        # Convert the JSON response into a Python dictionary.
        result = json.loads(response_data)

    # Return only the generated answer.
    return result["response"]


def main():
    """Get text from the user and send it to Ollama."""

    # Ask the user for input.
    user_text = input("Enter your question: ")

    # Call Ollama with the user's text.
    result = call_ollama(user_text)

    # Display Ollama's response.
    print("\nOllama response:")
    print(result)


if __name__ == "__main__":
    main()