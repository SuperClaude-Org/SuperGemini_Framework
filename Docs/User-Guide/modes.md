# SuperGemini Behavioral Modes Guide 🧠

## ✅ Verification Status
- **SuperGemini Version**: v4.0+ Compatible
- **Last Tested**: 2025-01-16
- **Test Environment**: Linux/Windows/macOS
- **Mode Activation**: ✅ All Verified

## 🧪 Testing Mode Activation

Before using this guide, verify modes activate correctly:

```bash
# Test analysis mode with creative exploration
/sg:analyze "vague project idea"
# Expected: Should analyze requirements and suggest implementation approaches

# Test Task Management mode  
/sg:implement "complex multi-file feature"
# Expected: Should break down into phases and coordinate steps

# Test Token Efficiency mode
/sg:analyze large-project/ --uc
# Expected: Should use symbols and compressed output format
```

**If tests fail**: Modes activate automatically based on request complexity - check behavior patterns below

## Quick Reference Table

| Mode | Purpose | Auto-Triggers | Key Behaviors | Best Used For |
|------|---------|---------------|---------------|---------------|
| **🧠 Creative Analysis** | Requirements exploration | "analyze", "explore", creative requests | Requirement analysis, solution exploration | New project planning, requirement clarification |
| **🔍 Introspection** | Meta-cognitive analysis | Error recovery, "analyze reasoning" | Transparent thinking markers (🤔, 🎯, 💡) | Debugging, learning, optimization |
| **📋 Task Management** | Complex coordination | >3 steps, >2 directories | Phase breakdown, memory persistence | Multi-step operations, project management |
| **🎯 Orchestration** | Intelligent tool selection | Multi-tool ops, >75% resources | Optimal tool routing, parallel execution | Complex analysis, performance optimization |
| **⚡ Token Efficiency** | Compressed communication | >75% context usage, `--uc` flag | Symbol systems, 30-50% token reduction | Resource constraints, large operations |
| **🎨 Standard** | Balanced default | Simple tasks, no complexity triggers | Clear professional communication | General development, straightforward tasks |

---

## Getting Started (2-Minute Overview)

**Modes activate automatically** - you don't need to think about them. They adapt Gemini CLI's behavior based on your task complexity and context.

**Quick Examples:**
```bash
# Automatic activation examples
/sg:analyze "mobile app" --analyze     # → Requirement analysis and suggestions
/sg:implement "auth system"        # → Multi-phase coordination  
"--uc analyze large-codebase/"     # → Compressed symbol output
```

**When to use manual flags:**
- Need specific behavior: `--analyze`, `--introspect`, `--uc`
- Override automatic detection for learning/debugging
- Optimize for specific constraints (memory, time, clarity)

---

## Mode Details

### 🧠 Creative Analysis Mode - Requirements Exploration

**Purpose**: Analyze vague ideas and provide structured implementation approaches.

**Auto-Activation Triggers:**
- Vague project requests: "I want to build...", "Thinking about creating..."
- Analysis keywords: analyze, explore, discuss, figure out, evaluate
- Uncertainty indicators: "maybe", "possibly", "could we"
- Manual flags: `--analyze`, `--explore`

**Note**: The previous flag has been removed. Use /sg:analyze for requirement analysis and exploration.

**Behavioral Changes:**
- **Requirements Analysis**: Analyzes project requirements and suggests implementation approaches
- **Solution Exploration**: Provides multiple viable solutions and architectural options
- **Technical Guidance**: Offers structured technical recommendations
- **Implementation Planning**: Converts analysis into actionable development plans
- **Context-Aware Suggestions**: Adapts recommendations based on project scope and constraints

**Example Experience:**
```
Standard Approach: "I'll build a user authentication system with JWT tokens..."
Analysis Approach: 
"🔍 Authentication System Analysis:
 - User auth requirements: session management, security levels
 - Implementation options: JWT, OAuth, session-based auth
 - Integration considerations: existing systems, third-party services
 - Security requirements: encryption, compliance standards
 📝 Outcome: Detailed technical implementation plan with alternatives"
```

