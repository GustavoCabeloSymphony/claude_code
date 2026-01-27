# Atlassian MCP Quick Start Guide

**Quick reference for setting up Atlassian MCP with Claude Code**

> For complete documentation, see [Atlassian MCP Integration - Complete Guide](./atlassian-mcp-claude-code-integration-2026-01-08.md)

## Prerequisites Checklist

- [ ] Node.js v18+ installed (`node --version`)
- [ ] Atlassian Cloud account with Jira/Confluence access
- [ ] Claude Code installed and up to date
- [ ] Modern web browser for OAuth

## Installation (Choose One Method)

### Method 1: Official Server (Recommended)

```bash
# User scope (available across all projects)
claude mcp add atlassian --transport sse "https://mcp.atlassian.com/v1/sse" --scope user

# Project scope (shared with team)
cd /path/to/your/project
claude mcp add atlassian --transport sse "https://mcp.atlassian.com/v1/sse" --scope project
```

### Method 2: Manual Configuration

Create `.mcp.json` in project root:

```json
{
  "mcpServers": {
    "Atlassian": {
      "command": "npx",
      "args": ["-y", "mcp-remote@latest", "https://mcp.atlassian.com/v1/sse"]
    }
  }
}
```

### Method 3: Self-Hosted (API Tokens)

1. **Get API Token**: https://id.atlassian.com/manage-profile/security/api-tokens

2. **Configure with environment variables**:

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": ["mcp-atlassian"],
      "env": {
        "JIRA_URL": "https://your-company.atlassian.net",
        "JIRA_USERNAME": "your.email@company.com",
        "JIRA_API_TOKEN": "your_api_token",
        "CONFLUENCE_URL": "https://your-company.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "your.email@company.com",
        "CONFLUENCE_API_TOKEN": "your_api_token"
      }
    }
  }
}
```

## Verification

```bash
# Check connection status
claude mcp list

# Should show:
# Atlassian
#   Status: ✓ Connected
#   Transport: sse
```

## First Steps in Claude Code

Try these commands in a Claude Code conversation:

```bash
"List all MCP tools available to you."

"Can you access Atlassian Jira and Confluence?"

"Search Jira for recent issues in project [YOUR-PROJECT-KEY]"

"Create a Jira ticket: [YOUR DESCRIPTION]"

"Search Confluence for documentation about [TOPIC]"
```

## Common Use Cases

### 1. Search for Jira Issues
```bash
"Show me all high-priority bugs in the Phoenix project"
```

### 2. Create Documentation
```sql
"Analyze this code and create a Confluence page explaining the architecture"
```

### 3. Create Tickets from Notes
```sql
"Create Jira tickets from this meeting notes document"
```

### 4. Get Ticket Details
```bash
"What are the requirements for PROJ-123?"
```

## Troubleshooting

### Tools Not Available?
```bash
# Restart Claude Code and try again
# Or remove and re-add:
claude mcp remove atlassian
claude mcp add atlassian --transport sse "https://mcp.atlassian.com/v1/sse" --scope user
```

### Authentication Fails?
- Ensure browser isn't blocking popups
- Check that Node.js v18+ is installed
- Try STDIO transport instead of SSE

### Windows Issues?
```bash
# Use cmd /c wrapper:
claude mcp add --transport stdio atlassian -- cmd /c npx -y mcp-remote https://mcp.atlassian.com/v1/sse
```

## Configuration File Locations

```bash
# Project scope
<project-root>/.mcp.json

# User scope
~/.claude.json

# Logs (for debugging)
# macOS: ~/Library/Logs/Claude Code/
# Linux: ~/.config/Claude Code/logs/
# Windows: %APPDATA%\Claude Code\logs\
```

## Useful Links

- 📖 **Full Documentation**: [Complete Guide](./atlassian-mcp-claude-code-integration-2026-01-08.md)
- 🔐 **API Tokens**: https://id.atlassian.com/manage-profile/security/api-tokens
- 📊 **Atlassian Status**: https://status.atlassian.com
- 🐛 **Report Issues**: https://github.com/anthropics/claude-code/issues
- 📘 **MCP Docs**: https://modelcontextprotocol.io

## Next Steps

1. ✅ Install and verify connection
2. ✅ Try basic commands in Claude Code
3. ✅ Explore your Jira projects and Confluence spaces
4. ✅ Read the [complete guide](./atlassian-mcp-claude-code-integration-2026-01-08.md) for advanced features
5. ✅ Check out real-world [use cases](./atlassian-mcp-claude-code-integration-2026-01-08.md#use-cases-and-examples)

---

**Need Help?** See the [troubleshooting section](./atlassian-mcp-claude-code-integration-2026-01-08.md#troubleshooting) in the complete guide.
