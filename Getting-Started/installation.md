# SuperGemini Installation Guide 📦

## 🎯 It's Easier Than It Looks!

SuperGemini installs in under 2 minutes with an interactive installer. The process involves installing the Python package and running the component installer to configure your Gemini CLI environment with TOML commands and AI agent personas.

## Quick Start 🚀

**Method 1: Python (Recommended)**
```bash
pip install SuperGemini
SuperGemini install
```

**Method 2: Direct Git Clone**
```bash
git clone https://github.com/SuperClaude-Org/SuperGemini_Framework.git
cd SuperGemini_Framework
pip install -e ".[dev]"
SuperGemini install --dry-run
```

**Method 3: Development Setup**
```bash
git clone https://github.com/SuperClaude-Org/SuperGemini_Framework.git
cd SuperGemini_Framework
pip install -e ".[dev]"
SuperGemini install --dry-run
```

---

**What Gets Installed:**
- 18 TOML-based slash commands (/sg:*) for Gemini CLI workflow automation
- 13 specialized AI agent personas with domain expertise
- 5 behavioral modes for different development contexts
- Core instruction files for systematic development practices
- Framework configuration in ~/.gemini directory

**Dry-run Preview:**
```bash
SuperGemini install --dry-run  # Preview changes without installing
```

## Before You Start 🔍

### What You Need 💻

**Required:**
- Python 3.8+ with pip
- Gemini CLI access and configuration
- 50MB free space for components

**Optional but Recommended:**
- Git (for version control integration)
- 1GB RAM for optimal performance with complex projects

### Quick Check 🔍

Run these commands to verify your system is ready:

```bash
# Verify Python (should be 3.8+)
python3 --version

# Verify Gemini CLI access (follow Gemini CLI setup if needed)
# SuperGemini enhances Gemini CLI with structured commands

# Check available disk space
df -h ~
```