#### Success Criteria  
- [ ] Responds with questions instead of immediate solutions
- [ ] Questions explore user needs, technical constraints, and business goals
- [ ] Maintains collaborative tone throughout discovery process
- [ ] Produces structured requirements or technical brief as outcome

**Verify:** `/sg:analyze "web app"` should analyze requirements and suggest implementation approaches  
**Test:** Vague requests should trigger analysis and provide structured recommendations  
**Check:** Analysis should provide clear next steps for implementation

**Works Best With:**
- **→ Task Management**: Requirements discovery → systematic implementation planning
- **→ Orchestration**: Requirements clarity → optimal tool selection for implementation
- **Manual Override**: Use `/sg:analyze` for requirement analysis on any project

---

### 🔍 Introspection Mode - Meta-Cognitive Analysis

**Purpose**: Expose reasoning process for learning optimization and transparent decision-making.

**Auto-Activation Triggers:**
- Self-analysis requests: "analyze my reasoning", "reflect on decision"
- Error recovery scenarios and unexpected results requiring investigation
- Complex problem solving with multiple viable approaches
- Pattern recognition needs for optimization opportunities
- Manual flag: `--introspect`

**Behavioral Changes:**
- **Reasoning Transparency**: Exposes thinking process with clear markers (🤔, 🎯, ⚡, 📊, 💡)
- **Decision Analysis**: Evaluates choice logic and considers alternative approaches
- **Pattern Recognition**: Identifies recurring behaviors and improvement opportunities
- **Meta-Learning**: Extracts insights for continuous framework improvement
- **Framework Compliance**: Validates actions against SuperGemini principles and quality gates

**Example Experience:**
```
Standard Approach: "I'll analyze this code structure and suggest improvements..."
Introspective Approach:
"🧠 Meta-Analysis: Why did I choose structural analysis over functional flow?
 🎯 Decision Logic: Saw class hierarchy → assumed OOP pattern dominance
 🔄 Alternative Considered: Data flow analysis might reveal hidden dependencies
 📊 Evidence Check: File imports suggest functional composition, not OOP
 💡 Learning: Need to analyze imports before choosing analysis strategy
 ⚡ Correction: Switching to functional flow analysis approach"
```

**Works Best With:**
- **→ Task Management**: Provides transparent reasoning for complex phase decisions
- **Any Mode**: Adds reasoning transparency layer to any other mode's operation
- **Manual Override**: Use `--introspect` for learning sessions and debugging workflows

---

### 📋 Task Management Mode - Complex Coordination

**Purpose**: Hierarchical task organization with session persistence for multi-step operations.

**Auto-Activation Triggers:**
- Operations requiring >3 coordinated steps
- Multiple file/directory scope (>2 directories OR >3 files)
- Complex dependencies requiring phases and checkpoints
- Quality improvement requests: polish, refine, enhance
- Manual flags: `--task-manage`, `--delegate`

**Behavioral Changes:**
- **Hierarchical Planning**: Breaks complex work into Plan → Phase → Task → Todo structure
- **Session Persistence**: Maintains project context and progress across interruptions
- **Memory Integration**: Uses write_memory/read_memory for state preservation
- **Progress Orchestration**: Coordinates TodoWrite with memory updates for tracking
- **Quality Gates**: Implements systematic validation checkpoints between phases

**Example Experience:**
```
Standard Approach: "I'll implement user authentication..." → Direct implementation
Task Management Approach:
"📋 Multi-Phase Implementation Plan:
 🎯 Phase 1: Security Requirements Analysis (Session 1)
 🎯 Phase 2: API Design & Documentation (Session 2)  
 🎯 Phase 3: Implementation & Testing (Session 3-4)
 🎯 Phase 4: Integration & Validation (Session 5)
 💾 Session persistence: Resume context automatically
 ✓ Quality gates: Validation before each phase transition"
```

**Works Best With:**
- **Analysis →**: Requirements analysis then systematic implementation
- **+ Orchestration**: Task coordination with optimal tool selection
- **+ Introspection**: Transparent reasoning for complex phase decisions

