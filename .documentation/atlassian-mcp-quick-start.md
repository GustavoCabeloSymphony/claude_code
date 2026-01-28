# Atlassian MCP Quick Start Guide

**Quick reference for setting up Atlassian MCP with Claude Code or Cursor**

This guide covers setup for both Claude Code and Cursor. Choose the instructions for your tool.

> For complete documentation, see [Atlassian MCP Integration - Complete Guide](./atlassian-mcp-claude-code-integration-2026-01-08.md)

## Prerequisites Checklist

- [ ] Node.js v18+ installed (`node --version`)
- [ ] Atlassian Cloud account with Jira/Confluence access
- [ ] Claude Code or Cursor installed and up to date
- [ ] Modern web browser for OAuth

## Installation

### For Claude Code

#### Method 1: Official Server with OAuth (Recommended)

Uses browser-based OAuth authentication - no API tokens needed.

```bash
# User scope (available across all projects)
claude mcp add --transport stdio atlassian npx -- -y mcp-remote https://mcp.atlassian.com/v1/sse

# Project scope (shared with team - each user authenticates with their own account)
cd /path/to/your/project
claude mcp add --transport stdio atlassian npx -- -y mcp-remote https://mcp.atlassian.com/v1/sse
```

**What happens next:**
1. Restart Claude Code
2. When you use any Atlassian tool, a browser window opens for OAuth authentication
3. Log in with your Atlassian account
4. Connection established - you're ready to go!

**Team setup note:** When configured at project level, the MCP server is shared but each team member authenticates with their own Atlassian account via OAuth.

#### Method 2: Manual Configuration

Edit `~/.claude.json` and add to the appropriate section:

**For user scope** (add to root-level `mcpServers`):
```json
{
  "mcpServers": {
    "atlassian": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"],
      "env": {}
    }
  }
}
```

**For project scope** (add to your project's `mcpServers`):
```json
{
  "projects": {
    "/path/to/your/project": {
      "mcpServers": {
        "atlassian": {
          "type": "stdio",
          "command": "npx",
          "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"],
          "env": {}
        }
      }
    }
  }
}
```

**After manual configuration:** Restart Claude Code for changes to take effect.

#### Method 3: Self-Hosted (API Tokens)

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

### For Cursor

#### Method 1: Cursor Settings UI (Recommended)

1. **Open Cursor Settings**:
   - macOS: `Cursor` → `Settings` → `Features` → `MCP Servers`
   - Windows/Linux: `File` → `Preferences` → `Settings` → `Features` → `MCP Servers`

2. **Add New MCP Server**:
   - Click "Add MCP Server"
   - Name: `atlassian`
   - Command: `npx`
   - Args: `-y`, `mcp-remote`, `https://mcp.atlassian.com/v1/sse`

3. **Restart Cursor** for changes to take effect

4. **Authenticate**: When you first use an Atlassian tool, a browser window opens for OAuth authentication

#### Method 2: Manual Configuration

**For workspace scope** (shared with team):

Create or edit `.cursor/mcp.json` in your project root:

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"]
    }
  }
}
```

**For user scope** (available across all projects):

Edit `~/.cursor/config.json`:

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"]
    }
  }
}
```

**After manual configuration:** Restart Cursor for changes to take effect.

#### What Happens Next (OAuth Flow)

1. Restart Cursor
2. Ask Cursor AI to use an Atlassian tool (e.g., "Get my Atlassian user information")
3. Browser opens for OAuth authentication
4. Log in with your Atlassian account
5. Connection established!

## Switching Atlassian Accounts (OAuth Method)

To change which Atlassian account is connected:

### Claude Code

```bash
# Remove the existing MCP server
claude mcp remove atlassian

# Re-add it (same command as installation)
claude mcp add --transport stdio atlassian npx -- -y mcp-remote https://mcp.atlassian.com/v1/sse

# Restart Claude Code
```

### Cursor

1. Remove MCP server via Settings UI or delete from config JSON
2. Re-add using installation method above
3. Restart Cursor

**For both tools:** When you next use an Atlassian tool, the OAuth flow will trigger and you can authenticate with a different account.

## Team/Shared Project Setup

When multiple team members work on the same project:

**What's Shared:**
- MCP server configuration (the `npx mcp-remote` command)
- Configuration file committed to version control

**What's Per-User:**
- OAuth authentication (each user logs in with their own Atlassian account)
- Access permissions (based on individual Atlassian account)
- Browser authentication session

### Setup Process for Claude Code

1. **One team member adds the MCP server** (project scope):
   ```bash
   cd /path/to/your/project
   claude mcp add --transport stdio atlassian npx -- -y mcp-remote https://mcp.atlassian.com/v1/sse
   ```

2. **Configuration is shared** via `~/.claude.json` (can be committed to git if desired, contains no secrets)

3. **Each team member:**
   - Opens the project in Claude Code
   - Restarts Claude Code
   - Uses any Atlassian tool to trigger OAuth authentication
   - Authenticates with their own Atlassian account

### Setup Process for Cursor

1. **One team member creates** `.cursor/mcp.json` in project root:
   ```json
   {
     "mcpServers": {
       "atlassian": {
         "command": "npx",
         "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"]
       }
     }
   }
   ```

