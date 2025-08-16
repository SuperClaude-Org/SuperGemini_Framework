# SuperClaude Installation Guide 📦

## 🎯 It's Easier Than It Looks!

**The honest truth**: This guide looks comprehensive because we want to cover all the details, but installation is actually simple. Most people are done in 2 minutes with one command!

## Quick Start 🚀

**🏆 The "Just Get It Working" Approach (Recommended for 90% of Users)**

### Option A: From PyPI (Recommended)
```bash
pip install SuperClaude

# Install with interactive selection
SuperClaude install

# That's it! 🎉
```

### Option B: From Source
```bash
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework
pip install .

# Install with interactive selection
SuperClaude install

# That's it! 🎉
```
### Option C: From npm (Global, after publishing this won't works for now)
```bash
npm install -g superclaude
superclaude --help
```
- Requires package to be published on npmjs.org.
- Installs the npm wrapper and sets up SuperClaude via pip.

### Option D: From npm (Local Project this won't works for now)
```bash
npm install superclaude
npx superclaude --help
```
- Installs SuperClaude wrapper inside your project.
- Use `npx` to run it locally.
- Also requires publishing to npmjs.org.

### Option E: From GitHub (Works without npm publish)
```bash
# Global install directly from GitHub
yarn global add github:SuperClaude-Org/SuperClaude_Framework
# or
npm install -g github:SuperClaude-Org/SuperClaude_Framework

superclaude --help
```
```bash
# Local project install from GitHub
npm install github:SuperClaude-Org/SuperClaude_Framework
npx superclaude --help
```
- Works immediately without publishing to npm registry.

- Runs SuperClaude instantly.
- First run may install Python package via pip.
- Subsequent runs skip reinstallation unless explicitly updated.

---

**What you just got:**
- ✅ 21 intelligent commands that auto-activate specialized capabilities
- ✅ 13 specialized AI agents with domain expertise and smart routing
- ✅ 5 behavioral modes for different types of work
- ✅ 6 MCP servers for extended functionality (optional)
- ✅ Session lifecycle management with persistent context
- ✅ About 2 minutes of your time and ~50MB disk space

**Nervous about what it will do?** See first with:
```bash
SuperClaude install --dry-run
```

## Before You Start 🔍

### What You Need 💻

SuperClaude works on **Windows**, **macOS**, and **Linux**. Here's what you need:

**Required:**
- **Python 3.8 or newer** - The framework is written in Python
- **Claude Code** - SuperClaude enhances Claude Code, so you need it installed first

**Optional (but recommended):**
- **Node.js 16+** - Only needed if you want MCP server integration
- **Git** - Helpful for development workflows

### Quick Check 🔍

Before installing, let's make sure you have the basics:

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
```bash
SuperClaude install
```
- **Stage 1**: Select MCP servers (Context7, Sequential, Magic, Playwright, etc.)
- **Stage 2**: Choose framework components (Core, Commands, Agents, Modes)
- **Time**: ~3-5 minutes depending on selections
- **Space**: ~50-100MB depending on selections
- **Good for**: All users - gives you full control over what gets installed
- **Interactive**: Shows detailed descriptions and lets you pick exactly what you want

### ⚡ Component-Specific Installation
```bash
SuperClaude install --components core commands modes
```
- **What**: Install only specific components you need
- **Available components**: core, commands, agents, modes, mcp, mcp_docs
- **Good for**: Users who know exactly what they want

### 🔍 Other Useful Options
```bash
# See all available components
SuperClaude install --list-components

# See what would be installed without doing it
SuperClaude install --dry-run

# System diagnostics and installation help
SuperClaude install --diagnose

# Quiet installation (minimal output)
SuperClaude install --quiet

# Install everything
SuperClaude install --components all
```

## Step-by-Step Installation 📋

### Prerequisites Setup 🛠️

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

**Missing Node.js? (Optional)**
```bash
# Linux (Ubuntu/Debian)
sudo apt update && sudo apt install nodejs npm

# macOS
brew install node

# Windows  
# Download from https://nodejs.org/
# Or use winget
winget install nodejs
```

### Getting SuperClaude 📥

**Option 1: From PyPI (Recommended)**
```bash
pip install SuperClaude
```

**Option 2: Clone from Git**
```bash
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework
pip install .
```

### Running the Installer 🎬

The installer is smart and will guide you through the process:

```bash
# See all available options
SuperClaude install --help

# Interactive installation (recommended)
SuperClaude install

# Want to see what would happen first?
SuperClaude install --dry-run

# Install specific components
SuperClaude install --components core commands agents modes

# Quiet installation (minimal output)
SuperClaude install --quiet
```

### During Installation 📱

