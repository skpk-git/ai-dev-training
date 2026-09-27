# subhashkumar_module5_2.py
# 
# make a python code to increase the context windows of LLM and change its temperature. 
# What is temperature?    

'''
What is temperature?

Temperature controls how random/creative the LLM's responses are.

0.0     → very predictable, focused, usually best for factual/technical tasks
0.3 0.7 → balanced
0.8 1.2 → more varied and creative

Higher values → more randomness, but potentially less consistent answers

For example, if you ask:

"Give me a name for a Python calculator program."

At low temperature, you might repeatedly get:

Python Calculator

At higher temperature, you might get:

CalcMaster, PyCalc, NumForge, QuickCalc

Context window

The context window is the amount of text/tokens the model can consider in a single request, 
including the conversation/history and your current prompt.

With Ollama, you can set it using num_ctx, and temperature options.
'''

#import requests
import urllib.request
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

context_window = int(input("Context window (e.g. 4096, 8192, 16384): "))
temperature = float(input("Temperature (e.g. 0.0, 0.7, 1.0): "))

prompt = input("\nEnter your question: ")

data = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False,
    "options": {
        "num_ctx": context_window,
        "temperature": temperature
    }
}

# Convert Python dictionary to JSON
json_data = json.dumps(data).encode("utf-8")

# Create HTTP request
request = urllib.request.Request(
    OLLAMA_URL,
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    with urllib.request.urlopen(request, timeout=120) as response:

        # Read response
        response_data = response.read().decode("utf-8")

        # Convert JSON response to Python dictionary
        result = json.loads(response_data)

        print("\n--- Response ---")
        print(result["response"])

except urllib.error.URLError as e:
    print("Could not connect to Ollama:")
    print(e)

except Exception as e:
    print("Error:")
    print(e)

#response = requests.post(OLLAMA_URL, json=data)
# if response.ok:
#     result = response.json()
#     print("\n--- Response ---")
#     print(result["response"])
# else:
#     print("HTTP Error:", response.status_code)
#     print(response.text)