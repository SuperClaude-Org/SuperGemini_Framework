# SuperGemini V4 Beta Installation Guide 📦

## 🎯 It's Easier Than It Looks!

**The honest truth**: This guide looks long because we want to cover all the details, but installation is actually pretty simple. Most people are done in 2 minutes with one command! 

### Step 1: Install the Package

**Option A: From PyPI (Recommended)**
```bash
uv add SuperGemini
```

**Option B: From Source**
```bash
git clone https://github.com/SuperClaude-Org/SuperGemini_Framework.git
cd SuperGemini_Framework
uv sync
```
### 🔧 UV / UVX Setup Guide

SuperGemini V4 Beta supports installation via [`uv`](https://github.com/astral-sh/uv) (a faster, modern Python package manager) or `uvx` for cross-platform usage.

### 🌀 Install with `uv`

Make sure `uv` is installed:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

> Or follow instructions from: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

Once `uv` is available, you can install SuperGemini like this:

```bash
uv venv
source .venv/bin/activate
uv pip install SuperGemini
```

### ⚡ Install with `uvx` (Cross-platform CLI)

If you’re using `uvx`, just run:

```bash
uvx pip install SuperGemini
```
## 🔧 UV / UVX Setup Guide

SuperGemini V4 Beta supports installation via [`uv`](https://github.com/astral-sh/uv) (a faster, modern Python package manager) or `uvx` for cross-platform usage.

### 🌀 Install with `uv`

Make sure `uv` is installed:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

> Or follow instructions from: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

Once `uv` is available, you can install SuperGemini like this:

```bash
uv venv
source .venv/bin/activate
uv pip install SuperGemini
```

### ⚡ Install with `uvx` (Cross-platform CLI)

If you’re using `uvx`, just run:

```bash
uvx pip install SuperGemini
```

### ✅ Finish Installation

After installing, continue with the usual installer step:

```bash
python3 -m SuperGemini install
```

Or using bash-style CLI:

```bash
SuperGemini install
```

### 🧠 Note:

* `uv` provides better caching and performance.
* Compatible with Python 3.8+ and works smoothly with SuperGemini.

---

### ⚠️ Important Note 
**After installing the SuperGemini.**
**You can use `SuperGemini commands`
, `python3 -m SuperGemini commands` or also `python3 SuperGemini commands`**

**What just happened?** SuperGemini tried to set up everything you need. Usually no complex configuration, dependency hunting, or setup headaches! 🎉

---

A comprehensive guide to installing SuperGemini V4 Beta. But remember - most people never need to read past the quick start above! 😊

## Before You Start 🔍

### What You Need 💻

SuperGemini works on **Windows**, **macOS**, and **Linux**. Here's what you need:

**Required:**
- **Python 3.8 or newer** - The framework is written in Python
- **Gemini CLI** - SuperGemini enhances Gemini CLI, so you need it installed first

**Optional (but recommended):**
- **Node.js 16+** - Only needed if you want MCP server integration
- **Git** - Helpful for development workflows

### Quick Check 🔍

Before installing, let's make sure you have the basics:

```bash
# Check Python version (should be 3.8+)
python3 --version

# Check if Claude CLI is installed
claude --version

# Check Node.js (optional, for MCP servers)
node --version
```

If any of these fail, see the [Prerequisites Setup](#prerequisites-setup-🛠️) section below.

## Quick Start 🚀

**🏆 The "Just Get It Working" Approach (Recommended for 90% of Users)**
**Option A: From PyPI (Recommended)**
```bash
pip install SuperGemini

# Install with recommended settings  
SuperGemini install --quick

# That's it! 🎉
```
**Option B: From Source**
```bash
# Clone the repo
git clone <repository-url>
cd SuperGemini
pip install .

# Install with recommended settings  
SuperGemini install --quick

# That's it! 🎉
```
**⚠️ Important Note**
**After installing the SuperGemini.**
**You can use `SuperGemini commands`
, `python3 -m SuperGemini commands` or also `python3 SuperGemini commands`**

**What you just got:**
- ✅ All 16 smart commands that auto-activate experts  
- ✅ 13 specialized domain expert agents that know when to help
- ✅ Advanced session management with brainstorming mode
- ✅ Python hooks system for intelligent framework coordination
- ✅ Intelligent routing that figures out complexity for you
- ✅ About 2 minutes of your time and ~50MB disk space

**Seriously, you're done.** Open Gemini CLI, type `/help`, and watch SuperGemini work its magic.

**Nervous about what it will do?** See first with:
```bash
SuperGemini install --quick --dry-run
```

## Installation Options 🎯

We have three installation profiles to choose from:

### 🎯 Minimal Installation
```bash
SuperGemini install --minimal
```
- **What**: Just the core framework files
- **Time**: ~1 minute
- **Space**: ~20MB  
- **Good for**: Testing, basic enhancement, minimal setups
- **Includes**: Core behavior documentation that guides Claude

### 🚀 Quick Installation (Recommended)
```bash
SuperGemini install --quick
```
- **What**: Core framework + 16 slash commands
- **Time**: ~2 minutes
- **Space**: ~50MB
- **Good for**: Most users, general development
- **Includes**: Everything in minimal + specialized commands like `/analyze`, `/build`, `/improve`

### 🪶 SuperGemini-Lite Installation (V4 Beta)
```bash
SuperGemini install --lite
```
- **What**: Streamlined version with core features only
- **Time**: ~1 minute
- **Space**: ~25MB
- **Good for**: Resource-constrained environments, basic enhancement
- **Includes**: Essential framework features without advanced orchestration

### 🔧 Developer Installation  
```bash
SuperGemini install --profile developer
```
- **What**: Everything including MCP server integration + Hooks system
- **Time**: ~5 minutes
- **Space**: ~100MB
- **Good for**: Power users, contributors, advanced workflows
- **Includes**: Everything + Context7, Sequential, Magic, Playwright, Morphllm, Serena servers + Python hooks

### 🎛️ Interactive Installation
```bash
SuperGemini install
```
- Lets you pick and choose components
- Shows detailed descriptions of what each component does
- Good if you want control over what gets installed

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
#or open command prompt or powershell
winget install python
```

**Missing Claude CLI?**
- Visit https://claude.ai/code for installation instructions
- SuperGemini enhances Gemini CLI, so you need it first

**Missing Node.js? (Optional)**
```bash
# Linux (Ubuntu/Debian)
sudo apt update && sudo apt install nodejs npm

# macOS
brew install node

# Windows  
# Download from https://nodejs.org/
#or open command prompt or powershell
winget install nodejs
```

### Getting SuperGemini 📥

**Option 1: From PyPI (Recommended)**
```bash
pip install SuperGemini
```

**Option 2: Download the latest release**
```bash
# Download and extract the latest release
# (Replace URL with actual release URL)
curl -L <release-url> -o superclaude-v3.zip
unzip superclaude-v3.zip
cd superclaude-v3
pip install .
```

**Option 3: Clone from Git**
```bash
git clone https://github.com/SuperClaude-Org/SuperGemini_Framework.git
cd SuperGemini_Framework
pip install .
```

### Running the Installer 🎬

The installer is pretty smart and will guide you through the process:

```bash
# See all available options
SuperGemini install --help

# Quick installation (recommended)
SuperGemini install --quick

# Want to see what would happen first?
SuperGemini install --quick --dry-run

# Install everything
SuperGemini install --profile developer

# Quiet installation (minimal output)
SuperGemini install --quick --quiet

# Force installation (skip confirmations)
python3 SuperGemini.py install --quick --force
```

### During Installation 📱

Here's what happens when you install:

1. **System Check** - Verifies you have required dependencies
2. **Directory Setup** - Creates `~/.claude/` directory structure
3. **Core Files** - Copies framework documentation files
4. **Commands** - Installs slash command definitions (if selected)
5. **MCP Servers** - Downloads and configures MCP servers (if selected)
6. **Hooks System** - Installs Python hooks for framework coordination (developer profile)
7. **Configuration** - Sets up `settings.json` with your preferences
8. **Validation** - Tests that everything works

The installer shows progress and will tell you if anything goes wrong.

## After Installation ✅

### Quick Test 🧪

Let's make sure everything worked:

```bash
# Check if files were installed
ls ~/.claude/

# Should show: GEMINI.md, COMMANDS.md, settings.json, etc.
```

**Test with Gemini CLI:**
1. Open Gemini CLI
2. Try typing `/help` - you should see SuperGemini commands
3. Try `/analyze --help` - should show command options

### What Got Installed 📂

SuperGemini V4 Beta installs to `~/.claude/` by default. Here's what you'll find:

```
~/.claude/
├── GEMINI.md              # Main framework entry point
├── FLAGS.md                # Command flags and options
├── PRINCIPLES.md           # Development principles
├── RULES.md                # Operational rules
├── ORCHESTRATOR.md         # Intelligent routing
├── MCP_*.md                # MCP server configurations
├── MODE_*.md               # Operational modes
├── SESSION_LIFECYCLE.md    # Session management
├── settings.json           # Configuration file
└── commands/               # Individual command definitions
    ├── analyze.md
    ├── build.md
    ├── improve.md
    └── ... (13 more)
```

**For Developer Installation (+Hooks System)**:
```
~/.claude/
├── [above files]           # Core framework files
└── hooks/                  # Python hooks system (developer profile)
    ├── framework_coordinator/
    ├── session_lifecycle/
    ├── performance_monitor/
    ├── quality_gates/
    └── install_hooks.py    # Hook installation script
```

**What each file does:**
- **GEMINI.md** - Tells Gemini CLI about SuperGemini and loads other files
- **settings.json** - Configuration (MCP servers, hooks, etc.)
- **commands/** - Detailed definitions for each slash command
- **hooks/** - Python hooks for advanced framework coordination (developer only)

### First Steps 🎯

Try these commands to get started:

```bash
# In Gemini CLI, try these:
/sg:help                    # See available commands
/sg:analyze README.md       # Analyze a file
/sg:build --help           # See build options
/sg:improve --help         # See improvement options
/sg:brainstorm "my app idea" # Try V4 Beta brainstorming mode
```

**Don't worry if it seems overwhelming** - SuperGemini enhances Gemini CLI gradually. You can use as much or as little as you want.

### Installing Hooks System (V4 Beta) 🔗

If you want to add the Python hooks system to an existing installation:

```bash
# Install hooks to existing SuperGemini installation
cd SuperGemini_Framework
python3 SuperGemini/Hooks/scripts/install_hooks.py

# Or upgrade existing installation with hooks
SuperGemini install --upgrade --hooks
```

**What the hooks system provides:**
- **Framework Coordinator**: Intelligent MCP server suggestions
- **Session Lifecycle**: Automatic checkpoint triggers  
- **Performance Monitor**: Real-time performance tracking (<100ms targets)
- **Quality Gates**: 8-step validation system

**Verification:**
```bash
# Test hooks installation
python3 SuperGemini/Hooks/scripts/test_hooks.py

# Check hook status
SuperGemini hooks --status
```

## Managing Your Installation 🛠️

### Updates 📅

Keep SuperGemini up to date:

```bash
# Check for updates
SuperGemini update

# Force update (overwrite local changes)
SuperGemini update --force

# Update specific components only
SuperGemini update --components core,commands

# See what would be updated
SuperGemini update --dry-run
```

**When to update:**
- When new SuperGemini versions are released
- If you're having issues (updates often include fixes)
- When new MCP servers become available

### Backups 💾

Create backups before major changes:

```bash
# Create a backup
SuperGemini backup --create

# List existing backups  
SuperGemini backup --list

# Restore from backup
SuperGemini backup --restore

# Create backup with custom name
SuperGemini backup --create --name "before-update"
```

**When to backup:**
- Before updating SuperGemini
- Before experimenting with settings
- Before uninstalling
- Periodically if you've customized heavily

### Uninstallation 🗑️

If you need to remove SuperGemini:

```bash
# Remove SuperGemini (keeps backups)
SuperGemini uninstall

# Complete removal (removes everything)
SuperGemini uninstall --complete

# See what would be removed
SuperGemini uninstall --dry-run
```

**What gets removed:**
- All files in `~/.claude/` 
- MCP server configurations
- SuperGemini settings from Gemini CLI

**What stays:**
- Your backups (unless you use `--complete`)
- Gemini CLI itself (SuperGemini doesn't touch it)
- Your projects and other files

## Troubleshooting 🔧

### Common Issues 🚨

**"Python not found"**
```bash
# Try python instead of python3
python --version

# Or check if it's installed but not in PATH
which python3
```

**"Claude CLI not found"**
- Make sure Gemini CLI is installed first
- Try `claude --version` to verify
- Visit https://claude.ai/code for installation help

**"Permission denied"**
```bash
# Try with explicit Python path
/usr/bin/python3 SuperGemini.py install --quick

# Or check if you need different permissions
ls -la ~/.claude/
```

**"MCP servers won't install"**
- Check that Node.js is installed: `node --version`
- Check that npm is available: `npm --version`  
- Try installing without MCP first: `--minimal` or `--quick`

**"Installation fails partway through"**
```bash
# Try with verbose output to see what's happening
SuperGemini install --quick --verbose

# Or try a dry run first
SuperGemini install --quick --dry-run
```

### Platform-Specific Issues 🖥️

**Windows:**
- Use `python` instead of `python3` if you get "command not found"
- Run Command Prompt as Administrator if you get permission errors
- Make sure Python is in your PATH

**macOS:**  
- You might need to approve SuperGemini in Security & Privacy settings
- Use `brew install python3` if you don't have Python 3.8+
- Try using `python3` explicitly instead of `python`

**Linux:**
- Make sure you have `python3-pip` installed
- You might need `sudo` for some package installations
- Check that `~/.local/bin` is in your PATH

### Still Having Issues? 🤔

**Check our troubleshooting resources:**
- GitHub Issues: https://github.com/SuperClaude-Org/SuperGemini_Framework/issues
- Look for existing issues similar to yours
- Create a new issue if you can't find a solution

**When reporting bugs, please include:**
- Your operating system and version
- Python version (`python3 --version`)
- Claude CLI version (`claude --version`)
- The exact command you ran
- The complete error message
- What you expected to happen

**Getting Help:**
- GitHub Discussions for general questions
- Check the README.md for latest updates
- Look at the ROADMAP.md to see if your issue is known

## Advanced Options ⚙️

### Custom Installation Directory

```bash
# Install to custom location
SuperGemini install --quick --install-dir /custom/path

# Use environment variable
export SUPERGEMINI_DIR=/custom/path
SuperGemini install --quick
```

### Component Selection

```bash
# See available components
SuperGemini install --list-components

# Install specific components only
SuperGemini install --components core,commands

# Skip certain components
SuperGemini install --quick --skip mcp
```

### Development Setup

If you're planning to contribute or modify SuperGemini:

```bash
# Developer installation with all components
SuperGemini install --profile developer

# Install in development mode (symlinks instead of copies)
SuperGemini install --profile developer --dev-mode

# Install with git hooks for development
SuperGemini install --profile developer --dev-hooks
```

## What's Next? 🚀

**Now that SuperGemini is installed (that was easy, right?):**

1. **Just start using it** - Try `/analyze some-file.js` or `/build` and see what happens ✨
2. **Don't stress about learning** - SuperGemini usually figures out what you need
3. **Experiment freely** - Commands like `/improve` and `/troubleshoot` are pretty forgiving
4. **Read guides if curious** - Check `Docs/` when you want to understand what just happened
5. **Give feedback** - Let us know what works and what doesn't

**The real secret**: SuperGemini is designed to enhance your existing workflow without you having to learn a bunch of new stuff. Just use it like you'd use regular Gemini CLI, but notice how much smarter it gets! 🎯

**Still feeling uncertain?** Start with just `/help` and `/analyze README.md` - you'll see how non-intimidating it actually is.

---

## Final Notes 📝

- **Installation takes 1-5 minutes** depending on what you choose
- **Disk space needed: 20-100MB** (not much!)
- **Works alongside existing tools** - doesn't interfere with your setup
- **Easy to uninstall** if you change your mind
- **Community supported** - we actually read and respond to issues
- ### ⚠️ Important Note 
**After installing the SuperGemini.**
**You can use `SuperGemini commands`
, `python3 -m SuperGemini commands` or also `python3 SuperGemini commands`**

Thanks for trying SuperGemini! We hope it makes your development workflow a bit smoother. 🙂

---

*Last updated: January 2025 (V4 Beta) - Let us know if anything in this guide is wrong or confusing!*
