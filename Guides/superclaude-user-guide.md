# SuperClaude User Guide

## The Simple Truth

**Behind the apparent complexity, SuperClaude is actually simple to use.**

You don't need to learn all the commands, flags, and agents. Just start using it!

SuperClaude has an **intelligent routing system** that tries to figure out what you need:
- Type `/analyze some-code/` → It picks the right analysis tools
- Ask about security → Security expert auto-activates  
- Work on frontend → UI specialist takes over
- Debug something → Investigation mode kicks in

**Learning emerges during use** - you'll naturally discover what works without studying manuals first.

The detailed guides below? They're here **when you want to understand** what just happened or dive deeper. But honestly? Most of the time you can just wing it.

---

**TL;DR**: Install it ([Installation Guide](installation-guide.md)), try `/analyze` or `/build` on your code, watch the magic happen. See [Examples Cookbook](examples-cookbook.md) for copy-paste commands.

---

## Just Start Here

**Want to skip the reading and jump right in?** Here's your 2-minute getting started:

```bash
# Try these commands in Claude Code:
/sc:load                    # Initialize session with project context
/sc:analyze README.md       # SuperClaude analyzes your project
/sc:brainstorm "task app"   # Interactive requirements discovery
/sc:implement user-auth     # Create features and components
/sc:build                   # Smart build with auto-optimization  
/sc:improve messy-file.js   # Clean up code automatically
/sc:save                    # Save session state and insights
```

**What just happened?** SuperClaude automatically:
- Initialized persistent session context
- Picked the right tools for each task
- Activated appropriate specialized agents
- Applied intelligent flags and optimizations
- Provided evidence-based suggestions
- Saved insights for future sessions

**See how easy that was?** No studying required - SuperClaude figures out the complexity so you don't have to.

Want to understand how it works? Keep reading. Want to just keep experimenting? Go for it!

---

## Welcome & Overview

### What is SuperClaude Really?

SuperClaude makes Claude Code smarter for development work. Instead of generic responses, you get specialized help from different agents (security, performance, frontend, etc.) who know their stuff, plus session persistence and behavioral intelligence.

**The honest truth**: SuperClaude v4.0.0 represents a major architectural evolution with new session lifecycle management and behavioral modes. It's significantly more capable than v3, with better context management and intelligent agent coordination.

**The neat part?** You don't need to manage any of this complexity. Just use normal commands like `/analyze` or `/build` and SuperClaude usually figures out which experts to involve and what tools to use.

### What SuperClaude Adds

**21 Specialized Commands** ([Commands Guide](commands-guide.md))
- **Planning tools**: `/estimate`, `/task`, `/brainstorm`
- **Development tools**: `/implement`, `/build`, `/design`, `/select-tool`
- **Analysis tools**: `/analyze`, `/troubleshoot`, `/explain`
- **Quality tools**: `/improve`, `/cleanup`, `/test`
- **Session tools**: `/load`, `/save`, `/reflect` ([Session Management Guide](session-management.md))
- **Plus utilities** for documentation, git, deployment, and more

**13 Specialized Agents** *(that know when to jump in)* ([Agents Guide](agents-guide.md))
- AI agents that adapt behavior for different domains
- **Auto-activate based on your requests** (security agent for security tasks, etc.)
- Manual control available, but usually not needed  

**6 MCP Server Integrations** *(smart external tools)*
- **Context7**: Official library documentation lookup
- **Sequential**: Complex multi-step analysis  
- **Magic**: Modern UI component generation
- **Playwright**: Browser automation and testing
- **Morphllm**: Intelligent file editing
- **Serena**: Semantic code analysis and memory
- **Auto-connects when needed** - you don't manage this stuff

**5 Behavioral Modes** *(intelligent adaptation)* ([Behavioral Modes Guide](behavioral-modes-guide.md))
- **Brainstorming Mode**: Interactive requirements discovery
- **Introspection Mode**: Meta-cognitive analysis and debugging
- **Task Management Mode**: Multi-layer orchestration and systematic delegation
- **Token Efficiency Mode**: Smart compression and optimization
- **Orchestration Mode**: Intelligent tool selection and resource efficiency
- **Auto-activate based on context** - you don't configure them

