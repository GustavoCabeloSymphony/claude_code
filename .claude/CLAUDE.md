## Atlassian MCP Authentication
When setting up or troubleshooting Atlassian MCP connections:

1. Check `~/.claude.json` for MCP configuration (NOT other locations)
2. If OAuth tokens are cached and stale, a full session restart is required - do not repeatedly retry within the same session
3. If authentication fails with 401, check if API tokens are blocked by org admin policy before trying alternative approaches
4. Never repeatedly cycle through transport methods (SSE, STDIO, OAuth) without user direction - ask which approach to use first
   Add under a ## MCP Configuration section, or merge with the Atlassian section above
   
## MCP Configuration

- MCP server configs are stored in `~/.claude.json` - always check there first
- After changing MCP credentials or config, inform the user a restart is needed rather than retrying in-session
- Do not remove and re-add MCP servers repeatedly as a troubleshooting strategy

## General Rules

- When the user asks to try their existing configuration first, do that before suggesting alternatives
- Do not install packages globally - always ask about virtual environments for Python projects
- When a first approach fails, explain why it failed and ask the user which direction to go rather than silently trying a different approach
