# Qwen Framework

Qwen Framework is an AI-enhanced development framework for Qwen CLI, adapted and forked from the **SuperGemini Framework**. It provides structured development capabilities with slash commands, behavioral modes, and specialized AI agents.

## Features

* **18 Slash Commands**: TOML-based commands for systematic workflow automation (`/qwen:analyze`, `/qwen:implement`, etc.)
* **Behavioral Modes**: Context-aware operation modes (Brainstorming, Introspection, Task Management, Token Efficiency)
* **Specialized AI Agents**: 13 domain experts (System Architect, Security Engineer, etc.)
* **MCP Server Integration**: Extended capabilities through MCP servers

## Installation

1. Clone this repository
2. Run the installation script:

   ```bash
   python install_qwen.py
   ```
3. Setup the framework:

   ```bash
   python setup_qwen.py
   ```

## Usage

After installation, you can use the following commands in Qwen CLI:

* `/qwen:analyze` - Comprehensive code analysis
* `/qwen:implement` - Implementation guidance
* `/qwen:design` - System design assistance
* `/qwen:test` - Test generation and validation
* And 14 more commands...

## Modes

Enable behavioral modes through flags:

* `--brainstorm` - Brainstorming mode for idea generation
* `--introspect` - Introspection mode for self-analysis
* `--task-manage` - Task management mode
* `--token-eff` - Token efficiency mode

## Uninstallation

To uninstall the framework:

```bash
python uninstall_qwen.py
```

---

### Acknowledgment

This framework was originally forked from the **SuperGemini Framework**. I would like to sincerely thank the **SuperClaude Team** for their outstanding work, which served as the foundation and inspiration for this contribution.

* https://github.com/SuperClaude-Org/SuperGemini_Framework
---