**Session Lifecycle System** *(persistent intelligence)*
- Session initialization with `/sc:load`
- Persistent context and memory across sessions
- Automatic checkpoints and progress tracking
- Session reflection and insights with `/sc:reflect`
- **Cross-session learning** - SuperClaude remembers and improves

### How It Works

**The simple version**: You type something like `/analyze auth.js` and SuperClaude figures out the rest.

**The slightly more detailed version**:

1. **Smart routing** - Analyzes what you're asking for
2. **Auto-expert selection** - Picks the right specialist (security, performance, etc.)
3. **Tool coordination** - Connects to external systems when helpful
4. **Quality assurance** - Makes sure suggestions are solid

**You don't see any of this complexity** - it just feels like Claude got way smarter about development stuff.

---

## Core Components Overview

### Commands: Your Toolkit

Commands are specialized tools that handle specific types of development work. Instead of generic "help me with this," you get purpose-built tools for different scenarios.

**Development**: `/build`, `/design`, `/implement`
**Analysis**: `/analyze`, `/troubleshoot`, `/explain`  
**Quality**: `/improve`, `/cleanup`, `/test`
**Session Management**: `/load`, `/save`, `/reflect`
**Planning & Discovery**: `/brainstorm`, `/estimate`, `/task`
**Utilities**: `/document`, `/git`, `/select-tool`, `/spawn`, `/index`

Each command auto-activates appropriate agents and integrates with relevant MCP servers.

### Agents: AI Specialists

13 specialized agents with domain expertise that activate automatically based on your requests:

**🏗️ System Architect** - Architecture design and technical decisions  
**🛡️ Security Engineer** - Security analysis and vulnerability assessment  
**⚡ Performance Engineer** - Optimization and scalability  
**🎨 Frontend Architect** - UI/UX and client-side development  
**⚙️ Backend Architect** - Server-side architecture and APIs  
**🔍 Root Cause Analyst** - Debugging and problem investigation  
**✨ Quality Engineer** - Code quality and testing strategies  
**📚 Learning Guide** - Educational explanations and mentoring  
**📋 Requirements Analyst** - Requirements discovery and PRDs  
**🛠️ DevOps Architect** - Infrastructure and deployment  
**🔧 Refactoring Expert** - Code improvement and technical debt  
**🐍 Python Expert** - Python-specific development  
**📝 Technical Writer** - Documentation and communication

### MCP Servers: External Capabilities

6 specialized external tools that enhance SuperClaude's capabilities:

**Context7** - Official documentation lookup for libraries and frameworks  
**Sequential** - Complex multi-step reasoning and analysis  
**Magic** - Modern UI component generation from 21st.dev patterns  
**Playwright** - Browser automation and E2E testing  
**Morphllm** - Pattern-based code editing with token optimization  
**Serena** - Semantic code understanding and project memory  

### Behavioral Modes: Adaptive Intelligence

5 modes that automatically adapt SuperClaude's behavior:

**Brainstorming Mode** - Activates for vague requests, guides requirement discovery  
**Introspection Mode** - Activates for error recovery and complex problem solving  
**Task Management Mode** - Activates for multi-step operations and large scope  
**Orchestration Mode** - Activates for multi-tool operations and performance needs  
**Token Efficiency Mode** - Activates for large operations and resource constraints  

---

## Getting Started Workflows

### Your First Session

```bash
# 1. Initialize session context
/sc:load

# 2. Explore your project
/sc:analyze .

# 3. Try interactive discovery
/sc:brainstorm "improve user experience"

# 4. Save your session
/sc:save
```

### Common Development Tasks

**Code Analysis**
```bash
/sc:analyze auth.js --focus security
/sc:explain complex-algorithm.py  
/sc:troubleshoot failing-tests/
```

