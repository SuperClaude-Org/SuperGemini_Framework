# SuperClaude Commands Guide 🛠️

## 💡 Don't Overthink It - SuperClaude Tries to Help

SuperClaude provides 21 specialized commands that automatically coordinate domain experts, MCP servers, and behavioral modes based on context. The system intelligently routes tasks to appropriate specialists while maintaining a simple, discoverable interface.

**Auto-Activation Philosophy**: Type `/sc:implement "user auth"` and watch as the security specialist activates, Context7 provides authentication patterns, and quality gates ensure completeness.

**Progressive Discovery**: Use `/sc:index` to explore commands relevant to your current context.

## Core Philosophy

**Core Principles:**
- **Context-Aware Routing**: Commands analyze intent and activate appropriate specialists
- **Safety First**: Dry-run options, backup creation, and validation gates
- **Progressive Enhancement**: Simple tasks stay simple, complex tasks get expert attention
- **Session Persistence**: Long-running workflows maintained across sessions

**Intelligent Activation:**
1. Parse command intent and parameters
2. Analyze complexity and domain requirements
3. Activate relevant specialists (frontend, backend, security, etc.)
4. Connect appropriate MCP servers (Context7, Sequential, Magic)
5. Apply behavioral modes (brainstorming, orchestration, etc.)
6. Execute with quality gates and progress tracking

---

## Quick "Just Try These" List 🚀

**Essential Commands (Start Here):**
```bash
/sc:brainstorm "mobile app idea"     # Interactive discovery
/sc:analyze src/                      # Code analysis
/sc:implement "user login"           # Feature implementation
/sc:troubleshoot "API not working"   # Problem solving
/sc:test --coverage                   # Quality assurance
```

**Discovery Pattern:**
1. Use `/sc:index` to explore available commands
2. Try `/sc:brainstorm` for project planning
3. Progress to `/sc:implement` for development
4. Use `/sc:reflect` to validate completion

---

**Realistic Command Assessment:**

**Highly Mature** (🔥 Production Ready): brainstorm, analyze, implement, troubleshoot
**Well Developed** (✅ Reliable): workflow, design, test, document, git
**Solid Foundation** (🔧 Functional): improve, cleanup, build, load, save
**Emerging** (🌱 Growing): spawn, task, estimate, reflect, select-tool
**Experimental** (🧪 Testing): index, explain

**Expectation**: Core commands deliver consistent results. Emerging commands are improving rapidly with each release.

## Quick Reference 📋

## Command Reference

| Command | Category | Specialists | MCP Servers | Best For |
|---------|----------|-------------|-------------|----------|
| **brainstorm** | Discovery | architect, analyst | sequential, context7 | Requirements exploration |
| **workflow** | Planning | architect, pm | sequential | Implementation planning |
| **implement** | Development | frontend, backend, security | context7, magic | Feature creation |
| **build** | Development | devops | - | Compilation, packaging |
| **design** | Planning | architect, ux | - | System architecture |
| **analyze** | Quality | analyzer | - | Code assessment |
| **troubleshoot** | Debug | analyzer, devops | sequential | Problem diagnosis |
| **explain** | Learning | - | - | Code explanation |
| **improve** | Quality | analyzer | morphllm | Code enhancement |
| **cleanup** | Quality | analyzer | morphllm | Technical debt |
| **test** | Quality | qa-specialist | playwright | Testing, validation |
| **document** | Quality | doc-specialist | - | Documentation |
| **estimate** | Planning | pm | - | Project estimation |
| **task** | Management | pm | serena | Task coordination |
| **spawn** | Management | pm | serena | Complex orchestration |
| **git** | Utility | devops | - | Version control |
| **index** | Utility | - | - | Command discovery |
| **load** | Session | - | serena | Context loading |
| **save** | Session | - | serena | Session persistence |
| **reflect** | Session | - | serena | Task validation |
| **select-tool** | Meta | - | all | Tool optimization |

**Selection Strategy**: Commands auto-activate based on keywords, file types, and project context. Use `/sc:select-tool` for optimization recommendations.

