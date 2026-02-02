# Tenx MCP Assessment

## Overview
This repository contains my work for the Tenx MCP assessment. It includes:
- MCP server configuration and troubleshooting
- Copilot rules file with best practices
- Research notes on Boris Cherny’s Claude Code workflow and community insights
- Documentation of testing, results, and reflections
- Source code and tests for a sample `reverse_string` function

---

## Setup

### MCP Server
- Config file: `.vscode/mcp.json`
- Confirmed connection with logs showing: Starting server    tenxfeedbackanalytics
Connection state: Running
Discovered 3 tools

- See [MCP_SETUP.md](MCP_SETUP.md) for full details.

### Rules File
- Location: `.github/copilot-instructions.md`
- Rules emphasize planning, verification, context persistence, and clarity.
- See [RULES_REPORT.md](RULES_REPORT.md) for testing evidence.

---

## Testing

### Reverse String Function
- Source: `src/reverse_string.py`
- Tests: `tests/run_tests.py`
- Run tests with:
```bash
$env:PYTHONPATH = 'C:\Users\mella\Tenacious week 0'
python tests/run_tests.py
```
### Result: 
All tests passed
