# SuperClaude Installation Guide 📦

## 🎯 It's Easier Than It Looks!

SuperClaude installs in under 2 minutes with an interactive installer. The process involves installing the Python package and running the component installer to configure your Claude Code environment.

## Quick Start 🚀

**Method 1: Python (Recommended)**
```bash
pip install SuperClaude
SuperClaude install
```

**Method 2: NPM (Cross-platform)**
```bash
npm install -g superclaude
superclaude install
```

**Method 3: Development**
```bash
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework
pip install -e ".[dev]"
SuperClaude install --dry-run
```

---

**What Gets Installed:**
- 21 slash commands (/sc:*) for workflow automation
- 13 specialized AI agents with domain expertise
- 6 behavioral modes for different contexts
- 6 MCP server configurations for enhanced capabilities
- Core instruction files in ~/.claude directory

**Dry-run Preview:**
```bash
SuperClaude install --dry-run  # Preview changes without installing
```

## Before You Start 🔍

### What You Need 💻

**Required:**
- Python 3.8+ with pip
- Claude Code installed and working
- 50MB free space for components

**Optional but Recommended:**
- Node.js 16+ (for MCP servers like Context7, Magic)
- Git (for version control integration)
- 1GB RAM for optimal performance

### Quick Check 🔍

Run these commands to verify your system is ready:

```bash
# Verify Python (should be 3.8+)
python3 --version

# Verify Claude Code availability
claude --version

# Optional: Check Node.js for MCP servers
node --version

# Check available disk space
df -h ~
```