## Development Commands 🔨

### /sc:workflow - Implementation Planning

**Purpose**: Generate structured implementation workflows from PRDs and feature requirements

**Usage**:
```bash
/sc:workflow "user authentication system"
/sc:workflow --strategy agile --format markdown
/sc:workflow "payment integration" --depth detailed
```

**Expert Activation**: Architect + Project Manager
**MCP Integration**: Sequential for structured analysis

**Examples**:
```bash
# Basic workflow generation
/sc:workflow "real-time chat feature"

# Agile sprint planning
/sc:workflow "e-commerce cart" --strategy agile --format sprint

# Enterprise architecture
/sc:workflow "microservices migration" --strategy enterprise
```

**Output**: Structured tasks, dependency mapping, time estimates, risk assessment

### /sc:implement - Feature Implementation

**Purpose**: Feature and code implementation with intelligent persona activation and MCP integration

**Usage**:
```bash
/sc:implement "user login with JWT"
/sc:implement --type frontend --framework react
/sc:implement "REST API" --focus security --validate
```

**Expert Activation**: Context-dependent (frontend, backend, security, database)
**MCP Integration**: Context7 (patterns), Magic (UI), Sequential (complex logic)

**Examples**:
```bash
# Full-stack feature
/sc:implement "user registration with email verification"

# Frontend focus
/sc:implement "responsive dashboard" --type frontend

# Security-focused
/sc:implement "OAuth integration" --focus security

# API development
/sc:implement "GraphQL mutations" --type backend --validate
```

**Auto-Activation Patterns**:
- "UI", "component" → Frontend specialist + Magic MCP
- "API", "endpoint" → Backend specialist + Context7
- "auth", "security" → Security specialist + validation gates
- "database", "schema" → Database specialist

---

### /sc:build - Project Building

**Purpose**: Build, compile, and package projects with intelligent error handling and optimization

**Usage**:
```bash
/sc:build
/sc:build --optimize --parallel
/sc:build --target production --fix-errors
```

**Expert Activation**: DevOps specialist
**Build System Detection**: npm, webpack, cargo, maven, gradle, make

**Examples**:
```bash
# Basic build
/sc:build

# Production optimization
/sc:build --target production --optimize

# Parallel compilation
/sc:build --parallel --jobs 4

# Error fixing
/sc:build --fix-errors --verbose
```

**Common Issues & Solutions**:
- **Missing dependencies**: Auto-installs with confirmation
- **Version conflicts**: Suggests resolution strategies
- **Memory issues**: Optimizes build parameters
- **Type errors**: Provides TypeScript fixes

---

### /sc:design - System Design

**Purpose**: Design system architecture, APIs, and component interfaces with comprehensive specifications

**Usage**:
```bash
/sc:design "microservices architecture"
/sc:design --type api --format openapi
/sc:design "database schema" --focus performance
```

**Expert Activation**: Architect + UX Designer (for UI)
**Output Formats**: Markdown, Mermaid diagrams, OpenAPI specs, ERD

**Examples**:
```bash
# System architecture
/sc:design "e-commerce platform architecture"

# API specification
/sc:design "REST API for blog" --type api --format openapi

# Database design
/sc:design "user management schema" --type database

# Component architecture
/sc:design "React component hierarchy" --type frontend
```

**Design Types**:
- **system**: Full architecture with service boundaries
- **api**: REST/GraphQL specifications
- **database**: Schema design with relationships
- **frontend**: Component and state architecture
- **integration**: Service communication patterns

## Analysis Commands 🔍

### /sc:analyze - Code Analysis

**Purpose**: Comprehensive code analysis across quality, security, performance, and architecture domains

**Usage**:
```bash
/sc:analyze src/
/sc:analyze --focus security --depth deep
/sc:analyze . --format report --export html
```

**Expert Activation**: Analyzer + domain specialists based on focus
**Language Support**: Python, JavaScript, TypeScript, Java, C++, Rust, Go, and more

