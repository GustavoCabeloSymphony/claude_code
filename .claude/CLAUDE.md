## Atlassian MCP Authentication
When setting up or troubleshooting Atlassian MCP connections:

1. Check `~/.claude.json` for MCP configuration (NOT other locations)
2. If OAuth tokens are cached and stale, a full session restart is required - do not repeatedly retry within the same session
3. If authentication fails with 401, check if API tokens are blocked by org admin policy before trying alternative approaches
4. Never repeatedly cycle through transport methods (SSE, STDIO, OAuth) without user direction - ask which approach to use first

### Restoring Atlassian MCP Configuration

**Backup Location**: `.claude/atlassian-mcp-config-backup.json`

**Current Working Configuration** (using mcp-remote with SSE):
```json
{
  "atlassian": {
    "type": "stdio",
    "command": "npx",
    "args": [
      "-y",
      "mcp-remote",
      "https://mcp.atlassian.com/v1/sse"
    ],
    "env": {}
  }
}
```

**How to Restore**:
1. Open `~/.claude.json` in a text editor
2. Navigate to the project-specific configuration at: `projects["/Users/gcabelo/Symphony/Projects/claude_code"]["mcpServers"]`
3. Add or replace the `atlassian` entry with the configuration from the backup file
4. Save the file
5. **Restart Claude Code completely** (not just the session - full application restart)
6. OAuth authentication will be triggered on first use - complete the browser-based authentication flow
7. Test the connection with a simple Atlassian tool call (e.g., search or get user info)

**Important Notes**:
- This is a **project-specific** configuration (not global)
- Uses `mcp-remote` to connect via SSE (Server-Sent Events)
- Requires `npx` to be available (Node.js installed)
- OAuth tokens are cached separately - if they become stale, full restart is required
- Do NOT manually add OAuth tokens - they are managed automatically during the authentication flow
   
## Before Changing Configuration

Before modifying any MCP or environment configuration, check these rules:

- [ ] Read the existing config from `~/.claude.json` FIRST before suggesting changes
- [ ] If something fails once, ask the user which approach to try - don't cycle through options automatically
- [ ] Never retry authentication/connection errors in the same session - tell user to restart Claude Code
- [ ] Don't remove and re-add servers as troubleshooting - diagnose the actual issue first
- [ ] For Python projects, ask about virtual environments before installing any packages

## MCP Configuration

- MCP server configs are stored in `~/.claude.json` - always check there first
- After changing MCP credentials or config, inform the user a restart is needed rather than retrying in-session
- Do not remove and re-add MCP servers repeatedly as a troubleshooting strategy

## General Rules

- When the user asks to try their existing configuration first, do that before suggesting alternatives
- Do not install packages globally - always ask about virtual environments for Python projects
- When a first approach fails, explain why it failed and ask the user which direction to go rather than silently trying a different approach
