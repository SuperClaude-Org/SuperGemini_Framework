# SuperClaude Troubleshooting Guide 🔧

## Quick Problem Diagnosis 🚨

**Something not working?** Start here for the fastest path to solutions. For working examples to compare against, see [Examples Cookbook](examples-cookbook.md).

### Immediate Solutions (Try These First)

**Commands not showing up?**
```bash
# Check if SuperClaude is installed
ls ~/.claude/CLAUDE.md

# If missing, reinstall
SuperClaude install
```

**Command not working as expected?**
```bash
# Try with help flag to see options
/sc:analyze --help

# Use preview mode to see what would happen
/sc:improve --preview src/file.js

# Start with smaller scope
/sc:analyze single-file.js  # instead of entire project
```

**Analysis taking forever?**
```bash
# Use focus to narrow scope
/sc:analyze --focus security src/

# Try quick depth instead of deep
/sc:analyze --depth quick large-project/

# Use compressed mode for efficiency
/sc:analyze --uc huge-codebase/
```

**Getting weird results?**
```bash
# Force safe mode for conservative execution
/sc:improve --safe-mode production-code/

# Add validation to check before doing anything
/sc:cleanup --validate --preview messy-code/

# Use explicit scope
/sc:build --scope file instead of --scope project
```

---

## Installation & Setup Issues 🛠️

### Installation Problems

**"Python not found"**
```bash
# Try different Python commands
python --version     # Windows often uses this
python3 --version    # Linux/macOS typically use this

# Check if Python is in PATH
which python3       # Linux/macOS
where python        # Windows

# Install Python if missing
# Ubuntu/Debian:
sudo apt update && sudo apt install python3 python3-pip

# macOS:
brew install python3

# Windows:
winget install python
# Or download from https://python.org/downloads/
```

**"SuperClaude command not found"**
```bash
# Try with explicit Python module
python3 -m SuperClaude install

# Check if it's installed
pip list | grep SuperClaude

# Install if missing
pip install SuperClaude

# Try with full path if PATH issues
/usr/bin/python3 -m SuperClaude install
```

**"Claude Code not found"**
- SuperClaude enhances Claude Code, so you need Claude Code installed first
- Visit https://claude.ai/code for installation instructions
- Make sure Claude Code is working before installing SuperClaude

**"Permission denied" errors**
```bash
# Check directory permissions
ls -la ~/.claude/

# Try with explicit Python path
/usr/bin/python3 -m SuperClaude install

# On Windows, run Command Prompt as Administrator
# On macOS, you might need to approve in Security & Privacy settings
```

### MCP Server Installation Issues

**"Node.js required for MCP servers"**
```bash
# Check if Node.js is installed
node --version
npm --version

# Install Node.js if missing
# Ubuntu/Debian:
sudo apt update && sudo apt install nodejs npm

# macOS:
brew install node

# Windows:
winget install nodejs
# Or download from https://nodejs.org/
```

**"MCP servers won't install"**
```bash
# Install without MCP servers first
SuperClaude install
# During interactive setup, select "Skip MCP Server installation"

# Install MCP servers separately later if needed
SuperClaude install --components mcp

# Check MCP server status
SuperClaude install --diagnose
```

**Installation fails partway through**
```bash
# Try with verbose output to see what's happening
SuperClaude install --verbose

# Try a dry run first to see what would happen
SuperClaude install --dry-run

# Run system diagnostics
SuperClaude install --diagnose

# Try installing specific components only
SuperClaude install --components core commands
```

### Platform-Specific Issues

**Windows Issues:**
- Use `python` instead of `python3` if you get "command not found"
- Run Command Prompt as Administrator if you get permission errors  
- Make sure Python is in your PATH environment variable
- Windows Defender might flag SuperClaude - add exclusion if needed

**macOS Issues:**
- Use `brew install python3` if you don't have Python 3.8+
- You might need to approve SuperClaude in Security & Privacy settings
- Try using `python3` explicitly instead of `python`
- Check that ~/.local/bin is in your PATH

