# SuperGemini v4.0.8 🚀
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/SuperGemini.svg)](https://pypi.org/project/SuperGemini/)
[![Version](https://img.shields.io/badge/version-4.0.8-blue.svg)](https://github.com/SuperClaude-Org/SuperGemini_Framework)
[![GitHub issues](https://img.shields.io/github/issues/SuperClaude-Org/SuperGemini_Framework)](https://github.com/SuperClaude-Org/SuperGemini_Framework/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/SuperClaude-Org/SuperGemini_Framework/blob/master/CONTRIBUTING.md)
[![Contributors](https://img.shields.io/github/contributors/SuperClaude-Org/SuperGemini_Framework)](https://github.com/SuperClaude-Org/SuperGemini_Framework/graphs/contributors)


SuperGemini is a meta-programming configuration framework that enhances Gemini CLI with structured development capabilities. It provides 18 slash commands in TOML format, 13 specialized AI agents with Persona Mode, behavioral instructions, and workflow automation for systematic software development.

## Quick Start

### Installation Methods

**Recommended: pipx (Isolated CLI Tool)**
```bash
# Install with pipx for clean, isolated environment
pipx install SuperGemini

# Setup SuperGemini for Gemini CLI (Choose one)
SuperGemini install --yes                    # Express setup (recommended)
SuperGemini install --profile minimal --yes  # Fastest (core only)
SuperGemini install --profile full --yes     # All features
```

**Alternative: pip (Traditional Installation)**
```bash
# Install with pip (may cause dependency conflicts)
pip install SuperGemini

# Or in a virtual environment (recommended if using pip)
python -m venv supergemini-env
source supergemini-env/bin/activate  # Linux/Mac
# or: supergemini-env\Scripts\activate  # Windows
pip install SuperGemini
```

### Usage with Gemini CLI
```bash
# Example commands after installation:
/sg:analyze src/
/sg:implement user authentication
```

**Why pipx?** SuperGemini is a standalone CLI tool. Using pipx:
- Prevents dependency conflicts with your projects
- Provides clean uninstallation
- Automatically manages virtual environments
- Keeps your system Python clean

**Note for pipx users:** If you encounter Node.js/npm detection issues during MCP setup, ensure these tools are available in your system PATH.

## What is SuperGemini? 💎

SuperGemini transforms Gemini CLI into a structured development platform by providing:

- **18 Slash Commands**: TOML-based commands for systematic workflow automation (/sg:analyze, /sg:implement, etc.)
- **Persona Mode**: 13 specialized AI agents that embody specific roles (system-architect, security-engineer, etc.)
- **Behavioral Instructions**: Core principles and rules for consistent development practices
- **Workflow Automation**: Systematic approaches to analysis, implementation, and optimization

Unlike traditional tools, SuperGemini uses **Persona Mode** where Gemini CLI embodies agent roles rather than spawning separate sub-agents.

[![GitHub Sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white)](https://github.com/sponsors/SuperClaude-Org)

## Documentation

### Getting Started
- [Quick Start Guide](Docs/Getting-Started/quick-start.md)
- [Installation Guide](Docs/Getting-Started/installation.md)

### User Guides
- [Commands Reference](Docs/User-Guide/commands.md) - 18 TOML-based slash commands
- [Agents Guide](Docs/User-Guide/agents.md) - 13 specialized AI personas
- [Behavioral Modes](Docs/User-Guide/modes.md) - Context-aware operation modes
- [Flags Guide](Docs/User-Guide/flags.md) - Command flags and options
- [MCP Servers](Docs/User-Guide/mcp-servers.md) - MCP server integration guide
- [Session Management](Docs/User-Guide/session-management.md) - Session lifecycle management

### Developer Resources
- [Technical Architecture](Docs/Developer-Guide/technical-architecture.md)
- [Contributing Code](Docs/Developer-Guide/contributing-code.md)
- [Testing & Debugging](Docs/Developer-Guide/testing-debugging.md)

### Reference
- [Quick Start Practices](Docs/Reference/quick-start-practices.md)
- [Examples Cookbook](Docs/Reference/examples-cookbook.md)
- [Troubleshooting](Docs/Reference/troubleshooting.md)

## Contributing

**Current Priorities:**
- 📝 Documentation improvements and usage examples
- 🎯 TOML command workflow patterns and best practices
- 🤖 New AI agent personas for specialized domains
- 🧪 Testing and validation for Gemini CLI integration
- 🌐 Translation and internationalization

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Contributors:** [View all contributors](https://github.com/SuperClaude-Org/SuperGemini_Framework/graphs/contributors)
