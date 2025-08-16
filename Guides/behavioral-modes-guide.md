# SuperClaude Behavioral Modes Guide 🧠

## 💡 The Simple Truth About Modes

**You don't need to understand behavioral modes to use SuperClaude.** They work automatically in the background, adapting how Claude Code behaves based on what you're trying to do.

**Here's what actually happens:**
- Type `/sc:brainstorm "app idea"` → Brainstorming mode kicks in with discovery questions 🤔
- Work on complex debugging → Introspection mode helps with systematic analysis 🔍  
- Handle large refactoring → Task Management mode breaks it into coordinated steps 📋
- Need multiple tools → Orchestration mode picks the best ones automatically 🎯
- Context getting full → Token Efficiency mode compresses without losing meaning ⚡

**Think of it like this**: SuperClaude has different "personalities" that automatically show up when they'd be most helpful. You just work normally, and the right approach appears! ✨

---

**TL;DR**: Behavioral modes are SuperClaude's way of being smarter about how it helps you. They activate automatically. You don't manage them, they manage themselves.

---

## 🚀 Just Try These (See Modes in Action)

```bash
# Brainstorming Mode - Interactive discovery
/sc:brainstorm "task management app"     # → Gets curious, asks discovery questions

# Introspection Mode - Deep thinking
/sc:troubleshoot "weird auth behavior"   # → Analyzes reasoning patterns systematically

# Task Management Mode - Complex coordination  
/sc:implement user-dashboard             # → Breaks into phases, delegates subtasks

# Orchestration Mode - Smart tool selection
/sc:analyze large-codebase/              # → Picks best tools, coordinates efficiently  

# Token Efficiency Mode - Compressed communication
/sc:improve --uc legacy-code/            # → Uses symbols, abbreviations, stays clear
```

**See the pattern?** You just say what you want to do. SuperClaude figures out the best way to help. The modes are the "how" - you focus on the "what". See [Examples Cookbook](examples-cookbook.md) for more working examples. 🎯

---

## The Five Behavioral Modes 🌟

### 🧠 Brainstorming Mode - Interactive Discovery

**What it does**: Turns SuperClaude into a collaborative discovery partner who helps you figure out what you actually want to build.

#### Automatic Activation 🪄
- **Vague requests**: "I want to build something...", "Maybe we could..."
- **Exploration words**: brainstorm, explore, discuss, figure out, not sure
- **Uncertainty**: "possibly", "thinking about", "could we"
- **Manual trigger**: `--brainstorm` or `--bs`

#### How It Changes SuperClaude 🔄
- **Socratic Dialogue**: Asks probing questions instead of jumping to solutions
- **Non-Presumptive**: Doesn't assume what you want, lets you guide discovery
- **Collaborative**: Partners with you rather than directing you
- **Brief Generation**: Turns conversations into structured requirement documents

#### Real Examples 📝

**Standard response:**
```
User: "I want to build a web app"
Claude: "I'll help you build a web application. What framework would you like to use?"
```

**Brainstorming mode:**
```
User: "I want to build a web app"
Claude: "🤔 Let's explore this together! Discovery questions:
         - What problem does this solve for your users?
         - Who are your target users and what are their main workflows?
         - What's your expected user volume and performance needs?
         - Any existing systems it needs to integrate with?
         - What's your timeline and technical constraints?
         
         📝 Once we explore these, I'll generate a structured brief for implementation!"
```

#### Perfect For 💫
- Early project planning and ideation
- Requirements discovery from vague ideas
- Turning "I need something that does..." into concrete specs
- Preventing scope creep through upfront exploration

---

### 🔍 Introspection Mode - Meta-Cognitive Analysis

**What it does**: Makes SuperClaude consciously analyze its own reasoning and decision-making process, especially when things go wrong or get complex.

#### Automatic Activation 🪄
- **Self-analysis requests**: "analyze my reasoning", "reflect on decision"
- **Error recovery**: When outcomes don't match expectations
- **Complex problems**: Multi-layered issues requiring conscious oversight
- **Pattern recognition**: Recurring behaviors or optimization needs
- **Manual trigger**: `--introspect` or `--introspection`

#### How It Changes SuperClaude 🔄
- **Self-Examination**: Consciously analyzes decision logic and reasoning chains
- **Transparency**: Exposes thinking with markers (🤔, 🎯, ⚡, 📊, 💡)
- **Pattern Detection**: Identifies recurring cognitive patterns and behaviors
- **Learning Focus**: Extracts insights for continuous improvement