**Linux Issues:**
- Make sure you have `python3-pip` installed: `sudo apt install python3-pip`
- You might need `sudo` for some package installations
- Check that `~/.local/bin` is in your PATH: `echo $PATH`
- Some distros need `python3-venv`: `sudo apt install python3-venv`

---

## Command Problems 🛠️

### Commands Not Working

**"Command not recognized"**
```bash
# Make sure you're using the right prefix
/sc:analyze          # Correct
/analyze             # Wrong - missing sc: prefix

# Check available commands
/sc:index

# Try the command with help
/sc:troubleshoot --help
```

**"No such file or directory"**
```bash
# Use absolute paths, not relative
/sc:analyze /home/user/project/src/    # Correct
/sc:analyze ../project/src/           # May not work

# Check if file exists first
ls -la /path/to/file.js
```

**Commands running but giving poor results**
```bash
# Be more specific with scope
/sc:analyze --focus security auth.js  # Instead of just /sc:analyze auth.js

# Use appropriate depth
/sc:analyze --think complex-system/    # For complex analysis
/sc:analyze --depth quick simple.js   # For simple files

# Add context with framework flags
/sc:build --c7 react-app/            # Use Context7 for React patterns
```

### Flag Issues

**"Flag not working"**
```bash
# Check spelling (common typos)
--ultracompressed    # Correct
--ultracompresed     # Wrong - typo

--agent security-engineer    # Correct  
--agent frontend-architect   # Wrong - should be frontend-architect

# Some flags need values
--scope project      # Correct
--scope             # Wrong - missing value

# Check for flag conflicts
--no-mcp --c7       # Conflict: --no-mcp overrides --c7
```

**"Flags seem ignored"**
```bash
# Explicit flags override auto-detection
/sc:analyze --agent security-engineer auth.js  # Forces security focus

# Check flag precedence
--safe-mode --optimize    # --safe-mode wins (safety first)

# Some combinations don't make sense
--no-mcp --sequential     # --no-mcp disables --sequential
```

### Scope and Focus Issues

**"Analysis too broad/narrow"**
```bash
# Use scope to control breadth
--scope file         # Single file only
--scope module       # Related files
--scope project      # Entire project  
--scope system       # Cross-project

# Use focus to control domain
--focus security     # Security-specific analysis
--focus performance  # Performance-specific analysis
--focus quality      # Code quality focus
```

**"Wrong expert activated"**
```bash
# Force specific agent
/sc:analyze --agent security-engineer frontend-code.js

# Use focus to guide agent selection
/sc:analyze --focus security auth-system/

# Check what got activated and why
/sc:analyze --verbose --introspect problem-area/
```

---

## Performance Issues ⚡

### Speed Problems

**"Commands too slow"**
```bash
# Use compressed mode
/sc:analyze --uc large-codebase/

# Disable MCP servers if not needed
/sc:analyze --no-mcp simple-project/

# Limit scope
/sc:analyze --scope file slow-analysis.js

# Use quick depth for faster analysis
/sc:analyze --depth quick instead of --depth deep
```

**"Context getting full"**
```bash
# Enable token efficiency mode
/sc:command --uc

# This automatically activates when context >75%
# Reduces token usage by 30-50% while preserving information
```

**"Too much output"**
```bash
# Use compressed communication
/sc:analyze --uc verbose-command/

# Remove verbose flag if present
/sc:build --verbose    # Remove --verbose

# Use answer-only for simple questions
/sc:explain React hooks --answer-only
```

### Memory and Resource Issues

**"Running out of resources"**
```bash
# Force safe mode (automatically manages resources)
/sc:command --safe-mode

# Control concurrency for parallel operations
/sc:analyze --delegate auto --concurrency 2

# Use efficient tools
--no-mcp          # Disable resource-heavy MCP servers
--uc              # Compress communication
--scope file      # Limit analysis scope
```

**"System becoming unresponsive"**
```bash
# Use safe mode with validation
/sc:improve --safe-mode --validate production-code/

# Limit concurrent operations
/sc:task --concurrency 1 large-operation

# Break large tasks into smaller pieces
/sc:analyze src/auth/     # Instead of entire src/
```

### Token Usage Optimization

