# SuperGemini Flags User Guide 🏁

## 🤖 Most Flags Activate Automatically - Don't Stress About It!

**The honest truth**: You don't need to memorize these flags. SuperGemini usually tries to add helpful ones based on what you're doing! 

**Here's what actually happens:**
- You type `/analyze auth.js` 
- SuperGemini detects it's security-related code
- **Usually adds** `--persona-security`, `--focus security`, `--validate`
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
/sg:analyze src/                    # Auto-picks the right analysis flags
/sg:build                          # Auto-optimizes based on your project  
/sg:improve messy-code.js          # Auto-activates quality and safety flags
/sg:troubleshoot "weird error"     # Auto-activates debugging and analysis flags
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
- Auto-enable the right analysis depth
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
**Auto-activates**: Complex debugging, multi-step analysis  
**Example**: `/troubleshoot "auth flow broken" --seq`

#### `--magic`
**What it does**: Enables Magic for UI component generation  
**When to use**: Creating UI components, design systems  
**Auto-activates**: UI component requests, frontend persona  
**Example**: `/build dashboard --magic` - Get modern UI components

#### `--play` / `--playwright`
**What it does**: Enables Playwright for browser automation and testing  
**When to use**: E2E testing, performance monitoring  
**Auto-activates**: Test workflows, QA persona  
**Example**: `/test e2e --play`

#### `--all-mcp`
**What it does**: Enables all MCP servers simultaneously  
**When to use**: Complex multi-domain problems  
**Auto-activates**: Problem complexity >0.8, multi-domain indicators  
**Example**: `/analyze entire-app/ --all-mcp`

#### `--no-mcp`
**What it does**: Disables all MCP servers, native tools only  
**When to use**: Faster execution, don't need specialized features  
**Example**: `/analyze simple-script.js --no-mcp`

**💡 Tip**: MCP servers add capabilities but use more tokens. `--c7` for docs, `--seq` for thinking, `--magic` for UI.

---

### Advanced Orchestration Flags 🎭

For complex operations and workflows.

#### `--delegate [files|folders|auto]`
**What it does**: Enables sub-agent delegation for parallel processing  
**When to use**: Large codebases, complex analysis  
**Auto-activates**: >7 directories or >50 files  
**Options**:
- `files` - Delegate individual file analysis
- `folders` - Delegate directory-level analysis  
- `auto` - Smart delegation strategy

**Example**: `/analyze monorepo/ --delegate auto`

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

#### `--concurrency [n]`
**What it does**: Control max concurrent sub-agents (1-15)  
**When to use**: Controlling resource usage  
**Example**: `/analyze --delegate auto --concurrency 3`

**💡 Tip**: These are powerful but complex. Start with `--delegate auto` for big projects, `--loop` for improvements.

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

#### Persona Flags
**Available personas**: architect, frontend, backend, analyzer, security, mentor, refactorer, performance, qa, devops, scribe  
**What they do**: Activates specialist behavior patterns  
**Example**: `/analyze --persona-security` - Security-focused analysis

**💡 Tip**: `--focus` is great for targeted analysis. Personas auto-activate but manual control helps.

---

## Common Flag Patterns 🔄

### Quick Analysis
```bash
/sg:analyze src/ --focus quality          # Quick quality check
/sg:analyze --uc --focus security         # Fast security scan
```

### Deep Investigation  
```bash
/sg:troubleshoot "bug" --seq             # Systematic debugging
/sg:analyze --seq --focus architecture    # Architectural analysis
```

### Large Project Work
```bash
/sg:analyze monorepo/ --delegate auto --uc     # Efficient large analysis
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
/sg:analyze --focus security --seq --validate   # Thorough security analysis
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
# → Security-focused analysis with systematic reasoning and official docs
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
/sg:analyze huge-monorepo/ --delegate auto --uc --focus architecture
# → Delegates work to sub-agents, compresses output, focuses on architecture
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
# Auto-adds: --delegate auto --uc
# Why: >50 files detected, context management needed

/sg:troubleshoot "complex system issue"  
# Auto-adds: --seq
# Why: Multi-component problem detected
```

### Domain-Based
```bash
/sg:build react-app/
# Auto-adds: --c7 --persona-frontend
# Why: Frontend framework detected

/sg:analyze --focus security
# Auto-adds: --persona-security --validate
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
/sg:review codebase/ --persona-qa --seq --focus quality --validate --c7
# → QA specialist + systematic analysis + quality focus + validation + docs
```

**Legacy System Modernization**:
```bash
/sg:improve legacy/ --wave-mode force --persona-architect --safe-mode --loop --c7
# → Wave orchestration + architect perspective + safety + iteration + docs
```