---

### 🎯 Orchestration Mode - Intelligent Tool Selection

**Purpose**: Optimize task execution through intelligent tool routing and parallel coordination.

**Auto-Activation Triggers:**
- Multi-tool operations requiring sophisticated coordination
- Performance constraints (>75% resource usage)
- Parallel execution opportunities (>3 independent files/operations)
- Complex routing decisions with multiple valid tool approaches

**Behavioral Changes:**
- **Intelligent Tool Routing**: Selects optimal MCP servers and native tools for each task type
- **Resource Awareness**: Adapts approach based on system constraints and availability
- **Parallel Optimization**: Identifies independent operations for concurrent execution
- **Performance Focus**: Maximizes speed and effectiveness through coordinated tool usage
- **Adaptive Fallback**: Switches tools gracefully when preferred options are unavailable

**Example Experience:**
```
Standard Approach: Sequential file-by-file analysis and editing
Orchestration Approach:
"🎯 Multi-Tool Coordination Strategy:
 🔍 Phase 1: Serena (semantic analysis) + Sequential (architecture review)
 ⚡ Phase 2: Morphllm (pattern edits) + Magic (UI components) 
 🧪 Phase 3: Playwright (testing) + Context7 (documentation patterns)
 🔄 Parallel execution: 3 tools working simultaneously
 📈 Efficiency gain: 60% faster than sequential approach"
```

**Works Best With:**
- **Task Management →**: Provides tool coordination for complex multi-phase plans
- **+ Token Efficiency**: Optimal tool selection with compressed communication
- **Any Complex Task**: Adds intelligent tool routing to enhance execution

---

### ⚡ Token Efficiency Mode - Compressed Communication

**Purpose**: Achieve 30-50% token reduction through symbol systems while preserving information quality.

**Auto-Activation Triggers:**
- Context usage >75% approaching limits
- Large-scale operations requiring resource efficiency
- User explicit flags: `--uc`, `--ultracompressed`
- Complex analysis workflows with multiple outputs

**Behavioral Changes:**
- **Symbol Communication**: Uses visual symbols for logic flows, status, and technical domains
- **Technical Abbreviation**: Context-aware compression for repeated technical terms
- **Structured Density**: Bullet points, tables, and concise formatting over verbose paragraphs
- **Information Preservation**: Maintains ≥95% information quality despite compression
- **Scannable Format**: Optimizes for quick comprehension and task completion

**Example Experience:**
```
Standard Approach: "The authentication system implementation shows a security vulnerability in the user validation function that needs immediate attention..."
Token Efficient Approach:
"🛡️ Security Alert:
 auth.js:45 → user val() → critical vuln
 📊 Impact: ❌ token bypass possible
 ⚡ Action: fix validation + audit ∵ high sev
 🔧 Est: 2h impl + 1h test"
```

**Works Best With:**
- **Any Mode**: Adds compression layer while preserving mode-specific behaviors
- **Orchestration →**: Compressed tool coordination and status updates
- **Manual Override**: Use `--uc` when context pressure or efficiency is priority

---

### 🎨 Standard Mode - Balanced Default

**Purpose**: Provide clear, professional communication for straightforward development tasks.

**Auto-Activation Triggers:**
- Simple, well-defined tasks without complexity indicators
- Single-file operations with clear requirements
- Basic explanations and standard development workflows
- No other mode triggers detected (default fallback)

**Behavioral Changes:**
- **Professional Communication**: Clear, concise technical language without compression
- **Moderate Detail**: Balanced information depth suitable for most development tasks
- **Standard Tool Selection**: Uses native Gemini capabilities and basic tools
- **Quality Focus**: Maintains code quality without complex orchestration overhead
- **Responsive Adaptation**: Ready to switch to specialized modes when complexity increases

**Example Experience:**
```
Standard Approach: Consistent, professional baseline for all tasks
"I'll implement the login function with proper error handling:
 
 1. Validate user input (email format, password requirements)
 2. Authenticate against database with secure hashing
 3. Generate JWT token with appropriate expiration
 4. Return success response with user data
 
 The implementation will follow security best practices and include comprehensive error handling."
```