If any checks fail, see [Prerequisites Setup](#prerequisites-setup-🛠️) below.

```bash
# Check Python version (should be 3.8+)
python3 --version

# Check if Claude Code is available
claude --version

# Check Node.js (optional, for MCP servers)
node --version
```

If any of these fail, see the [Prerequisites Setup](#prerequisites-setup-🛠️) section below.

## Installation Options 🎛️

### 🎯 Interactive Installation (Default - Recommended)

### ⚡ Component-Specific Installation

### 🔍 Other Useful Options

**Node.js Installation:**
```bash
# Linux (Ubuntu/Debian)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# macOS
brew install node

# Windows
winget install OpenJS.NodeJS
# Or download from https://nodejs.org/
```

### Getting SuperClaude 📥

**Choose Your Preferred Method:**

**Python Users:**
```bash
pip install SuperClaude
```

**JavaScript/Node.js Users:**
```bash
npm install -g superclaude
```

**Development/Contributors:**
```bash
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework
pip install -e ".[dev]"
```

### Running the Installer 🎬

**Interactive Installation (Default):**
```bash
SuperClaude install
```
The installer will:
1. Detect your system configuration
2. Show available components with descriptions
3. Let you select which components to install
4. Configure MCP servers if desired
5. Create backups before making changes

**Command-line Options:**
```bash
SuperClaude install --components core mcp modes  # Specific components
SuperClaude install --dry-run                    # Preview only
SuperClaude install --force --yes                # Skip confirmations
SuperClaude install --install-dir /custom/path   # Custom location
```

### During Installation 📱

**Installation Steps:**

1. **System Check** - Validates Python, Claude Code, permissions
2. **Component Discovery** - Scans available components and dependencies
3. **User Selection** - Interactive menu for component choices
4. **Backup Creation** - Saves existing ~/.claude configuration
5. **File Installation** - Copies framework files with merge logic
6. **MCP Configuration** - Sets up .claude.json for selected servers
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
# Check SuperClaude version
SuperClaude --version

# List installed components
SuperClaude install --list-components

# Test basic functionality
echo "Test analysis" | claude
# Then try: /sc:analyze README.md

# Verify MCP servers (if installed)
ls ~/.claude/.claude.json
```

**Expected Results:**
- ✅ Version number displays correctly
- ✅ Components list shows installed items
- ✅ Slash commands available in Claude Code
- ✅ MCP servers connect successfully

### What Got Installed 📂

**Files in ~/.claude:**
```
~/.claude/
├── CLAUDE.md           # Main instruction file with @imports
├── FLAGS.md            # Behavioral flags system
├── RULES.md            # Development rules
├── PRINCIPLES.md       # Engineering principles
├── MCP_*.md            # MCP server instructions
├── MODE_*.md           # Behavioral modes
├── .claude.json        # MCP server configurations
└── [your files]        # Preserved customizations
```

**Component Breakdown:**
- **Core**: Essential framework files and behavioral instructions
- **Commands**: 21 slash commands for workflow automation
- **Modes**: 6 behavioral modes for different contexts
- **Agents**: 13 specialized AI personas
- **MCP**: Configuration for 6 MCP servers
- **MCP Docs**: Documentation for MCP server usage

### First Steps 🎯

**Try These Commands:**
```bash
# Interactive requirements discovery
/sc:brainstorm "mobile app idea"

# Analyze existing code
/sc:analyze src/

# Generate implementation workflow
/sc:workflow "user authentication system"

# Get command help
/sc:index
```

**Learning Path:**
1. Start with `/sc:brainstorm` for project discovery
2. Use `/sc:analyze` to understand existing code
3. Try `/sc:implement` for feature development
4. Explore `/sc:index` for command discovery

## Managing Your Installation 🛠️

### Updates 📅

**Update SuperClaude:**
```bash
# Update core package
pip install --upgrade SuperClaude
# or: npm update -g superclaude

# Update components
SuperClaude update

# Update specific components
SuperClaude install --components mcp modes --force
```

**Version Management:**
- Updates preserve user customizations
- New components available via `SuperClaude install --list-components`
- Selective updates possible for individual components

### Backups 💾

**Automatic Backups:**
- Created before every installation/update
- Stored in ~/.claude.backup.YYYYMMDD_HHMMSS
- Include all customizations and configurations

**Manual Backup Management:**
```bash
# Create backup
SuperClaude backup --create

# List available backups
SuperClaude backup --list

# Restore from backup
SuperClaude backup --restore ~/.claude.backup.20241201_143022

# Manual backup (alternative)
cp -r ~/.claude ~/.claude.backup.manual
```

### Uninstallation 🗑️

**Complete Removal:**
```bash
# Remove SuperClaude components (preserves user files)
SuperClaude uninstall

# Remove Python package
pip uninstall SuperClaude
# or: npm uninstall -g superclaude

# Manual cleanup (if needed)
rm -rf ~/.claude/FLAGS.md ~/.claude/RULES.md ~/.claude/MODE_*.md
```

**What Gets Preserved:**
- Your custom CLAUDE.md content
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

**Missing Claude Code?**
- Visit https://claude.ai/code for installation instructions
- SuperClaude enhances Claude Code, so you need it first

**MCP Server Requirements:**
Some MCP servers require Node.js for optimal functionality:
- Context7: Library documentation lookup
- Magic: UI component generation
- Sequential: Advanced reasoning

Install Node.js 16+ for full MCP capabilities.

## Troubleshooting 🔧

**Common Issues:**

**Permission Denied:**
```bash
# Linux/macOS: Use --user flag
pip install --user SuperClaude

# Or fix permissions
sudo chown -R $USER ~/.claude
```

**Python Version Issues:**
```bash
# Verify Python 3.8+
python3 --version

# Use specific Python version
python3.9 -m pip install SuperClaude
```

**Claude Code Not Found:**
- Install Claude Code from https://claude.ai/code
- Verify with: `claude --version`
- Check PATH configuration

**Get Help:**
- GitHub Issues: https://github.com/SuperClaude-Org/SuperClaude_Framework/issues
- Include: OS, Python version, error message, steps to reproduce

## Advanced Options ⚙️

**Custom Installation Directory:**
```bash
# Install to custom location
SuperClaude install --install-dir /path/to/custom/claude

# Set environment variable
export CLAUDE_CONFIG_DIR=/path/to/custom/claude
SuperClaude install
```

**Development Setup:**
```bash
# Clone repository
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install in development mode
pip install -e ".[dev]"

# Run tests
SuperClaude install --dry-run
python scripts/validate_pypi_ready.py
```

## What's Next? 🚀

**Recommended Next Steps:**

1. **Learn Commands**: Start with [Commands Guide](../User-Guide/commands.md)
2. **Try Examples**: Explore [Examples Cookbook](../Reference/examples-cookbook.md)
3. **Configure MCP**: Set up [MCP Servers](../User-Guide/mcp-servers.md)
4. **Understand Modes**: Read [Behavioral Modes](../User-Guide/modes.md)
5. **Join Community**: Follow development on [GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework)

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

**What's Next**: Your Claude Code now has enhanced capabilities. Try `/sc:brainstorm` for your first SuperClaude experience!

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