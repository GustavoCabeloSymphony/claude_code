# Research Documentation Index

This directory contains research documentation and guides for various technical topics.

## Available Documentation

### Atlassian Integration

**[Atlassian MCP Integration with Claude Code - Complete Guide](./atlassian-mcp-claude-code-integration-2026-01-08.md)**
- **Date:** 2026-01-08
- **Status:** Completed
- **Confidence:** High
- **Topics:** Atlassian, Jira, Confluence, MCP, Claude Code, OAuth, API Integration
- **Summary:** Comprehensive guide covering installation, configuration, authentication, and usage of Atlassian's MCP server with Claude Code. Includes troubleshooting, security considerations, use cases, and comparison with traditional CLI tools. Based on 45 authoritative sources including official Atlassian documentation and community resources.
- **Key Sections:**
  - Prerequisites and system requirements
  - Multiple installation methods (official and self-hosted)
  - Step-by-step configuration for Claude Code
  - OAuth 2.1 and API token authentication
  - Real-world use cases and workflow examples
  - Comprehensive troubleshooting guide
  - Security best practices
  - Complete reference links (45 sources)

## Quick Start Guides

### Setting up Atlassian MCP with Claude Code

```bash
# Quick installation (recommended)
claude mcp add atlassian --transport sse "https://mcp.atlassian.com/v1/sse" --scope user

# Verify installation
claude mcp list
```

For full details, see the [complete guide](./atlassian-mcp-claude-code-integration-2026-01-08.md).

## Document Organization

Research documents follow this naming convention:
- `topic-name-YYYY-MM-DD.md` - Main research document
- Includes metadata (date, status, confidence level)
- Comprehensive source citations with URLs and access dates
- Version history for updated documents

## Contributing

When adding new research documentation:
1. Follow the template in existing documents
2. Include comprehensive source citations with full URLs
3. Add entry to this README.md index
4. Use descriptive filenames with dates
5. Include metadata section at the top

## Research Standards

All research documents in this directory follow these standards:
- **Metadata**: Date, status, confidence level, tags
- **Executive Summary**: 2-3 paragraph overview
- **Source Citations**: Full URLs with access dates and reliability ratings
- **Practical Examples**: Code snippets and real-world use cases
- **Version History**: Track updates and revisions
- **Gaps and Limitations**: Document what needs further research

---

**Last Updated:** 2026-01-08