**Examples**:
```bash
# Full project analysis
/sc:analyze .

# Security audit
/sc:analyze src/ --focus security --depth deep

# Performance bottlenecks
/sc:analyze --focus performance --profile

# Architecture review
/sc:analyze --focus architecture --dependencies
```

**Focus Areas**:
- **quality**: Code smells, maintainability, complexity
- **security**: Vulnerabilities, best practices, compliance
- **performance**: Bottlenecks, optimization opportunities
- **architecture**: Dependencies, coupling, design patterns

---

### /sc:troubleshoot - Problem Diagnosis

**Purpose**: Diagnose and resolve issues in code, builds, deployments, and system behavior

**Usage**:
```bash
/sc:troubleshoot "API returns 500 error"
/sc:troubleshoot --logs server.log --focus performance
/sc:troubleshoot --type build --verbose
```

**Expert Activation**: Analyzer + DevOps (for deployment issues)
**MCP Integration**: Sequential for systematic debugging

**Examples**:
```bash
# General issue diagnosis
/sc:troubleshoot "users can't login"

# Build failures
/sc:troubleshoot --type build --fix-suggestions

# Performance issues
/sc:troubleshoot "slow page load" --logs access.log

# Database problems
/sc:troubleshoot "connection timeout" --focus database
```

**Systematic Methodology**:
1. **Symptom Analysis**: Parse error messages and logs
2. **Root Cause Investigation**: Follow dependency chains
3. **Hypothesis Testing**: Validate potential causes
4. **Solution Ranking**: Prioritize fixes by impact/effort
5. **Verification**: Ensure resolution doesn't break other components

---

### /sc:explain - Code & Concept Explanation

**Purpose**: Provide clear explanations of code, concepts, and system behavior with educational clarity

**Usage**:
```bash
/sc:explain "async/await in JavaScript"
/sc:explain src/auth.py --level beginner
/sc:explain --concept "dependency injection" --examples
```

**Teaching Approaches**: Beginner, intermediate, expert levels with progressive detail
**Educational Focus**: Concepts, patterns, best practices, common pitfalls

**Examples**:
```bash
# Code explanation
/sc:explain src/components/UserAuth.jsx

# Concept clarification
/sc:explain "microservices vs monolith" --pros-cons

# Pattern explanation
/sc:explain "observer pattern" --examples react

# Beginner-friendly
/sc:explain "what is REST API" --level beginner --examples
```

**Explanation Styles**:
- **code-walkthrough**: Line-by-line code analysis
- **concept**: High-level explanation with examples
- **pattern**: Design pattern with use cases
- **comparison**: Side-by-side analysis of approaches
- **tutorial**: Step-by-step learning progression

## Quality Commands ✨

### /sc:improve - Code Enhancement

**Purpose**: Apply systematic improvements to code quality, performance, and maintainability

**Usage**:
```bash
/sc:improve src/components/
/sc:improve --type performance --preview
/sc:improve . --focus maintainability --safe-mode
```

**Expert Activation**: Analyzer + Performance Engineer (for performance focus)
**MCP Integration**: Morphllm for pattern-based improvements

**Examples**:
```bash
# General improvements
/sc:improve src/

# Performance optimization
/sc:improve --type performance --measure-impact

# Code quality enhancement
/sc:improve --focus quality --preview --backup

# Safe refactoring
/sc:improve legacy/ --safe-mode --tests-required
```

**Improvement Types**:
- **performance**: Optimization, caching, algorithm improvements
- **quality**: Code smells, readability, maintainability
- **security**: Vulnerability fixes, best practices
- **accessibility**: UI/UX improvements
- **architecture**: Design pattern application

---

### /sc:cleanup - Technical Debt Reduction

**Purpose**: Systematically clean up code, remove dead code, and optimize project structure

**Usage**:
```bash
/sc:cleanup
/sc:cleanup --type imports --organize
/sc:cleanup --dead-code --confirm-before-delete
```

**Expert Activation**: Analyzer
**MCP Integration**: Morphllm for pattern-based cleanup