#### Real Examples 📝

**Standard response:**
```
User: "The solution didn't work as expected"
Claude: "Let me look at the code and find the issue."
```

**Introspection mode:**
```
User: "The solution didn't work as expected"
Claude: "🎯 Decision Analysis: Expected X → got Y
         🔍 Pattern Check: Similar logic errors in auth.js:15, config.js:22
         📊 Framework Compliance: Missed validation step from quality gates
         🤔 Reasoning: Why did I choose async/await over promises here?
         💡 Insight: Need systematic validation before implementation
         
         Let me apply this learning to fix the current issue properly."
```

#### Perfect For 💫
- Debugging complex problems that require meta-thinking
- Understanding why certain approaches were chosen
- Learning from mistakes and improving patterns
- Framework compliance checking and optimization

---

### 📋 Task Management Mode - Orchestration & Delegation

**What it does**: Transforms SuperClaude into a project coordinator that breaks complex work into systematic phases and coordinates multiple sub-tasks efficiently.

#### Automatic Activation 🪄
- **Multi-step operations**: 3+ steps (build, implement, create, fix, refactor)
- **Complex scope**: system-wide, feature-complete, comprehensive changes
- **File thresholds**: >2 directories OR >3 files OR complexity >0.4
- **Quality improvements**: polish, refine, enhance keywords
- **Manual triggers**: `--delegate`, `--loop`, `--concurrency`

#### How It Changes SuperClaude 🔄
- **Orchestration Mindset**: Breaks complex work into coordinated layers
- **Delegation Strategy**: Parallel processing with intelligent sub-task routing
- **State Management**: Single focus protocol with real-time progress tracking
- **Quality Gates**: Evidence-based validation before task completion
- **Progressive Systems**: Systematic enhancement through compound intelligence

#### Real Examples 📝

**Standard response:**
```
User: "I need to refactor this authentication system"
Claude: "I'll refactor the authentication system for you."
```

**Task Management mode:**
```
User: "I need to refactor this authentication system"
Claude: "📋 Detected: system-wide auth refactor → delegation mode activated

         🔄 Phase 1: Security Analysis & Dependencies
         - Analyze current auth.js, middleware.js, session.js
         - Map security vulnerabilities and performance bottlenecks
         - Document current API contracts and integrations
         
         🔄 Phase 2: Core Implementation  
         - Refactor authentication logic with modern patterns
         - Update middleware for improved security
         - Enhance session management with proper cleanup
         
         🔄 Phase 3: Integration & Validation
         - Update all dependent components and routes
         - Run comprehensive security and integration tests
         - Performance benchmarking and optimization
         
         📊 Progress tracking: Each phase validates before proceeding
         ✅ Quality gates: Security, performance, compatibility checks"
```

#### Perfect For 💫
- Large refactoring projects that span multiple files
- Feature implementation requiring coordination
- System-wide changes that need careful orchestration
- Complex builds that benefit from parallel processing

---

### 🎯 Orchestration Mode - Intelligent Tool Selection

**What it does**: Optimizes SuperClaude's tool selection and resource usage, automatically choosing the most powerful and efficient approach for each task.

#### Automatic Activation 🪄
- **Multi-tool operations**: Tasks requiring coordination between different tools
- **Performance constraints**: >75% resource usage detected
- **Parallel opportunities**: >3 files or independent operations possible
- **Complex routing**: Multiple valid approaches available
- **Manual trigger**: `--orchestrate`

#### How It Changes SuperClaude 🔄
- **Smart Tool Selection**: Always chooses the most powerful tool for each task type
- **Resource Awareness**: Adapts approach based on system constraints
- **Parallel Thinking**: Identifies independent operations for concurrent execution
- **Efficiency Focus**: Optimizes for speed and effectiveness over familiarity

#### Tool Selection Matrix 🛠️

| Task Type | Best Tool | Alternative | Why Better |
|-----------|-----------|-------------|------------|
| UI components | Magic MCP | Manual coding | Modern patterns, accessibility |
| Deep analysis | Sequential MCP | Native reasoning | Structured multi-step thinking |
| Symbol operations | Serena MCP | Manual search | Semantic understanding |
| Pattern edits | Morphllm MCP | Individual edits | Bulk operations, consistency |
| Documentation | Context7 MCP | Web search | Official patterns, versioned |
| Browser testing | Playwright MCP | Unit tests | Real user interactions |
| Multi-file edits | MultiEdit | Sequential Edits | Atomic operations, rollback |

