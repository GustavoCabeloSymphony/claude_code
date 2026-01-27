# Claude Code Configuration

A custom Claude Code workspace with automated markdown formatting, custom agents, and workflow enhancements.

## Overview

This project provides a tailored Claude Code environment with:

- **Automated Markdown Formatting**: Post-processing hook that automatically detects and adds language tags to code blocks
- **Custom Agents**: Specialized agents for documentation maintenance and code optimization
- **Smart Hooks**: Python-based automation that runs after file edits

## Features

### 🔧 Automatic Markdown Formatting

When Claude Code writes or edits markdown files, a Python hook automatically:

- Detects code block languages (Python, JavaScript, JSON, SQL, Bash, etc.)
- Adds appropriate language tags to unlabeled code fences
- Removes excessive blank lines
- Preserves all code content without modification

### 📚 Custom Agents

**readme-maintainer**: Specialized agent for creating and maintaining project documentation
- Analyzes project structure and dependencies
- Creates comprehensive README files
- Updates documentation to reflect code changes
- Ensures accuracy between docs and implementation

### ⚡ Custom Commands

**optimize**: Performance analysis command for identifying bottlenecks and suggesting improvements
- Available via `/optimize` command
- Uses Claude Sonnet 4.5 for detailed analysis

## Project Structure

```text
claude_code/
├── .claude/
│   ├── agents/
│   │   └── readme-maintainer.md    # Documentation maintenance agent
│   ├── commands/
│   │   └── optimize.md             # Performance analysis command
│   ├── hooks/
│   │   └── markdown_formatter.py   # Post-edit markdown formatter
│   └── settings.json               # Hook configuration
├── .venv/                          # Python virtual environment
└── test.md                         # Test file for hook validation
```

## Prerequisites

- [Claude Code](https://claude.com/claude-code) CLI installed
- Python 3.9 or higher
- macOS, Linux, or Windows with WSL

## Installation

1. **Clone or navigate to this project directory:**

```bash
cd /Users/gcabelo/Symphony/Projects/claude_code
```

2. **Ensure Python virtual environment is activated (if needed):**

```bash
source .venv/bin/activate  # macOS/Linux
```

3. **The hooks and agents are automatically loaded by Claude Code from the `.claude/` directory**

## Configuration

### Hooks Configuration

The markdown formatter hook is configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/markdown_formatter.py"
          }
        ]
      }
    ]
  }
}
```

This configuration triggers the formatter after any `Edit` or `Write` tool usage on markdown files.

### Markdown Formatter Capabilities

The formatter detects the following languages:

- **Python**: Detects `def`, `import`, `from` statements
- **JavaScript**: Detects `function`, `const`, arrow functions, `console.log`
- **JSON**: Validates JSON structure
- **SQL**: Detects `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE` statements
- **Bash**: Detects shebangs and common shell keywords
- **Fallback**: Unrecognized code blocks are tagged as `text`

## Usage

### Using the Markdown Formatter

The hook runs automatically - no manual action required. When Claude Code edits markdown files:

1. Write or edit any `.md` or `.mdx` file
2. Hook automatically processes the file
3. Console output confirms formatting: `✓ Fixed markdown formatting in [file]`

### Using Custom Agents

Agents are invoked automatically by Claude Code when relevant, or can be referenced in conversations:

```text
"Use the readme-maintainer agent to update the documentation"
```

### Using Custom Commands

```text
/optimize
```

Then provide or select the code you want analyzed.

## Development

### Testing the Hook

Use the included `test.md` file to verify hook functionality:

```bash
# In Claude Code, edit test.md and observe the automatic formatting
```

### Adding New Language Detection

Edit `.claude/hooks/markdown_formatter.py` and add patterns to the `detect_language()` function:

```python
# Example: Add TypeScript detection
if re.search(r'\binterface\s+\w+', s) or \
   re.search(r'\btype\s+\w+\s*=', s):
    return 'typescript'
```

### Creating New Commands

Add new command files to `.claude/commands/`:

```markdown
---
description: Your command description
model: claude-sonnet-4-5
---

Your command prompt here
```

### Creating New Agents

Add new agent files to `.claude/agents/`:

```markdown
---
name: agent-name
description: Agent description and usage instructions
tools: Read, Write, Edit, Bash
model: sonnet
---

Agent system prompt and instructions
```

## How It Works

### Hook Execution Flow

1. Claude Code executes `Edit` or `Write` tool
2. Post-tool-use hook triggers
3. Python script receives tool input via JSON stdin
4. Script checks if file is markdown (`.md`, `.mdx`)
5. Reads file content and applies formatting rules
6. Writes formatted content back if changes detected
7. Outputs confirmation message

### Language Detection Algorithm

The formatter uses regex pattern matching:

```python
# Example: Python detection
if re.search(r'^\s*def\s+\w+\s*\(', code, re.M):
    return 'python'
```

Falls back to `text` for unrecognized patterns.

## Troubleshooting

### Hook Not Running

- Verify `.claude/settings.json` exists and is valid JSON
- Check that `markdown_formatter.py` is executable: `chmod +x .claude/hooks/markdown_formatter.py`
- Ensure Python 3 is in your PATH: `which python3`

### Incorrect Language Detection

- Update regex patterns in `detect_language()` function
- Consider adding more specific patterns for your use case
- Language detection is best-effort; manual tags still work

### Custom Agents Not Found

- Verify agent files are in `.claude/agents/` directory
- Check that agent files have proper frontmatter with `name` field
- Restart Claude Code after adding new agents

## Best Practices

1. **Hook Development**: Test hooks with `try-except` blocks to prevent blocking Claude Code
2. **Agent Design**: Keep agents focused on specific tasks
3. **Language Detection**: Prioritize precision over recall for code block tagging
4. **Documentation**: Update this README when adding new hooks or agents

## Contributing

When extending this configuration:

1. Test new hooks thoroughly with various markdown files
2. Document new agents in this README
3. Add examples for new commands
4. Ensure hooks fail gracefully without blocking Claude Code

## License

This configuration is free to use and modify for personal or commercial projects.

## Acknowledgments

- Built for [Claude Code](https://claude.com/claude-code) by Anthropic
- Markdown formatting inspired by common linting tools
- Language detection patterns based on standard syntax conventions
