# SuperGemini Troubleshooting Guide

> **Need a Quick Fix?** For the top 10 most common issues with rapid 2-minute solutions, see the [Common Issues Quick Reference](common-issues.md) first.

> **Command Context**: This guide covers both **Terminal Commands** (for installation issues) and **Gemini CLI Commands** (`/sc:` for development issues). Look for section headers to know which type to use.

**Comprehensive Problem Resolution**: Step-by-step solutions for complex SuperGemini issues, from installation problems to advanced configuration challenges. Each solution includes diagnosis steps, resolution procedures, and prevention strategies.

**When to Use This Guide**: Use this comprehensive guide when the [quick fixes](common-issues.md) don't resolve your issue, or when you need detailed diagnosis and prevention strategies.

## Installation Issues

> **🚀 Quick Fix**: For common installation problems like permission denied, Python version issues, or component failures, try the [Common Issues Quick Reference](common-issues.md#top-10-quick-fixes) first.

### Advanced Installation Diagnosis

**Issue: Complex Dependency Conflicts**
```bash
# Error message variations
ERROR: Package has conflicting dependencies
ERROR: Cannot resolve version requirements
ERROR: Installation failed due to environment conflicts

# Advanced Diagnosis
pip list --outdated
pip check
python3 -m pip debug --verbose

# Solution 1: Virtual environment isolation
python3 -m venv fresh-superclaude-env
source fresh-superclaude-env/bin/activate
pip install --upgrade pip setuptools wheel
pip install SuperGemini

# Solution 2: Dependency conflict resolution
pip install pip-tools
pip-compile requirements.in  # If you have requirements.in
pip-sync requirements.txt

# Solution 3: System package manager conflicts (Linux)
# Use pipx for isolated installation
python3 -m pip install --user pipx
pipx install SuperGemini
pipx ensurepath

# Prevention
# Use virtual environments for all Python development
# Regular dependency audits and updates
```

**Issue: Partial Component Installation**
```bash
# Symptoms: Some components install, others fail silently

# Advanced Diagnosis
python3 -m SuperGemini install --dry-run --verbose
cat ~/.gemini/GEMINI.md | grep -E "@|import"
ls -la ~/.gemini/

# Component dependency validation
python3 -c "
import importlib
components = ['FLAGS', 'RULES', 'PRINCIPLES', 'MODE_Task_Management']
for comp in components:
    try:
        print(f'✅ {comp}: Available')
    except ImportError:
        print(f'❌ {comp}: Missing')
"

# Solution: Incremental installation with validation
for component in core agents modes mcp; do
    echo "Installing $component..."
    python3 -m SuperGemini install --components $component
    # Validate after each component
    if ! cat ~/.gemini/GEMINI.md | grep -q "@"; then
        echo "❌ Component $component failed"
        break
    fi
done

# Prevention
# Install components one at a time for large projects
# Validate installation after each component
```

### Platform-Specific Issues

**Windows Platform Issues:**
```cmd
# Issue: Path separator problems
ERROR: Cannot find file 'C:\Users\name\.gemini\GEMINI.md'

# Solution: Use proper Windows paths
set CLAUDE_CONFIG_DIR=C:\Users\%USERNAME%\.gemini
python -m SuperGemini install --install-dir "%CLAUDE_CONFIG_DIR%"

# Issue: Node.js not found for MCP servers
# Solution: Install Node.js from official source
winget install OpenJS.NodeJS
# or download from https://nodejs.org/

# Issue: PowerShell execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**macOS Platform Issues:**
```bash
# Issue: Homebrew Python conflicts
# Solution: Use pyenv for Python management
brew install pyenv
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
pyenv install 3.9.0
pyenv global 3.9.0

# Issue: Rosetta compatibility on Apple Silicon
# Solution: Install native Python and Node.js
arch -arm64 brew install python@3.9
arch -arm64 brew install node
```

**Linux Distribution Issues:**
```bash
# Ubuntu/Debian
# Issue: Missing system dependencies
sudo apt update
sudo apt install python3-dev python3-pip build-essential

# CentOS/RHEL
# Issue: Python 3.8+ not available
sudo yum install python39 python39-pip
python3.9 -m pip install SuperGemini

# Arch Linux
# Issue: Package conflicts
sudo pacman -S python python-pip
pip install --user SuperGemini
```

## Command Issues

> **🚀 Quick Fix**: For command recognition problems, timeouts, or basic execution issues, try the [Common Issues Quick Reference](common-issues.md#4--commands-not-working-in-gemini-code) first.

### Advanced Command Diagnosis

**Issue: Command Timeout or Hanging**
```bash
# Symptoms: Command runs but never completes

# Diagnosis
# Check system resources
top
df -h
ps aux | grep gemini

# Solution 1: Reduce scope
/sc:analyze src/ --scope file    # Instead of entire project
/sc:implement "simple task"      # Instead of complex features

# Solution 2: Use scope limiting
/sc:analyze ./specific-folder/ --scope module  # Limit analysis scope
/sc:implement "feature" --scope file            # Focus on specific files

# Solution 3: Clear session data and restart
# Remove old session files if they exist
rm -rf ~/.gemini/sessions/old-*
# Restart Gemini CLI session

# Prevention
# Use appropriate scope for large projects
# Monitor system resources before large operations
```

**Issue: Command Returns Unexpected Results**
```bash
# Symptoms: Command executes but produces wrong output

# Diagnosis
# Check current directory and context
pwd
ls -la
/sc:reflect  # Check current session context

# Solution 1: Reset session context
/sc:save "backup-session"  # Backup current state
# Restart Gemini CLI and reload if needed

# Solution 2: Use explicit scope
/sc:analyze ./specific-folder/  # Explicit path
/sc:implement "specific task in authentication module"

# Solution 3: Verification check
# Verify GEMINI.md contains SuperGemini framework instructions
grep "SuperGemini" ~/.gemini/GEMINI.md
# Check for proper command imports

# Prevention
# Use explicit paths and clear task descriptions
# Save session state before complex operations
```

### Command Selection and Routing Issues

**Issue: Wrong Agent or Mode Activated**
```bash
# Symptoms: Wrong specialist activated for the task

# Example problem
/sc:implement "database optimization"
# Activates frontend-architect instead of database specialist

# Diagnosis
# Check keyword patterns and triggers
/sc:explain "why was frontend-architect selected for database work?"

# Solution 1: Use explicit keywords
/sc:implement "PostgreSQL database performance optimization"
# More specific keywords trigger correct specialist

# Solution 2: Use specific backend terminology
/sc:implement "database performance optimization for PostgreSQL queries"

# Solution 3: Use domain-specific terminology
/sc:implement "PostgreSQL performance tuning and query optimization"

# Prevention
# Use domain-specific terminology
# Include technology names in descriptions
```

**Issue: Mode Selection Problems**
```bash
# Symptoms: Wrong behavioral mode for the task complexity

# Diagnosis
# Check complexity score and mode thresholds
/sc:reflect "task complexity analysis"

# Example: Task management mode not activating for complex project
/sc:implement "entire microservices platform"
# Should activate task management mode but doesn't

# Solution 1: Use complex project language
/sc:implement "multi-service platform with authentication, database, and API gateway"

# Solution 2: Break down complexity
/sc:analyze "microservices platform requirements"  # Plan first
/sc:implement "authentication service"  # Then implement pieces

# Solution 3: Use descriptive complexity language
/sc:implement "comprehensive microservices platform with authentication, API gateway, and database"

# Prevention
# Describe task complexity explicitly
# Use workflow planning for large projects
```

## Agent & Mode Issues

> **🚀 Quick Fix**: For basic agent and mode issues, most problems can be resolved by restarting Gemini CLI and checking component installation with `python3 -m SuperGemini install --components agents modes --force`.

### Advanced Agent Diagnosis

**Issue: Expected Agent Not Activating**
```bash
# Example: Security agent not activating for security-related tasks
/sc:implement "user login system"
# Expected: security-engineer activation
# Actual: Only backend-architect activates

# Diagnosis
# Check agent trigger patterns
/sc:explain "agent activation patterns for security tasks"

# Solution 1: Use explicit security keywords
/sc:implement "secure user authentication with JWT and encryption"
# Keywords: "secure", "authentication", "encryption" trigger security-engineer

# Solution 2: Use security terminology
/sc:implement "secure user authentication with encryption and validation"

# Solution 3: Multi-keyword approach
/sc:implement "user login with security best practices and vulnerability protection"

# Verification
# Check which agents activated in response
/sc:reflect "which agents were activated for the last task?"
```

**Issue: Too Many Agents Activating**
```bash
# Symptoms: Overwhelming agent coordination, slow performance

# Example: Simple task activating multiple agents
/sc:implement "add console.log statement"
# Multiple agents activate unnecessarily

# Solution 1: Reduce task scope
/sc:implement "add debug logging to user.js line 45"
# More specific, simpler task

# Solution 2: Use scope limiting
/sc:implement "logging" --scope file

# Solution 3: Use simple task description
/sc:implement "add console.log to function start"

# Prevention
# Use specific, focused task descriptions
# Avoid complex terminology for simple tasks
```

**Issue: Agent Coordination Conflicts**
```bash
# Symptoms: Agents providing conflicting recommendations

# Diagnosis
# Review agent recommendations and conflicts
/sc:reflect "agent coordination issues in last task"

# Solution 1: Use domain-specific language
/sc:implement "secure payment system with encryption and PCI compliance"
# Use security keywords to activate security expertise

# Solution 2: Sequential task breakdown
/sc:analyze "payment system architecture requirements"
/sc:implement "secure payment backend with JWT authentication"
/sc:implement "responsive payment UI with form validation"

# Solution 3: Single-domain focus
/sc:implement "payment backend API with database integration"

# Prevention
# Break complex tasks into domain-specific subtasks
# Use lead agent designation for complex coordination
```

### Behavioral Mode Problems

**Issue: Brainstorming Mode Not Activating**
```bash
# Expected: Interactive discovery for vague requests
/sc:brainstorm "build something for productivity"
# Should activate brainstorming mode but doesn't

# Diagnosis
# Check for explicit brainstorming keywords
echo "Requirements: vague project, needs discovery"

# Solution 1: Use uncertainty indicators
/sc:brainstorm "maybe we could build some kind of productivity tool"
# Keywords: "maybe", "some kind of" trigger exploration

# Solution 2: Use brainstorming language patterns
/sc:brainstorm "let's explore what kind of productivity tool might work best"

# Solution 3: Question-based approach
/sc:brainstorm "not sure what kind of productivity solution we need"

# Verification
# Mode should respond with Socratic questions
```

**Issue: Task Management Mode Overwhelming Simple Tasks**
```bash
# Symptoms: Simple task gets complex project management treatment

# Example
/sc:implement "fix typo in README"
# Activates task management mode unnecessarily

# Solution 1: Use simple language
/sc:implement "correct spelling error in README.md"

# Solution 2: Scope limitation
/sc:implement "typo fix" --scope file

# Solution 3: Single-step indication
/sc:implement "one-line fix in README"

# Prevention
# Use simple, direct language for simple tasks
# Indicate single-step nature explicitly
```

## MCP Server Issues

> **🚀 Quick Fix**: For Node.js missing or MCP connection problems, see [Common Issues Quick Reference](common-issues.md#8--nodejs-missing-for-mcp-servers) for rapid solutions.

### Advanced MCP Diagnosis

**Issue: Context7 Server Not Connecting**
```bash
# Error message
ERROR: MCP server 'context7' failed to connect

# Diagnosis
# Check Node.js installation
node --version  # Should be 16.0.0 or higher
npm list -g @context7/mcp-server

# Check server configuration
cat ~/.gemini/.gemini.json | grep context7

# Solution 1: Install/reinstall Node.js and server
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
npm install -g @context7/mcp-server

# Solution 2: Reconfigure MCP servers
python3 -m SuperGemini install --components mcp --force

# Solution 3: Manual server testing
node -e "console.log('Node.js working')"
npm test @context7/mcp-server

# Verification
/sc:implement "React component" --c7
# Should connect to Context7 for React patterns
```

**Issue: MCP Server Communication Timeout**
```bash
# Error message
ERROR: MCP server request timeout after 30 seconds

# Diagnosis
# Check network connectivity and server health
ping context7-server.example.com
curl -I https://context7-api.example.com/health

# Check system resources
top
free -h

# Solution 1: Reduce operation complexity
/sc:implement "simpler task breakdown"  # Break complex task into smaller parts

# Solution 2: Restart Gemini CLI session
# MCP servers restart with Gemini CLI session restart

# Solution 3: Disable problematic server temporarily
/sc:implement "task" --no-mcp
# or
/sc:implement "task" --seq --magic  # Enable specific servers only

# Prevention
# Monitor system resources before large operations
# Use server-specific flags for targeted operations
```

**Issue: Sequential MCP Server Errors**
```bash
# Error message
ERROR: Sequential reasoning server encountered internal error

# Diagnosis
# Check Sequential server logs
tail -f ~/.gemini/logs/sequential-mcp.log

# Check server installation
npm list -g @sequential/mcp-server

# Solution 1: Restart Gemini CLI session
# This restarts all MCP servers including Sequential

# Solution 2: Use alternative reasoning approach
/sc:analyze complex-problem
# Use native Gemini reasoning without MCP servers

# Solution 3: Reinstall Sequential MCP
npm uninstall -g @sequential/mcp-server
npm install -g @sequential/mcp-server@latest

# Verification
/sc:troubleshoot "test complex debugging scenario" --seq
# Should activate Sequential reasoning successfully
```

### MCP Server Configuration Issues

**Issue: Magic MCP Server Not Generating UI Components**
```bash
# Symptoms: UI component requests not producing expected output

# Diagnosis
# Check Magic server installation
npm list -g @magic/ui-generator
cat ~/.gemini/config.json | grep -i magic

# Solution 1: Verify Magic server installation
npm list -g @magic/ui-generator
npm install -g @magic/ui-generator@latest

# Solution 2: Use explicit Magic activation
/sc:implement "React button component" --magic --ui

# Solution 3: Check component request format
/sc:implement "modern responsive navigation component with accessibility"
# More descriptive request for better Magic activation

# Verification
# Should produce complete UI component with modern patterns
```

**Issue: Playwright MCP Server Browser Automation Failures**
```bash
# Error message
ERROR: Playwright browser automation failed - browser not installed

# Diagnosis
npm list -g playwright
npx playwright --version

# Solution 1: Install Playwright browsers
npx playwright install
npx playwright install-deps

# Solution 2: Specify browser explicitly
/sc:test "login flow" --browser chromium --playwright

# Solution 3: Fallback to headless mode
/sc:test "ui validation" --headless --playwright

# Verification
/sc:test "simple page load test" --play
# Should successfully run browser automation
```

## Session Management Issues

### Session Lifecycle Problems

**Issue: Session Context Lost After Restart**
```bash
# Symptoms: Previous work context not available after Gemini CLI restart

# Diagnosis
# Check session persistence
ls ~/.gemini/sessions/
/sc:load  # Lists available sessions

# Solution 1: Save session before closing
/sc:save "current-work-session"
# Before closing Gemini CLI

# Solution 2: Enable regular session saving
# Use /sc:save periodically during long sessions

# Solution 3: Manual session recovery
/sc:load "last-session"
/sc:reflect "previous work context"

# Prevention
# Always save important session state
# Use descriptive session names for easy identification
```

**Issue: Session Memory Corruption**
```bash
# Error message
ERROR: Session data corrupted - cannot restore context

# Diagnosis
# Check session file integrity
ls -la ~/.gemini/sessions/
file ~/.gemini/sessions/session-*.json

# Solution 1: Restore from backup
/sc:load "backup-session-20241201"  # Use backup session

# Solution 2: Partial context recovery
/sc:reflect "what do I remember about the project?"
# Manually rebuild context

# Solution 3: Fresh session with project analysis
/sc:analyze project-directory/
# Start fresh with new project analysis

# Prevention
# Regular session backups with meaningful names
# Avoid force-closing Gemini CLI during session operations
```

**Issue: Cross-Session Context Inconsistency**
```bash
# Symptoms: Different sessions provide inconsistent project understanding

# Diagnosis
# Compare session contexts
/sc:load "session-1" && /sc:reflect "project understanding"
/sc:load "session-2" && /sc:reflect "project understanding"

# Solution 1: Consolidate session contexts
/sc:load "session-1"
/sc:save "consolidated-session"
/sc:load "session-2"
/sc:save "consolidated-session"

# Solution 2: Rebuild authoritative context
/sc:analyze project/ --scope project
/sc:save "authoritative-project-context"

# Solution 3: Use session hierarchy
/sc:load "main-project-session"  # Primary context
/sc:load "feature-branch-session"

# Prevention
# Maintain single authoritative session per project
# Use session inheritance for feature branches
```

### Memory and Context Issues

**Issue: Context Memory Leaks**
```bash
# Symptoms: Session memory usage grows over time, performance degrades

# Diagnosis
# Check session size and memory usage
du -sh ~/.gemini/sessions/
ls -la ~/.gemini/sessions/

# Solution 1: Clean old sessions manually
# Remove old session files manually
rm ~/.gemini/sessions/old-session-*.json

# Solution 2: Archive current context and start fresh
/sc:save "archived-context-$(date +%Y%m%d)"
# Start a new Gemini CLI session for fresh memory

# Solution 3: Regular session maintenance
# Save important sessions and restart Gemini CLI periodically

# Prevention
# Regular session maintenance and archiving
# Use focused contexts for specific features
```

## Configuration Issues

### Configuration Problems and Validation

**Issue: GEMINI.md Import Conflicts**
```bash
# Error message
ERROR: Circular import detected in GEMINI.md

# Diagnosis
# Check import structure
grep -n "@" ~/.gemini/GEMINI.md
# Look for circular references

# Solution 1: Fix circular imports
# Edit ~/.gemini/GEMINI.md to remove problematic @imports
# Remove any @GEMINI.md references from imported files

# Solution 2: Reset to default configuration
cp ~/.gemini/GEMINI.md ~/.gemini/GEMINI.md.backup
python3 -m SuperGemini install --reset-config

# Solution 3: Manual configuration repair
cp ~/.gemini/GEMINI.md ~/.gemini/GEMINI.md.backup
python3 -m SuperGemini install --components core --force

# Verification
# Check that imports work correctly
grep "@" ~/.gemini/GEMINI.md
# Verify no circular references
```

**Issue: Component Configuration Conflicts**
```bash
# Symptoms: Components interfering with each other

# Diagnosis
# Check component installation status
cat ~/.gemini/GEMINI.md
ls ~/.gemini/

# Solution 1: Reinstall in correct order
python3 -m SuperGemini install --components core agents modes mcp --force

# Solution 2: Fresh installation
rm -rf ~/.gemini/
python3 -m SuperGemini install --fresh

# Solution 3: Verify installation integrity
cat ~/.gemini/GEMINI.md | grep -E "@|SuperGemini"

# Prevention
# Install components in dependency order
# Always backup configuration before major changes
```

**Issue: Custom Configuration Not Loading**
```bash
# Symptoms: Personal customizations in GEMINI.md not taking effect

# Diagnosis
# Check file syntax and structure
cat ~/.gemini/GEMINI.md
# Look for syntax errors

# Solution 1: Check configuration syntax
# Look for syntax errors in GEMINI.md
cat ~/.gemini/GEMINI.md | grep -E "error|Error|invalid"

# Solution 2: Backup and reset
cp ~/.gemini/GEMINI.md ~/.gemini/GEMINI.md.custom
python3 -m SuperGemini install --reset-config
# Manually merge custom content back

# Solution 3: Step-by-step integration
python3 -m SuperGemini install --components core  # Base installation
# Add custom content gradually and test

# Prevention
# Always backup custom configurations before updates
# Test configuration changes before committing
```

### Reset and Recovery Procedures

**Issue: Complete Configuration Corruption**
```bash
# Symptoms: SuperGemini completely non-functional after configuration changes

# Emergency Recovery Procedure
# Step 1: Backup current state
cp -r ~/.gemini ~/.gemini.corrupted.$(date +%Y%m%d)

# Step 2: Complete reset
rm -rf ~/.gemini/
python3 -m SuperGemini install --fresh

# Step 3: Selective recovery
# Restore specific custom files from backup if needed
cp ~/.gemini.corrupted.*/custom-file.md ~/.gemini/

# Step 4: Gradual reconfiguration
python3 -m SuperGemini install --components core agents modes
# Test after each component

# Prevention
# Regular configuration backups
# Test configuration changes in non-production environment
```

## Performance Issues

> **🚀 Quick Fix**: For memory errors or resource issues, see [Common Issues Quick Reference](common-issues.md#9--memoryresource-errors) for immediate solutions.

### Advanced Performance Optimization

**Issue: Slow Command Execution**
```bash
# Symptoms: Commands taking much longer than expected

# Diagnosis
# Check system resources
top
df -h
iostat 1 5

# Check process resource usage
ps aux | grep -i gemini
top | grep -i gemini

# Solution 1: Reduce operation scope
/sc:analyze src/ --scope file          # Instead of entire project
/sc:implement "simple task"            # Focus on simple tasks

# Solution 2: Use efficient command patterns
# Focus on specific files instead of entire project
/sc:analyze specific-file.py --scope file

# Solution 3: Clear session data and restart
# Remove old session files if they exist
rm -rf ~/.gemini/sessions/old-*
# Restart Gemini CLI session

# Prevention
# Monitor system resources before large operations
# Use appropriate scope for project size
```

**Issue: Memory Usage Problems**
```bash
# Symptoms: High memory usage, system slowdown

# Diagnosis
# Check memory usage
free -h
ps aux --sort=-%mem | head -10

# Solution 1: Limit operation scope
/sc:analyze . --scope module  # Instead of entire project

# Solution 2: Clear session cache
rm -rf ~/.gemini/sessions/old-*
# Remove old session files

# Solution 3: Restart Gemini CLI session
# This clears memory and resets context

# Prevention
# Regular cache cleanup
# Use memory-efficient modes for large projects
# Monitor memory usage during long sessions
```

**Issue: MCP Server Performance Bottlenecks**
```bash
# Symptoms: MCP server operations causing delays

# Diagnosis
# Check MCP server installation
npm list -g | grep -E "context7|sequential|magic|playwright"

# Solution 1: Selective MCP server usage
/sc:implement "task" --c7 --seq  # Use only needed servers
# Instead of --all-mcp

# Solution 2: Restart Gemini CLI session
# This restarts all MCP servers

# Solution 3: Local fallback mode
/sc:implement "task" --no-mcp
# Use native capabilities when MCP servers slow

# Prevention
# Use targeted MCP server activation
# Monitor MCP server health regularly
# Keep MCP servers updated
```

### Resource Usage Monitoring

**Issue: Identifying Resource Bottlenecks**
```bash
# Comprehensive resource monitoring

# System-level monitoring
htop
iotop
netstat -i

# Monitor Gemini CLI performance
time /sc:analyze small-file.py  # Time simple operations

# Analysis and optimization
# Based on monitoring results:
# - High CPU: Reduce operation scope with --scope flags
# - High Memory: Clear old sessions and restart Gemini CLI
# - High I/O: Focus on specific files instead of entire projects
# - High Network: Use --no-mcp for local operations
```

## Common Error Messages

### Frequently Encountered Errors

**Error: "Command not recognized"**
```bash
# Full error message
ERROR: Command '/sc:analyze' not recognized by Gemini CLI

# Meaning: SuperGemini instructions not loaded into Gemini CLI session
# Resolution:
1. Verify SuperGemini installation: python3 -m SuperGemini --version
2. Check ~/.gemini/GEMINI.md exists and contains SuperGemini instructions
3. Restart Gemini CLI completely
4. If persistent: python3 -m SuperGemini install --components core --force
```

**Error: "Component dependency not met"**
```bash
# Full error message
ERROR: Component 'mcp' installation failed - dependency 'core' not met

# Meaning: Attempting to install component without required dependencies
# Resolution:
1. Install dependencies first: python3 -m SuperGemini install --components core
2. Then install desired component: python3 -m SuperGemini install --components mcp
3. Or reinstall completely: python3 -m SuperGemini install --fresh
```

**Error: "MCP server connection failed"**
```bash
# Full error message
ERROR: MCP server 'context7' connection failed - server not responding

# Meaning: MCP server unavailable or misconfigured
# Resolution:
1. Check Node.js installation: node --version (should be 16+)
2. Reinstall MCP servers: python3 -m SuperGemini install --components mcp --force
3. Check server installation: npm list -g | grep -E "context7|sequential|magic"
4. Test without MCP: /sc:command --no-mcp
```

**Error: "Session context corrupted"**
```bash
# Full error message
ERROR: Cannot load session - data corruption detected

# Meaning: Session file damaged or incompatible format
# Resolution:
1. Try backup session: /sc:load "backup-session-name"
2. List available sessions: /sc:load (shows all sessions)
3. Start fresh: /sc:analyze project-directory/
4. Rebuild context: /sc:analyze . && /sc:save "new-session"
```

**Error: "Agent activation failed"**
```bash
# Full error message
ERROR: No suitable agent found for task complexity

# Meaning: Task description insufficient for agent selection
# Resolution:
1. Add specific keywords: /sc:implement "React TypeScript component with security validation"
2. Use explicit focus: /sc:implement "React component with TypeScript and accessibility"
3. Break down complex tasks: /sc:analyze "complex task requirements" first, then implement pieces
```

### Error Interpretation Strategies

**Reading Error Context:**
```bash
# Error format understanding
ERROR: [Component] [Operation] failed - [Specific reason] [Error code]

# Example breakdown
ERROR: MCP context7 connection failed - timeout after 30s [E001]
# Component: MCP context7 server
# Operation: connection attempt  
# Reason: timeout after 30 seconds
# Code: E001 (network/connectivity issue)

# Resolution strategy based on error structure
1. Component issues → Check component installation and configuration
2. Operation issues → Verify prerequisites and permissions
3. Specific reasons → Address the exact cause mentioned
4. Error codes → Look up in documentation or report to support
```

## Getting Help

### Bug Reporting Process

**Required Information for Bug Reports:**
```bash
# Essential diagnostic information
python3 -m SuperGemini --version        # Version information
uname -a                                 # System information  
python3 --version                        # Python version
node --version                           # Node.js version (if using MCP)

# SuperGemini-specific diagnostics
ls -la ~/.gemini/
cat ~/.gemini/GEMINI.md | head -20

# Error reproduction
# 1. Exact command that caused the issue
# 2. Expected behavior vs actual behavior
# 3. Screenshots or terminal output
# 4. Steps to reproduce consistently
```

**Bug Report Template:**
```markdown
## Bug Report

**SuperGemini Version:** [Output of `python3 -m SuperGemini --version`]

**Environment:**
- OS: [Linux/macOS/Windows + version]
- Python: [Output of `python --version`]
- Node.js: [Output of `node --version`] (if using MCP servers)
- Gemini CLI Version: [Output of `gemini --version`]

**Description:**
[Clear description of the issue]

**Steps to Reproduce:**
1. [Step one]
2. [Step two]  
3. [Step three]

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happens]