**Works Best With:**
- **→ Any Mode**: Serves as baseline that other modes enhance
- **Mode Switching**: Automatically escalates to specialized modes when needed
- **Clarity Priority**: When straightforward communication is more important than optimization

---

## Advanced Usage

### Mode Combinations

**Multi-Mode Workflows:**
```bash
# Discovery → Planning → Implementation
/sg:analyze "microservices architecture" --task-manage
# → Analysis: requirement evaluation and architecture planning
# → Task Management: multi-phase coordination

# Analysis with transparency and efficiency
/sg:analyze legacy-system/ --introspect --uc
# → Introspection: transparent reasoning
# → Token Efficiency: compressed output
```

### Manual Mode Control

**Force Specific Behaviors:**
- `--analyze`: Force requirement analysis for any task
- `--introspect`: Add reasoning transparency to any mode
- `--task-manage`: Enable hierarchical coordination
- `--orchestrate`: Optimize tool selection and parallel execution
- `--uc`: Compress communication for efficiency

**Override Examples:**
```bash
# Force analysis on "clear" requirements
/sg:analyze "user login implementation"

# Add reasoning transparency to debugging
/sg:fix auth-issue --introspect

# Enable task management for simple operations
/sg:update styles.css --task-manage
```

### Mode Boundaries and Priority

**When Modes Activate:**
1. **Complexity Threshold**: >3 files → Task Management
2. **Resource Pressure**: >75% usage → Token Efficiency  
3. **Multi-Tool Need**: Complex analysis → Orchestration
4. **Uncertainty**: Vague requirements → Analysis Mode
5. **Error Recovery**: Problems → Introspection

**Priority Rules:**
- **Safety First**: Quality and validation always override efficiency
- **User Intent**: Manual flags override automatic detection
- **Context Adaptation**: Modes stack based on complexity
- **Resource Management**: Efficiency modes activate under pressure

---

## Real-World Examples

### Complete Workflow Examples

**New Project Development:**
```bash
# Phase 1: Analysis (Analysis Mode provides structured approach)
"I want to build a productivity app"
→ 🤔 Socratic questions about users, features, platform choice
→ 📝 Structured requirements brief

# Phase 2: Planning (Task Management Mode auto-activates)  
/sg:implement "core productivity features"
→ 📋 Multi-phase breakdown with dependencies
→ 🎯 Phase coordination with quality gates

# Phase 3: Implementation (Orchestration Mode coordinates tools)
/sg:develop frontend + backend
→ 🎯 Magic (UI) + Context7 (patterns) + Sequential (architecture)
→ ⚡ Parallel execution optimization
```

**Debugging Complex Issues:**
```bash
# Problem analysis (Introspection Mode auto-activates)
"Users getting intermittent auth failures"
→ 🤔 Transparent reasoning about potential causes
→ 🎯 Hypothesis formation and evidence gathering
→ 💡 Pattern recognition across similar issues

# Systematic resolution (Task Management coordinates)
/sg:fix auth-system --comprehensive
→ 📋 Phase 1: Root cause analysis
→ 📋 Phase 2: Solution implementation  
→ 📋 Phase 3: Testing and validation
```

### Mode Combination Patterns

**High-Complexity Scenarios:**
```bash
# Large refactoring with multiple constraints
/sg:modernize legacy-system/ --introspect --uc --orchestrate
→ 🔍 Transparent reasoning (Introspection)
→ ⚡ Compressed communication (Token Efficiency)  
→ 🎯 Optimal tool coordination (Orchestration)
→ 📋 Systematic phases (Task Management auto-activates)
```

---

## Quick Reference

### Mode Activation Patterns