#### Resource Management Zones 📊

**🟢 Green Zone (0-75%)**
- Full capabilities available
- Use all tools and features  
- Normal verbosity and detail

**🟡 Yellow Zone (75-85%)**
- Activate efficiency mode
- Reduce verbosity intelligently
- Defer non-critical operations

**🔴 Red Zone (85%+)**
- Essential operations only
- Minimal output, maximum efficiency
- Fail fast on complex requests

#### Real Examples 📝

**Standard response:**
```
User: "/sc:analyze large-project/"
Claude: "I'll analyze your project files."
[Uses basic file reading and native analysis]
```

**Orchestration mode:**
```
User: "/sc:analyze large-project/"
Claude: "🎯 Orchestration: large-project analysis
         📊 Resource Status: 45% → Green Zone
         🛠️ Tool Selection Matrix:
         - File discovery: Glob (batch patterns)
         - Code analysis: Sequential MCP (structured reasoning)  
         - Documentation: Context7 MCP (framework patterns)
         - Parallel execution: 3 concurrent analysis threads
         
         ⚡ Executing optimized analysis workflow..."
```

#### Perfect For 💫
- Large codebases requiring efficient analysis
- Performance-critical operations
- Tasks benefiting from parallel processing
- Resource-constrained environments

---

### ⚡ Token Efficiency Mode - Compressed Communication

**What it does**: Transforms SuperClaude's communication style to use symbols, abbreviations, and compressed formats while preserving 95%+ of information quality.

#### Automatic Activation 🪄
- **Context pressure**: >75% context usage or resource constraints
- **Large operations**: Complex analysis workflows needing optimization
- **User requests**: `--uc`, `--ultracompressed` flags
- **Efficiency needs**: When speed and conciseness are priorities

#### How It Changes SuperClaude 🔄
- **Symbol Communication**: Visual symbols for logic, status, and technical domains
- **Abbreviation Systems**: Context-aware compression for technical terms
- **30-50% Compression**: Significant token reduction while preserving meaning
- **Structured Output**: Bullet points, tables, concise explanations

#### Symbol Reference 🔤

**Core Logic & Flow**
- `→` leads to, implies (`auth.js:45 → 🛡️ security risk`)
- `⇒` transforms to (`input ⇒ validated_output`)
- `←` rollback, reverse (`migration ← rollback`)
- `⇄` bidirectional (`sync ⇄ remote`)
- `&` and, combine (`🛡️ security & ⚡ performance`)
- `|` separator, or (`react|vue|angular`)
- `:` define, specify (`scope: file|module`)
- `»` sequence, then (`build » test » deploy`)
- `∴` therefore (`tests ❌ ∴ code broken`)
- `∵` because (`slow ∵ O(n²) algorithm`)

**Status & Progress**
- `✅` completed, passed
- `❌` failed, error  
- `⚠️` warning, review needed
- `🔄` in progress
- `⏳` waiting, pending
- `🚨` critical, urgent

**Technical Domains**
- `⚡` Performance (speed, optimization)
- `🔍` Analysis (search, investigation)
- `🔧` Configuration (setup, tools)
- `🛡️` Security (protection, safety)
- `📦` Deployment (package, bundle)
- `🎨` Design (UI, frontend)
- `🏗️` Architecture (system structure)

#### Abbreviation Systems 📝

**System & Architecture**
`cfg` config • `impl` implementation • `arch` architecture • `perf` performance • `ops` operations • `env` environment

**Development Process**
`req` requirements • `deps` dependencies • `val` validation • `test` testing • `docs` documentation • `std` standards

**Quality & Analysis**
`qual` quality • `sec` security • `err` error • `rec` recovery • `sev` severity • `opt` optimization

#### Real Examples 📝

**Standard response:**
```
User: "Analyze the authentication system performance"
Claude: "I'll analyze the authentication system's performance. The user validation function in auth.js line 45 has a security vulnerability. The build process completed successfully, now running tests, then deploying. Performance analysis shows the algorithm is slow because it's O(n²) complexity."
```

