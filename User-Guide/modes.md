# SuperClaude Behavioral Modes Guide 🧠

## 💡 The Simple Truth About Modes

SuperClaude employs 6 behavioral modes that automatically adapt Claude Code's communication style, tool selection, and workflow approach based on task context and complexity. Modes work seamlessly in the background - you don't need to think about them.

**Automatic Intelligence**: Type `/sc:brainstorm "mobile app"` → Brainstorming mode activates with Socratic questions. Type `/sc:analyze src/` → Introspection mode provides transparent reasoning. Type complex multi-file operations → Task Management coordinates execution phases.

**Behind the Scenes**: Modes enhance your experience by optimizing communication patterns, resource usage, and workflow orchestration based on what you're trying to accomplish.

---

## 🚀 Just Try These (See Modes in Action)

**Automatic Mode Examples:**
```bash
# Brainstorming mode activates automatically
/sc:brainstorm "fitness tracking app"
# → Socratic questions about users, features, goals

# Introspection mode shows reasoning
/sc:analyze --focus security 
# → Transparent thinking: "🤔 Why security first? 🎯 Risk assessment shows..."

# Task Management coordinates complex work
/sc:implement "user authentication with email verification"
# → Phases: analysis → design → implementation → testing

# Orchestration optimizes tool selection  
/sc:improve src/ --focus performance
# → Magic + Morphllm + Sequential coordination

# Token Efficiency compresses output
"--uc implement auth API"
# → "auth.js:45 → 🔧 JWT middleware ⇒ validated_user"
```

**Mode Detection Logic:**
- **Keywords**: "brainstorm", "maybe" → Brainstorming
- **Complexity**: >3 files → Task Management  
- **Performance**: Resource pressure → Token Efficiency
- **Multi-tool**: Complex analysis → Orchestration
- **Error recovery**: Problems → Introspection

---

## The Six Behavioral Modes 🌟

### 🧠 Brainstorming Mode - Interactive Discovery

**Purpose**: Collaborative requirements exploration through Socratic dialogue

**Auto-Activation Triggers:**
- Vague requests: "I want to build...", "Thinking about creating..."
- Exploration keywords: brainstorm, explore, discuss, figure out, not sure
- Uncertainty: "maybe", "possibly", "could we"
- Manual flags: `--brainstorm`, `--bs`

**What Changes:**
- **Socratic Questions**: Probing questions to uncover hidden requirements
- **Non-Presumptive**: Avoid assumptions, let you guide discovery
- **Collaborative**: Partner in exploration rather than directive consultation
- **Brief Generation**: Synthesize insights into structured requirements

**Example Experience:**
```
You: "I want to build a web app"
Brainstorming: "🤔 Discovery Questions:
               - What problem does this solve for users?
               - Who are your target users and workflows?
               - Expected user volume and performance needs?
               - Any existing systems to integrate with?"
```

---

### 🔍 Introspection Mode - Meta-Cognitive Analysis

**Purpose**: Transparent reasoning and self-analysis for learning optimization

**Auto-Activation Triggers:**
- Self-analysis requests: "analyze my reasoning", "reflect on decision"
- Error recovery: unexpected results or outcomes
- Complex problem solving requiring meta-cognition
- Manual flag: `--introspect`

**What Changes:**
- **Transparency**: Expose thinking with markers (🤔, 🎯, ⚡, 📊, 💡)
- **Pattern Detection**: Identify recurring behaviors and optimizations
- **Self-Examination**: Analyze decision logic and reasoning chains
- **Learning Focus**: Extract insights for continuous improvement

**Example Experience:**
```
Standard: "I'll analyze this code structure"
Introspective: "🧠 Reasoning: Why structural over functional analysis?
               🔄 Alternative: Could start with data flow patterns
               💡 Learning: Structure-first works for OOP, not functional"
```

---

### 📋 Task Management Mode - Orchestration & Delegation

**Purpose**: Hierarchical organization with persistent memory for complex multi-step operations

**Auto-Activation Triggers:**
- Operations >3 steps requiring coordination
- Multiple file/directory scope (>2 directories OR >3 files)
- Complex dependencies requiring phases
- Manual flags: `--task-manage`, `--delegate`

