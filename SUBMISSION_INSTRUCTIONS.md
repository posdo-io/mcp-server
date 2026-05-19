# Directory Submission — status and manual follow-ups

Captured on 2026-05-19 during the initial release sprint.

## Status

| Directory | Method | Status | Identifier |
|---|---|---|---|
| **Official MCP Registry** | `mcp-publisher` CLI (GitHub OAuth) | ✅ Published | `io.github.posdo-io/mcp-server@0.1.0` |
| **PulseMCP** | Ingests weekly from the Official Registry | ⏳ Auto, ETA <7 days | (will appear at pulsemcp.com after weekly sync) |
| **mcpmarket (Cline)** | GitHub issue on `cline/mcp-marketplace` | ✅ Issue created | [#1618](https://github.com/cline/mcp-marketplace/issues/1618) — review pending (typically 2 days) |
| **Smithery** | CLI `smithery mcp publish` requires API key signup | ⏸️ Manual | See below |
| **Glama** | Web form on `glama.ai/mcp/servers/add` requires login | ⏸️ Manual | See below |

## Manual follow-ups

### Smithery (5 min)

1. Sign up at https://smithery.ai (Google or GitHub OAuth)
2. Generate an API key at https://smithery.ai/account/api-keys
3. Run from any shell:

   ```bash
   npm install -g @smithery/cli
   export SMITHERY_API_KEY=sk_xxx   # paste key from step 2
   smithery mcp publish https://pos.do/mcp -n posdo-io/mcp-server
   ```

   If the CLI prompts interactively for the key, paste it then.

Smithery also auto-scans `https://pos.do/.well-known/mcp/server-card.json` once you submit the URL, so all 7 tools should populate automatically.

### Glama (3 min)

1. Sign in at https://glama.ai (GitHub OAuth)
2. Open https://glama.ai/mcp/servers/add
3. Paste the repo URL: `https://github.com/posdo-io/mcp-server`
4. Submit. Glama runs an MCP Inspector session against `https://pos.do/mcp` and indexes the 7 tools.

The repo has the `mcp`, `mcp-server`, `model-context-protocol` GitHub topics applied, so Glama's crawler may pick it up even without manual submission. Manual submit is faster.

### Optional: PulseMCP nudge

PulseMCP ingests the Official MCP Registry weekly. If you want to expedite the listing:

1. Go to https://www.pulsemcp.com/contact
2. Mention `io.github.posdo-io/mcp-server` is live on the Official Registry
3. They may run the sync ad-hoc

### Optional: GitHub org avatar

The `posdo-io` GitHub org has no avatar set. To use this server's logo as the org avatar:

1. Go to https://github.com/organizations/posdo-io/settings/profile
2. Upload `logo.png` from this repo (already 400×400, brand-aligned)

GitHub's REST API does not support org avatar upload (only via UI).

## Re-verification after manual follow-ups

After Smithery / Glama submissions complete, confirm the listings:

```bash
# Smithery — public server page
curl -sI "https://smithery.ai/server/posdo-io/mcp-server" | head -2

# Glama — public server page
curl -sI "https://glama.ai/mcp/servers/posdo-io/mcp-server" | head -2

# Official Registry — already published, this checks visibility
curl -sS "https://registry.modelcontextprotocol.io/v0/servers?name=io.github.posdo-io/mcp-server" \
  | jq '.servers[0] | {name, version, status}'
```

## Re-publishing a new version

When the server changes (new tool, new field, new coverage milestone):

1. Bump `version` in `server.json` and `CHANGELOG.md`
2. Tag the repo: `git tag -a vX.Y.Z -m "..."` and `git push origin vX.Y.Z`
3. Re-run the publisher: `mcp-publisher login github -token $GITHUB_TOKEN && mcp-publisher publish`
4. Smithery + Glama re-scan on schedule (Smithery accepts manual `smithery mcp publish` re-runs too)
5. mcpmarket update: open a new issue or comment on the original one if minor
