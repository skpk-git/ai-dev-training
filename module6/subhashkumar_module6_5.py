# subhashkumar_module6_5.py

#Use langchain framework to make an agent to do math operations. Then connect another agent to get the output of first agent and reflect on it. 

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama


# ---------------------------------------------------------
# Calculator tool
# ---------------------------------------------------------

@tool
def calculator(expression: str) -> str:
    """
    Perform a basic mathematical calculation.

    Example:
        25 * 4
        100 / 5
        (10 + 5) * 2
    """

    try:
        # Simple demonstration only.
        # Do NOT use unrestricted eval() with untrusted input
        # in a production application.
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"


# ---------------------------------------------------------
# Agent 1 - Math Agent
# ---------------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

math_agent = create_agent(
    model=llm,
    tools=[calculator],
    system_prompt="""
    You are a mathematics agent.

    Solve the user's mathematical problem.

    Always use the calculator tool for calculations
    instead of calculating manually.

    Return the calculation and the final answer clearly.
    """
)


# ---------------------------------------------------------
# Agent 2 - Reflection Agent
# ---------------------------------------------------------

reflection_agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="""
    You are a reflection and verification agent.

    You will receive the output produced by another
    mathematics agent.

    Carefully review the mathematical calculation.

    Check:
    1. Whether the calculation is correct.
    2. Whether the reasoning makes sense.
    3. Whether the final answer matches the calculation.

    If it is correct, say that it is correct.

    If it is incorrect, explain the mistake and provide
    the corrected answer.
    """
)


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

while True:

    question = input("\nEnter a math question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    # -----------------------------------------------------
    # Agent 1 processes the question
    # -----------------------------------------------------

    math_result = math_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    math_output = math_result["messages"][-1].content

    print("\n===== AGENT 1: MATH AGENT =====")
    print(math_output)


    # -----------------------------------------------------
    # Agent 2 receives Agent 1's output
    # -----------------------------------------------------

    reflection_prompt = f"""
    The user asked:

    {question}

    The mathematics agent produced this answer:

    {math_output}

    Review this answer carefully and provide your
    verification.
    """

    reflection_result = reflection_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": reflection_prompt
            }
        ]
    })

    reflection_output = reflection_result["messages"][-1].content

    print("\n===== AGENT 2: REFLECTION AGENT =====")
    print(reflection_output)