| Trigger Type | Example Input | Mode Activated | Key Behavior |
|--------------|---------------|----------------|--------------|
| **Vague Request** | "I want to build an app" | 🧠 Analysis | Requirements analysis and suggestions |
| **Complex Scope** | >3 files or >2 directories | 📋 Task Management | Phase coordination |
| **Multi-Tool Need** | Analysis + Implementation | 🎯 Orchestration | Tool optimization |
| **Error Recovery** | "This isn't working as expected" | 🔍 Introspection | Transparent reasoning |
| **Resource Pressure** | >75% context usage | ⚡ Token Efficiency | Symbol compression |
| **Simple Task** | "Fix this function" | 🎨 Standard | Clear, direct approach |

### Manual Override Commands

```bash
# Force specific mode behaviors
/sg:analyze "project concept" # Requirements analysis
/sg:command --introspect    # Reasoning transparency
/sg:command --task-manage   # Hierarchical coordination
/sg:command --orchestrate   # Tool optimization
/sg:command --uc           # Token compression

# Combine multiple modes
/sg:command --introspect --uc    # Transparent + efficient
/sg:command --task-manage --orchestrate  # Coordinated + optimized
```

---

## 🚨 Quick Troubleshooting

### Common Issues (< 2 minutes)
- **Mode not activating**: Use analysis commands: `/sg:analyze`, `--introspect`, `--uc`
- **Wrong mode active**: Check complexity triggers and keywords in request
- **Mode switching unexpectedly**: Normal behavior based on task evolution
- **Performance impact**: Modes optimize performance, shouldn't slow execution
- **Mode conflicts**: Check flag priority rules in [Flags Guide](flags.md)

### Immediate Fixes
- **Force specific mode**: Use explicit commands like `/sg:analyze` or `--task-manage`
- **Reset mode behavior**: Restart Gemini CLI session to reset mode state
- **Check mode indicators**: Look for 🤔, 🎯, 📋 symbols in responses
- **Verify complexity**: Simple tasks use Standard mode, complex tasks auto-switch

### Mode-Specific Troubleshooting

**Analysis Mode Issues:**
```bash
# Problem: Need better requirement analysis
# Solution: Use analysis commands explicitly
/sg:analyze "web app"                          # Analyze requirements
"I have a vague idea about..."                # Use for requirement analysis
"Maybe we could build..."                     # Triggers analysis mode
```

**Task Management Mode Issues:**
```bash
# Problem: Simple tasks getting complex coordination
# Quick Fix: Reduce scope or use simpler commands
/sg:implement "function" --no-task-manage     # Disable coordination
/sg:simple-fix bug.js                         # Use basic commands
# Check if task really is complex (>3 files, >2 directories)
```

**Token Efficiency Mode Issues:**
```bash
# Problem: Output too compressed or unclear
# Quick Fix: Disable compression for clarity
/sg:command --no-uc                           # Disable compression
/sg:command --verbose                         # Force detailed output
# Use when clarity is more important than efficiency
```

**Introspection Mode Issues:**
```bash
# Problem: Too much meta-commentary, not enough action
# Quick Fix: Disable introspection for direct work
/sg:command --no-introspect                   # Direct execution
# Use introspection only for learning and debugging
```

**Orchestration Mode Issues:**
```bash
# Problem: Tool coordination causing confusion
# Quick Fix: Simplify tool usage
/sg:command --no-mcp                          # Native tools only
/sg:command --simple                          # Basic execution
# Check if task complexity justifies orchestration
```

### Error Code Reference

| Mode Error | Meaning | Quick Fix |
|------------|---------|-----------|
| **A001** | Analysis mode needed | Use `/sg:analyze` command for requirement analysis |
| **T001** | Task management overhead | Use `--no-task-manage` for simple tasks |
| **U001** | Token efficiency too aggressive | Use `--verbose` or `--no-uc` |
| **I001** | Introspection mode stuck | Use `--no-introspect` for direct action |
| **O001** | Orchestration coordination failed | Use `--no-mcp` or `--simple` |
| **M001** | Mode conflict detected | Check flag priority rules |
| **M002** | Mode switching loop | Restart session to reset state |
| **M003** | Mode not recognized | Update SuperGemini or check spelling |

### Progressive Support Levels

**Level 1: Quick Fix (< 2 min)**
- Use manual flags to override automatic mode selection
- Check if task complexity matches expected mode behavior
- Try restarting Gemini CLI session