**Security Audit**:
```bash
/sg:scan --persona-security --seq --focus security --validate
# → Security specialist + systematic analysis + security focus + validation
```

### Performance Optimization

**For Speed**:
```bash
/sg:analyze --no-mcp --uc --scope file
# → Disable extra features, compress output, limit scope
```

**For Thoroughness**:
```bash
/sg:analyze --all-mcp --seq --delegate auto
# → All capabilities, systematic analysis, parallel processing
```

### Custom Workflows

**Bug Investigation Workflow**:
```bash
/sg:troubleshoot "specific error" --seq --validate
/sg:analyze affected-files/ --focus quality --persona-analyzer  
/sg:test --play --coverage
```

**Feature Development Workflow**:
```bash
/sg:design new-feature --persona-architect --c7
/sg:build --magic --persona-frontend --validate
/sg:test --play --coverage
/sg:document --persona-scribe --c7
```

## Quick Reference 📋

### Most Useful Flags
| Flag | Purpose | When to Use |
|------|---------|-------------|
| `--seq` | Systematic analysis | Complex problems |
| `--uc` | Compress output | Large operations |
| `--safe-mode` | Conservative execution | Important code |
| `--c7` | Official docs | Framework work |
| `--focus security` | Security focus | Security concerns |
| `--delegate auto` | Parallel processing | Large codebases |
| `--validate` | Check before action | Risky operations |

### Flag Combinations That Work Well
```bash
# Safe improvement
--safe-mode --validate --preview

# Deep analysis  
--seq --c7

# Large project
--delegate auto --uc --focus

# Learning
--verbose --c7 --persona-mentor

# Security work
--persona-security --focus security --validate

# Performance work
--persona-performance --focus performance --play
```

### Auto-Activation Triggers
- **--seq**: Complex debugging, multi-step analysis
- **--uc**: Context >75%, large operations  
- **--safe-mode**: Resource usage >85%, production
- **--delegate**: >7 directories or >50 files
- **--c7**: Framework imports, documentation requests
- **--seq**: Debugging keywords, multi-step analysis
- **Personas**: Domain-specific keywords and patterns

## Troubleshooting Flag Issues 🚨

### Common Problems

**"Flags don't seem to work"**
- Check spelling (common typos: `--ultracompresed`, `--persona-fronted`)
- Some flags need values: `--scope project`, `--focus security`
- Flag conflicts: `--no-mcp` overrides `--c7`, `--seq`, etc.

**"Operation too slow"**
- Try `--uc` for compression
- Use `--no-mcp` to disable extra features
- Limit scope: `--scope file` instead of `--scope project`

**"Too much output"**
- Add `--uc` for compression
- Remove `--verbose` if present
- Use `--answer-only` for simple questions

**"Not thorough enough"**
- Add `--seq` for systematic analysis
- Enable relevant MCP servers: `--seq`, `--c7`
- Use appropriate persona: `--persona-analyzer`

**"Changes too risky"**
- Always use `--safe-mode` for important code
- Add `--validate` to check first
- Use `--preview` to see changes before applying

### Flag Conflicts

**These override others**:
- `--no-mcp` overrides all MCP flags (`--c7`, `--seq`, etc.)
- `--safe-mode` overrides optimization flags
- Last persona flag wins: `--persona-frontend --persona-backend` → backend

**Precedence order**:
1. Safety flags (`--safe-mode`) beat optimization
2. Explicit flags beat auto-activation
4. Scope: system > project > module > file

## Tips for Effective Flag Usage 💡

### Starting Out (The Honest Truth)
1. **Just ignore flags at first** - Auto-activation handles most cases pretty well
2. **Watch what gets auto-activated** - You'll learn by seeing what SuperGemini picks
3. **Use `--help` when curious** - Many commands show what flags are available
4. **Trust the automation** - SuperGemini usually picks reasonable defaults

### Getting Advanced (If You Want To)
1. **Experiment with overrides** - Try `--persona-security` on non-security code for different perspectives
2. **Learn the useful combos** - `--safe-mode --validate` for important stuff
3. **Understand the performance trade-offs** - Fast (`--uc --no-mcp`) vs thorough (`--think-hard --all-mcp`)
4. **Use flags for learning** - `--verbose` when you want to understand what's happening

### Performance Tips (For Power Users)
- **For speed**: `--uc --no-mcp --scope file`
- **For thoroughness**: `--seq --all-mcp --delegate auto`
- **For safety**: `--safe-mode --validate --preview`
- **For learning**: `--verbose --c7 --persona-mentor`

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