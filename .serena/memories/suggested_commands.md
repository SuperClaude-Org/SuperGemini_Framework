# SuperGemini Framework Suggested Commands

## Installation Commands
```bash
# Install from PyPI
pip install SuperGemini

# Verify installation
SuperGemini --version

# Quick install all components
SuperGemini install --quick --yes

# Interactive installation
SuperGemini install

# Install specific components
SuperGemini install --components commands mcp

# List available components
SuperGemini install --list-components
```

## Development Commands (17 Specialized Commands)
```gemini
# Development Commands
/sg:implement     # Implementation assistance
/sg:build         # Build with framework detection
/sg:design        # Design guidance

# Analysis Commands  
/sg:analyze --seq # Analysis with sequential thinking
/sg:troubleshoot  # Problem investigation
/sg:explain       # Code explanation

# Quality Commands
/sg:improve --focus performance  # Performance optimization
/sg:test          # Testing assistance
/sg:cleanup       # Code cleanup

# Planning Commands
/sg:workflow      # Workflow planning
/sg:task          # Task management
/sg:estimate      # Estimation assistance

# Other Commands
/sg:document      # Documentation generation
/sg:git           # Git operations
/sg:index         # Indexing operations
/sg:load          # Context loading
/sg:spawn         # Process spawning
```

## Flag Support
```bash
--seq      # Activate sequential-thinking MCP
--c7       # Activate Context7 documentation  
--verbose  # Detailed output
--quiet    # Minimal output
```

## Configuration Files
- `~/.gemini/settings.json` - Main configuration and MCP servers
- `~/.gemini/commands/sg/*.toml` - Command definitions

## Build and Development
```bash
# Build package
python -m build

# Install in development mode
pip install -e .

# Run tests (if available)
python -m pytest
```