**Examples**:
```bash
# Full project cleanup
/sc:cleanup --comprehensive --backup

# Import optimization
/sc:cleanup --type imports --sort --remove-unused

# Dead code removal
/sc:cleanup --dead-code --analyze-usage

# File organization
/sc:cleanup --organize-files --follow-conventions
```

**Cleanup Operations**:
- **dead-code**: Unused functions, variables, imports
- **imports**: Sort, deduplicate, organize imports
- **formatting**: Consistent code style
- **files**: Directory organization and naming
- **dependencies**: Remove unused packages

---

### /sc:test - Testing & Quality Assurance

**Purpose**: Execute tests with coverage analysis and automated quality reporting

**Usage**:
```bash
/sc:test
/sc:test --type e2e --coverage
/sc:test --fix --watch
```

**Expert Activation**: QA Specialist
**MCP Integration**: Playwright (for E2E testing)

**Examples**:
```bash
# Run all tests
/sc:test --coverage --report

# Unit tests only
/sc:test --type unit --watch

# E2E browser testing
/sc:test --type e2e --browsers chrome,firefox

# Fix failing tests
/sc:test --fix --preview-changes
```

**Test Types**:
- **unit**: Individual function/component testing
- **integration**: Module interaction testing
- **e2e**: End-to-end browser automation
- **performance**: Load and stress testing
- **accessibility**: WCAG compliance validation

## Documentation Commands 📝

### /sc:document - Documentation Generation

**Purpose**: Generate focused documentation for components, functions, APIs, and features

**Usage**:
```bash
/sc:document src/api/
/sc:document --type api --format openapi
/sc:document . --style technical --audience developers
```

**Expert Activation**: Documentation Specialist
**Documentation Types**: API docs, README, inline comments, user guides

**Examples**:
```bash
# Component documentation
/sc:document src/components/ --inline-comments

# API documentation
/sc:document --type api --format swagger

# User documentation
/sc:document --type user-guide --audience end-users

# Technical documentation
/sc:document --style technical --diagrams
```

**Documentation Styles**:
- **technical**: Developer-focused with code examples
- **user**: End-user guides and tutorials
- **api**: REST/GraphQL API specifications
- **inline**: Code comments and docstrings
- **architectural**: System design documentation

## Project Management Commands 📊

### /sc:estimate - Project Estimation

**Purpose**: Provide development estimates for tasks, features, or projects with intelligent analysis

**Usage**: `/sc:estimate "user authentication system"`, `/sc:estimate --detailed --team-size 3`

**Expert Activation**: Project Manager
**Features**: Time estimates, complexity analysis, resource allocation, risk assessment

**Examples**: Project estimates, sprint planning, resource allocation, timeline forecasting

---

### /sc:task - Project Management

**Purpose**: Execute complex tasks with intelligent workflow management and delegation

**Usage**: `/sc:task "implement payment system"`, `/sc:task --breakdown --priority high`

**Expert Activation**: Project Manager
**MCP Integration**: Serena for task persistence
**Features**: Task breakdown, priority management, cross-session tracking, dependency mapping

---

### /sc:spawn - Meta-System Orchestration

**Purpose**: Meta-system task orchestration with intelligent breakdown and delegation

**Usage**: `/sc:spawn "full-stack e-commerce platform"`, `/sc:spawn --parallel --monitor`

**Expert Activation**: Project Manager + Multiple domain specialists
**Features**: Complex workflow orchestration, parallel execution, progress monitoring, resource management

## Version Control Commands 🔄

### /sc:git - Version Control

**Purpose**: Git operations with intelligent commit messages and workflow optimization

**Usage**: `/sc:git commit "add user auth"`, `/sc:git --smart-messages --conventional`

**Expert Activation**: DevOps specialist
**Features**: Smart commit messages, branch management, conflict resolution, workflow optimization

**Examples**: Intelligent commits, branch strategies, merge conflict resolution, release management

## Utility Commands 🔧

### /sc:index - Command Discovery

**Purpose**: Generate comprehensive project documentation and knowledge base with intelligent organization