If any checks fail, see [Prerequisites Setup](#prerequisites-setup-🛠️) below.

```bash
# Check Python version (should be 3.8+)
python3 --version

# Check if you have Gemini CLI access configured
# SuperGemini will enhance your Gemini CLI experience
```

If any of these fail, see the [Prerequisites Setup](#prerequisites-setup-🛠️) section below.

## Installation Options 🎛️

### 🎯 Interactive Installation (Default - Recommended)

### ⚡ Component-Specific Installation

### 🔍 Other Useful Options

**Development Mode Installation:**
```bash
# Clone and install in development mode
git clone https://github.com/SuperClaude-Org/SuperGemini_Framework.git
cd SuperGemini_Framework
pip install -e ".[dev]"
SuperGemini install --dry-run
```

### Getting SuperGemini 📥

**Choose Your Preferred Method:**

**Python Users:**
```bash
pip install SuperGemini
```

**Development Setup:**
```bash
git clone https://github.com/SuperClaude-Org/SuperGemini_Framework.git
cd SuperGemini_Framework
```

**Development/Contributors:**
```bash
git clone https://github.com/SuperClaude-Org/SuperGemini_Framework.git
cd SuperGemini_Framework
pip install -e ".[dev]"
```

### Running the Installer 🎬

**Interactive Installation (Default):**
```bash
SuperGemini install
```
The installer will:
1. Detect your system configuration and Gemini CLI setup
2. Show available components with descriptions (Commands, Agents, Modes, Core)
3. Let you select which components to install interactively
4. Configure SuperGemini framework files
5. Create backups before making changes

**Command-line Options:**
```bash
SuperGemini install --components core commands agents  # Specific components
SuperGemini install --dry-run                          # Preview only
SuperGemini install --force --yes                      # Skip confirmations
SuperGemini install --install-dir /custom/path         # Custom location
```

### During Installation 📱

**Installation Steps:**

1. **System Check** - Validates Python, Gemini CLI setup, permissions
2. **Component Discovery** - Scans available components and dependencies
3. **User Selection** - Interactive menu for component choices
4. **Backup Creation** - Saves existing ~/.gemini configuration if present
5. **File Installation** - Copies TOML commands, agents, and framework files
6. **Configuration Setup** - Sets up SuperGemini framework configuration
7. **Verification** - Tests installation and provides next steps

**Progress Indicators:**
- ✅ Step completion checkmarks
- 🔄 Real-time progress bars for file operations
- ⚠️ Warnings for potential issues
- 📊 Summary statistics (files installed, space used)

## After Installation ✅

### Quick Test 🧪

**Verify Installation:**
```bash
# Check SuperGemini version
SuperGemini --version

# List installed components
SuperGemini install --list-components

# Test basic functionality with Gemini CLI
# Try: /sg:analyze README.md
# Try: /sg:implement user authentication

# Verify SuperGemini configuration
ls ~/.gemini/
```

**Expected Results:**
- ✅ Version number displays correctly
- ✅ Components list shows installed items
- ✅ TOML slash commands available in Gemini CLI (/sg:*)
- ✅ SuperGemini framework configuration active

### What Got Installed 📂

**Files in ~/.gemini:**
```
~/.gemini/
├── GEMINI.md           # Main instruction file with @imports
├── FLAGS.md            # Behavioral flags system
├── RULES.md            # Development rules
├── PRINCIPLES.md       # Engineering principles
├── MCP_*.md            # MCP server instructions
├── MODE_*.md           # Behavioral modes
├── .gemini.json        # MCP server configurations
└── [your files]        # Preserved customizations
```

**Component Breakdown:**
- **Core**: Essential framework files and behavioral instructions
- **Commands**: 18 TOML-based slash commands for workflow automation
- **Modes**: 5 behavioral modes for different contexts
- **Agents**: 13 specialized AI personas
- **MCP**: Optional MCP server integrations
- **Framework**: Core TOML command structure and persona system

### First Steps 🎯

**Try These Commands:**
```bash
# Analyze existing code
/sg:analyze src/

# Generate implementation workflow
/sg:workflow "user authentication system"

# Get command help
/sg:index
```

**Learning Path:**
1. Use `/sg:analyze` to understand existing code
2. Try `/sg:implement` for feature development
3. Use `/sg:workflow` for systematic planning
4. Explore `/sg:index` for command discovery

## Managing Your Installation 🛠️

### Updates 📅

**Update SuperGemini:**
```bash
# Update core package
pip install --upgrade SuperGemini

# Update components
SuperGemini update

# Update specific components
SuperGemini install --components mcp modes --force
```

**Version Management:**
- Updates preserve user customizations
- New components available via `SuperGemini install --list-components`
- Selective updates possible for individual components

### Backups 💾

**Automatic Backups:**
- Created before every installation/update
- Stored in ~/.gemini.backup.YYYYMMDD_HHMMSS
- Include all customizations and configurations

**Manual Backup Management:**
```bash
# Create backup
SuperGemini backup --create

# List available backups
SuperGemini backup --list

# Restore from backup
SuperGemini backup --restore ~/.gemini.backup.20241201_143022

# Manual backup (alternative)
cp -r ~/.gemini ~/.gemini.backup.manual
```

### Uninstallation 🗑️

**Complete Removal:**
```bash
# Remove SuperGemini components (preserves user files)
SuperGemini uninstall

# Remove Python package
pip uninstall SuperGemini
# or: npm uninstall -g superclaude

# Manual cleanup (if needed)
rm -rf ~/.gemini/FLAGS.md ~/.gemini/RULES.md ~/.gemini/MODE_*.md
```

**What Gets Preserved:**
- Your custom GEMINI.md content
- Personal configuration files
- Project-specific customizations
- Created backups (manual removal required)

## Prerequisites Setup 🛠️

**Missing Python?**
```bash
# Linux (Ubuntu/Debian)
sudo apt update && sudo apt install python3 python3-pip

# macOS  
brew install python3

# Windows
# Download from https://python.org/downloads/
# Or use winget
winget install python
```

**Missing Gemini CLI?**
- Visit Google AI Studio for Gemini CLI installation instructions
- SuperGemini enhances Gemini CLI, so you need it first

**Optional MCP Servers:**
SuperGemini includes optional MCP server integrations:
- Context7: Library documentation (requires Node.js)
- Magic: UI component generation (requires Node.js)
- Sequential: Advanced reasoning

MCP servers enhance functionality but are not required for core features.

## Troubleshooting 🔧

**Common Issues:**

**Permission Denied:**
```bash
# Linux/macOS: Use --user flag
pip install --user SuperGemini

# Or fix permissions
sudo chown -R $USER ~/.gemini
```

**Python Version Issues:**
```bash
# Verify Python 3.8+
python3 --version

# Use specific Python version
python3.9 -m pip install SuperGemini
```

**Gemini CLI Not Found:**
- Install Gemini CLI from Google AI Studio
- Verify with: `gemini --version`
- Check PATH configuration

**Get Help:**
- GitHub Issues: https://github.com/SuperClaude-Org/SuperGemini_Framework/issues
- Include: OS, Python version, error message, steps to reproduce

## Advanced Options ⚙️

**Custom Installation Directory:**
```bash
# Install to custom location
SuperGemini install --install-dir /path/to/custom/gemini

# Set environment variable
export GEMINI_CONFIG_DIR=/path/to/custom/gemini
SuperGemini install
```

**Development Setup:**
```bash
# Clone repository
git clone https://github.com/SuperClaude-Org/SuperGemini_Framework.git
cd SuperGemini_Framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install in development mode
pip install -e ".[dev]"

# Run tests
SuperGemini install --dry-run
python scripts/validate_pypi_ready.py
```

## What's Next? 🚀

**Recommended Next Steps:**

1. **Learn Commands**: Start with [Commands Guide](../User-Guide/commands.md)
2. **Try Examples**: Explore [Examples Cookbook](../Reference/examples-cookbook.md)
3. **Configure MCP**: Set up [MCP Servers](../User-Guide/mcp-servers.md)
4. **Understand Modes**: Read [Behavioral Modes](../User-Guide/modes.md)
5. **Join Community**: Follow development on [GitHub](https://github.com/SuperClaude-Org/SuperGemini_Framework)

**Essential Guides:**
- 🚀 [Quick Start Guide](quick-start.md) - 5-minute setup
- 🔧 [Commands Reference](../User-Guide/commands.md) - All 21 commands
- 🧐 [Best Practices](../Reference/best-practices.md) - Optimization tips
- 🎆 [Troubleshooting](../Reference/troubleshooting.md) - Problem solving

---

## Final Notes 📝

**Installation Summary:**
- **Time**: 2-5 minutes typical installation
- **Space**: 50MB for full installation
- **Requirements**: Python 3.8+, Claude Code, 1GB RAM recommended
- **Platform**: Linux, macOS, Windows supported
- **Usage**: Immediate access to 21 commands and 6 behavioral modes

**What's Next**: Your Gemini CLI now has enhanced capabilities with SuperGemini Framework!

---

## Related Guides

**Documentation Roadmap:**

**Beginner** (🌱 Start Here)
- [Quick Start Guide](quick-start.md) - 5-minute setup
- [Commands Reference](../User-Guide/commands.md) - Basic usage

**Intermediate** (🌿 Growing)
- [Behavioral Modes](../User-Guide/modes.md) - Context optimization
- [MCP Servers](../User-Guide/mcp-servers.md) - Enhanced capabilities
- [Examples Cookbook](../Reference/examples-cookbook.md) - Practical patterns

**Advanced** (🌲 Expert)
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - System design
- [Contributing Code](../Developer-Guide/contributing-code.md) - Development
- [Best Practices](../Reference/best-practices.md) - Optimization strategies