**Feature Development**
```bash
/sc:brainstorm "user dashboard"
/sc:design user-dashboard --type component
/sc:implement user-dashboard
/sc:test user-dashboard
```

**Code Quality**
```bash
/sc:improve legacy-code/
/sc:cleanup technical-debt/
/sc:build --optimize
```

### Working with Different Domains

**Frontend Development**
- Use `/sc:design` for UI components
- Magic MCP auto-activates for modern patterns
- Frontend agent provides specialized guidance

**Backend Development** 
- Use `/sc:analyze` for API design
- Context7 MCP provides framework documentation
- Backend agent handles server-side architecture

**Security Analysis**
- Use `/sc:analyze --focus security`
- Security agent auto-activates
- Sequential MCP provides systematic analysis

---

## Key Takeaways

### SuperClaude's Core Value

SuperClaude v4.0.0 transforms Claude Code into an intelligent development partner through:
- **21 specialized commands** including session management and brainstorming
- **13 expert agents** with enhanced coordination and specialization  
- **5 behavioral modes** that adapt intelligently to different work types
- **Session persistence** that remembers and learns across sessions
- **Advanced orchestration** with quality gates
- **6 MCP servers** including intelligent editing and semantic analysis

### The Power is in the Coordination

SuperClaude's power comes from intelligent system integration:
- **Session lifecycle** maintains context across all interactions
- **Behavioral modes** adapt automatically to different work patterns
- **Agents coordinate** seamlessly for multi-domain problems  
- **MCP servers** integrate intelligently based on task requirements
- **Quality gates** ensure consistent, reliable outcomes
- **Memory system** enables continuous learning and improvement

### Start Simple, Scale Intelligently

The best approach to SuperClaude v4.0.0 is progressive:
1. **Initialize sessions** with `/sc:load` to experience persistent context
2. **Try brainstorming** with `/sc:brainstorm` for interactive discovery
3. **Trust behavioral modes** to adapt automatically to your work patterns
4. **Use session persistence** with `/sc:save` to build continuous context
5. **Experiment with advanced features** like multi-layer orchestration

### When to Use SuperClaude

**SuperClaude v4.0.0 Excels At:**
- Persistent development workflows with cross-session context
- Interactive requirements discovery and project brainstorming
- Intelligent code analysis with semantic understanding
- Adaptive task management with behavioral intelligence
- Cross-domain coordination requiring multiple agents and modes
- Session-based learning that builds project understanding over time

**When to Use Standard Claude Code:**
- Simple questions that don't need specialized tools
- Creative writing or non-technical content creation
- General research topics outside software development
- Open-ended ideation without specific implementation needs

---

## Related Guides

**🚀 Getting Started (Essential)**
- [Installation Guide](installation-guide.md) - Complete setup and configuration  
- [Examples Cookbook](examples-cookbook.md) - Copy-paste examples for common tasks
- [Troubleshooting Guide](troubleshooting-guide.md) - Quick solutions when things go wrong

**📚 Core Knowledge (Recommended)**
- [Commands Guide](commands-guide.md) - All 21 commands with real examples
- [Agents Guide](agents-guide.md) - 13 AI specialists and when they help
- [Behavioral Modes Guide](behavioral-modes-guide.md) - How SuperClaude adapts automatically
- [Flags Guide](flags-guide.md) - Manual control and optimization options

**💼 Practical Application (Next Steps)**
- [Session Management Guide](session-management.md) - Persistent context across sessions
- [Best Practices Guide](best-practices.md) - Proven patterns for maximum effectiveness

**🔧 Advanced Understanding (Optional)**
- [Technical Architecture Guide](technical-architecture.md) - Internal system design

**📖 Reading Path Recommendations:**

*For New Users*: Installation → Examples Cookbook → Commands → Start Building!

*For Power Users*: Best Practices → Session Management → Technical Architecture

*When Stuck*: Troubleshooting → Examples Cookbook → Ask in Issues

Remember: You can use SuperClaude effectively without reading any of these guides. They're here when you get curious about how it works or want to unlock advanced capabilities!