**Usage**: `/sc:index`, `/sc:index --category development`, `/sc:index --search "testing"`

**Features**: Command discovery, capability exploration, contextual recommendations, usage patterns

**Examples**: Find relevant commands, explore capabilities, discover usage patterns, get contextual help

---

### /sc:load - Session Context Loading

**Purpose**: Session lifecycle management with Serena MCP integration for project context loading

**Usage**: `/sc:load src/`, `/sc:load --focus architecture`, `/sc:load "previous session"`

**Expert Activation**: Context analysis
**MCP Integration**: Serena for project memory
**Features**: Project structure analysis, context restoration, session initialization, intelligent onboarding

## Session & Intelligence Commands 🧠

### /sc:brainstorm - Interactive Requirements Discovery

**Purpose**: Interactive requirements discovery through Socratic dialogue and systematic exploration

**Usage**: `/sc:brainstorm "mobile app idea"`, `/sc:brainstorm --strategy systematic --depth deep`

**Expert Activation**: Architect + Analyst + PM
**MCP Integration**: Sequential for structured reasoning, Context7 for patterns

**Features**: Socratic dialogue, requirement elicitation, PRD generation, feasibility analysis, creative problem solving

---

### /sc:reflect - Task Reflection & Validation

**Purpose**: Task reflection and validation using Serena MCP analysis capabilities

**Usage**: `/sc:reflect`, `/sc:reflect --type completion`, `/sc:reflect "payment integration"`

**Expert Activation**: Context analysis
**MCP Integration**: Serena for intelligence analysis

**Features**: Progress analysis, completion validation, quality assessment, next steps recommendation

---

### /sc:save - Session Persistence

**Purpose**: Session lifecycle management with Serena MCP integration for session context persistence

**Usage**: `/sc:save "payment-integration-complete"`, `/sc:save --checkpoint --description "auth module done"`

**Expert Activation**: Session management
**MCP Integration**: Serena for context persistence

**Features**: Session checkpointing, context preservation, progress tracking, cross-session continuity

---

### /sc:select-tool - Intelligent Tool Selection

**Purpose**: Intelligent MCP tool selection based on complexity scoring and operation analysis

**Usage**: `/sc:select-tool "implement user auth"`, `/sc:select-tool --analyze-complexity --recommend`

**Expert Activation**: Meta-analysis
**MCP Integration**: All servers for capability assessment

**Features**: Complexity analysis, tool recommendation, MCP coordination, optimization strategies, resource planning

## Command Tips & Patterns 💡

**Effective Flag Combinations:**
```bash
# Development workflow
/sc:analyze --focus quality && /sc:improve --preview && /sc:test --coverage

# Production preparation
/sc:build --optimize --target production && /sc:test --type e2e

# Deep analysis
/sc:analyze --focus security --depth deep --export report

# Safe refactoring
/sc:improve --safe-mode --backup --tests-required
```

**Command Chaining Strategies:**
- **Analysis → Improvement → Testing**: Quality enhancement workflow
- **Brainstorm → Design → Implement**: Feature development lifecycle
- **Load → Analyze → Reflect**: Project onboarding pattern
- **Build → Test → Document**: Release preparation sequence

**Common Workflow Patterns:**

**New Project Onboarding:**
```bash
/sc:load . → /sc:analyze --comprehensive → /sc:document --type overview → /sc:save "project-analyzed"
```

**Feature Development:**
```bash
/sc:brainstorm "feature idea" → /sc:design → /sc:implement → /sc:test → /sc:document
```

**Bug Investigation:**
```bash
/sc:troubleshoot "issue description" → /sc:analyze --focus problem-area → /sc:improve --fix
```

**Pre-Deployment:**
```bash
/sc:test --comprehensive → /sc:analyze --focus security → /sc:build --production → /sc:git commit
```

**Quality Improvement:**
```bash
/sc:analyze --focus quality → /sc:cleanup → /sc:improve → /sc:test → /sc:reflect
```

**Common Issues & Solutions:**

