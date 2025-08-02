# SuperGemini Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/SuperGemini.svg)](https://pypi.org/project/SuperGemini/)
[![Version](https://img.shields.io/badge/version-3.1.1-blue.svg)](https://github.com/SuperGemini-Org/SuperGemini_Framework)
[![GitHub issues](https://img.shields.io/github/issues/SuperGemini-Org/SuperGemini_Framework)](https://github.com/SuperGemini-Org/SuperGemini_Framework/issues)

A framework that extends Gemini CLI with specialized commands, personas, and MCP server integration.

## Overview

SuperGemini Framework enhances Gemini CLI with development-focused capabilities:
- 17 specialized commands for common development tasks
- Domain-specific personas for contextual assistance
- MCP server integration for documentation and automation
- Task management and workflow optimization

## Features

### Commands
17 essential commands for development tasks:

**Development**: `/sg:implement`, `/sg:build`, `/sg:design`  
**Analysis**: `/sg:analyze`, `/sg:troubleshoot`, `/sg:explain`  
**Quality**: `/sg:improve`, `/sg:test`, `/sg:cleanup`  
**Planning**: `/sg:workflow`, `/sg:task`, `/sg:estimate`  
**Others**: `/sg:document`, `/sg:git`, `/sg:index`, `/sg:load`, `/sg:spawn`

### Personas
Domain-specific assistants for contextual guidance:
- **architect** - Systems design and architecture
- **frontend** - UI/UX development and accessibility  
- **backend** - Server-side development and infrastructure
- **analyzer** - Debugging and investigation
- **security** - Security analysis and vulnerabilities
- **scribe** - Documentation and technical writing

Additional specialists for performance, QA, DevOps, and refactoring.

### MCP Integration
External service integrations:
- **Context7** - Official library documentation and patterns 
- **Sequential** - Complex multi-step analysis  
- **Playwright** - Browser automation and testing

**Note**: Magic MCP (UI component generation) is currently disabled due to Gemini API compatibility issues.

## Installation

**Step 1: Install Package**
```bash
pip install SuperGemini
```

**Step 2: Configure Gemini CLI**
```bash
python -m SuperGemini install
```

**Installation Options:**
```bash
python -m SuperGemini install --minimal      # Core only
python -m SuperGemini install --interactive  # Choose components  
python -m SuperGemini install --help         # View all options
```

## Configuration

Customization options:
- `~/.gemini/settings.json` - Main configuration
- `~/.gemini/*.md` - Framework behavior files

Default configuration is suitable for most use cases.

## Documentation

Reference guides:
- [User Guide](https://github.com/SuperGemini-Org/SuperGemini_Framework/blob/master/Docs/supergemini-user-guide.md) - Complete overview and usage
- [Commands Guide](https://github.com/SuperGemini-Org/SuperGemini_Framework/blob/master/Docs/commands-guide.md) - All commands explained  
- [Flags Guide](https://github.com/SuperGemini-Org/SuperGemini_Framework/blob/master/Docs/flags-guide.md) - Command flags and options
- [Personas Guide](https://github.com/SuperGemini-Org/SuperGemini_Framework/blob/master/Docs/personas-guide.md) - Understanding the persona system
- [Installation Guide](https://github.com/SuperGemini-Org/SuperGemini_Framework/blob/master/Docs/installation-guide.md) - Detailed installation instructions

## Requirements

- Python 3.8+
- Node.js 18+ (for MCP servers)
- Gemini CLI

## Author

Created by hyunjaelim - Inspired by the SuperClaude Framework architecture

## Acknowledgments

This project is inspired by and based on the **SuperClaude Framework** architecture developed by the SuperClaude Framework Contributors.

- **Original Project**: [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- **Original License**: MIT License
- **Our Implementation**: SuperGemini is an independent implementation that adapts the SuperClaude architecture for Gemini CLI compatibility

We express our gratitude to the original SuperClaude team for their innovative framework design and for releasing it under the MIT License, which enables projects like SuperGemini to exist.

**Note**: SuperGemini is not affiliated with or endorsed by the original SuperClaude project. It is a separate, independent implementation created specifically for Gemini CLI users.

## License

MIT - [See LICENSE file for details](https://opensource.org/licenses/MIT)

Inspired by SuperClaude Framework architecture

---

SuperGemini Framework - Enhanced development workflow for Gemini CLI