**Token Efficiency mode:**
```
User: "Analyze the authentication system performance"
Claude: "⚡ auth.js perf analysis:
         🛡️ auth.js:45 → sec risk in user val()
         📊 build ✅ » test 🔄 » deploy ⏳  
         🔍 perf: slow ∵ O(n²) algo
         
         ∴ rec: impl O(log n) lookup & fix sec val"
```

#### Perfect For 💫
- Large context situations requiring efficiency
- Complex analysis that would normally be verbose
- Performance-critical operations
- Users who prefer concise, information-dense output

---

## How Modes Work Together 🤝

### Mode Coordination Examples

**Building a New Feature** (Multiple Modes)
```bash
# Starts in Brainstorming Mode
/sc:brainstorm "user dashboard"
# 🧠 Discovery questions about requirements

# Transitions to Task Management Mode  
/sc:implement user-dashboard-feature
# 📋 Breaks into coordinated implementation phases

# Orchestration Mode kicks in for complex parts
# 🎯 Chooses best tools for UI (Magic MCP), testing (Playwright MCP)

# Token Efficiency if context gets full
# ⚡ Compresses communication while maintaining quality
```

**Debugging Complex Issues**
```bash
# Starts in Introspection Mode
/sc:troubleshoot "authentication randomly failing"
# 🔍 Systematic analysis of reasoning and patterns

# Orchestration Mode for tool selection
# 🎯 Uses Sequential MCP for structured investigation

# Task Management if solution is complex
# 📋 Coordinates fix across multiple files and systems
```

### Mode Priority System 📊

1. **User-Triggered** (`--brainstorm`, `--uc`, etc.) - Always override automatic
2. **Context-Critical** (Token Efficiency when context >85%) - High priority
3. **Task-Appropriate** (Task Management for 3+ steps) - Standard priority
4. **Enhancement** (Orchestration for optimization) - Background priority

### Mode Switching 🔄

Modes can:
- **Layer together**: Task Management + Orchestration + Token Efficiency
- **Switch dynamically**: Brainstorming → Task Management → Orchestration  
- **Enhance each other**: Introspection + Task Management for better quality

---

## Manual Control 🎛️

### Force Specific Modes

```bash
# Force Brainstorming Mode
/sc:analyze --brainstorm project-requirements

# Force Token Efficiency
/sc:implement --uc user-authentication  

# Force Task Management
/sc:refactor --delegate large-codebase/

# Force Orchestration
/sc:build --orchestrate complex-project/

# Force Introspection
/sc:troubleshoot --introspect "reasoning issues"

# Disable all modes (baseline Claude)
/sc:analyze --no-modes legacy-code/
```

### When to Use Manual Control 🤔

**Force Brainstorming when:**
- You have specific requirements but want to explore alternatives
- Working with stakeholders who need guided discovery
- Converting existing features into comprehensive specs

**Force Token Efficiency when:**
- Working in resource-constrained environments
- Need maximum information density
- Dealing with very large contexts

**Force Task Management when:**
- Want explicit task breakdown for complex work
- Need to coordinate multiple team members
- Require detailed progress tracking

**Force Orchestration when:**
- Performance is critical
- Want to see tool selection reasoning
- Working with multiple MCP servers

**Force Introspection when:**
- Learning how SuperClaude makes decisions  
- Debugging framework behavior
- Want transparent reasoning for auditing

---

## Real-World Scenarios 🌍

### Scenario 1: Building a Task Management App

**Phase 1: Discovery** (Brainstorming Mode)
```bash
/sc:brainstorm "task management app for development teams"

# Mode activates automatically, provides discovery questions:
# - What problems do current tools not solve?
# - How do teams currently track tasks?
# - Integration needs with existing tools?
# - Expected team size and usage patterns?

# Result: Structured requirements brief ready for implementation
```

**Phase 2: Implementation** (Task Management Mode)
```bash  
/sc:implement task-management-app --from-brief requirements.md

# Mode activates for complex implementation:
# Phase 1: Data models and API design
# Phase 2: Core functionality and business logic  
# Phase 3: UI components and user experience
# Phase 4: Integration, testing, and deployment

# Each phase validates before proceeding
```

**Phase 3: Optimization** (Orchestration + Token Efficiency)
```bash
/sc:improve performance task-management-app/

# Orchestration selects best tools for analysis
# Token Efficiency kicks in for large codebase analysis  
# Result: Optimized, production-ready application
```