**What Changes:**
- **Memory Integration**: Session persistence and context preservation
- **Phase Coordination**: Break complex work into manageable phases
- **Progress Tracking**: TodoWrite + memory updates for state management
- **Quality Gates**: Systematic validation at each phase

**Task Hierarchy:**
```
📋 Plan → 🎯 Phase → 📦 Task → ✓ Todo
```

**Example Experience:**
```
/sc:implement "payment system"
→ Phase 1: Security analysis
→ Phase 2: API design  
→ Phase 3: Implementation
→ Phase 4: Testing & validation
→ Session persistence across interruptions
```

---

### 🎯 Orchestration Mode - Intelligent Tool Selection

**Purpose**: Optimal task routing and resource efficiency through smart tool coordination

**Auto-Activation Triggers:**
- Multi-tool operations requiring coordination
- Performance constraints (>75% resource usage)
- Parallel execution opportunities (>3 files)
- Complex routing decisions

**What Changes:**
- **Smart Tool Selection**: Choose optimal tool for each task type
- **Resource Awareness**: Adapt approach based on system constraints  
- **Parallel Thinking**: Identify independent operations for concurrency
- **Efficiency Focus**: Optimize tool usage for speed and effectiveness

**Tool Selection Matrix:**
- UI components → Magic MCP > Manual coding
- Deep analysis → Sequential MCP > Native reasoning
- Pattern edits → Morphllm MCP > Individual edits
- Documentation → Context7 MCP > Web search

**Example Experience:**
```
Complex multi-file refactoring:
→ Serena: Symbol analysis
→ Sequential: Strategy planning  
→ Morphllm: Pattern application
→ Parallel execution coordination
```

---

### ⚡ Token Efficiency Mode - Compressed Communication

**Purpose**: Symbol-enhanced communication for 30-50% token reduction while preserving clarity

**Auto-Activation Triggers:**
- Context usage >75% or resource constraints
- Large-scale operations requiring efficiency
- User flags: `--uc`, `--ultracompressed`
- Complex analysis workflows

**What Changes:**
- **Symbol Communication**: Visual symbols for logic, status, domains
- **Abbreviation Systems**: Context-aware compression for technical terms
- **Structured Output**: Bullet points, tables over verbose paragraphs
- **Information Density**: Maximum clarity per token

**Symbol Examples:**
```
Standard: "The authentication system has a security vulnerability"
Compressed: "auth.js:45 → 🛡️ sec risk in user val()"

Standard: "Build completed, now testing, then deploying"
Compressed: "build ✅ » test 🔄 » deploy ⏳"
```

---

### 🎨 Standard Mode - Balanced Default

**Purpose**: Balanced communication for general-purpose development tasks

**Default Behavior:**
- Clear, professional communication
- Moderate detail level
- Standard tool selection
- Quality-focused workflows

**When Active:**
- Simple, straightforward tasks
- No complexity triggers detected
- User preference for standard behavior
- Balanced resource usage scenarios

---

### 🔍 Introspection Mode - Meta-Cognitive Analysis

**Purpose**: Meta-cognitive analysis and reasoning transparency for complex problem solving and decision optimization.

**Auto-Activation Triggers:**
- Self-analysis requests: "analyze my reasoning", "reflect on decision"
- Error recovery scenarios and unexpected results
- Complex problem solving requiring multi-step reasoning
- Pattern recognition needs and optimization opportunities
- Manual flag: `--introspect`

**Capabilities:**
- **Reasoning Transparency**: Expose thinking process with clear markers (🤔, 🎯, ⚡, 📊, 💡)
- **Decision Analysis**: Evaluate choice logic and alternative approaches
- **Pattern Detection**: Identify recurring behaviors and optimization opportunities
- **Learning Optimization**: Extract insights for continuous improvement

**Examples:**
```bash
# Decision analysis after unexpected results
"The API optimization didn't improve performance as expected"
# 🤔 Decision Analysis: Why did I choose caching over database optimization?
# 📊 Evidence Review: Database queries actually the bottleneck
# 💡 Learning: Profile first, then optimize based on data

# Pattern recognition for improvement
"I keep having authentication issues"
# 🎯 Pattern Analysis: Similar auth failures in projects X, Y, Z
# ⚡ Root Cause: Consistent token refresh logic gap
# 📊 Solution Strategy: Centralized auth state management
```

---