Here's what happens when you install:

1. **System Check** - Verifies you have required dependencies
2. **Component Selection** - Interactive selection of what to install
3. **MCP Server Setup** - Downloads and configures MCP servers (if selected)
4. **API Key Collection** - Prompts for required API keys for selected servers
5. **Framework Installation** - Copies framework documentation files
6. **Configuration Setup** - Creates settings and CLAUDE.md imports
7. **Validation** - Tests that everything works

The installer shows progress and will tell you if anything goes wrong.

## After Installation ✅

### Quick Test 🧪

Let's make sure everything worked:

```bash
# Check if files were installed
ls ~/.claude/

# Should show: CLAUDE.md, RULES.md, PRINCIPLES.md, etc.
```

**Test with Claude Code:**
1. Open Claude Code
2. Try typing `/sc:help` - you should see SuperClaude commands
3. Try `/sc:analyze --help` - should show command options

### What Got Installed 📂

SuperClaude installs to `~/.claude/` by default. Here's what you'll find:

```
~/.claude/
├── CLAUDE.md              # Main framework entry point
├── FLAGS.md               # Command flags and options
├── PRINCIPLES.md          # Development principles
├── RULES.md               # Operational rules
├── MCP_*.md               # MCP server configurations
├── MODE_*.md              # Behavioral modes
├── settings.json          # Configuration file (if created)
└── SuperClaude/           # Framework components
    ├── Core/              # Core framework files
    ├── Commands/          # 21 command definitions
    ├── Agents/            # 13 specialized agents
    ├── Modes/             # 5 behavioral modes
    └── MCP/               # MCP server configurations
```

