# SuperGemini V4 Beta Flags User Guide 🏁

## 🤖 Most Flags Activate Automatically - Don't Stress About It!

**The honest truth**: You don't need to memorize these flags. SuperGemini usually tries to add helpful ones based on what you're doing! 

**Here's what actually happens:**
- You type `/analyze auth.js` 
- SuperGemini detects it's security-related code
- **Usually activates** security-auditor agent, `--focus security`, `--validate`
- You often get expert security analysis without managing any flags

**When might you manually use flags?**
- You want to **override** what SuperGemini picked (rare)
- You're **curious** about specific aspects (`--focus performance`)
- You want to **experiment** with different approaches

**Bottom line**: Just use basic commands and let the auto-activation work. These flags are here when you want them, not because you need them. 🎯

---

## 🚀 Just Try These (No Flag Knowledge Required)

```bash
# These work great with zero flag knowledge:
/sg:analyze src/                    # Auto-activates appropriate expert agents
/sg:build                          # Auto-optimizes based on your project  
/sg:improve messy-code.js          # Auto-activates quality agents and safety flags
/sg:troubleshoot "weird error"     # Auto-activates root-cause-analyzer and debugging flags
/sg:brainstorm "my app idea"       # Auto-activates brainstorm-PRD agent for requirements
```

**See? No flags needed.** Everything below is for when you get curious about what's happening behind the scenes.

---

A practical guide to SuperGemini's flag system. Flags are like command-line options that change how SuperGemini behaves - think of them as superpowers for your commands.

## What Are Flags? 🤔

**Flags are modifiers** that change how SuperGemini processes your requests. They come after commands and start with `--`.