**"Using too many tokens"**
```bash
# Enable ultra-compressed mode
/sc:command --uc

# Focus on specific areas
/sc:analyze --focus performance --scope module

# Use efficient MCP combinations
--seq --c7       # Good combination for structured analysis
--all-mcp        # Avoid unless you need all capabilities
```

**"Context limits reached"**
```bash
# SuperClaude should auto-activate --uc when context >75%
# If not happening, force it:
/sc:continue --uc

# Break large operations into smaller chunks
/sc:analyze src/auth/ && /sc:analyze src/api/

# Use session management
/sc:save --checkpoint before-large-operation
```

---

## Agent & MCP Server Issues 🤖

### Agent Activation Problems

**"Wrong agent activated"**
```bash
# Check what triggered automatic selection
/sc:analyze --verbose --introspect file.js

# Force specific agent
/sc:analyze --agent security-engineer auth.js
/sc:build --agent frontend-architect ui-components/

# Use focus to guide agent selection
/sc:analyze --focus security        # Guides toward security-engineer
/sc:build --focus performance       # Guides toward performance-engineer
```

**"Agent not working as expected"**
```bash
# Verify agent capabilities
/sc:index --category agents

# Try with different focus
/sc:analyze --agent root-cause-analyst --focus debugging bug-report/

# Check if additional tools are needed
/sc:analyze --agent security-engineer --seq --c7 auth-system/
```

### MCP Server Problems

**"MCP server not activating"**
```bash
# Check if MCP servers are installed
SuperClaude install --diagnose

# Force MCP server activation
/sc:analyze --c7 react-components/      # Force Context7
/sc:debug --seq complex-problem/        # Force Sequential
/sc:build --magic ui-components/        # Force Magic

# Check MCP server status
SuperClaude install --list-components | grep mcp
```

**"Sequential MCP too slow"**
```bash
# Sequential is designed for complex problems
# For simple tasks, disable it:
/sc:explain simple-function --no-mcp

# Use appropriate depth
/sc:debug --think simple-bug/           # Instead of --think-hard
/sc:debug --ultrathink critical-issue/  # Only for critical issues
```

**"Context7 not finding docs"**
```bash
# Make sure you're using current framework names
"React hooks"       # Good - specific and current
"old JavaScript"    # Poor - too vague

# Be specific about versions
"Next.js 14 routing"    # Good
"Next.js routing"       # Less specific

# Context7 works best with mainstream frameworks
React, Vue, Angular, Next.js, Express    # Well supported
Obscure frameworks                        # May have limited docs
```

**"Magic MCP not generating good UI"**
```bash
# Be specific about component requirements
/sc:build --magic "responsive login form with validation"

# Include design system context
/sc:build --magic --c7 "dashboard using Material-UI patterns"

# Magic works best with modern UI frameworks
"React component"     # Good
"plain HTML"         # Use native tools instead
```

**"Playwright MCP tests failing"**
```bash
# Check browser requirements
# Playwright needs browsers installed - this may happen automatically

# Be specific about test requirements
/sc:test --play "login flow with form validation"

# Start with simple tests first
/sc:test --play "page loads"    # Simple
/sc:test --play "complex user journey"    # More complex
```

### Tool Coordination Issues

**"Multiple MCP servers conflicting"**
```bash
# Not all combinations work well together
--all-mcp           # Can be overwhelming, use sparingly

# Good combinations:
--seq --c7          # Sequential reasoning + official docs
--magic --c7        # UI generation + framework patterns
--seq --play        # Systematic testing approach

# Avoid unless needed:
--morph --serena --magic --seq    # Too many tools
```

**"Auto-activation not working"**
```bash
# Force the tools you want
/sc:analyze --agent security-engineer --c7 --seq auth-system/

# Use introspection to see what's happening
/sc:troubleshoot --introspect "why isn't this working?"

# Check trigger conditions
Framework code → Should activate Context7
Complex debugging → Should activate Sequential  
UI components → Should activate Magic
```

---

## Integration Problems 🔗

### Framework Integration