**Error Messages:**
```
[Paste exact error messages here]
```

**Debug Information:**
[Attach output of `ls -la ~/.gemini/` and first 20 lines of GEMINI.md]

**Additional Context:**
[Any other relevant information]
```

### Available Support Channels

**Primary Support Channels:**

1. **GitHub Issues** (Technical Problems)
   - URL: https://github.com/SuperGemini-Org/SuperGemini_Framework/issues
   - Use for: Bug reports, installation issues, feature requests
   - Response time: 24-48 hours for critical issues

2. **GitHub Discussions** (General Help)
   - URL: https://github.com/SuperGemini-Org/SuperGemini_Framework/discussions
   - Use for: Usage questions, best practices, community support
   - Response time: Community-driven, usually <24 hours

3. **Documentation** (Self-Service)
   - Installation Guide: [../Getting-Started/installation.md](../Getting-Started/installation.md)
   - Troubleshooting: This guide
   - Examples: [examples-cookbook.md](examples-cookbook.md)

**Community Support:**
- Community-maintained FAQ and tips
- User-contributed examples and workflows
- Peer support for common issues

**Enterprise Support:**
- Available for organizations requiring dedicated support
- Contact: [GitHub repository maintainers](https://github.com/SuperGemini-Org/SuperGemini_Framework)

## Frequently Asked Questions

### Installation and Setup

**Q: Can I use SuperGemini without Node.js?**
A: Yes, but with limited functionality. Core SuperGemini works with Python only. MCP servers (Context7, Magic, Sequential) require Node.js 16+ for enhanced capabilities.

**Q: Does SuperGemini work on Windows?**
A: Yes, SuperGemini supports Windows 10/11. Use PowerShell or Command Prompt for installation. Some features may require WSL for optimal compatibility.

**Q: How much disk space does SuperGemini require?**
A: Core installation: ~50MB. With all MCP servers: ~200MB. Session storage grows over time but can be managed with cleanup commands.

**Q: Can I install SuperGemini in a virtual environment?**
A: Yes, recommended for isolation. Use `python -m venv superclaude-env && source superclaude-env/bin/activate && pip install SuperGemini`.

### Usage and Features

**Q: How do I know which agent will activate for my task?**
A: Use descriptive keywords related to your domain (e.g., "secure" for security-engineer, "React" for frontend-architect). Check [Agents Guide](../User-Guide/agents.md) for trigger patterns.

**Q: Can I use specific MCP servers only?**
A: Yes, use server-specific flags like `--c7` (Context7), `--seq` (Sequential), `--magic` (Magic UI), or `--no-mcp` for none.

**Q: How do I save and resume work sessions?**
A: Use `/sc:save "session-name"` to save and `/sc:load "session-name"` to resume. See [Session Management](../User-Guide/session-management.md) for details.

**Q: What's the difference between modes and agents?**
A: Modes control behavior style (brainstorming, task management, etc.). Agents provide domain expertise (security, frontend, etc.). They work together automatically.

### Troubleshooting

**Q: Commands are slow or hanging - what should I do?**
A: 1) Check system resources with `top`, 2) Reduce scope with `--scope file`, 3) Focus on specific tasks, 4) Restart Gemini CLI session to clear cache.

**Q: How do I reset SuperGemini to default configuration?**
A: `cp ~/.gemini/GEMINI.md ~/.gemini/GEMINI.md.backup && python3 -m SuperGemini install --reset-config` creates backup and resets to defaults.

**Q: Can I contribute to SuperGemini development?**
A: Yes! See [Contributing Guide](../Developer-Guide/contributing-code.md) for development setup and contribution process.

## System Diagnostics

### Diagnostic Commands and Health Checks

**Comprehensive System Health Check:**
```bash
# Complete SuperGemini diagnostics
python3 -m SuperGemini --version
ls -la ~/.gemini/
cat ~/.gemini/GEMINI.md | head -10

