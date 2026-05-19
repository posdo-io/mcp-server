"""Search restaurants in Madrid via the POS.DO MCP server (JSON-RPC over HTTP).

Run: python search_example.py

Requires: requests (`pip install requests`).
"""

import json
import sys

import requests

ENDPOINT = "https://pos.do/mcp"


def call_tool(name: str, arguments: dict) -> dict:
    """Invoke an MCP tool via tools/call. Returns the parsed result payload."""
    response = requests.post(
        ENDPOINT,
        headers={"Content-Type": "application/json"},
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments},
        },
        timeout=15,
    )
    response.raise_for_status()
    rpc = response.json()
    if "error" in rpc:
        raise RuntimeError(f"MCP error: {rpc['error']}")
    # tools/call wraps the JSON payload as a string inside content[0].text.
    text = rpc["result"]["content"][0]["text"]
    return json.loads(text)


def main() -> int:
    result = call_tool(
        "search_restaurants",
        {
            "city": "Madrid",
            "cuisine": "italian",
            "features": "terrace",
            "limit": 5,
        },
    )
    print(f"Found {result.get('count', 0)} restaurants near {result['city']}:\n")
    for r in result.get("restaurants", []):
        print(
            f"  {r.get('name'):<40}  "
            f"rating={r.get('google_rating')}  "
            f"cuisine={r.get('cuisine_type')}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