### Scenario 2: Debugging Authentication Issues

**Investigation** (Introspection Mode)
```bash
/sc:troubleshoot "users can't log in on mobile but desktop works"

# Introspection mode analyzes systematically:
# 🔍 Pattern analysis: Mobile vs desktop differences
# 🤔 Reasoning: What could cause platform-specific auth issues?
# 📊 Evidence gathering: Session handling, cookies, API calls
# 💡 Hypothesis formation and testing approach
```

**Systematic Fix** (Task Management + Orchestration)
```bash
/sc:implement auth-mobile-fix

# Task Management coordinates the fix:
# Phase 1: Mobile session analysis (Playwright MCP for testing)
# Phase 2: API compatibility fixes (Sequential MCP for logic)
# Phase 3: Cross-platform validation (multiple tools)

# Orchestration ensures optimal tool usage throughout
```

### Scenario 3: Large Codebase Refactoring

**Planning** (Brainstorming + Introspection)
```bash
/sc:brainstorm "refactor legacy PHP app to modern architecture"

# Brainstorming explores scope and requirements
# Introspection analyzes current architecture patterns
# Result: Clear migration strategy and requirements
```

**Execution** (Task Management + Token Efficiency)
```bash
/sc:refactor --delegate legacy-app/ --target modern-architecture

# Task Management breaks into systematic phases
# Token Efficiency handles large codebase analysis efficiently
# Phase coordination ensures no breaking changes
```

---

## FAQ 🙋

### Do I need to understand behavioral modes?

**No!** They work automatically. You focus on what you want to do, modes handle how SuperClaude helps you. Think of them like having different experts who automatically step in when needed.

### How do I know which mode is active?

Look for **behavioral markers**:
- 🤔 **Questions and exploration** = Brainstorming Mode
- 🔍 **Reasoning analysis symbols** = Introspection Mode  
- 📋 **Phase breakdowns and delegation** = Task Management Mode
- 🎯 **Tool selection matrices** = Orchestration Mode
- ⚡ **Symbols and abbreviations** = Token Efficiency Mode

### Can I disable behavioral modes?

**Yes!** Use `--no-modes` flag:
```bash
/sc:analyze --no-modes simple-file.js
```

This gives you baseline Claude behavior without mode enhancements.

### Which mode should I use manually?

**Usually none!** Automatic activation works well 95% of the time. Manual control is for:
- **Learning**: Force modes to see how they work
- **Special cases**: Unusual requirements or constraints  
- **Team coordination**: Explicit task breakdowns for collaboration
- **Performance**: Force efficiency in resource-constrained environments

### Can multiple modes be active at once?

**Yes!** Modes often layer together:
- Task Management + Orchestration (complex projects with optimal tools)
- Introspection + Token Efficiency (deep analysis with compressed output)
- Brainstorming + Task Management (discovery → implementation pipeline)

### Do modes work with all commands?

Most commands work with modes, but some have natural affinities:
- `/sc:brainstorm` → Always Brainstorming Mode
- `/sc:troubleshoot` → Often Introspection Mode  
- `/sc:implement` (complex) → Usually Task Management Mode
- Large operations → Often trigger Orchestration Mode
- High context → May activate Token Efficiency Mode

### Are modes related to agents?

**Yes, but differently!** 
- **Agents** = Who helps (security-engineer, frontend-architect, etc.)
- **Modes** = How they help (systematically, efficiently, collaboratively)

Modes determine the behavioral approach, agents provide domain expertise. A security-engineer might work in Task Management mode for complex security implementations, or Introspection mode for security analysis.

---

## Technical Reference 🔧

### Complete Trigger Lists

**Brainstorming Mode Triggers**
- **Keywords**: brainstorm, explore, discuss, figure out, not sure, maybe, possibly, thinking about, could we
- **Phrases**: "I want to build...", "thinking about creating...", "not sure how to...", "maybe we could..."
- **Context**: Vague requirements, early planning, stakeholder discussions
- **Manual**: `--brainstorm`, `--bs`

**Introspection Mode Triggers**  
- **Keywords**: analyze reasoning, reflect on, why did, decision logic, pattern check
- **Context**: Error recovery, unexpected results, complex problem solving, framework discussions
- **Indicators**: Multiple failed approaches, recurring issues, need for meta-analysis
- **Manual**: `--introspect`, `--introspection`