### 📋 Task Management Mode - Orchestration & Delegation

**Purpose**: Hierarchical task organization with intelligent delegation for complex multi-step operations.

**Auto-Activation Triggers:**
- Operations with >3 steps requiring coordination
- Multiple file/directory scope (>2 directories OR >3 files)
- Complex dependencies requiring phases
- Manual flags: `--task-manage`, `--delegate`

**Capabilities:**
- **Phase Management**: Break complex tasks into manageable phases with dependencies
- **Intelligent Delegation**: Route subtasks to appropriate specialist agents
- **Progress Tracking**: Monitor completion across multiple parallel operations
- **Quality Gates**: Validation checkpoints between phases

**Examples:**
```bash
# E-commerce platform development (auto-delegates to multiple agents)
/sc:implement "complete e-commerce platform with payment integration"
# Phase 1: Architecture → system-architect
# Phase 2: Backend APIs → backend-architect + security-engineer  
# Phase 3: Frontend UI → frontend-architect + quality-engineer
# Phase 4: Payment Integration → security-engineer + backend-architect
# Phase 5: Testing & Deployment → devops-architect + quality-engineer

# Large codebase refactoring (delegates by file type and complexity)
/sc:improve legacy-codebase/ --comprehensive
# Delegation: Python files → python-expert + refactoring-expert
# Delegation: React components → frontend-architect + refactoring-expert
# Delegation: API endpoints → backend-architect + security-engineer
```

---

### 🎯 Orchestration Mode - Intelligent Tool Selection

**Purpose**: Intelligent tool selection and resource optimization for maximum efficiency and parallel execution.

**Auto-Activation Triggers:**
- Multi-tool operations requiring coordination
- Performance constraints (>75% resource usage)
- Parallel execution opportunities (>3 independent operations)
- Complex routing decisions with multiple valid approaches

**Capabilities:**
- **Smart Tool Selection**: Choose optimal tools for each task type (MCP servers, native tools)
- **Resource Awareness**: Adapt approach based on system constraints and availability
- **Parallel Optimization**: Identify and execute independent operations concurrently
- **Efficiency Focus**: Maximize speed and effectiveness through intelligent coordination

**Tool Selection Matrix:**
| Task Type | Optimal Tool | Fallback | Parallel Opportunity |
|-----------|-------------|----------|---------------------|
| UI Components | Magic MCP | Native coding | ✅ Multiple components |
| Code Analysis | Sequential MCP | Native reasoning | ✅ Multiple files |
| Documentation | Context7 MCP | Web search | ✅ Multiple topics |
| Multi-file edits | MultiEdit | Sequential edits | ❌ Dependencies exist |

**Resource Management Zones:**
- **🟢 Green (0-75%)**: Full capabilities, all tools available
- **🟡 Yellow (75-85%)**: Efficiency mode, reduced verbosity
- **🔴 Red (85%+)**: Essential operations only, minimal output

---

### ⚡ Token Efficiency Mode - Compressed Communication

**Purpose**: Symbol-enhanced communication achieving 30-50% token reduction while preserving information quality.

**Auto-Activation Triggers:**
- Context usage >75% or resource constraints
- Large-scale operations requiring efficiency
- User requests brevity: `--uc`, `--ultracompressed`
- Complex analysis workflows needing optimization

**Symbol Systems:**

**Core Logic**: → (leads to), ⇒ (transforms), ← (rollback), ⇄ (bidirectional)
**Status**: ✅ (completed), ❌ (failed), ⚠️ (warning), 🔄 (in progress)
**Technical**: ⚡ (performance), 🔍 (analysis), 🔧 (config), 🛡️ (security)

**Abbreviation Systems:**
- **System**: `cfg` config, `impl` implementation, `arch` architecture, `perf` performance
- **Process**: `req` requirements, `deps` dependencies, `val` validation, `test` testing
- **Quality**: `qual` quality, `sec` security, `err` error, `opt` optimization

**Examples (30-50% compression):**
```
Standard: "The authentication system has a security vulnerability in the user validation function"
Compressed: "auth.js:45 → 🛡️ sec risk in user val()"

Standard: "Performance analysis shows the algorithm is slow because of O(n²) complexity"  
Compressed: "⚡ perf analysis: slow ∵ O(n²) complexity"

Standard: "Build process completed successfully, now running tests, then deploying"
Compressed: "build ✅ » test 🔄 » deploy ⏳"
```