**Basic syntax** (but you usually don't need to know this):
```bash
/sg:command --flag-name
/sg:command --flag-name value  
/sg:analyze src/ --focus security --depth deep
```

**How flags actually work in practice**:
1. **Auto-activation** - SuperGemini adds them based on context (this is the main way! 🎯)
2. **Manual override** - You can add them explicitly if you want different behavior

**Why flags exist** (mostly automatic benefits):
- Get better, more focused results
- Auto-enable the right thinking depth
- Connect to special capabilities when useful
- Optimize for speed or detail based on your task
- Direct attention to what you're actually working on

**The key point**: SuperGemini handles flag selection intelligently so you don't have to think about it! 🧠

## Flag Categories 📂

### Planning & Analysis Flags 🧠

These control how deeply SuperGemini thinks about your request.

#### `--plan`
**What it does**: Shows execution plan before doing anything  
**When to use**: When you want to see what SuperGemini will do first  
**Example**: `/build --plan` - See build steps before running

#### `--seq`
**What it does**: Multi-file analysis (~4K tokens)  
**When to use**: Complex problems involving several files  
**Auto-activates**: Import chains >5 files, cross-module calls >10 references  
**Example**: `/analyze complex-system/ --seq`

#### `--systematic` 
**What it does**: Deep architectural analysis (~10K tokens)  
**When to use**: System-wide problems, architectural decisions  
**Auto-activates**: System refactoring, bottlenecks >3 modules  
**Example**: `/improve legacy-system/ --systematic`

#### `--ultrathink`
**What it does**: Maximum depth analysis (~32K tokens)  
**When to use**: Critical system redesign, complex debugging  
**Auto-activates**: Legacy modernization, critical vulnerabilities  
**Example**: `/troubleshoot "entire auth system broken" --ultrathink`

**💡 Tip**: Start with `--seq`, only go deeper if needed. More thinking = slower but more thorough.

---

### Efficiency & Control Flags ⚡

Control output style, safety, and performance.

#### `--uc` / `--ultracompressed`
**What it does**: 60-80% token reduction using symbols  
**When to use**: Large operations, when context is getting full  
**Auto-activates**: Context usage >75%, large-scale operations  
**Example**: `/analyze huge-codebase/ --uc`

#### `--safe-mode`
**What it does**: Maximum validation, conservative execution  
**When to use**: Production environments, risky operations  
**Auto-activates**: Resource usage >85%, production environment  
**Example**: `/improve production-code/ --safe-mode`

#### `--validate`
**What it does**: Pre-operation validation and risk assessment  
**When to use**: Want to check before making changes  
**Auto-activates**: Risk score >0.7  
**Example**: `/cleanup legacy/ --validate`

#### `--verbose`
**What it does**: Maximum detail and explanation  
**When to use**: Learning, debugging, need full context  
**Example**: `/build --verbose` - See every build step

#### `--answer-only`
**What it does**: Direct response without task creation  
**When to use**: Quick questions, don't want workflow automation  
**Example**: `/explain React hooks --answer-only`

**💡 Tip**: `--uc` is great for big operations. `--safe-mode` for anything important. `--verbose` when you're learning.

---

### MCP Server Flags 🔧

Enable specialized capabilities through MCP servers.

#### `--c7` / `--context7`
**What it does**: Enables Context7 for official library documentation  
**When to use**: Working with frameworks, need official docs  
**Auto-activates**: External library imports, framework questions  
**Example**: `/build react-app/ --c7` - Get React best practices

#### `--seq` / `--sequential`
**What it does**: Enables Sequential for complex multi-step analysis  
**When to use**: Complex debugging, system design  
**Auto-activates**: Complex debugging, `--seq` flags  
**Example**: `/troubleshoot "auth flow broken" --seq`

#### `--magic`
**What it does**: Enables Magic for UI component generation  
**When to use**: Creating UI components, design systems  
**Auto-activates**: UI component requests, frontend persona  
**Example**: `/build dashboard --magic` - Get modern UI components

#### `--play` / `--playwright`
**What it does**: Enables Playwright for browser automation and testing  
**When to use**: E2E testing, performance monitoring  
**Auto-activates**: Test workflows, QA specialist agent  
**Example**: `/test e2e --play`

#### `--morph` / `--fast-apply`
**What it does**: Enables Morphllm for intelligent file editing with Fast Apply  
**When to use**: Multi-file edits, pattern-based transformations  
**Auto-activates**: Complex refactoring, bulk file updates  
**Example**: `/refactor --morph pattern-updates/`

#### `--serena` / `--semantic`
**What it does**: Enables Serena for semantic analysis and memory operations  
**When to use**: Symbol analysis, project-wide context, session management  
**Auto-activates**: Complex symbol operations, memory commands  
**Example**: `/analyze --serena --semantic large-codebase/`

#### `--all-mcp`
**What it does**: Enables all MCP servers simultaneously  
**When to use**: Complex multi-domain problems  
**Auto-activates**: Problem complexity >0.8, multi-domain indicators  
**Example**: `/analyze entire-app/ --all-mcp`

#### `--no-mcp`
**What it does**: Disables all MCP servers, native tools only  
**When to use**: Faster execution, don't need specialized features  
**Example**: `/analyze simple-script.js --no-mcp`

**💡 Tip**: MCP servers add capabilities but use more tokens. `--c7` for docs, `--seq` for thinking, `--magic` for UI, `--serena` for memory & semantic analysis.

---

### Advanced Orchestration Flags 🎭

For complex operations and workflows.

#### `--wave-mode [auto|force|off]`
**What it does**: Multi-stage execution with compound intelligence  
**When to use**: Complex improvements, systematic analysis  
**Auto-activates**: Complexity >0.8 AND files >20 AND operation types >2  
**Example**: `/improve legacy-system/ --wave-mode force`

#### `--loop`
**What it does**: Iterative improvement mode  
**When to use**: Quality improvement, refinement operations  
**Auto-activates**: Polish, refine, enhance keywords  
**Example**: `/improve messy-code.js --loop`

#### `--iterations [n]`
**What it does**: Control number of improvement cycles (1-10)  
**When to use**: Controlling iterative enhancement depth  
**Example**: `/improve --loop --iterations 5`

#### `--interactive`
**What it does**: Enables user confirmation between iterations  
**When to use**: Want control over iterative process  
**Example**: `/improve --loop --interactive`

**💡 Tip**: These are powerful but useful. Start with `--loop` for improvements.

---

### Session & Workflow Flags 🔄

These V4 Beta flags control session management and advanced workflows.

#### `--brainstorm`
**What it does**: Activates brainstorming mode for requirements discovery  
**When to use**: Ambiguous project ideas, need specification development  
**Auto-activates**: Exploration keywords, "not sure", project planning  
**Example**: `/brainstorm "task management app" --brainstorm`

#### `--max-rounds [n]`
**What it does**: Controls brainstorming dialogue rounds (default: 15)  
**When to use**: Controlling brainstorming session depth  
**Example**: `/brainstorm idea --max-rounds 10`

#### `--prd`
**What it does**: Generates Product Requirements Document from brainstorming  
**When to use**: Convert discussions to formal specifications  
**Auto-activates**: End of successful brainstorming sessions  
**Example**: `/brainstorm app-idea --prd`

**💡 Tip**: V4 Beta introduces powerful session management - let brainstorming mode guide requirement discovery naturally.

---

### Focus & Scope Flags 🎯

Direct SuperGemini's attention to specific areas.

#### `--scope [level]`
**Options**: file, module, project, system  
**What it does**: Sets analysis scope  
**Example**: `/analyze --scope module auth/`

#### `--focus [domain]`
**Options**: performance, security, quality, architecture, accessibility, testing  
**What it does**: Focuses analysis on specific domain  
**Example**: `/analyze --focus security --scope project`

#### Agent Flags
**Available agents**: system-architect, frontend-specialist, backend-engineer, root-cause-analyzer, security-auditor, code-educator, code-refactorer, performance-optimizer, qa-specialist, devops-engineer, technical-writer, python-ultimate-expert, brainstorm-PRD  
**What they do**: Activates specialized domain expert agents (V4 Beta enhancement)  
**Example**: `/analyze --agent security-auditor` - Security-focused analysis with expert agent

**💡 Tip**: `--focus` is great for targeted analysis. Expert agents auto-activate but manual control helps.

---

## Common Flag Patterns 🔄

### Quick Analysis
```bash
/sg:analyze src/ --focus quality          # Quick quality check
/sg:analyze --uc --focus security         # Fast security scan
```

### Deep Investigation  
```bash
/sg:troubleshoot "bug" --seq --seq      # Systematic debugging
/sg:analyze --systematic --focus architecture  # Architectural analysis
```

### Large Project Work
```bash
/sg:analyze monorepo/ --uc     # Efficient large analysis
/sg:improve legacy/ --wave-mode auto --safe-mode  # Safe systematic improvement
```

### Learning & Documentation
```bash
/sg:explain React hooks --c7 --verbose    # Detailed explanation with docs
/sg:document api/ --persona-scribe        # Professional documentation
```

### Performance-Focused
```bash
/sg:analyze --focus performance --play     # Performance analysis with testing
/sg:build --uc --no-mcp                   # Fast build without extra features
```

### Security-Focused
```bash
/sg:analyze --focus security --seq --validate  # Thorough security analysis
/sg:scan --persona-security --safe-mode         # Conservative security scan
```

## Practical Examples 💡

### Before/After: Basic Analysis
**Before** (basic):
```bash
/sg:analyze auth.js
# → Simple file analysis
```

**After** (with flags):
```bash
/sg:analyze auth.js --focus security --seq --c7
# → Security-focused analysis with deep thinking and official docs
# → Much more thorough, finds security patterns, checks against best practices
```

### Before/After: Large Project
**Before** (slow):
```bash
/sg:analyze huge-monorepo/
# → Tries to analyze everything at once, may timeout or use too many tokens
```

**After** (efficient):
```bash
/sg:analyze huge-monorepo/ --uc --focus architecture
# → Compresses output, focuses on architecture
# → Faster, more focused, better results
```

### Before/After: Improvement Work
**Before** (risky):
```bash
/sg:improve legacy-system/
# → May make too many changes, could break things
```

**After** (safe):
```bash
/sg:improve legacy-system/ --safe-mode --loop --validate --preview
# → Safe changes only, iterative approach, validates first, shows preview
# → Much safer, progressive improvement
```

## Auto-Activation Examples 🤖

SuperGemini usually adds flags based on context. Here's when it tries:

### Complexity-Based
```bash
/sg:analyze huge-codebase/
# Auto-adds: --uc
# Why: >50 files detected, context management needed

/sg:troubleshoot "complex system issue"  
# Auto-adds: --seq --seq
# Why: Multi-component problem detected
```

### Domain-Based
```bash
/sg:build react-app/
# Auto-activates: frontend-specialist agent + --c7
# Why: Frontend framework detected

/sg:analyze --focus security
# Auto-activates: security-auditor agent + --validate
# Why: Security focus triggers security specialist
```

### Performance-Based
```bash
# When context usage >75%
/sg:analyze large-project/
# Auto-adds: --uc
# Why: Token optimization needed

# When risk score >0.7
/sg:improve production-code/
# Auto-adds: --safe-mode --validate
# Why: High-risk operation detected
```

## Advanced Usage 🚀

### Complex Flag Combinations

**Comprehensive Code Review**:
```bash
/sg:review codebase/ --agent qa-specialist --systematic --focus quality --validate --c7
# → QA specialist agent + deep thinking + quality focus + validation + docs
```

**Legacy System Modernization**:
```bash
/sg:improve legacy/ --wave-mode force --agent system-architect --safe-mode --loop --c7
# → Wave orchestration + architect agent + safety + iteration + docs
```

**Security Audit**:
```bash
/sg:scan --agent security-auditor --ultrathink --focus security --validate --seq
# → Security auditor agent + maximum thinking + security focus + validation + systematic analysis
```

### Performance Optimization

**For Speed**:
```bash
/sg:analyze --no-mcp --uc --scope file
# → Disable extra features, compress output, limit scope
```

**For Thoroughness**:
```bash
/sg:analyze --all-mcp --systematic
# → All capabilities, systematic analysis
```

### Custom Workflows

**Bug Investigation Workflow**:
```bash
/sg:troubleshoot "specific error" --seq --seq --validate
/sg:analyze affected-files/ --focus quality --agent root-cause-analyzer  
/sg:test --play --coverage
```

**Feature Development Workflow**:
```bash
/sg:design new-feature --agent system-architect --c7
/sg:build --magic --agent frontend-specialist --validate
/sg:test --play --coverage
/sg:document --agent technical-writer --c7
```

## Quick Reference 📋

### Most Useful Flags
| Flag | Purpose | When to Use |
|------|---------|-------------|
| `--seq` | Deeper analysis | Complex problems |
| `--uc` | Compress output | Large operations |
| `--safe-mode` | Conservative execution | Important code |
| `--c7` | Official docs | Framework work |
| `--seq` | Systematic analysis | Debugging |
| `--focus security` | Security focus | Security concerns |

| `--validate` | Check before action | Risky operations |
| `--brainstorm` | Requirements discovery | Ambiguous projects |
| `--serena` | Semantic analysis | Symbol operations |

### Flag Combinations That Work Well
```bash
# Safe improvement
--safe-mode --validate --preview

# Deep analysis  
--seq --seq --c7

# Large project
--uc --focus

# Learning
--verbose --c7 --agent code-educator

# Security work
--agent security-auditor --focus security --validate

# Performance work
--agent performance-optimizer --focus performance --play

# Requirements discovery
--brainstorm --max-rounds 10 --prd
```

### Auto-Activation Triggers
- **--seq**: Complex imports, cross-module calls
- **--uc**: Context >75%, large operations  
- **--safe-mode**: Resource usage >85%, production

- **--c7**: Framework imports, documentation requests
- **--seq**: Debugging keywords, --seq flags
- **--serena**: Symbol operations, memory commands
- **--brainstorm**: Exploration keywords, ambiguous requests
- **Expert Agents**: Domain-specific keywords and patterns

## Troubleshooting Flag Issues 🚨

### Common Problems

**"Flags don't seem to work"**
- Check spelling (common typos: `--ultracompresed`, `--agent fronted-specialist`)
- Some flags need values: `--scope project`, `--focus security`
- Flag conflicts: `--no-mcp` overrides `--c7`, `--seq`, `--serena`, etc.

**"Operation too slow"**
- Try `--uc` for compression
- Use `--no-mcp` to disable extra features
- Limit scope: `--scope file` instead of `--scope project`

**"Too much output"**
- Add `--uc` for compression
- Remove `--verbose` if present
- Use `--answer-only` for simple questions

**"Not thorough enough"**
- Add `--seq` or `--systematic`
- Enable relevant MCP servers: `--seq`, `--c7`
- Use appropriate agent: `--agent root-cause-analyzer`

**"Changes too risky"**
- Always use `--safe-mode` for important code
- Add `--validate` to check first
- Use `--preview` to see changes before applying

### Flag Conflicts

**These override others**:
- `--no-mcp` overrides all MCP flags (`--c7`, `--seq`, `--serena`, etc.)
- `--safe-mode` overrides optimization flags
- Last agent flag wins: `--agent frontend-specialist --agent backend-engineer` → backend-engineer

**Precedence order**:
1. Safety flags (`--safe-mode`) beat optimization
2. Explicit flags beat auto-activation
3. Thinking depth: `--ultrathink` > `--systematic` > `--seq`
4. Scope: system > project > module > file

## Tips for Effective Flag Usage 💡

### Starting Out (The Honest Truth)
1. **Just ignore flags at first** - Auto-activation handles most cases pretty well
2. **Watch what gets auto-activated** - You'll learn by seeing what SuperGemini picks
3. **Use `--help` when curious** - Many commands show what flags are available
4. **Trust the automation** - SuperGemini usually picks reasonable defaults

### Getting Advanced (If You Want To)
1. **Experiment with overrides** - Try `--agent security-auditor` on non-security code for different perspectives
2. **Learn the useful combos** - `--safe-mode --validate` for important stuff, `--brainstorm --prd` for new projects
3. **Understand the performance trade-offs** - Fast (`--uc --no-mcp`) vs thorough (`--systematic --all-mcp`)
4. **Use flags for learning** - `--verbose` when you want to understand what's happening

### Performance Tips (For Power Users)
- **For speed**: `--uc --no-mcp --scope file`
- **For thoroughness**: `--systematic --all-mcp`
- **For safety**: `--safe-mode --validate --preview`
- **For learning**: `--verbose --c7 --agent code-educator`
- **For project discovery**: `--brainstorm --max-rounds 15 --prd`

---

## Final Notes 📝

**The real truth about flags** 💯:
- **Auto-activation usually works pretty well** compared to manual flag selection
- **You can ignore most of this guide** and just use basic commands
- **Flags are here when you want them** - not because you need them
- **Learning happens naturally** through use, not through studying guides 😊

**Don't feel overwhelmed** 🧘‍♂️:
- SuperGemini tries to work well without flag knowledge
- The detailed info above is for curiosity, not necessity
- Auto-activation keeps getting smarter based on usage patterns
- You're not missing out by not memorizing flags

**When you actually need flags**:
- Overriding auto-activation (rare)
- Experimenting with different approaches (fun)
- Optimizing for specific performance needs (advanced)
- Learning about what happened (educational)

**Start simple, stay simple** 🎯:
- Use basic commands: `/analyze`, `/build`, `/improve`
- Let auto-activation handle the complexity
- Add manual flags only when you want to experiment
- Trust that SuperGemini knows what it's doing

---

*Remember: Behind all this apparent complexity, SuperGemini is actually simple to use. Just start typing commands! 🚀*