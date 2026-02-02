

## Overview
This document summarizes my work on configuring the Tenx MCP server, creating and refining a rules file for Copilot, conducting research into best practices, and documenting testing outcomes. It reflects both technical troubleshooting and the learning process of guiding AI agent behavior.

---

## What I Did
- **MCP Server Setup:**  
  Configured `.vscode/mcp.json` to connect to the Tenx MCP proxy. Started the server in VS Code and confirmed active connection through logs showing *“Discovered 3 tools.”*
- **Troubleshooting:**  
  Attempted manual requests with PowerShell using GitHub PATs, which failed with `401 Unauthorized`. Cleared cached tokens, retried OAuth flow, and documented.
- **Rules File Creation:**  
  Added `.github/copilot-instructions.md` with rules inspired by Boris Cherny’s Claude Code workflow and community best practices:
  - Plan-first approach  
  - Verification & validation  
  - Context persistence  
  - Multi-path suggestions  
  - Minimalism & clarity
- **Testing:**  
  Asked Copilot to implement a `reverse_string` function with tests. Observed plan-first behavior, verification steps, and context persistence. Captured logs and test results.
- **Research:**  
  Studied Boris Cherny’s workflow (Substack, VibesParking blog) and community discussions on Claude Code and AI agent orchestration. Summarized findings in `RESEARCH_NOTES.md`.

---

## What Worked
- MCP server connected successfully and listed tools, confirming active logging.  
- Copilot followed the plan-first rule, outlining environment setup, file creation, and test strategy.  
- Verification rules worked: Copilot created tests and explained how to run them.  
- Context persistence was evident: Copilot remembered prior environment details and adapted instructions.  
- Documentation artifacts (`MCP_SETUP.md`, `RULES_REPORT.md`, `RESEARCH_NOTES.md`) captured progress and insights.

---

## What Didn’t Work
- Manual PowerShell requests with GitHub PATs failed (`401 Unauthorized`) because the proxy requires OAuth tokens.  
- Initial test run produced `ModuleNotFoundError` until `$env:PYTHONPATH` was set correctly.  
- Multi-path suggestions were less distinct — Copilot tended to converge on one solution.  
- Copilot showed uncertainty about dependency management (e.g., whether to add `pyproject.toml` or `requirements.txt`).

---

## Insights Gained
- **Rules steer behavior:** Plan-first and verification rules significantly improved clarity and reproducibility.  
- **OAuth vs PAT:** MCP proxy enforces OAuth tokens; PATs are insufficient for authentication.  
- **Troubleshooting matters:** Documenting failed attempts (401 errors, cached tokens) demonstrates persistence and comprehension.  
- **Context persistence is powerful:** Copilot carried forward rubric requirements and environment details, aligning with my workflow.  
- **Iterative refinement:** Rules are not absolute; they require testing and adjustment to achieve desired agent behavior.

---

