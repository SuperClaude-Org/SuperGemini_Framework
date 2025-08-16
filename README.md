# SuperGemini Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/SuperGemini.svg?cache=none)](https://pypi.org/project/SuperGemini/)
[![Version](https://img.shields.io/badge/version-3.2.2-blue.svg)](https://github.com/SuperClaude-Org/SuperGemini_Framework)
[![GitHub issues](https://img.shields.io/github/issues/SuperClaude-Org/SuperGemini_Framework)](https://github.com/SuperClaude-Org/SuperGemini_Framework/issues)

A framework that extends Gemini CLI with specialized commands, personas, and MCP server integration.

## ✨ Features

### 🚀 14 Specialized Commands
**Development**: `/sg:implement`, `/sg:build`, `/sg:design`  
**Analysis**: `/sg:analyze`, `/sg:troubleshoot`, `/sg:explain`  
**Quality**: `/sg:improve`, `/sg:test`, `/sg:cleanup`  
**Planning**: `/sg:estimate`  
**Others**: `/sg:document`, `/sg:git`, `/sg:index`, `/sg:load`

### 🎭 Domain-Specific Personas
- **architect** - Systems design and architecture
- **frontend** - UI/UX development and accessibility  
- **backend** - Server-side development and infrastructure
- **analyzer** - Debugging and investigation
- **security** - Security analysis and vulnerabilities
- **scribe** - Documentation and technical writing

### 🔌 MCP Server Integration
- **Context7** - Official library documentation
- **Sequential** - Multi-step analysis (--seq flag)
- **Playwright** - Browser automation and testing

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 18+ (for MCP servers and Gemini CLI)
- Gemini CLI (`npm install -g @google/gemini-cli`)

### Quick Install
```bash
# Install from PyPI
pip install SuperGemini

# Verify installation
SuperGemini --version  # Should show: SuperGemini v3.2.2

# Install all components
SuperGemini install --quick --yes
```

### Custom Installation
```bash
# Interactive installation
SuperGemini install

# Install specific components
SuperGemini install --components commands mcp

# List available components
SuperGemini install --list-components
```

### Components
- **core** - Framework documentation and core files
- **commands** - 14 slash commands for Gemini CLI (TOML format)
- **mcp** - MCP server integration (auto-installs npm packages)

## 🎯 Usage

### Basic Commands
```gemini
/sg:analyze --seq      # Activate sequential-thinking for analysis
/sg:build             # Build with framework detection
/sg:improve --focus performance  # Performance optimization
```

### Flag Support
- `--seq` - Activate sequential-thinking MCP
- `--c7` - Activate Context7 documentation
- `--verbose` - Detailed output
- `--quiet` - Minimal output

## 🛠️ Configuration

Configuration files are stored in `~/.gemini/`:
- `settings.json` - Main configuration and MCP servers
- `commands/sg/*.toml` - Command definitions

## 🤝 Contributing

Contributions are welcome! Please check our [issues](https://github.com/SuperClaude-Org/SuperGemini_Framework/issues) page.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Mithun Gowda B** - [GitHub](https://github.com/mithun50)
- **NomenAK** - [GitHub](https://github.com/NomenAK)

## 🔗 Links

- [PyPI Package](https://pypi.org/project/SuperGemini/)
- [GitHub Repository](https://github.com/SuperClaude-Org/SuperGemini_Framework)
- [Issue Tracker](https://github.com/SuperClaude-Org/SuperGemini_Framework/issues)
