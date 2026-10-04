# subhashkumar_module8_3.py

# make an MCP to connect user question to ollama and show the result via the MCP viewer. 

import json
import urllib.request
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Ollama MCP Server")

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"


@mcp.tool()
def ask_ollama(question: str) -> str:
    """
    Send a user question to the local Ollama LLM
    and return the generated answer.
    """

    request_data = {
        "model": OLLAMA_MODEL,
        "prompt": question,
        "stream": False
    }

    data = json.dumps(request_data).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))

        return result["response"]

    except Exception as e:
        return f"Error connecting to Ollama: {e}"


if __name__ == "__main__":
    mcp.run()