**"SuperClaude doesn't understand my framework"**
```bash
# Use Context7 for mainstream frameworks
/sc:build --c7 vue-app/
/sc:build --c7 angular-app/  
/sc:build --c7 next-js-app/

# For custom frameworks, be explicit
/sc:build "custom React setup with Vite and TypeScript"

# Include relevant files in analysis
/sc:analyze package.json tsconfig.json src/
```

**"Not following project conventions"**
```bash
# Make sure SuperClaude sees your config files
/sc:load .  # Loads project context including configs

# Point to specific patterns
/sc:analyze existing-component.js  # Show example before asking for new ones

# Use --safe mode to be conservative
/sc:improve --safe existing-code.js
```

### Build System Issues

**"Build commands not working"**
```bash
# Make sure build tools are in PATH
npm --version
yarn --version  
pnpm --version

# Check if package.json has scripts
cat package.json | grep scripts

# Use specific build type
/sc:build --type prod    # Production build
/sc:build --type dev     # Development build
```

**"Tests not running"**
```bash
# Check test framework is configured
/sc:test --type unit     # For unit tests
/sc:test --type e2e      # For end-to-end tests

# Make sure test files exist
ls tests/
ls **/*.test.js

# Try with specific test runner
/sc:test jest           # If using Jest
/sc:test --play         # For browser tests
```

### Version Control Issues

**"Git operations failing"**
```bash
# Always check status first
git status
git branch

# Make sure you're on a feature branch
git checkout -b feature/my-changes

# Use SuperClaude git helpers
/sc:git --smart-commit "describe your changes"
/sc:git status          # Enhanced status
```

**"Commit messages poor quality"**
```bash
# Use smart commit for better messages
/sc:git --smart-commit add .

# Be descriptive about changes
/sc:git commit "implement user authentication with JWT tokens"

# Review before committing
git diff --staged
```

---

## Quality & Safety Issues 🛡️

### Unsafe Code Generation

**"Generated code breaks things"**
```bash
# Always use safe mode for important code
/sc:improve --safe-mode production-code.js

# Use preview to see changes first
/sc:refactor --preview --safe legacy-system/

# Validate before applying
/sc:cleanup --validate --preview messy-code/
```

**"Too many changes at once"**
```bash
# Use iterative improvement
/sc:improve --loop --iterations 3 --safe complex-file.js

# Break into smaller scopes
/sc:improve --scope file individual-file.js
/sc:improve --scope module related-files/

# Use validation gates
/sc:refactor --validate --interactive large-changes/
```

**"Changes don't follow project standards"**
```bash
# Load project context first
/sc:load .  # Understand project patterns

# Use safe mode
/sc:improve --safe existing-code.js

# Point to examples
/sc:analyze good-example.js && /sc:improve bad-example.js
```

### Test and Validation Problems

**"Tests being disabled or skipped"**
```bash
# Never acceptable - SuperClaude should never skip tests
# If this happens, it's a bug - report it

# Force test validation
/sc:test --coverage --validate

# Check for skipped tests
grep -r "skip\|disable" tests/
```

**"Quality checks not running"**
```bash
# Force quality analysis
/sc:analyze --focus quality --validate codebase/

# Run comprehensive tests
/sc:test --type all --coverage

# Use quality-focused agents
/sc:analyze --agent quality-engineer --agent refactoring-expert code/
```

### Security Issues

**"Security analysis missing vulnerabilities"**
```bash
# Force security focus
/sc:analyze --focus security --agent security-engineer system/

# Use deep security analysis  
/sc:scan --ultrathink --focus security --validate critical-system/

# Check specific areas
/sc:analyze --focus security auth/ payment/ user-data/
```

**"Generated code has security flaws"**
```bash
# Always use safe mode for security-sensitive code
/sc:implement --safe-mode --focus security auth-system

# Validate security explicitly
/sc:analyze --focus security --validate generated-code.js

# Use security-focused agents
/sc:implement --agent security-engineer payment-processing
```

---

## Advanced Troubleshooting 🔬

### Systematic Problem Analysis

When basic solutions don't work, use systematic debugging:

**Step 1: Gather Information**
```bash
# Check system status
SuperClaude install --diagnose

# Check git status
git status && git branch

# Check project structure
/sc:load . --summary

# Verify component installation
SuperClaude install --list-components
```