---

## How Modes Work Together 🤝

**Mode Coordination Patterns:**

**Discovery → Implementation Workflow:**
```bash
# Brainstorming discovers requirements
/sc:brainstorm "e-commerce platform"
→ Requirements brief generated

# Task Management coordinates implementation  
/sc:implement "payment integration"
→ Phase 1: Architecture (Orchestration mode for tool selection)
→ Phase 2: Implementation (Token Efficiency if complex)
→ Phase 3: Testing (Introspection for quality analysis)
```

**Multi-Mode Complex Scenarios:**

**Large Codebase Refactoring:**
1. **Brainstorming**: Explore improvement goals and priorities
2. **Introspection**: Analyze current code patterns and issues
3. **Task Management**: Coordinate multi-phase refactoring plan
4. **Orchestration**: Select optimal tools (Morphllm + Sequential + Serena)
5. **Token Efficiency**: Compress communication during execution

**Performance Optimization:**
1. **Task Management**: Break into analysis → optimization → validation phases
2. **Orchestration**: Coordinate Sequential (analysis) + Magic (UI fixes) + Playwright (testing)
3. **Introspection**: Transparent reasoning about bottleneck identification
4. **Token Efficiency**: Compress performance metrics and results

**Mode Priority System:**
- **Safety First**: Introspection overrides efficiency when quality matters
- **Context Adaptation**: Modes layer based on complexity and scope
- **Resource Management**: Token Efficiency activates under pressure
- **User Intent**: Manual flags override automatic detection

---

## Manual Control 🎛️

**Force Specific Modes:**

**Mode Activation Flags:**
```bash
# Force brainstorming for requirement exploration
/sc:implement "user auth" --brainstorm

# Enable introspection for learning/debugging
/sc:analyze src/ --introspect

# Activate task management for complex coordination
/sc:improve legacy-code/ --task-manage

# Enable orchestration for optimal tool selection
/sc:refactor components/ --orchestrate

# Force token efficiency for compressed output
/sc:analyze large-project/ --uc
```

**When to Use Manual Control:**

**Override Automatic Detection:**
- Simple task needs structured approach → `--task-manage`
- Want transparent reasoning → `--introspect`
- Need compressed output → `--uc`
- Force collaborative discovery → `--brainstorm`

**Learning and Development:**
- Study reasoning patterns → `--introspect`
- Practice requirement discovery → `--brainstorm`  
- Understand tool coordination → `--orchestrate`
- Optimize token usage → `--token-efficient`

**Resource Management:**
- High memory pressure → `--uc`
- Complex multi-tool scenarios → `--orchestrate`
- Large scope coordination → `--task-manage`

**Mode Combination:**
```bash
# Multiple modes for complex scenarios
/sc:implement "microservices architecture" --brainstorm --task-manage --orchestrate

# Analysis with reasoning transparency
/sc:analyze security-audit/ --introspect --uc
```

---

## Real-World Scenarios 🌍

**Scenario 1: New Project Startup**

```bash
# Phase 1: Discovery (Brainstorming Mode)
/sc:brainstorm "task management mobile app"
```
*Experience*: Socratic questions about users, features, platform choice, backend needs
*Outcome*: Structured requirements brief with technical specifications

```bash
# Phase 2: Planning (Task Management Mode)  
/sc:workflow "implement core task features"
```
*Experience*: Multi-phase breakdown with dependencies and time estimates
*Outcome*: Systematic implementation plan with quality gates

```bash
# Phase 3: Implementation (Orchestration Mode)
/sc:implement "user authentication with social login"
```
*Experience*: Magic (UI) + Context7 (auth patterns) + Security specialist coordination
*Outcome*: Complete auth system with tests and documentation

---

**Scenario 2: Authentication Debugging**

```bash
# Step 1: Problem Analysis (Introspection Mode)
/sc:troubleshoot "users getting 401 errors intermittently"
```
*Experience*: 
```
🤔 Reasoning: Why intermittent? Session timing vs token expiry
🔍 Investigation: Check auth middleware, session storage, token validation
🎯 Hypothesis: Race condition in token refresh
📊 Evidence: Log patterns show timing correlation
💡 Solution: Implement token refresh queue
```

