# subhashkumar_module7_3.py

import urllib.request
import json


# IP address of the computer running FastAPI
server_ip = "192.168.1.50"

url = f"http://{server_ip}:8000/server-health"


# POST request does not require a body for this example
request = urllib.request.Request(
    url,
    method="POST",
    headers={
        "Content-Type": "application/json"
    },
    data=b"{}"
)


try:

    with urllib.request.urlopen(request) as response:

        result = response.read().decode("utf-8")

        data = json.loads(result)

        print("Server Response:")
        print(json.dumps(data, indent=4))


except Exception as e:

    print("Error calling API:")
    print(e)