# Verify core functionality
grep "SuperGemini" ~/.gemini/GEMINI.md
# Should show SuperGemini framework instructions

# Check MCP server installations (if using)
node --version
npm list -g | grep -E "context7|sequential|magic|playwright"
```

**Quick Health Verification:**
```bash
# Basic functionality test
python3 -m SuperGemini --version        # Version verification
ls ~/.gemini/                           # Check installation
cat ~/.gemini/GEMINI.md | grep "@"      # Check imports

# Test core functionality in Gemini CLI
# Try: /sc:analyze README.md
```

**Component-Specific Diagnostics:**
```bash
# Test specific components
cat ~/.gemini/GEMINI.md | grep -E "FLAGS|RULES|PRINCIPLES"  # Core components
cat ~/.gemini/GEMINI.md | grep -E "MODE_|MCP_"              # Modes and MCP

# Check MCP server installations
npm list -g | grep -E "context7|sequential|magic|playwright"

# Test session functionality
ls ~/.gemini/sessions/ 2>/dev/null || echo "No sessions directory found"
```

### System Requirement Validation

**Automated Compatibility Check:**
```bash
# System requirements validation
python3 --version  # Should be 3.8+
which gemini       # Should return path to Gemini CLI
df -h ~            # Check disk space (50MB+ available)
touch ~/.gemini/test && rm ~/.gemini/test  # Test write permissions

