# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SuperGemini is a meta-programming framework that enhances Gemini CLI with structured development capabilities. It operates through **behavioral instruction injection** - modifying AI behavior via configuration files rather than code changes.

**Key Architecture Pattern**: This is NOT a traditional Python application. SuperGemini is a **configuration distribution system** that:
1. Installs behavioral instruction files (`.md`, `.toml`) to `~/.gemini/`
2. These files modify Gemini CLI behavior through instruction injection
3. Python code (`setup/`, `SuperGemini/`) handles installation/management, not runtime execution

**Package Aliases**: The CLI is accessible via three entry points:
- `SuperGemini` (primary, capitalized)
- `supergemini` (lowercase alias)
- `sg` (short form)

Documentation MUST use `SuperGemini` (capitalized) for consistency. See `pyproject.toml:44-47` for authoritative source.

## Development Commands

### Installation & Setup
```bash
# Development installation (editable mode)
pip install -e .

# Install with pipx (production-like testing)
pipx install .

# Run the CLI directly
python -m SuperGemini install --help
SuperGemini --version
```

### Testing
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_mcp_prerequisites.py

# Run with coverage
pytest --cov=SuperGemini --cov=setup --cov-report=html

# Run tests matching pattern
pytest -k "test_find_node"
```

### Code Quality
```bash
# Format code with black
black SuperGemini/ setup/ tests/

# Lint with flake8
flake8 SuperGemini/ setup/ --max-line-length=88

# Type checking with mypy
mypy SuperGemini/ setup/
```

### Building & Distribution
```bash
# Build distribution packages
python -m build

