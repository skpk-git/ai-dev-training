# subhashkumar_module6_4.py

#Use langchain framework to make an agent to do math operations. 

# python -m pip install langchain langchain-ollama
    

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama


# --------------------------------------------------
# Math tool
# --------------------------------------------------

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression.

    Use this tool for addition, subtraction,
    multiplication, division and other basic
    mathematical calculations.
    """

    try:
        # Evaluate the mathematical expression
        result = eval(expression, {"__builtins__": {}}, {})

        return str(result)

    except Exception as e:
        return f"Error calculating expression: {e}"


# --------------------------------------------------
# Local LLM
# --------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# --------------------------------------------------
# Create LangChain agent
# --------------------------------------------------

agent = create_agent(
    model=llm,
    tools=[calculator],
    system_prompt="""
You are a helpful math assistant.

When the user asks you to perform a mathematical
calculation, use the calculator tool.

Always use the calculator tool instead of trying
to calculate the answer yourself.
"""
)


# --------------------------------------------------
# Get question from user
# --------------------------------------------------

while True:

    question = input(
        "\nEnter a math question (or type exit): "
    )

    if question.lower() == "exit":
        break

    # Run the agent
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    # Get final response
    print("\nAnswer:")

    print(
        result["messages"][-1].content
    )

