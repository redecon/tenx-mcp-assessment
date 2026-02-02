

## Purpose
This document records my research into best practices for configuring and guiding AI coding agents. It draws on Boris Cherny’s Claude Code workflow, community discussions, and technical guides to inform the rules I created in `.github/copilot-instructions.md`.

---

## Sources Consulted

### Boris Cherny’s Claude Code Workflow
- **13 Lessons for Agentic Velocity**: Boris Cherny, creator of Claude Code, shared his workflow for running multiple agents in parallel, verifying every change, and shipping pull requests in one shot .
- **Tips and Techniques**: Cherny’s setup includes running 5 instances of Claude Code simultaneously, using planning mode before edits, and verification loops to ensure correctness .
- **Core Practices**: He emphasizes starting sessions in planning mode, creating slash commands, leveraging sub-agents, and formatting code consistently .

### Community Best Practices
- **Claude Code Docs**: Best practices include configuring environments, scaling across parallel sessions, and understanding constraints of autonomous agents. Claude Code is designed to explore, plan, and implement tasks, but requires careful guidance to avoid errors .
- **AI Agent Guidebook (GitHub)**: Provides comparative insights across Claude Code, GitHub Copilot, and Gemini CLI. Highlights multi-agent orchestration, production templates, and MCP server integration .
- **Engineering Notes Guide**: Consolidates community knowledge into workflows for testing, quality assurance, security, and multi-agent collaboration. Emphasizes reproducibility and organizational impact .

---

## Key Best Practices Identified

1. **Plan-First Approach**
   - Always begin with a planning step before executing code.
   - Helps align agent behavior with user intent and rubric requirements.

2. **Verification Loops**
   - Require agents to test or validate outputs before finalizing.
   - Improves reliability and reduces errors.

3. **Parallel Sessions**
   - Running multiple agents in parallel can accelerate workflows.
   - Each agent can explore different solution paths.

4. **Context Persistence**
   - Agents should carry forward project goals and constraints across sessions.
   - Prevents loss of rubric alignment or coding style consistency.

5. **Minimalism & Clarity**
   - Rules should emphasize concise, modular outputs.
   - Avoid cluttered or verbose responses.

6. **Community Insights**
   - Multi-agent orchestration and MCP integration are emerging best practices.
   - Testing and reproducibility are critical for production readiness.

---

## Insights Gained
- Boris Cherny’s workflow demonstrates that **rules are not just prompts but structural guides** for agent behavior.
- Community practices reinforce the importance of **verification, reproducibility, and organizational alignment**.
- By combining Cherny’s plan-first and verification rules with community emphasis on reproducibility, I created a rules file tailored to my workflow and rubric expectations.
- Rules act as a **steering mechanism**: they don’t change the model itself, but they direct its behavior toward clarity, persistence, and alignment.

---

## Next Steps
- Continue testing Copilot with different rule configurations.
- Explore whether multi-agent orchestration (parallel sessions) can be simulated in VS Code.
- Document further refinements in `RULES_REPORT.md`.

---
