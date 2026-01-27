# Atlassian MCP Connection - Quick Setup Guide

**Purpose**: Step-by-step instructions for connecting Claude Code to Atlassian (Jira & Confluence) via MCP
**Last Updated**: 2026-01-13
**Status**: Verified Working

## Platform Compatibility

This guide supports:
- ✓ **macOS** (verified on Darwin 25.2.0)
- ✓ **Linux** (Ubuntu, Debian, RHEL, etc.)
- ✓ **Windows** (Windows 10/11, WSL)

All commands work across platforms unless marked with platform-specific headers.

## Prerequisites

1. **Node.js v18+** - Required for mcp-remote proxy
   ```bash
   node --version  # Verify installation
   ```

   Download from [nodejs.org](https://nodejs.org) for your platform.

2. **Atlassian Cloud Account** with access to Jira/Confluence

3. **Claude Code** - Latest version from [code.claude.com](https://code.claude.com)

## Service Account Setup (Recommended for Team/Production Use)

For automation and production environments, use a dedicated service account instead of personal credentials.

### Step 1: Create Service Account

1. **In Atlassian Admin Console**:
   - Navigate to: https://admin.atlassian.com
   - Go to **Directory** → **Users**
   - Click **Add users** or **Create user**
   - Create account with naming convention (e.g., `claude-integration@company.com` or `service-mcp@company.com`)
   - Use a shared email accessible to the team (or create dedicated mailbox)

2. **Set Strong Password**:
   - Use password manager to generate and store credentials
   - Enable 2FA/MFA if required by organization policy

### Step 2: Add Service Account to Jira Projects

The service account **must be added to each Jira project** it needs to access:

1. **Navigate to Project Settings**:
   - Open Jira project (e.g., PAR, DEV, etc.)
   - Click **Project settings** (gear icon, bottom left)
   - Select **People** or **Users and roles**

2. **Add Service Account**:
   - Click **Add people** or **Add users**
   - Search for the service account email
   - Select the account

3. **Assign Appropriate Role**:
   - **Developer** - Can create, view, edit issues and transitions
   - **Administrator** - Full project access (use sparingly)
   - **Custom Role** - Define specific permissions

**Recommended Permissions for MCP Integration**:
- Browse Projects
- Create Issues
- Edit Issues
- Add Comments
- Transition Issues
- View Development Tools (if needed)

### Step 3: Add Service Account to Confluence Spaces

For Confluence access:

1. **Navigate to Space Settings**:
   - Open Confluence space
   - Click **Space settings** (gear icon)
   - Select **Space permissions**

2. **Add Service Account**:
   - Click **Edit permissions**
   - Under **Individual Users**, add the service account
   - Grant permissions:
     - **View** - Read pages
     - **Add** - Create pages
     - **Edit** - Modify pages
     - **Delete** (optional) - Remove pages

### Step 4: Authenticate MCP with Service Account

When running the OAuth flow (Step 2 of Installation):
- Use the **service account credentials** to log in
- The OAuth tokens will be associated with the service account
- All MCP operations will execute as the service account

**Benefits**:
- ✓ Consistent permissions across team
- ✓ Audit trail shows "service-mcp@company.com" not individual users
- ✓ No disruption when team members leave
- ✓ Centralized permission management

**Important Notes**:
- Service account access is **scoped to projects/spaces** it's been added to
- If you get "permission denied" errors, verify service account is added to the project
- Service account can only perform actions permitted by its assigned role
- OAuth tokens inherit service account permissions

## Installation Steps

### Step 1: Add Atlassian MCP Server

**All Platforms (macOS, Linux, Windows)**:

Run this command to configure the MCP server:

```bash
claude mcp add atlassian --transport sse "https://mcp.atlassian.com/v1/sse" --scope user
```

**Options**:
- `--scope user` - Available across all projects (recommended for personal use)
- `--scope project` - Creates `.mcp.json` in project root (for team collaboration)

**Note for Windows Users**: If you encounter issues with the SSE transport, see the [Authentication Errors](#issue-authentication-errors) troubleshooting section for Windows-specific alternative commands.

### Step 2: Authenticate via OAuth 2.1

After running the command:

1. A browser window will automatically open
2. Navigate to Atlassian login page
3. Log in with your credentials
4. Select your workspace/organization
5. Review and approve requested permissions:
   - Read Jira issues
   - Write Jira issues
   - Read Confluence pages
   - Write Confluence content
6. You'll be redirected to localhost callback
7. Connection confirmed in Claude Code

### Step 3: Verify Connection

```bash
claude mcp list
```

Expected output:
```text
atlassian: https://mcp.atlassian.com/v1/sse (SSE) - ✓ Connected
```

## Basic Usage

### Fetch a Jira Ticket

In Claude Code conversation:
```text
"Fetch ticket PAR-1 from Jira"
```

Claude will use `mcp__atlassian__search` or `mcp__atlassian__getJiraIssue` to retrieve details.

### Search Across Jira and Confluence

```bash
"Search for 'authentication' across Jira and Confluence"
```

### Create a Jira Ticket

```bash
"Create a new task in project PAR with summary 'Setup authentication'
and description 'Implement OAuth 2.1 flow'"
```

### Search Confluence Pages

```text
"Find all Confluence pages about API documentation"
```

## Available Tools

**Jira Operations**:
- `getJiraIssue` - Get issue by ID/key
- `createJiraIssue` - Create new issues
- `editJiraIssue` - Update issues
- `searchJiraIssuesUsingJql` - Search with JQL
- `addCommentToJiraIssue` - Add comments
- `transitionJiraIssue` - Change status

**Confluence Operations**:
- `getConfluencePage` - Get page content
- `createConfluencePage` - Create pages
- `updateConfluencePage` - Update pages
- `searchConfluenceUsingCql` - Search with CQL
- `getConfluenceSpaces` - List spaces

**Unified Search**:
- `search` - Natural language search across Jira & Confluence

## Troubleshooting

### Issue: MCP Tools Not Available

**Solution**:
1. Restart Claude Code
2. Remove and re-add the server:
   ```bash
   claude mcp remove atlassian
   claude mcp add atlassian --transport sse "https://mcp.atlassian.com/v1/sse" --scope user
   ```

### Issue: Authentication Errors

If you encounter authentication errors, try these platform-specific alternatives:

**macOS**:
```bash
# Usually works with standard command, but if issues occur:
claude mcp add --transport stdio atlassian npx -- -y mcp-remote https://mcp.atlassian.com/v1/sse
```

**Windows**:
```bash
# Use cmd /c wrapper
claude mcp add --transport stdio atlassian -- cmd /c npx -y mcp-remote https://mcp.atlassian.com/v1/sse
```

**Linux/WSL**:
```bash
# Use absolute path to npx
claude mcp add --transport stdio atlassian /usr/bin/npx -- -y mcp-remote https://mcp.atlassian.com/v1/sse
```

### Issue: Connection Drops

Try switching from SSE to STDIO transport:
```bash
claude mcp remove atlassian
claude mcp add --transport stdio atlassian npx -- -y mcp-remote https://mcp.atlassian.com/v1/sse
```

## Configuration Files

### File Locations by Platform

**User Scope** (all platforms):

| Platform | Path |
|----------|------|
| **macOS/Linux** | `~/.claude.json` |
| **Windows** | `%USERPROFILE%\.claude.json`<br>(typically `C:\Users\<username>\.claude.json`) |

**Project Scope** (all platforms):
- `<project-root>/.mcp.json` (same for all platforms)

### Example Configuration

Example `.mcp.json` (works on all platforms):
```json
{
  "mcpServers": {
    "Atlassian": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@latest",
        "https://mcp.atlassian.com/v1/sse"
      ]
    }
  }
}
```

## Security Notes

- OAuth 2.1 provides secure authentication
- All traffic encrypted via HTTPS/TLS 1.2+
- Respects existing Jira/Confluence permissions
- Tokens stored securely by mcp-remote
- Session-based authentication with automatic refresh

## Verified Working Setup

**Test Environment**:
- **OS**: macOS Darwin 25.2.0 *(also works on Linux and Windows)*
- **Node.js**: v18+
- **Transport**: SSE (Server-Sent Events)
- **Authentication**: OAuth 2.1
- **Status**: ✓ Connected

**Test Case**:
- Successfully fetched ticket PAR-1
- Search functionality working
- OAuth authentication completed

**Platform-Specific Notes**:
- **macOS/Linux**: Works out of the box with SSE transport
- **Windows**: May require `cmd /c` wrapper for STDIO transport (see troubleshooting)
- **WSL**: Works like native Linux, may need absolute paths

## Useful Links

- **API Token Management**: https://id.atlassian.com/manage-profile/security/api-tokens
- **Atlassian Status**: https://status.atlassian.com
- **Claude Code Docs**: https://code.claude.com/docs
- **MCP Documentation**: https://modelcontextprotocol.io

## Quick Reference Commands

**All Platforms**:
```bash
# List all MCP servers
claude mcp list

# Remove Atlassian server
claude mcp remove atlassian

# Add with user scope (works on all platforms)
claude mcp add atlassian --transport sse "https://mcp.atlassian.com/v1/sse" --scope user

# Add with project scope (works on all platforms)
claude mcp add atlassian --transport sse "https://mcp.atlassian.com/v1/sse" --scope project

# Check in Claude Code conversation
/mcp
```

**Platform-Specific (if SSE fails)**:

macOS/Linux:
```bash
claude mcp add --transport stdio atlassian npx -- -y mcp-remote https://mcp.atlassian.com/v1/sse
```

Windows:
```bash
claude mcp add --transport stdio atlassian -- cmd /c npx -y mcp-remote https://mcp.atlassian.com/v1/sse
```

---

## For Agent Handoff

This guide provides all necessary steps to establish and verify Atlassian MCP connection.

**Quick Start (Personal Use)**:
1. Follow Installation Steps 1-3 for basic setup
2. Use personal Atlassian account for OAuth
3. Test with Basic Usage examples

**Team/Production Setup**:
1. Create service account (see Service Account Setup section)
2. Add service account to required Jira projects with Developer role
3. Add service account to required Confluence spaces with View/Add/Edit permissions
4. Follow Installation Steps 1-3, authenticating with service account
5. Verify connection can access project resources

**Common Issues**:
- "Permission denied" → Service account not added to project
- "Cannot create issue" → Service account lacks Create Issues permission
- "Cannot find project" → Service account not added to project members

If issues arise, consult the Troubleshooting section.
