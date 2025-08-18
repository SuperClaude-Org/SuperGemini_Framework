# SuperGemini Installation Guide 📦

## Quick Start 🚀

```bash
# Install SuperGemini
pip install SuperGemini

# Run installer (automatically installs everything)
SuperGemini install
```

That's it! SuperGemini is now ready to use.

## What Gets Installed

Running `SuperGemini install` automatically installs:
- **Core Framework**: Essential files (GEMINI.md, FLAGS.md, RULES.md, PRINCIPLES.md)
- **18 Commands**: TOML-based slash commands (/sg:*)
- **13 AI Agents**: Specialized personas for different domains
- **5 Behavioral Modes**: Context-aware operation modes
- **7 MCP Servers**: All servers installed (3 disabled by default: magic, serena, morphllm)

Installation location: `~/.gemini/`

## Prerequisites

- Python 3.8 or higher
- pip package manager
- 50MB free disk space

## Verification

After installation:
```bash
# Check version
SuperGemini --version

# Test with Gemini CLI
/sg:analyze README.md
```

## Development Setup

For contributors:
```bash
git clone https://github.com/SuperClaude-Org/SuperGemini_Framework.git
cd SuperGemini_Framework
pip install -e ".[dev]"
```

## Uninstall

```bash
# Remove SuperGemini
SuperGemini uninstall

# Remove Python package
pip uninstall SuperGemini
```

## Troubleshooting

**Permission Denied:**
```bash
pip install --user SuperGemini
```

**Python Version Issues:**
```bash
python3 -m pip install SuperGemini
```

## Support

- GitHub Issues: https://github.com/SuperClaude-Org/SuperGemini_Framework/issues
- Documentation: [Quick Start Guide](quick-start.md)