**Task Management Mode Triggers**
- **Operations**: build, implement, create, fix, refactor (3+ steps)
- **Scope**: system, feature, comprehensive, complete, end-to-end
- **Thresholds**: >2 directories OR >3 files OR complexity score >0.4
- **Keywords**: polish, refine, enhance, coordinate, manage
- **Manual**: `--delegate`, `--loop`, `--concurrency`

**Orchestration Mode Triggers**
- **Conditions**: Multi-tool operations, >3 files, parallel opportunities
- **Performance**: >75% resource usage, efficiency requirements
- **Complexity**: Multiple valid approaches, tool selection decisions
- **Manual**: `--orchestrate`

**Token Efficiency Mode Triggers**
- **Resource**: Context >75%, large-scale operations, memory constraints
- **User requests**: `--uc`, `--ultracompressed`, brevity requirements  
- **Workflow**: Complex analysis needing optimization, high information density
- **Manual**: `--uc`, `--ultracompressed`, `--token-efficient`

### Flag Reference Table 🏳️

| Flag | Mode | Purpose | Usage |
|------|------|---------|-------|
| `--brainstorm`, `--bs` | Brainstorming | Force discovery mode | Requirements exploration |
| `--introspect` | Introspection | Force reasoning analysis | Decision transparency |
| `--delegate` | Task Management | Force delegation mode | Complex coordination |
| `--delegate` | Task Management | Enable delegation mode | Parallel processing |
| `--loop` | Task Management | Enable iteration cycles | Improvement workflows |
| `--orchestrate` | Orchestration | Force tool optimization | Performance priority |
| `--uc`, `--ultracompressed` | Token Efficiency | Force compression | Resource constraints |
| `--no-modes` | None | Disable all modes | Baseline behavior |

### Integration with Framework Components

**With Agents** 🤖
- Modes determine **how** agents work
- Agents provide **domain expertise**
- Example: security-engineer in Task Management mode = systematic security implementation

**With Commands** 🛠️
- Commands trigger mode activation
- Modes enhance command execution
- Example: `/sc:implement` complex features → Task Management mode activation

**With MCP Servers** 🔧
- Orchestration mode optimizes MCP usage
- Task Management coordinates multi-MCP operations
- Token Efficiency compresses MCP communications

### Performance Metrics 📊

**Mode Efficiency Gains**
- **Brainstorming**: 60-80% better requirement clarity
- **Introspection**: 40-60% improved decision quality
- **Task Management**: 40-70% time savings via delegation
- **Orchestration**: 20-40% performance improvement via optimal tools
- **Token Efficiency**: 30-50% token reduction with 95%+ information preservation

**Resource Impact**
- Brainstorming: Low overhead, high value for unclear requirements
- Introspection: Medium overhead, high value for complex problems
- Task Management: Variable overhead, scales with task complexity
- Orchestration: Low overhead, improves overall efficiency
- Token Efficiency: Negative overhead (saves resources), maintains quality

---

*Behavioral modes are SuperClaude's intelligence system - they make Claude Code smarter about how it helps you. You don't manage them, they manage themselves to give you the best experience! 🧠✨*

---

## Related Guides

**🚀 Getting Started (Essential)**
- [SuperClaude User Guide](superclaude-user-guide.md) - Framework overview and philosophy
- [Examples Cookbook](examples-cookbook.md) - See modes in action with real examples

**🛠️ Working with Modes (Recommended)**
- [Commands Guide](commands-guide.md) - Commands that trigger different modes
- [Agents Guide](agents-guide.md) - How agents work within different modes
- [Session Management Guide](session-management.md) - Mode persistence across sessions

**⚙️ Control and Optimization (Advanced)**
- [Flags Guide](flags-guide.md) - Manual mode control with flags like --brainstorm, --uc
- [Best Practices Guide](best-practices.md) - Proven patterns for mode utilization
- [Technical Architecture Guide](technical-architecture.md) - Mode detection and activation system

**🔧 When Modes Don't Work as Expected**
- [Troubleshooting Guide](troubleshooting-guide.md) - Mode activation and behavioral issues

**📖 Recommended Learning Path:**
1. [Examples Cookbook](examples-cookbook.md) - See auto-activation in practice
2. [Commands Guide](commands-guide.md) - Understand mode triggers
3. [Best Practices Guide](best-practices.md) - Master mode coordination patterns