**Step 2: Isolate the Problem**
```bash
# Test with minimal scope
/sc:analyze simple-file.js --no-mcp

# Test with different agents
/sc:analyze --agent learning-guide simple-problem

# Test with different tools
/sc:analyze --c7 vs /sc:analyze --seq vs /sc:analyze --no-mcp
```

**Step 3: Use Diagnostic Mode**
```bash
# Enable introspection
/sc:troubleshoot --introspect "specific problem description"

# Use verbose mode
/sc:analyze --verbose --introspect problem-area/

# Get reasoning transparency
/sc:debug --think --introspect complex-issue/
```

### Framework Debugging

**SuperClaude Behavior Issues:**
```bash
# Check mode activation
/sc:command --introspect  # See which modes activated and why

# Force specific modes
/sc:brainstorm --brainstorm idea  # Force brainstorming even for clear ideas
/sc:analyze --no-modes simple-file.js  # Disable all modes

# Check agent selection logic
/sc:analyze --verbose domain-specific-code/
```

**Integration Debugging:**
```bash
# Test MCP server combinations
/sc:test --c7 --seq --magic complex-feature/    # Multiple servers
/sc:test --no-mcp simple-feature/               # No servers

# Check flag precedence
/sc:improve --safe-mode --optimize code/  # Safe mode should win
```

### Performance Profiling

**Identify Bottlenecks:**
```bash
# Time operations
time /sc:analyze large-project/

# Use resource monitoring
/sc:analyze --uc --orchestrate --delegate auto huge-codebase/

# Profile tool usage
/sc:analyze --verbose --introspect slow-operation/
```

**Optimize Performance:**
```bash
# Best performance combination
/sc:analyze --uc --no-mcp --scope file --depth quick

# Best quality combination  
/sc:analyze --all-mcp --think-hard --delegate auto

# Balanced approach
/sc:analyze --c7 --seq --uc --focus specific-area
```

---

## Getting Help 🆘

### When to Escalate

**Try advanced troubleshooting first:**
1. Check this guide for your specific issue
2. Use `--introspect` mode to understand what's happening
3. Try with `--safe-mode` and `--validate` flags
4. Use minimal scope (`--scope file`) to isolate issues
5. Check GitHub issues for similar problems

**Report bugs when:**
- Commands consistently fail with error messages
- SuperClaude skips or disables tests (never acceptable)
- Security analysis misses obvious vulnerabilities
- Generated code breaks existing functionality despite `--safe-mode`
- MCP servers installed but not activating
- Framework installation fails with clear error messages

### Bug Reporting Template

When reporting issues, include:

```
**Issue Description:**
[What you expected vs what happened]

**Environment:**
- Operating System: [Windows/macOS/Linux + version]
- Python Version: [python3 --version]  
- SuperClaude Version: [pip show SuperClaude]
- Claude Code Version: [claude --version]

**Command Used:**
[Exact command that caused the issue]

**Error Message:**
[Complete error message, if any]

**Steps to Reproduce:**
1. [First step]
2. [Second step]
3. [Result]

**Expected Behavior:**
[What should have happened]

**Additional Context:**
[Any other relevant information]
```

### Community Resources

- **GitHub Issues**: https://github.com/SuperClaude-Org/SuperClaude_Framework/issues
- **Installation Guide**: /home/anton/SuperClaude_Framework/Guides/installation-guide.md  
- **Commands Guide**: /home/anton/SuperClaude_Framework/Guides/commands-guide.md
- **Agents Guide**: /home/anton/SuperClaude_Framework/Guides/agents-guide.md

### Self-Help Resources

**Quick Reference Checks:**
```bash
# See all available commands  
/sc:index

# Get help for specific command
/sc:analyze --help

# System diagnostics
SuperClaude install --diagnose

# Check what's installed
SuperClaude install --list-components

# See project status
/sc:load . --summary
```

---

## Prevention Tips 💡

### Avoiding Common Problems

**Before Starting Work:**
1. Always run `/sc:load .` to understand the project
2. Check `git status` and create a feature branch
3. Use `--safe-mode` for production code
4. Start with smaller scope and expand as needed

