/**
 * Search restaurants in Madrid via the POS.DO MCP server (JSON-RPC over HTTP).
 *
 * Run: node search_example.js
 *
 * No dependencies — uses Node 18+ global fetch.
 */

const ENDPOINT = "https://pos.do/mcp";

async function callTool(name, args) {
  const response = await fetch(ENDPOINT, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: 1,
      method: "tools/call",
      params: { name, arguments: args },
    }),
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  const rpc = await response.json();
  if (rpc.error) {
    throw new Error(`MCP error: ${JSON.stringify(rpc.error)}`);
  }
  // tools/call wraps the JSON payload as a string inside content[0].text.
  return JSON.parse(rpc.result.content[0].text);
}

(async () => {
  const result = await callTool("search_restaurants", {
    city: "Madrid",
    cuisine: "italian",
    features: "terrace",
    limit: 5,
  });
  console.log(`Found ${result.count} restaurants near ${result.city}:\n`);
  for (const r of result.restaurants || []) {
    console.log(
      `  ${r.name.padEnd(40)}  rating=${r.google_rating}  cuisine=${r.cuisine_type}`
    );
  }
})();
