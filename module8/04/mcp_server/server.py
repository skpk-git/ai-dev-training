import json
import urllib.request

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("User Database MCP Server")

API_URL = "http://127.0.0.1:8000"


def call_api(url, method="GET", data=None):

    headers = {
        "Content-Type": "application/json"
    }

    body = None

    if data is not None:
        body = json.dumps(data).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=body,
        headers=headers,
        method=method
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(
            response.read().decode("utf-8")
        )


@mcp.tool()
def get_users() -> list:
    """
    Get all users from the database.
    """

    return call_api(
        f"{API_URL}/users"
    )


@mcp.tool()
def get_user_by_id(user_id: int) -> dict:
    """
    Get a user using the user ID.
    """

    return call_api(
        f"{API_URL}/users/{user_id}"
    )


@mcp.tool()
def add_user(
    name: str,
    phone: str,
    user_key: str
) -> dict:
    """
    Add a new user to the database.
    """

    return call_api(
        f"{API_URL}/users",
        method="POST",
        data={
            "name": name,
            "phone": phone,
            "user_key": user_key
        }
    )


if __name__ == "__main__":
    mcp.run()

#python -m uvicorn api.api:app --host 127.0.0.1 --port 8000

#mcp dev mcp_server/server.py