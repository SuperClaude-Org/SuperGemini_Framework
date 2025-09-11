# SuperGemini Quick Start Guide

> **Command Context**: This guide uses both **Terminal Commands** (for installation) and **Gemini CLI Commands** (`/sg:` for development). See sections below for where to run each type.

## The Simple Truth

SuperGemini transforms Gemini CLI into a structured development framework with just one installation command. Behind the simple interface, intelligent routing automatically selects the right tools, activates domain experts, and coordinates complex workflows.

**5-Minute Start**: Install → Try `/sg:analyze` → Watch the magic happen.

## Just Start Here

### 🖥️ Installation (2 minutes) - Run in Terminal
```bash
# Recommended: pipx (isolated environment)
pipx install SuperGemini && SuperGemini install

# Alternative: pip (traditional)
pip install SuperGemini && SuperGemini install
```

### 💬 First Commands (3 minutes) - Type in Gemini CLI
```
# Interactive project discovery (brainstorm mode)
/sg:analyze "web app for task management"

# Analyze existing code
/sg:analyze src/

# Generate implementation plan
/sg:workflow "add user authentication"
```

**What Happens Automatically:**
- Domain experts activate based on context (frontend, backend, security)
- MCP servers connect for enhanced capabilities
- Behavioral modes adapt to task complexity
- Progress tracking and session management

---

## What is SuperGemini Really?

SuperGemini is a meta-programming framework that enhances Gemini CLI with:

**18 Slash Commands** for workflow automation (/sg:analyze, /sg:implement, /sg:workflow)
**13 AI Specialists** with domain expertise (architect, security, frontend, backend)
**6 Behavioral Modes** for different contexts (brainstorming, introspection, orchestration)
**6 MCP Servers** for enhanced capabilities (Context7, Sequential, Magic, Playwright)

**Version 4.0** delivers production-ready workflow orchestration with intelligent agent coordination and session persistence.

## How It Works

**User Experience:**
You type `/sg:implement "user login"` → SuperGemini analyzes requirements → activates security specialist → connects to Context7 for authentication patterns → generates complete implementation with tests.

**Technical Workflow:**
1. **Command Parser** analyzes intent and complexity
2. **Agent Router** selects appropriate domain specialists
3. **MCP Coordinator** activates relevant servers (Context7, Sequential, etc.)
4. **Session Manager** tracks progress and maintains context
5. **Quality Gates** ensure completeness and validation

---

## First Steps Workflow

**First Session Pattern:**
```bash
# 1. Project Discovery (brainstorm mode)
/sg:analyze "e-commerce mobile app"

# 2. Load Context (existing projects)
/sg:load src/

# 3. Analyze Current State
/sg:analyze --focus architecture

# 4. Plan Implementation
/sg:workflow "add payment integration"

# 5. Implement Features
/sg:implement "Stripe payment flow"

# 6. Validate Quality
/sg:test --coverage

# 7. Save Session
/sg:save "payment-integration-complete"
```

**Domain-Specific Workflows:**
- **Frontend**: Magic MCP activates for UI components
- **Backend**: Security specialist ensures proper validation
- **DevOps**: Infrastructure specialist handles deployment
- **Testing**: QA specialist creates comprehensive test suites

---

## Key Takeaways

### SuperGemini's Core Value

SuperGemini transforms Gemini CLI from a general-purpose AI assistant into a **specialized development framework** with:

- **Systematic Workflows** instead of ad-hoc requests
- **Domain Expertise** through specialized agents
- **Tool Coordination** with MCP server integration
- **Session Persistence** for long-term project continuity
- **Quality Assurance** through built-in validation gates

### The Power is in the Coordination

**Intelligent Coordination Benefits:**

- **Auto-activation**: Right tools for the right tasks
- **Multi-agent Workflows**: Frontend + Backend + Security working together
- **Context Preservation**: No losing track of complex projects
- **Parallel Processing**: Multiple operations running simultaneously
- **Progressive Enhancement**: Simple tasks stay simple, complex tasks get expert attention

### Start Simple, Scale Intelligently

**Learning Path:**

**Week 1**: Master core commands (`/sg:analyze`, `/sg:implement`, `/sg:workflow`)
**Week 2**: Explore behavioral modes and flag combinations
**Week 3**: Configure MCP servers for enhanced capabilities
**Week 4**: Create custom workflows and session management patterns

**Usage Recommendations:**
- Start with simple commands and let complexity emerge naturally
- Use `/sg:index` to discover relevant commands for your context
- Enable MCP servers gradually as you understand their benefits
- Save successful patterns with `/sg:save` for reuse

### When to Use SuperGemini

**Use SuperGemini When:**
- Building software projects (any language/framework)
- Need systematic workflows and quality gates
- Working on complex, multi-component systems
- Require session persistence across development cycles
- Want specialized domain expertise (security, performance, etc.)

**Use Standard Gemini CLI When:**
- Simple questions or explanations
- One-off coding tasks
- Learning programming concepts
- Quick prototypes or experiments

**SuperGemini Excellence**: Multi-step development workflows with quality requirements

---

## Next Steps

**Learning Progression:**

**🌱 Beginner (First Week)**
- [Installation Guide](installation.md) - Get set up
- [Commands Reference](../User-Guide/commands.md) - Learn core commands
- [Examples Cookbook](../Reference/examples-cookbook.md) - Try practical examples

**🌿 Intermediate (Growing Skills)**
- [Behavioral Modes](../User-Guide/modes.md) - Optimize for context
- [Agents Guide](../User-Guide/agents.md) - Understand specialists
- [Session Management](../User-Guide/session-management.md) - Long-term projects

**🌲 Advanced (Expert Usage)**
- [MCP Servers](../User-Guide/mcp-servers.md) - Enhanced capabilities
- [Best Practices](../Reference/quick-start-practices.md) - Optimization strategies
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - Deep understanding

**🚑 Support**
- [Troubleshooting](../Reference/troubleshooting.md) - Problem solving
- [Contributing](../Developer-Guide/contributing-code.md) - Join development