**Command Not Found:**
- Verify SuperClaude installation: `SuperClaude --version`
- Check component installation: `SuperClaude install --list-components`
- Restart Claude Code session

**Slow Performance:**
- Use `--scope file` to limit analysis scope
- Enable specific MCP servers only: `--c7 --seq` instead of `--all-mcp`
- Use `--concurrency 2` to limit parallel operations

**MCP Server Issues:**
- Check server status: `ls ~/.claude/.claude.json`
- Restart with: `SuperClaude install --components mcp --force`
- Use `--no-mcp` for native-only execution

**Scope Management:**
- Use `--scope file|module|project` to control analysis depth
- Limit with `--focus` specific areas
- Use `--dry-run` for preview without execution

---

## Final Notes 📝

**Command Reliability & Evolution:**

SuperClaude commands are actively developed with regular improvements. Core commands (brainstorm, analyze, implement) are production-ready, while emerging commands (spawn, estimate) are rapidly maturing.

**Discovery-Based Learning:**
1. Start with `/sc:index` to explore available commands
2. Use `/sc:brainstorm` for project-specific guidance
3. Try commands in `--dry-run` mode first
4. Progress from simple to complex commands naturally
5. Save successful patterns with `/sc:save`

**Getting Help:**
- In-app: `/sc:index --help` or `/sc:explain "command name"`
- Documentation: [SuperClaude Guides](../README.md)
- Issues: [GitHub Repository](https://github.com/SuperClaude-Org/SuperClaude_Framework/issues)
- Community: [Discussions](https://github.com/SuperClaude-Org/SuperClaude_Framework/discussions)

## Related Guides

**Learning Progression:**

**🌱 Essential (Week 1)**
- [Quick Start Guide](../Getting-Started/quick-start.md) - Get up and running
- [Installation Guide](../Getting-Started/installation.md) - Setup and configuration
- This Commands Guide - Master core commands

**🌿 Recommended (Week 2-3)**
- [Behavioral Modes](modes.md) - Context optimization
- [Agents Guide](agents.md) - Specialist coordination
- [Examples Cookbook](../Reference/examples-cookbook.md) - Practical patterns

**🌳 Advanced (Month 2+)**
- [MCP Servers](mcp-servers.md) - Enhanced capabilities
- [Best Practices](../Reference/best-practices.md) - Optimization mastery
- [Session Management](session-management.md) - Long-term workflows

**🔧 Expert**
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - System understanding
- [Contributing Code](../Developer-Guide/contributing-code.md) - Framework development

## Command Flags & Options

**Common Flags Across Commands:**

**Scope Control**: `--scope file|module|project|system`
**Focus Areas**: `--focus quality|security|performance|architecture`
**Output Control**: `--format text|json|html|markdown`
**Safety**: `--dry-run`, `--backup`, `--safe-mode`
**Performance**: `--parallel`, `--concurrency N`
**MCP Control**: `--c7`, `--seq`, `--magic`, `--morph`, `--serena`, `--play`

**Expert Activation System:**
- **Context-based**: Keywords trigger appropriate specialists
- **Domain-specific**: Frontend, backend, security, DevOps, QA
- **Progressive**: Simple tasks use fewer experts, complex tasks activate multiple
- **Intelligent routing**: Best expert for each subtask

**MCP Server Integration:**
- **Context7**: Documentation and patterns
- **Sequential**: Multi-step reasoning
- **Magic**: UI component generation
- **Playwright**: Browser automation
- **Morphllm**: Code transformation
- **Serena**: Session and memory management

---

**Your SuperClaude Journey:**

SuperClaude grows with you. Start simple with `/sc:brainstorm` and `/sc:analyze`, then discover advanced capabilities naturally. Each command learns from your usage patterns and becomes more helpful over time.

🚀 **The magic happens when you stop thinking about tools and start focusing on your goals.** SuperClaude handles the orchestration, expert coordination, and quality gates automatically.

**Remember**: There's no wrong way to explore. Use `/sc:index` whenever you need guidance, and don't hesitate to experiment with new commands and flag combinations.