**What each file does:**
- **CLAUDE.md** - Tells Claude Code about SuperClaude and loads other files
- **RULES.md** - Operational rules and workflow patterns
- **PRINCIPLES.md** - Development principles and decision frameworks
- **FLAGS.md** - Command flags and behavioral controls
- **SuperClaude/** - Complete framework with commands, agents, and modes

### First Steps 🎯

Try these commands to get started:

```bash
# In Claude Code, try these:
/sc:help                    # See available commands
/sc:analyze README.md       # Analyze a file
/sc:build --help           # See build options
/sc:improve --help         # See improvement options
/sc:brainstorm "my app idea" # Try brainstorming mode
/sc:load                   # Initialize session with context
```

**Don't worry if it seems overwhelming** - SuperClaude enhances Claude Code gradually. You can use as much or as little as you want.

## Managing Your Installation 🛠️

### Updates 📅

Keep SuperClaude up to date:

```bash
# Update the package
pip install --upgrade SuperClaude

# Reinstall components
SuperClaude install --force

# Update specific components only
SuperClaude install --components core commands --force
```

### Backups 💾

SuperClaude automatically creates backups during installation. You can also create manual backups of your `~/.claude/` directory:

```bash
# Create a backup
cp -r ~/.claude/ ~/.claude_backup_$(date +%Y%m%d)

# Restore from backup
rm -rf ~/.claude/
cp -r ~/.claude_backup_20250115/ ~/.claude/
```

### Uninstallation 🗑️

If you need to remove SuperClaude:

```bash
# Remove just the package
pip uninstall SuperClaude

# Remove all SuperClaude files (keeps your other Claude settings)
rm -rf ~/.claude/SuperClaude/
rm -f ~/.claude/CLAUDE.md ~/.claude/RULES.md ~/.claude/PRINCIPLES.md ~/.claude/FLAGS.md
rm -f ~/.claude/MCP_*.md ~/.claude/MODE_*.md
```

**What gets removed:**
- All SuperClaude files in `~/.claude/`
- The SuperClaude Python package

**What stays:**
- Your other Claude Code settings
- Your projects and other files
- Any backups you created

## Troubleshooting 🔧

### Common Issues 🚨

**"Python not found"**
```bash
# Try python instead of python3
python --version

# Or check if it's installed but not in PATH
which python3
```

**"Claude Code not found"**
- Make sure Claude Code is installed first
- Visit https://claude.ai/code for installation help

**"Permission denied"**
```bash
# Try with explicit Python path
/usr/bin/python3 -m SuperClaude install

# Or check if you need different permissions
ls -la ~/.claude/
```

**"MCP servers won't install"**
- Check that Node.js is installed: `node --version`
- Check that npm is available: `npm --version`
- Try installing without MCP first: select "Skip MCP Server installation" during interactive setup

**"Installation fails partway through"**
```bash
# Try with verbose output to see what's happening
SuperClaude install --verbose

# Or try a dry run first
SuperClaude install --dry-run

# Try system diagnostics
SuperClaude install --diagnose
```

### Platform-Specific Issues 🖥️

**Windows:**
- Use `python` instead of `python3` if you get "command not found"
- Run Command Prompt as Administrator if you get permission errors
- Make sure Python is in your PATH

**macOS:**
- You might need to approve SuperClaude in Security & Privacy settings
- Use `brew install python3` if you don't have Python 3.8+
- Try using `python3` explicitly instead of `python`

**Linux:**
- Make sure you have `python3-pip` installed
- You might need `sudo` for some package installations
- Check that `~/.local/bin` is in your PATH

### Still Having Issues? 🤔

**Check our troubleshooting resources:**
- GitHub Issues: https://github.com/SuperClaude-Org/SuperClaude_Framework/issues
- Look for existing issues similar to yours
- Create a new issue if you can't find a solution

**When reporting bugs, please include:**
- Your operating system and version
- Python version (`python3 --version`)
- Claude Code version (`claude --version`)
- The exact command you ran
- The complete error message
- What you expected to happen

## Advanced Options ⚙️

### Custom Installation Directory
```bash
# Install to custom location
SuperClaude install --install-dir /custom/path

# Use environment variable
export SUPERCLAUDE_DIR=/custom/path
SuperClaude install
```

### Development Setup

If you're planning to contribute or modify SuperClaude:

```bash
# Clone the repository
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework

# Install in development mode
pip install -e .

# Install all components
SuperClaude install --components all
```

## What's Next? 🚀

**Now that SuperClaude is installed:**

1. **Just start using it** - Try `/sc:analyze some-file.js` or `/sc:build` and see what happens ✨
2. **Don't stress about learning** - SuperClaude usually figures out what you need
3. **Experiment freely** - Commands like `/sc:improve` and `/sc:troubleshoot` are pretty forgiving
4. **Use session management** - Try `/sc:load` and `/sc:save` for persistent context ([Session Management Guide](session-management.md))
5. **Explore behavioral modes** - Let SuperClaude adapt to your workflow automatically ([Behavioral Modes Guide](behavioral-modes-guide.md))
6. **Give feedback** - Let us know what works and what doesn't

**The real secret**: SuperClaude is designed to enhance your existing workflow without you having to learn a bunch of new stuff. Just use it like you'd use regular Claude Code, but notice how much smarter it gets! 🎯

**Still feeling uncertain?** Start with just `/sc:help` and `/sc:analyze README.md` - you'll see how approachable it actually is.

**Next Steps:**
- [Examples Cookbook](examples-cookbook.md) - Copy-paste commands for common tasks
- [SuperClaude User Guide](superclaude-user-guide.md) - Complete framework overview
- [Commands Guide](commands-guide.md) - All 21 commands with examples

---

## Final Notes 📝

- **Installation takes 1-5 minutes** depending on what you choose
- **Disk space needed: 20-100MB** (not much!)
- **Works alongside existing tools** - doesn't interfere with your setup
- **Easy to uninstall** if you change your mind
- **Community supported** - we actively read and respond to issues
- **Available commands**: Use `SuperClaude [command]`, `python3 -m SuperClaude [command]`, or `/sc:[command]` in Claude Code

Thanks for trying SuperClaude! We hope it makes your development workflow smoother and more intelligent. 🙂

---

## Related Guides

**🚀 What to Do Next (Essential)**
- [Examples Cookbook](examples-cookbook.md) - Copy-paste commands to get started immediately
- [SuperClaude User Guide](superclaude-user-guide.md) - Complete framework overview and philosophy

**📚 Learning the System (Recommended)**
- [Commands Guide](commands-guide.md) - All 21 commands with practical examples
- [Session Management Guide](session-management.md) - Persistent context and project memory
- [Behavioral Modes Guide](behavioral-modes-guide.md) - How SuperClaude adapts automatically

**🔧 When You Need Help**
- [Troubleshooting Guide](troubleshooting-guide.md) - Solutions for installation and usage issues
- [Best Practices Guide](best-practices.md) - Proven patterns for effective usage

**🎯 Advanced Usage (Optional)**
- [Agents Guide](agents-guide.md) - Understanding the 13 specialized AI experts
- [Flags Guide](flags-guide.md) - Manual control and optimization options
- [Technical Architecture Guide](technical-architecture.md) - Internal system design

**📖 Recommended Reading Path After Installation:**
1. [Examples Cookbook](examples-cookbook.md) - Try commands immediately
2. [Commands Guide](commands-guide.md) - Learn your toolkit
3. [Session Management Guide](session-management.md) - Enable persistent context
4. [Best Practices Guide](best-practices.md) - Optimize your workflow

---

*Last updated: August 2025 - Let us know if anything in this guide is wrong or confusing!*