```bash
# Step 2: Systematic Fix (Task Management Mode)
/sc:implement "token refresh queue with retry logic"
```
*Experience*: Phase coordination across middleware, frontend, and testing
*Outcome*: Robust authentication flow with comprehensive error handling

---

**Scenario 3: Large Codebase Refactoring**

```bash
# Phase 1: Assessment (Token Efficiency + Introspection)
/sc:analyze legacy-codebase/ --focus maintainability --uc
```
*Experience*:
```
🔍 Analysis:
  auth.js:142 → 🛡️ sec vuln (hardcoded keys)
  ui-comp/ → 🎨 inconsistent patterns
  api/ → ⚡ perf bottlenecks (N+1 queries)
📊 Debt: 847 lines need refactoring
💡 Priority: sec → perf → patterns
```

```bash
# Phase 2: Planning (Task Management + Orchestration)  
/sc:improve legacy-codebase/ --task-manage --orchestrate
```
*Experience*: Multi-phase plan with Morphllm (patterns) + Sequential (analysis) + Serena (context)
*Outcome*: Systematic refactoring with progress tracking and rollback safety

```bash
# Phase 3: Quality Validation (Introspection)
/sc:reflect "refactoring impact assessment"
```
*Experience*: Transparent analysis of improvements, remaining debt, and success metrics
*Outcome*: Evidence-based completion assessment with next steps

---

**Scenario 4: Performance Optimization**

```bash
# Discovery (Brainstorming Mode for unclear performance issues)
/sc:brainstorm "app feels slow but unclear where"
```
*Experience*: Questions about user workflows, data volumes, environment differences
*Outcome*: Focused performance investigation scope

```bash
# Systematic Analysis (Task Management + Token Efficiency)
/sc:analyze --focus performance --task-manage --uc
```
*Experience*:
```
Phase 1: Frontend metrics → ⚡ bundle size 2.4MB
Phase 2: API latency → 📊 db queries avg 1.2s  
Phase 3: Infrastructure → 🔧 memory usage 85%
Priority: db opt → bundle split → memory tuning
```

```bash
# Coordinated Fixes (Orchestration Mode)
/sc:improve --focus performance --orchestrate
```
*Experience*: Sequential (analysis) + Morphllm (code patterns) + Context7 (optimization patterns)
*Outcome*: 60% performance improvement with systematic validation

---

## FAQ 🙋

**Q: How do I know which mode is active?**
A: Modes work transparently, but you can identify them by communication patterns:
- 🤔 Questions and discovery → Brainstorming
- 🧠 🎯 Reasoning markers → Introspection  
- Phase breakdowns → Task Management
- Tool coordination mentions → Orchestration
- Symbol-compressed output → Token Efficiency

**Q: Can I disable modes?**
A: Modes enhance rather than restrict. For minimal behavior, avoid complexity triggers:
- Simple, single-task requests
- Specific file operations
- Clear, unambiguous instructions

**Q: Do modes affect performance?**
A: Modes optimize performance:
- **Token Efficiency**: 30-50% reduction in context usage
- **Orchestration**: Parallel processing and optimal tool selection
- **Task Management**: Systematic execution prevents rework

**Q: Can modes conflict with each other?**
A: Modes are designed to work together:
- **Hierarchical**: Task Management coordinates other modes
- **Contextual**: Token Efficiency activates under resource pressure
- **Complementary**: Introspection provides transparency for any mode

**Q: How do modes relate to agents and commands?**
A: Integrated coordination:
- **Commands** trigger appropriate modes automatically
- **Agents** work within mode communication patterns
- **MCP servers** are selected by Orchestration mode logic

**Q: What if automatic detection is wrong?**
A: Manual override available:
```bash
/sc:command --brainstorm      # Force discovery approach
/sc:command --no-introspect   # Suppress reasoning markers
/sc:command --uc              # Force compression
```

---

## Technical Reference 🔧

**Mode Activation Triggers:**

| Mode | Automatic Triggers | Manual Flags |
|------|-------------------|--------------|
| **Brainstorming** | "brainstorm", "explore", "maybe", "not sure" | `--brainstorm`, `--bs` |
| **Introspection** | Error recovery, self-analysis requests | `--introspect` |
| **Task Management** | >3 steps, >2 directories, >3 files | `--task-manage`, `--delegate` |
| **Orchestration** | Multi-tool ops, >75% resources, >3 files | `--orchestrate` |
| **Token Efficiency** | >75% context, large ops, resource pressure | `--uc`, `--ultracompressed` |
| **Standard** | Simple tasks, no complexity triggers | Default |