# Check distribution
twine check dist/*

# Test installation from built package
pip install dist/SuperGemini-*.whl
```

## Critical Architecture Concepts

### 1. Component-Based Installation System

**Location**: `setup/components/`

SuperGemini installs **six component types** to `~/.gemini/`:

```
setup/components/
├── core.py        # Core framework files (PRINCIPLES.md, RULES.md, FLAGS.md)
├── commands.py    # /sg: slash commands (18 TOML files → ~/.gemini/commands/sg/)
├── modes.py       # Behavioral modes (brainstorming, introspection, etc.)
├── mcp.py         # MCP server configurations (context7, sequential, magic, etc.)
├── mcp_docs.py    # MCP documentation files
```

**Key Pattern**: Each component extends `setup/core/base.py:Component` abstract class:
- `get_metadata()` - component identity
- `validate_prerequisites()` - installation requirements
- `install()` - copy files to ~/.gemini
- `uninstall()` - remove component files
- `update()` - version management

### 2. Dual Directory Structure

**CRITICAL**: This project has TWO primary directories with similar names but different purposes:

**`SuperGemini/`** (Package Source):
- **Purpose**: Source files that get COPIED during installation
- Contains: Commands/, Agents/, Modes/, Core/, Config/, MCP/
- These are `.md` and `.toml` files that modify Gemini CLI behavior
- **Never executed directly** - they are configuration/instruction files

**`setup/`** (Installation Engine):
- **Purpose**: Python code that performs the installation
- Contains: components/, core/, services/, utils/
- This IS the executable code that runs during `SuperGemini install`
- Handles file copying, validation, configuration management

**Mental Model**:
- `SuperGemini/` = "payload" (what gets installed)
- `setup/` = "installer" (how it gets installed)

### 3. Command Namespace: `/sg:` vs `SuperGemini`

**Two distinct command spaces**:

**Terminal Commands** (installer management):
```bash
SuperGemini install --yes         # Runs setup/core/installer.py
SuperGemini update                # Updates installed components
SuperGemini uninstall             # Removes ~/.gemini files
```

**Gemini CLI Commands** (after installation):
```
/sg:analyze src/                  # Uses ~/.gemini/commands/sg/analyze.toml
/sg:implement "feature"           # Uses ~/.gemini/commands/sg/implement.toml
/sg:save checkpoint              # Uses ~/.gemini/commands/sg/save.toml
```

**Critical Distinction**: `/sg:` commands are NOT Python functions. They are TOML configuration files that inject prompts into Gemini CLI.

### 4. Instruction Injection Mechanism

**How commands work** (`setup/components/commands.py:377-463`):

1. Source: `SuperGemini/Commands/analyze.md` (Markdown with front matter)
2. Conversion: `_convert_md_to_toml()` converts to TOML format
3. Installation: Copied to `~/.gemini/commands/sg/analyze.toml`
4. Gemini CLI reads TOML and injects prompt when `/sg:analyze` is typed

**TOML Structure**:
```toml
prompt = """SuperGemini Framework Command: /sg:analyze

[Full command instructions here...]

When handling flags:
- --seq: Activate sequential-thinking MCP server
- --c7: Activate context7 MCP server
"""

description = "Analyze codebase architecture"
```

### 5. Agent System (Persona Mode)

**Location**: `SuperGemini/Agents/` (13 specialized agent files)

**Not sub-agents**: SuperGemini uses "Persona Mode" - Gemini CLI *embodies* the agent role rather than spawning separate processes.

**Agent Files** (Markdown instruction files):
```
backend-architect.md       # Backend system design
frontend-architect.md      # UI/UX architecture
security-engineer.md       # Security analysis (veto authority)
system-architect.md        # High-level system design
performance-engineer.md    # Optimization specialist
quality-engineer.md        # Testing and validation
python-expert.md          # Python-specific expertise
devops-architect.md       # Infrastructure and deployment
learning-guide.md         # Educational guidance
refactoring-expert.md     # Code quality improvement
requirements-analyst.md    # Requirements discovery
root-cause-analyst.md     # Problem diagnosis
technical-writer.md       # Documentation specialist
```

**Activation Pattern**: Agents auto-activate based on:
- Keyword triggers (e.g., "security" → security-engineer)
- File types (e.g., `.py` → python-expert)
- Complexity scoring (system-architect for complex multi-domain tasks)
- Explicit mention (e.g., "@agent-security-engineer")

## File Organization Standards

### Where to Place New Files

**Component Source Files** (what users get):
- New commands → `SuperGemini/Commands/[name].md`
- New agents → `SuperGemini/Agents/[name].md`
- New modes → `SuperGemini/Modes/[name].md`
- Core behavioral files → `SuperGemini/Core/`

**Installation Code** (how it gets there):
- Component installers → `setup/components/[type].py`
- Shared services → `setup/services/` (files.py, settings.py, etc.)
- Utilities → `setup/utils/` (logger.py, security.py, ui.py)
- Tests → `tests/test_[component].py`

**Documentation**:
- Claude Code analysis/reports → `claudedocs/` (gitignored, working files)
- User guides → `Docs/User-Guide/`
- Developer guides → `Docs/Developer-Guide/`
- Reference material → `Docs/Reference/`

**Never Create**:
- Test files next to source (use `tests/` directory)
- Scripts in project root (would clutter)
- Temporary debug files (use `claudedocs/` or delete after use)

## Common Development Workflows

### Adding a New Command

1. **Create command file**: `SuperGemini/Commands/newcommand.md`
   ```markdown
   ---
   description: "Brief command description"
   allowed-tools: ["Read", "Write", "Bash"]
   ---

   # /sg:newcommand

   [Command instructions here]
   ```

2. **Register in installer**: Edit `setup/components/commands.py:20-40`
   ```python
   def _get_command_files(self) -> List[str]:
       return [
           # ... existing commands ...
           "newcommand.toml",
       ]
   ```

3. **Test installation**:
   ```bash
   SuperGemini install --components commands --force
   # Verify: ls ~/.gemini/commands/sg/ | grep newcommand
   ```

### Adding a New Agent

1. **Create agent file**: `SuperGemini/Agents/new-agent.md`
   - Include trigger keywords, capabilities, integration notes
   - Follow existing agent file structure

2. **Document in user guide**: Add entry to `Docs/User-Guide/agents.md`

3. **No code changes needed** - agents auto-activate based on file presence

### Modifying Core Behavioral Rules

**Files**: `SuperGemini/Core/` (PRINCIPLES.md, RULES.md, FLAGS.md, etc.)

These inject into GEMINI.md during installation. Changes affect Gemini CLI behavior globally.

**Testing changes**:
```bash
SuperGemini install --components core --force
# Verify: cat ~/.gemini/GEMINI.md | grep "your change"
```

## Testing Strategy

### Test Structure
```
tests/
├── test_mcp_prerequisites.py    # MCP installation validation
├── conftest.py                  # Pytest fixtures (if exists)
└── [component]_test.py          # Component-specific tests
```

### Key Testing Principles

1. **Test Installation, Not Runtime**: Commands don't execute in Python - test file copying, TOML generation, validation

2. **Mock ~/.gemini Directory**: Use `tmp_path` fixture to avoid affecting real Gemini CLI

3. **Component Isolation**: Test each component independently

**Example Test Pattern**:
```python
def test_commands_component_installation(tmp_path):
    """Test that commands install correctly to sg/ subdirectory"""
    component = CommandsComponent(install_dir=tmp_path)

    # Test prerequisites
    valid, errors = component.validate_prerequisites()
    assert valid, f"Prerequisites failed: {errors}"

    # Test installation
    config = {"force": True}
    assert component.install(config)

    # Verify files
    commands_dir = tmp_path / "commands" / "sg"
    assert commands_dir.exists()
    assert (commands_dir / "analyze.toml").exists()
```

## Documentation Syntax Standards

**CRITICAL**: Command syntax inconsistencies cause user confusion.

### Standard Patterns

**Product Name** (prose):
```markdown
✅ SuperGemini is a meta-programming framework
❌ supergemini is a framework
```

**CLI Executable** (terminal commands):
```bash
✅ SuperGemini install --yes
✅ SuperGemini update
❌ superclaude install  # Wrong project
```

**Slash Commands** (Gemini CLI):
```markdown
✅ /sg:analyze src/
✅ /sg:implement "feature"
❌ /SG:analyze  # Wrong case
❌ /sc:analyze  # Wrong prefix (that's SuperClaude)
```

**Related Projects** (SuperClaude-Org ecosystem):
- SuperGemini: `/sg:` prefix (this project)
- SuperClaude: `/sc:` prefix (Claude Code framework)
- SuperQwen: `/sq:` prefix (Qwen framework)

See `claudedocs/CSI_WF.md` for complete standardization rules.

## MCP Server Integration

**MCP = Model Context Protocol** - external tool integration system

**Six Core Servers** (configured in `setup/components/mcp.py`):
1. **context7** - Official library documentation
2. **sequential** - Multi-step reasoning engine
3. **magic** - UI component generation (21st.dev)
4. **playwright** - Browser automation and testing
5. **morphllm** - Pattern-based code transformation
6. **serena** - Semantic code understanding + session memory

**Configuration Files**: `SuperGemini/MCP/Docs/MCP_[ServerName].md`

**Installation Trigger**: `SuperGemini install --components mcp`

**Prerequisites**: Most MCP servers require Node.js. Installation validates via:
- `setup/utils/environment.py` - PATH detection
- `setup/services/mcp.py` - Node.js version checking
- Version manager support (nvm, fnm) auto-detected

## Version Management

**Single Source of Truth**: `VERSION` file in project root

**Version Access**:
```python
# In code
from SuperGemini.version import __version__

# From CLI
SuperGemini --version
```

**Version Update Process**:
1. Update `VERSION` file (e.g., `4.3.0` → `4.2.2`)
2. Version automatically propagates to:
   - `pyproject.toml` (dynamic = {file = "VERSION"})
   - `setup.py` (`get_version()` reads VERSION file)
   - `SuperGemini/version.py` (generated during build)
   - All component metadata (`get_metadata()["version"]`)

## Security Considerations

**Installation Validation** (`setup/utils/security.py`):
- Path traversal prevention (`validate_installation_target()`)
- Permission checking before file operations
- Safe path resolution (no symlink attacks)

**User Trust Model**:
- Files installed to `~/.gemini/` (user-owned directory)
- No system-wide modifications
- No privilege escalation
- Users explicitly run `SuperGemini install`

**External Integrations**:
- MCP servers run in separate processes
- Node.js/npm checked but not automatically installed
- User controls which components to install

## Performance Optimization

**Large Documentation**: Some docs exceed 4000 lines (technical-architecture.md, testing-debugging.md)
- Use navigation links and table of contents
- Consider splitting into smaller focused documents

**Installation Speed**:
- Minimal dependencies (only setuptools required)
- File copying, not code generation
- Component-based installation (install only what you need)

## Common Pitfalls

### 1. Confusing Source vs Installation Directories
❌ **Wrong**: Editing `~/.gemini/commands/sg/analyze.toml` directly
✅ **Right**: Edit `SuperGemini/Commands/analyze.md`, reinstall with `--force`

### 2. Testing Commands as Python Functions
❌ **Wrong**: `from SuperGemini.Commands import analyze`
✅ **Right**: Test file installation and TOML generation

### 3. Breaking Command Syntax Standards
❌ **Wrong**: Using `superclaude install` in documentation
✅ **Right**: Always use `SuperGemini install` (capitalized)

### 4. Ignoring Component Dependencies
**Components have install order** (`setup/components/[type].py:get_dependencies()`):
- Core must install first (provides base behavioral files)
- Other components depend on core existing

### 5. Hardcoding Paths
❌ **Wrong**: `/home/user/.gemini/commands/sg/`
✅ **Right**: `self.install_dir / "commands" / "sg"`
Use `setup/__init__.py:DEFAULT_INSTALL_DIR` constant

## Cross-Platform Compatibility

**Supported**: Linux, macOS, Windows (Python 3.8+)

**Path Handling**: Always use `pathlib.Path`, never string concatenation
```python
# ✅ Right
config_path = Path.home() / ".gemini" / "config.json"

# ❌ Wrong
config_path = os.path.expanduser("~") + "/.gemini/config.json"
```

**Shell Commands**: Platform detection in `setup/services/files.py`
- Windows: Uses PowerShell equivalents when needed
- Unix: Standard bash commands

## Project Ecosystem Context

SuperGemini is part of **SuperClaude-Org** - a family of AI enhancement frameworks:

- **SuperGemini** (this project) - Gemini CLI enhancement
- **SuperClaude** - Claude Code enhancement
- **SuperQwen** - Qwen CLI enhancement

**Shared Architecture**: All three use similar patterns:
- Behavioral instruction injection
- Component-based installation
- Slash command systems (different prefixes)
- Agent-based specialization

**Cross-Project References**:
- Legitimate: `@superclaude-org/superagent` (npm MCP server)
- Legacy/Errors: `superclaude install` (should be `SuperGemini install`)

See `claudedocs/CSI_WF.md` for disambiguation strategy.

## Getting Help

**Documentation Structure**:
```
Docs/
├── Getting-Started/      # Installation, quick start
├── User-Guide/          # Commands, agents, modes, flags
├── Developer-Guide/     # Architecture, contributing, testing
└── Reference/           # Best practices, troubleshooting
```

**Key Developer Guides**:
- `Docs/Developer-Guide/technical-architecture.md` - System design (150+ sections)
- `Docs/Developer-Guide/contributing-code.md` - Development workflows
- `Docs/Developer-Guide/testing-debugging.md` - QA procedures

**Issue Reporting**: See `CONTRIBUTING.md:12-44` for bug report template requirements

## Build & Release Process

**Not documented in codebase** - no CI/CD configs found in this analysis.

**Manual Build**:
```bash
# Bump version in VERSION file
echo "4.2.2" > VERSION

# Build distribution
python -m build

# Upload to PyPI (requires credentials)
twine upload dist/*
```

**NPM Wrapper**: Separate npm package (`@superclaude-org/supergemini`) wraps Python package for Node.js users.