2. **Commit to git** (this file contains no secrets, only the MCP server configuration)

3. **Each team member:**
   - Pulls the project
   - Restarts Cursor
   - Uses any Atlassian tool to trigger OAuth authentication
   - Authenticates with their own Atlassian account

**Result:** Everyone uses the same MCP server but with their own credentials and permissions.

## Verification

### Claude Code

```bash
# Check connection status
claude mcp list

# Should show:
# atlassian: npx -y mcp-remote https://mcp.atlassian.com/v1/sse - ✓ Connected
```

**Testing the connection:**

```bash
# Get your Atlassian user info (triggers OAuth if first time)
"Get my Atlassian user information"

# List accessible resources
"What Atlassian sites do I have access to?"

# Test Jira access
"List my Jira projects"

# Test Confluence access
"List my Confluence spaces"
```

### Cursor

**Check MCP Status:**
- Open Cursor Settings → Features → MCP Servers
- Verify `atlassian` server is listed and active

**Testing the connection:**

In Cursor AI chat, try:
```text
Get my Atlassian user information
```

If successful, you'll see your Atlassian account details. Then try:
```bash
What Atlassian sites do I have access to?
List my Jira projects
List my Confluence spaces
```

## First Steps

After OAuth authentication is complete, try these commands (works in both Claude Code and Cursor):

```bash
"Search Jira for recent issues in project [YOUR-PROJECT-KEY]"

"Create a Jira ticket: [YOUR DESCRIPTION]"

"Search Confluence for documentation about [TOPIC]"

"Show me all high-priority bugs in [PROJECT]"
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

### Tools Not Available After Installation?

**Claude Code:** Restart Claude Code - this is required after adding the MCP server.

**Cursor:**
- Restart Cursor after configuration changes
- Check Settings → Features → MCP Servers to verify server is active
- Look for error messages in MCP server status

### OAuth Authentication Issues?

**Browser window doesn't open:**
- Check that Node.js v18+ is installed (`node --version`)
- Ensure your browser isn't blocking popups
- Try manually opening: https://mcp.atlassian.com

**Wrong account authenticated:**

Claude Code:
```bash
# Remove and re-add to trigger new OAuth flow
claude mcp remove atlassian
claude mcp add --transport stdio atlassian npx -- -y mcp-remote https://mcp.atlassian.com/v1/sse
# Restart Claude Code, then authenticate with correct account
```

Cursor:
- Remove MCP server from Settings UI or delete from config file
- Re-add the server
- Restart Cursor
- Authenticate with the correct account when prompted

**Connection shows as disconnected:**
```bash
# Check MCP status
claude mcp list

# If disconnected, try using a tool to trigger reconnection
# Or restart Claude Code
```

### Windows Issues?
```bash
# Use cmd /c wrapper:
claude mcp add --transport stdio atlassian -- cmd /c npx -y mcp-remote https://mcp.atlassian.com/v1/sse
```

### Can't Access Certain Projects/Spaces?
- OAuth uses your personal Atlassian account permissions
- Ensure your account has access to the Jira projects or Confluence spaces
- Check permissions at your Atlassian site admin panel

## Configuration File Locations

### Claude Code

```bash
# User scope
~/.claude.json

# Project scope (in ~/.claude.json under "projects" section)
~/.claude.json

# Logs
# macOS: ~/Library/Logs/Claude Code/
# Linux: ~/.config/Claude Code/logs/
# Windows: %APPDATA%\Claude Code\logs\
```

### Cursor

```bash
# Workspace scope (team-shared)
<project-root>/.cursor/mcp.json

# User scope
~/.cursor/config.json

# Logs
# macOS: ~/Library/Application Support/Cursor/logs/
# Linux: ~/.config/Cursor/logs/
# Windows: %APPDATA%\Cursor\logs\
```

**Important:**
- OAuth credentials are managed by `mcp-remote` via browser authentication
- No API tokens or passwords are stored in config files
- Each user authenticates independently with their own Atlassian account
- Configuration files only contain the MCP server setup (safe to commit to git)

## Useful Links

- 📖 **Full Documentation**: [Complete Guide](./atlassian-mcp-claude-code-integration-2026-01-08.md)
- 🔐 **API Tokens**: https://id.atlassian.com/manage-profile/security/api-tokens
- 📊 **Atlassian Status**: https://status.atlassian.com
- 🐛 **Report Issues**: https://github.com/anthropics/claude-code/issues
- 📘 **MCP Docs**: https://modelcontextprotocol.io

## Next Steps

1. ✅ Install and verify connection
2. ✅ Try basic commands in your AI coding assistant
3. ✅ Explore your Jira projects and Confluence spaces
4. ✅ Read the [complete guide](./atlassian-mcp-claude-code-integration-2026-01-08.md) for advanced features
5. ✅ Check out real-world [use cases](./atlassian-mcp-claude-code-integration-2026-01-08.md#use-cases-and-examples)

---

**Need Help?** See the [troubleshooting section](./atlassian-mcp-claude-code-integration-2026-01-08.md#troubleshooting) in the complete guide.