**Flag Reference:**

**Mode Control Flags:**
- `--brainstorm` / `--bs`: Force collaborative discovery
- `--introspect`: Enable reasoning transparency
- `--task-manage`: Activate hierarchical coordination
- `--orchestrate`: Optimize tool selection and parallelization
- `--token-efficient` / `--uc`: Enable symbol compression

**Mode Integration Flags:**
- `--think`: Enable Sequential MCP (moderate analysis)
- `--think-hard`: Deep analysis with Sequential + Context7
- `--ultrathink`: Maximum analysis with all MCP servers
- `--safe-mode`: Conservative execution with validation

**Mode Interaction with Framework Components:**

**Agent Coordination:**
- Modes influence agent communication patterns
- Task Management coordinates multi-agent workflows
- Orchestration optimizes agent-tool combinations
- Token Efficiency compresses agent outputs

**Command Integration:**
- Commands auto-select appropriate modes
- Mode flags override automatic selection
- Complex commands activate Task Management
- Analysis commands trigger Introspection

**MCP Server Selection:**
- Orchestration mode optimizes MCP coordination
- Token Efficiency mode minimizes MCP overhead  
- Task Management preserves MCP context across phases
- Brainstorming leverages Sequential for structured thinking

**Performance Metrics:**

| Mode | Token Reduction | Processing Speed | Quality Impact |
|------|----------------|------------------|----------------|
| **Brainstorming** | 0% | Standard | +Requirements clarity |
| **Introspection** | -10% (detail) | -15% (analysis) | +Learning, +Debugging |
| **Task Management** | +20% (structure) | +30% (parallel) | +Completeness |
| **Orchestration** | +15% (efficiency) | +45% (parallel) | +Tool optimization |
| **Token Efficiency** | +30-50% | +25% (less context) | Maintained (95%+) |
| **Standard** | Baseline | Baseline | Baseline |

---

## The Magic of Intelligent Adaptation ✨

SuperClaude's behavioral modes represent a breakthrough in AI framework design: **intelligence that adapts to you, not the other way around**. The system observes your context, analyzes task complexity, and seamlessly adjusts its communication style, tool selection, and workflow approach.

**You Don't Need to Think About Modes** - they work transparently in the background, enhancing your experience without adding complexity. Start a vague project idea and watch Brainstorming mode guide discovery. Tackle complex refactoring and see Task Management coordinate phases. Work under resource pressure and observe Token Efficiency compress communication while preserving clarity.

**The Result**: Claude Code transforms from a capable assistant into an **intelligent partner** that matches your needs at every step of the development journey.

---

## Related Guides

**Learning Progression:**

**🌱 Essential (Week 1)**
- [Quick Start Guide](../Getting-Started/quick-start.md) - Experience modes naturally
- [Commands Reference](commands.md) - Commands automatically activate modes
- [Installation Guide](../Getting-Started/installation.md) - Set up behavioral modes

**🌿 Intermediate (Week 2-3)**  
- [Agents Guide](agents.md) - How modes coordinate with specialists
- [Flags Guide](flags.md) - Manual mode control and optimization
- [Examples Cookbook](../Reference/examples-cookbook.md) - Mode patterns in practice

**🌲 Advanced (Month 2+)**
- [MCP Servers](mcp-servers.md) - Mode integration with enhanced capabilities
- [Session Management](session-management.md) - Task Management mode workflows  
- [Best Practices](../Reference/best-practices.md) - Mode optimization strategies

**🔧 Expert**
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - Mode implementation details
- [Contributing Code](../Developer-Guide/contributing-code.md) - Extend mode capabilities

**Mode-Specific Guides:**
- **Brainstorming**: [Requirements Discovery Patterns](../Reference/examples-cookbook.md#requirements)
- **Task Management**: [Session Management Guide](session-management.md)
- **Orchestration**: [MCP Servers Guide](mcp-servers.md)
- **Token Efficiency**: [Performance Optimization](../Reference/best-practices.md#efficiency)