# Expected validations:
# ✅ Python 3.8+ detected
# ✅ Gemini CLI installation verified  
# ✅ Sufficient disk space (50MB minimum)
# ✅ Write permissions to ~/.gemini directory
# ⚠️  Node.js 16+ recommended for MCP servers
```

**Manual Verification Steps:**
```bash
# Python version check
python3 --version
# Should be 3.8.0 or higher

# Gemini CLI availability
gemini --version
# Should return version number without error

# Directory permissions
ls -la ~/.gemini/
touch ~/.gemini/test-write && rm ~/.gemini/test-write
# Should succeed without permission errors

# Optional: Node.js for MCP servers
node --version
# Should be 16.0.0 or higher for full MCP functionality

# System resources
df -h ~                    # Check available disk space
free -h                    # Check available memory (1GB+ recommended)
```

**Performance Baseline Testing:**
```bash
# Establish performance baselines
time python3 -m SuperGemini --version    # Basic command speed
time /sc:analyze README.md               # Simple analysis speed test  

# Test with different scopes
time /sc:analyze . --scope file          # File-scoped analysis
time /sc:analyze . --scope module        # Module-scoped analysis
```

---

## Related Guides

### Essential Troubleshooting Resources

**Installation and Setup:**
- [Installation Guide](../Getting-Started/installation.md) - Complete installation procedures and platform-specific setup
- [Quick Start Guide](../Getting-Started/quick-start.md) - Basic setup verification and first steps
- [System Requirements](../Getting-Started/installation.md#prerequisites-setup-🛠️) - Hardware and software requirements

**Configuration and Customization:**
- [Configuration Overview](../User-Guide/flags.md) - Configuration flags and customization options
- [Session Management](../User-Guide/session-management.md) - Session lifecycle and persistence troubleshooting
- [MCP Servers](../User-Guide/mcp-servers.md) - MCP server setup and connection troubleshooting

**Usage and Features:**
- [Commands Reference](../User-Guide/commands.md) - Command syntax and usage examples
- [Agents Guide](../User-Guide/agents.md) - Agent activation patterns and coordination troubleshooting
- [Behavioral Modes](../User-Guide/modes.md) - Mode selection and behavioral troubleshooting

**Advanced Topics:**
- [Examples Cookbook](examples-cookbook.md) - Working examples and practical troubleshooting scenarios
- [Best Practices](quick-start-practices.md) - Performance optimization and efficiency troubleshooting
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - Deep system understanding for complex issues

### Developer Resources

**Framework Development:**
- [Contributing Code](../Developer-Guide/contributing-code.md) - Development environment setup and troubleshooting
- [Testing & Debugging](../Developer-Guide/testing-debugging.md) - Advanced debugging techniques and testing procedures

**Community Support:**
- [GitHub Issues](https://github.com/SuperGemini-Org/SuperGemini_Framework/issues) - Bug reports and technical support
- [GitHub Discussions](https://github.com/SuperGemini-Org/SuperGemini_Framework/discussions) - Community help and best practices
- [Contributing Guidelines](../CONTRIBUTING.md) - How to contribute fixes and improvements

### Quick Reference Links

**Immediate Help:**
- Installation Issues → [Installation Guide](../Getting-Started/installation.md)
- Command Problems → [Commands Reference](../User-Guide/commands.md)
- Performance Issues → [Best Practices](quick-start-practices.md)
- Configuration Issues → [MCP Servers](../User-Guide/mcp-servers.md)

**Learning Resources:**
- New Users → [Quick Start Guide](../Getting-Started/quick-start.md)
- Practical Examples → [Examples Cookbook](examples-cookbook.md)
- Advanced Usage → [Technical Architecture](../Developer-Guide/technical-architecture.md)

---

**Emergency Recovery:**
If SuperGemini is completely non-functional:
1. Backup current configuration: `cp -r ~/.gemini ~/.gemini.backup`
2. Complete reset: `rm -rf ~/.gemini && python3 -m SuperGemini install --fresh`
3. Restore custom configurations gradually from backup
4. If issues persist, report to [GitHub Issues](https://github.com/SuperGemini-Org/SuperGemini_Framework/issues) with diagnostic information

**Verification Steps:**
After every solution, verify with these commands:
- ✅ `python3 -m SuperGemini --version` - Should return version number
- ✅ `cat ~/.gemini/GEMINI.md | grep SuperGemini` - Should show framework content
- ✅ Try `/sc:analyze README.md` in Gemini CLI - Should work without errors