**During Development:**  
1. Use `--preview` flags when available
2. Validate changes before applying: `--validate`
3. Save checkpoints: `/sc:save --checkpoint "before major change"`
4. Test incrementally rather than making large changes

**For Complex Operations:**
1. Use `--think` flags for systematic analysis
2. Force appropriate experts with `--agent` when needed
3. Break large tasks into smaller scopes
4. Use `--iterative` for step-by-step improvements

**Resource Management:**
1. Monitor context usage - auto `--uc` should kick in at 75%
2. Use `--concurrency` to control parallel operations
3. Clean up temporary files and workspace regularly
4. Use `--safe-mode` when resource usage is high

### Best Practices

**Command Usage:**
- Be specific rather than vague: "analyze auth security" vs "look at this"
- Use appropriate scope: file → module → project → system
- Combine flags thoughtfully: `--safe-mode --validate` for production
- Let auto-activation work - manual override only when needed

**Project Integration:**
- Load project context before major operations: `/sc:load .`
- Follow existing patterns rather than imposing new ones
- Use framework-specific tools: `--c7` for documented frameworks
- Respect existing test and build configurations

**Quality Assurance:**
- Never skip or disable tests to make things work
- Use validation flags: `--validate --preview --safe-mode`
- Test changes incrementally rather than all at once
- Maintain clean git history with descriptive commits

---

## Quick Reference Cards 📋

### Emergency Fixes
```bash
# Command not working
/sc:command --help
/sc:command --preview --safe-mode

# Installation broken
SuperClaude install --diagnose
SuperClaude install --force

# Performance issues  
/sc:command --uc --no-mcp --scope file

# Quality issues
/sc:command --safe-mode --validate --preview

# MCP servers not working
SuperClaude install --components mcp --force
```

### Common Flag Combinations
```bash
# Safe production work
--safe-mode --validate --preview

# Fast analysis
--uc --no-mcp --depth quick

# Deep investigation  
--think-hard --seq --c7 --introspect

# UI development
--magic --c7 --agent frontend-architect

# Security work
--agent security-engineer --focus security --validate
```

### Scope Control
```bash
--scope file          # Single file
--scope module        # Related files  
--scope project       # Entire project
--scope system        # Cross-project

--focus performance   # Performance-specific
--focus security      # Security-specific  
--focus quality       # Quality-specific
--focus architecture  # Architecture-specific
```

---

## Related Guides

**🚀 When Troubleshooting Fails (Essential)**
- [Installation Guide](installation-guide.md) - Reinstall or fix setup issues
- [Examples Cookbook](examples-cookbook.md) - Working examples to verify functionality
- [SuperClaude User Guide](superclaude-user-guide.md) - Framework overview and expectations

**📚 Understanding What Should Work (Recommended)**
- [Commands Guide](commands-guide.md) - How commands should behave normally
- [Agents Guide](agents-guide.md) - When specialists should activate
- [Behavioral Modes Guide](behavioral-modes-guide.md) - How automatic adaptation should work
- [Session Management Guide](session-management.md) - Session lifecycle issues

**⚙️ Advanced Problem Solving (When Basics Don't Work)**
- [Flags Guide](flags-guide.md) - Flag conflicts and optimization issues
- [Best Practices Guide](best-practices.md) - Prevention patterns and optimal workflows
- [Technical Architecture Guide](technical-architecture.md) - Internal system understanding

**📖 Recommended Troubleshooting Path:**
1. Try solutions in [Quick Problem Diagnosis](#quick-problem-diagnosis-) first
2. Check [Examples Cookbook](examples-cookbook.md) to verify expected behavior
3. Review [Commands Guide](commands-guide.md) for correct usage patterns
4. Use [Best Practices Guide](best-practices.md) for prevention strategies

---

*Remember: SuperClaude is designed to be helpful and safe. When in doubt, use `--safe-mode --validate --preview` to see what would happen before applying changes. Most issues can be resolved by being more specific about what you want and using appropriate safety flags.*

**Happy troubleshooting! 🚀**