**Level 2: Detailed Help (5-15 min)**
```bash
# Mode-specific diagnostics
/sg:help modes                            # List all available modes
/sg:reflect --type mode-status            # Check current mode state
# Review request complexity and triggers
```
- See [Common Issues Guide](../Reference/common-issues.md) for mode installation problems

**Level 3: Expert Support (30+ min)**
```bash
# Deep mode analysis
SuperGemini diagnose --modes
# Check mode activation patterns
# Review behavioral triggers and thresholds
```
- See [Diagnostic Reference Guide](../Reference/diagnostic-reference.md) for behavioral mode analysis

**Level 4: Community Support**
- Report mode issues at [GitHub Issues](https://github.com/SuperGemini-Org/SuperGemini_Framework/issues)
- Include examples of unexpected mode behavior
- Describe desired vs actual mode activation

### Success Validation

After applying mode fixes, test with:
- [ ] Simple requests use Standard mode (clear, direct responses)
- [ ] Complex requests auto-activate appropriate modes (coordination, reasoning)
- [ ] Manual flags override automatic detection correctly
- [ ] Mode indicators (🤔, 🎯, 📋) appear when expected
- [ ] Performance remains good across different modes

## Quick Troubleshooting (Legacy)
- **Mode not activating** → Use analysis commands: `/sg:analyze`, `--introspect`, `--uc`
- **Wrong mode active** → Check complexity triggers and keywords in request
- **Mode switching unexpectedly** → Normal behavior based on task evolution  
- **Performance impact** → Modes optimize performance, shouldn't slow execution
- **Mode conflicts** → Check flag priority rules in [Flags Guide](flags.md)

## Frequently Asked Questions

**Q: How do I know which mode is active?**
A: Look for these indicators in communication patterns:
- 🤔 Requirements analysis → Analysis Mode
- 🎯 Reasoning transparency → Introspection  
- Phase breakdowns → Task Management
- Tool coordination → Orchestration
- Symbol compression → Token Efficiency

**Q: Can I force specific modes?**
A: Yes, use manual flags to override automatic detection:
```bash
/sg:analyze "project concept" # Requirements analysis
/sg:command --introspect     # Add transparency
/sg:command --task-manage    # Enable coordination
/sg:command --uc            # Compress output
```

**Q: Do modes affect performance?**
A: Modes enhance performance through optimization:
- **Token Efficiency**: 30-50% context reduction
- **Orchestration**: Parallel processing
- **Task Management**: Prevents rework through systematic planning

**Q: Can modes work together?**
A: Yes, modes are designed to complement each other:
- **Task Management** coordinates other modes
- **Token Efficiency** compresses any mode's output
- **Introspection** adds transparency to any workflow

---

## Summary

SuperGemini's 6 behavioral modes create an **intelligent adaptation system** that matches your needs automatically:

- **🧠 Analysis**: Transforms vague ideas into clear implementation plans
- **🔍 Introspection**: Provides transparent reasoning for learning and debugging
- **📋 Task Management**: Coordinates complex multi-step operations
- **🎯 Orchestration**: Optimizes tool selection and parallel execution
- **⚡ Token Efficiency**: Compresses communication while preserving clarity
- **🎨 Standard**: Maintains professional baseline for straightforward tasks

**The key insight**: You don't need to think about modes - they work transparently to enhance your development experience. Simply describe what you want to accomplish, and SuperGemini automatically adapts its approach to match your needs.

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
- [Best Practices](../Reference/quick-start-practices.md) - Mode optimization strategies

**🔧 Expert**
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - Mode implementation details
- [Contributing Code](../Developer-Guide/contributing-code.md) - Extend mode capabilities

**Mode-Specific Guides:**
- **Analysis**: [Requirements Analysis Patterns](../Reference/examples-cookbook.md#requirements)
- **Task Management**: [Session Management Guide](session-management.md)
- **Orchestration**: [MCP Servers Guide](mcp-servers.md)
- **Token Efficiency**: [Performance Optimization](../Reference/quick-start-practices.md#efficiency)