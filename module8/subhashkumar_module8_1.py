# subhashkumar_module8_1.py

# make MCP to show system date and random number. What is MCP?  What are tools? Is there system prompt? 

# show MCP result using an MCP viewer. 

"""
What is MCP?

MCP = Model Context Protocol.

Think of MCP as a standard connection between an AI application and external capabilities.

For example:

                 MCP
                  │
        ┌─────────┴─────────┐
        │                   │
      Tool 1              Tool 2
   System Date         Random Number
        │                   │
        └─────────┬─────────┘
                  │
              MCP Server

An MCP server can expose tools, resources, and prompts to an MCP client/host.

What is a Tool?

An MCP tool is an operation that an AI application can call.

For example:

@mcp.tool()
def get_system_date():
    ...

This tells MCP:

"I have an operation called get_system_date that can be called by an MCP client."


What about System Prompt?

This is an important distinction.

MCP does NOT require a system prompt.

We can have:

MCP Server
   │
   ├── Tool: get_system_date
   └── Tool: get_random_number

with no LLM at all.

The MCP server simply provides tools.

For example:

MCP Inspector
       │
       │ call get_random_number
       ▼
MCP Server
       │
       ▼
Random number = 5832

No system prompt is involved.

A system prompt belongs to the LLM interaction, not to the basic MCP tool itself.

MCP also has a separate concept called an MCP Prompt. An MCP prompt is a user-selectable message template, which is different from an LLM system prompt.

So:

Concept	Purpose
MCP Tool	Performs an operation
MCP Resource	Provides data/context
MCP Prompt	Provides a reusable prompt template
System Prompt	Gives instructions to an LLM

"""


from datetime import datetime
import random

from mcp.server.fastmcp import FastMCP


# Create MCP server
mcp = FastMCP("System Information Server")


@mcp.tool()
def get_system_date() -> str:
    """
    Return the current system date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@mcp.tool()
def get_random_number() -> int:
    """
    Generate a random number between 1 and 1000.
    """
    return random.randint(1, 1000)


if __name__ == "__main__":
    mcp.run()


#Show the result using MCP Inspector

#mcp dev subhashkumar_module8_1.py
# python -m mcp dev subhashkumar_module8_1.py

"""
MCP Inspector
────────────────────────────

Server: System Information Server

Tools
 ├── get_system_date
 │
 └── get_random_number
 
"""