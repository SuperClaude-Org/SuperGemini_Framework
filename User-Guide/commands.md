# SuperGemini Commands Guide 🛠️

## 💡 Don't Overthink It - SuperGemini Tries to Help

SuperGemini provides 21 specialized commands that automatically coordinate domain experts, MCP servers, and behavioral modes based on context. The system intelligently routes tasks to appropriate specialists while maintaining a simple, discoverable interface.

**Auto-Activation Philosophy**: Type `/sg:implement "user auth"` and watch as the security specialist activates, Context7 provides authentication patterns, and quality gates ensure completeness.

**Progressive Discovery**: Use `/sg:index` to explore commands relevant to your current context.

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
/sg:brainstorm "mobile app idea"     # Interactive discovery
/sg:analyze src/                      # Code analysis
/sg:implement "user login"           # Feature implementation
/sg:troubleshoot "API not working"   # Problem solving
/sg:test --coverage                   # Quality assurance
```

**Discovery Pattern:**
1. Use `/sg:index` to explore available commands
2. Try `/sg:brainstorm` for project planning
3. Progress to `/sg:implement` for development
4. Use `/sg:reflect` to validate completion

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

**Selection Strategy**: Commands auto-activate based on keywords, file types, and project context. Use `/sg:select-tool` for optimization recommendations.

## Development Commands 🔨

### /sg:workflow - Implementation Planning

**Purpose**: Generate structured implementation workflows from PRDs and feature requirements

**Usage**:
```bash
/sg:workflow "user authentication system"
/sg:workflow --strategy agile --format markdown
/sg:workflow "payment integration" --depth detailed
```

**Expert Activation**: Architect + Project Manager
**MCP Integration**: Sequential for structured analysis

**Examples**:
```bash
# Basic workflow generation
/sg:workflow "real-time chat feature"

# Agile sprint planning
/sg:workflow "e-commerce cart" --strategy agile --format sprint

# Enterprise architecture
/sg:workflow "microservices migration" --strategy enterprise
```

**Output**: Structured tasks, dependency mapping, time estimates, risk assessment

### /sg:implement - Feature Implementation

**Purpose**: Feature and code implementation with intelligent persona activation and MCP integration

**Usage**:
```bash
/sg:implement "user login with JWT"
/sg:implement --type frontend --framework react
/sg:implement "REST API" --focus security --validate
```

**Expert Activation**: Context-dependent (frontend, backend, security, database)
**MCP Integration**: Context7 (patterns), Magic (UI), Sequential (complex logic)

**Examples**:
```bash
# Full-stack feature
/sg:implement "user registration with email verification"

# Frontend focus
/sg:implement "responsive dashboard" --type frontend

# Security-focused
/sg:implement "OAuth integration" --focus security

# API development
/sg:implement "GraphQL mutations" --type backend --validate
```

**Auto-Activation Patterns**:
- "UI", "component" → Frontend specialist + Magic MCP
- "API", "endpoint" → Backend specialist + Context7
- "auth", "security" → Security specialist + validation gates
- "database", "schema" → Database specialist

---

### /sg:build - Project Building

**Purpose**: Build, compile, and package projects with intelligent error handling and optimization

**Usage**:
```bash
/sg:build
/sg:build --optimize --parallel
/sg:build --target production --fix-errors
```

**Expert Activation**: DevOps specialist
**Build System Detection**: npm, webpack, cargo, maven, gradle, make

**Examples**:
```bash
# Basic build
/sg:build

# Production optimization
/sg:build --target production --optimize

# Parallel compilation
/sg:build --parallel --jobs 4

# Error fixing
/sg:build --fix-errors --verbose
```

**Common Issues & Solutions**:
- **Missing dependencies**: Auto-installs with confirmation
- **Version conflicts**: Suggests resolution strategies
- **Memory issues**: Optimizes build parameters
- **Type errors**: Provides TypeScript fixes

---

### /sg:design - System Design

**Purpose**: Design system architecture, APIs, and component interfaces with comprehensive specifications

**Usage**:
```bash
/sg:design "microservices architecture"
/sg:design --type api --format openapi
/sg:design "database schema" --focus performance
```

**Expert Activation**: Architect + UX Designer (for UI)
**Output Formats**: Markdown, Mermaid diagrams, OpenAPI specs, ERD

**Examples**:
```bash
# System architecture
/sg:design "e-commerce platform architecture"

# API specification
/sg:design "REST API for blog" --type api --format openapi

# Database design
/sg:design "user management schema" --type database

# Component architecture
/sg:design "React component hierarchy" --type frontend
```

**Design Types**:
- **system**: Full architecture with service boundaries
- **api**: REST/GraphQL specifications
- **database**: Schema design with relationships
- **frontend**: Component and state architecture
- **integration**: Service communication patterns

## Analysis Commands 🔍

### /sg:analyze - Code Analysis

**Purpose**: Comprehensive code analysis across quality, security, performance, and architecture domains

**Usage**:
```bash
/sg:analyze src/
/sg:analyze --focus security --depth deep
/sg:analyze . --format report --export html
```

**Expert Activation**: Analyzer + domain specialists based on focus
**Language Support**: Python, JavaScript, TypeScript, Java, C++, Rust, Go, and more

**Examples**:
```bash
# Full project analysis
/sg:analyze .

# Security audit
/sg:analyze src/ --focus security --depth deep

# Performance bottlenecks
/sg:analyze --focus performance --profile

# Architecture review
/sg:analyze --focus architecture --dependencies
```

**Focus Areas**:
- **quality**: Code smells, maintainability, complexity
- **security**: Vulnerabilities, best practices, compliance
- **performance**: Bottlenecks, optimization opportunities
- **architecture**: Dependencies, coupling, design patterns

---

### /sg:troubleshoot - Problem Diagnosis

**Purpose**: Diagnose and resolve issues in code, builds, deployments, and system behavior

**Usage**:
```bash
/sg:troubleshoot "API returns 500 error"
/sg:troubleshoot --logs server.log --focus performance
/sg:troubleshoot --type build --verbose
```

**Expert Activation**: Analyzer + DevOps (for deployment issues)
**MCP Integration**: Sequential for systematic debugging

**Examples**:
```bash
# General issue diagnosis
/sg:troubleshoot "users can't login"

# Build failures
/sg:troubleshoot --type build --fix-suggestions

# Performance issues
/sg:troubleshoot "slow page load" --logs access.log

# Database problems
/sg:troubleshoot "connection timeout" --focus database
```

**Systematic Methodology**:
1. **Symptom Analysis**: Parse error messages and logs
2. **Root Cause Investigation**: Follow dependency chains
3. **Hypothesis Testing**: Validate potential causes
4. **Solution Ranking**: Prioritize fixes by impact/effort
5. **Verification**: Ensure resolution doesn't break other components

---

### /sg:explain - Code & Concept Explanation

**Purpose**: Provide clear explanations of code, concepts, and system behavior with educational clarity

**Usage**:
```bash
/sg:explain "async/await in JavaScript"
/sg:explain src/auth.py --level beginner
/sg:explain --concept "dependency injection" --examples
```

**Teaching Approaches**: Beginner, intermediate, expert levels with progressive detail
**Educational Focus**: Concepts, patterns, best practices, common pitfalls

**Examples**:
```bash
# Code explanation
/sg:explain src/components/UserAuth.jsx

# Concept clarification
/sg:explain "microservices vs monolith" --pros-cons

# Pattern explanation
/sg:explain "observer pattern" --examples react

# Beginner-friendly
/sg:explain "what is REST API" --level beginner --examples
```

**Explanation Styles**:
- **code-walkthrough**: Line-by-line code analysis
- **concept**: High-level explanation with examples
- **pattern**: Design pattern with use cases
- **comparison**: Side-by-side analysis of approaches
- **tutorial**: Step-by-step learning progression

## Quality Commands ✨

### /sg:improve - Code Enhancement

**Purpose**: Apply systematic improvements to code quality, performance, and maintainability

**Usage**:
```bash
/sg:improve src/components/
/sg:improve --type performance --preview
/sg:improve . --focus maintainability --safe-mode
```

**Expert Activation**: Analyzer + Performance Engineer (for performance focus)
**MCP Integration**: Morphllm for pattern-based improvements

**Examples**:
```bash
# General improvements
/sg:improve src/

# Performance optimization
/sg:improve --type performance --measure-impact

# Code quality enhancement
/sg:improve --focus quality --preview --backup

# Safe refactoring
/sg:improve legacy/ --safe-mode --tests-required
```

**Improvement Types**:
- **performance**: Optimization, caching, algorithm improvements
- **quality**: Code smells, readability, maintainability
- **security**: Vulnerability fixes, best practices
- **accessibility**: UI/UX improvements
- **architecture**: Design pattern application

---

### /sg:cleanup - Technical Debt Reduction

**Purpose**: Systematically clean up code, remove dead code, and optimize project structure

**Usage**:
```bash
/sg:cleanup
/sg:cleanup --type imports --organize
/sg:cleanup --dead-code --confirm-before-delete
```

**Expert Activation**: Analyzer
**MCP Integration**: Morphllm for pattern-based cleanup

**Examples**:
```bash
# Full project cleanup
/sg:cleanup --comprehensive --backup

# Import optimization
/sg:cleanup --type imports --sort --remove-unused

# Dead code removal
/sg:cleanup --dead-code --analyze-usage

# File organization
/sg:cleanup --organize-files --follow-conventions
```

**Cleanup Operations**:
- **dead-code**: Unused functions, variables, imports
- **imports**: Sort, deduplicate, organize imports
- **formatting**: Consistent code style
- **files**: Directory organization and naming
- **dependencies**: Remove unused packages

---

### /sg:test - Testing & Quality Assurance

**Purpose**: Execute tests with coverage analysis and automated quality reporting

**Usage**:
```bash
/sg:test
/sg:test --type e2e --coverage
/sg:test --fix --watch
```

**Expert Activation**: QA Specialist
**MCP Integration**: Playwright (for E2E testing)

**Examples**:
```bash
# Run all tests
/sg:test --coverage --report

# Unit tests only
/sg:test --type unit --watch

# E2E browser testing
/sg:test --type e2e --browsers chrome,firefox

# Fix failing tests
/sg:test --fix --preview-changes
```

**Test Types**:
- **unit**: Individual function/component testing
- **integration**: Module interaction testing
- **e2e**: End-to-end browser automation
- **performance**: Load and stress testing
- **accessibility**: WCAG compliance validation

## Documentation Commands 📝

### /sg:document - Documentation Generation

**Purpose**: Generate focused documentation for components, functions, APIs, and features

**Usage**:
```bash
/sg:document src/api/
/sg:document --type api --format openapi
/sg:document . --style technical --audience developers
```

**Expert Activation**: Documentation Specialist
**Documentation Types**: API docs, README, inline comments, user guides

**Examples**:
```bash
# Component documentation
/sg:document src/components/ --inline-comments

# API documentation
/sg:document --type api --format swagger

# User documentation
/sg:document --type user-guide --audience end-users

# Technical documentation
/sg:document --style technical --diagrams
```

**Documentation Styles**:
- **technical**: Developer-focused with code examples
- **user**: End-user guides and tutorials
- **api**: REST/GraphQL API specifications
- **inline**: Code comments and docstrings
- **architectural**: System design documentation

## Project Management Commands 📊

### /sg:estimate - Project Estimation

**Purpose**: Provide development estimates for tasks, features, or projects with intelligent analysis

**Usage**: `/sg:estimate "user authentication system"`, `/sg:estimate --detailed --team-size 3`

**Expert Activation**: Project Manager
**Features**: Time estimates, complexity analysis, resource allocation, risk assessment

**Examples**: Project estimates, sprint planning, resource allocation, timeline forecasting

---

### /sg:task - Project Management

**Purpose**: Execute complex tasks with intelligent workflow management and delegation

**Usage**: `/sg:task "implement payment system"`, `/sg:task --breakdown --priority high`

**Expert Activation**: Project Manager
**MCP Integration**: Serena for task persistence
**Features**: Task breakdown, priority management, cross-session tracking, dependency mapping

---

### /sg:spawn - Meta-System Orchestration

**Purpose**: Meta-system task orchestration with intelligent breakdown and delegation

**Usage**: `/sg:spawn "full-stack e-commerce platform"`, `/sg:spawn --parallel --monitor`

**Expert Activation**: Project Manager + Multiple domain specialists
**Features**: Complex workflow orchestration, parallel execution, progress monitoring, resource management

## Version Control Commands 🔄

### /sg:git - Version Control

**Purpose**: Git operations with intelligent commit messages and workflow optimization

**Usage**: `/sg:git commit "add user auth"`, `/sg:git --smart-messages --conventional`

**Expert Activation**: DevOps specialist
**Features**: Smart commit messages, branch management, conflict resolution, workflow optimization

**Examples**: Intelligent commits, branch strategies, merge conflict resolution, release management

## Utility Commands 🔧

### /sg:index - Command Discovery

**Purpose**: Generate comprehensive project documentation and knowledge base with intelligent organization

**Usage**: `/sg:index`, `/sg:index --category development`, `/sg:index --search "testing"`

**Features**: Command discovery, capability exploration, contextual recommendations, usage patterns

**Examples**: Find relevant commands, explore capabilities, discover usage patterns, get contextual help

---

### /sg:load - Session Context Loading

**Purpose**: Session lifecycle management with Serena MCP integration for project context loading

**Usage**: `/sg:load src/`, `/sg:load --focus architecture`, `/sg:load "previous session"`

**Expert Activation**: Context analysis
**MCP Integration**: Serena for project memory
**Features**: Project structure analysis, context restoration, session initialization, intelligent onboarding

## Session & Intelligence Commands 🧠

### /sg:brainstorm - Interactive Requirements Discovery

**Purpose**: Interactive requirements discovery through Socratic dialogue and systematic exploration

**Usage**: `/sg:brainstorm "mobile app idea"`, `/sg:brainstorm --strategy systematic --depth deep`

**Expert Activation**: Architect + Analyst + PM
**MCP Integration**: Sequential for structured reasoning, Context7 for patterns

**Features**: Socratic dialogue, requirement elicitation, PRD generation, feasibility analysis, creative problem solving

---

### /sg:reflect - Task Reflection & Validation

**Purpose**: Task reflection and validation using Serena MCP analysis capabilities

**Usage**: `/sg:reflect`, `/sg:reflect --type completion`, `/sg:reflect "payment integration"`

**Expert Activation**: Context analysis
**MCP Integration**: Serena for intelligence analysis

**Features**: Progress analysis, completion validation, quality assessment, next steps recommendation

---

### /sg:save - Session Persistence

**Purpose**: Session lifecycle management with Serena MCP integration for session context persistence

**Usage**: `/sg:save "payment-integration-complete"`, `/sg:save --checkpoint --description "auth module done"`

**Expert Activation**: Session management
**MCP Integration**: Serena for context persistence

**Features**: Session checkpointing, context preservation, progress tracking, cross-session continuity

---

### /sg:select-tool - Intelligent Tool Selection

**Purpose**: Intelligent MCP tool selection based on complexity scoring and operation analysis

**Usage**: `/sg:select-tool "implement user auth"`, `/sg:select-tool --analyze-complexity --recommend`

**Expert Activation**: Meta-analysis
**MCP Integration**: All servers for capability assessment

**Features**: Complexity analysis, tool recommendation, MCP coordination, optimization strategies, resource planning

## Command Tips & Patterns 💡

**Effective Flag Combinations:**
```bash
# Development workflow
/sg:analyze --focus quality && /sg:improve --preview && /sg:test --coverage

# Production preparation
/sg:build --optimize --target production && /sg:test --type e2e

# Deep analysis
/sg:analyze --focus security --depth deep --export report

# Safe refactoring
/sg:improve --safe-mode --backup --tests-required
```

**Command Chaining Strategies:**
- **Analysis → Improvement → Testing**: Quality enhancement workflow
- **Brainstorm → Design → Implement**: Feature development lifecycle
- **Load → Analyze → Reflect**: Project onboarding pattern
- **Build → Test → Document**: Release preparation sequence

**Common Workflow Patterns:**

**New Project Onboarding:**
```bash
/sg:load . → /sg:analyze --comprehensive → /sg:document --type overview → /sg:save "project-analyzed"
```

**Feature Development:**
```bash
/sg:brainstorm "feature idea" → /sg:design → /sg:implement → /sg:test → /sg:document
```

**Bug Investigation:**
```bash
/sg:troubleshoot "issue description" → /sg:analyze --focus problem-area → /sg:improve --fix
```

**Pre-Deployment:**
```bash
/sg:test --comprehensive → /sg:analyze --focus security → /sg:build --production → /sg:git commit
```

**Quality Improvement:**
```bash
/sg:analyze --focus quality → /sg:cleanup → /sg:improve → /sg:test → /sg:reflect
```

**Common Issues & Solutions:**

**Command Not Found:**
- Verify SuperGemini installation: `SuperGemini --version`
- Check component installation: `SuperGemini install --list-components`
- Restart Claude Code session

**Slow Performance:**
- Use `--scope file` to limit analysis scope
- Enable specific MCP servers only: `--c7 --seq` instead of `--all-mcp`
- Use `--concurrency 2` to limit parallel operations

**MCP Server Issues:**
- Check server status: `ls ~/.claude/.claude.json`
- Restart with: `SuperGemini install --components mcp --force`
- Use `--no-mcp` for native-only execution

**Scope Management:**
- Use `--scope file|module|project` to control analysis depth
- Limit with `--focus` specific areas
- Use `--dry-run` for preview without execution

---

## Final Notes 📝

**Command Reliability & Evolution:**

SuperGemini commands are actively developed with regular improvements. Core commands (brainstorm, analyze, implement) are production-ready, while emerging commands (spawn, estimate) are rapidly maturing.

**Discovery-Based Learning:**
1. Start with `/sg:index` to explore available commands
2. Use `/sg:brainstorm` for project-specific guidance
3. Try commands in `--dry-run` mode first
4. Progress from simple to complex commands naturally
5. Save successful patterns with `/sg:save`

**Getting Help:**
- In-app: `/sg:index --help` or `/sg:explain "command name"`
- Documentation: [SuperGemini Guides](../README.md)
- Issues: [GitHub Repository](https://github.com/SuperClaude-Org/SuperGemini_Framework/issues)
- Community: [Discussions](https://github.com/SuperClaude-Org/SuperGemini_Framework/discussions)

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

**Your SuperGemini Journey:**

SuperGemini grows with you. Start simple with `/sg:brainstorm` and `/sg:analyze`, then discover advanced capabilities naturally. Each command learns from your usage patterns and becomes more helpful over time.

🚀 **The magic happens when you stop thinking about tools and start focusing on your goals.** SuperGemini handles the orchestration, expert coordination, and quality gates automatically.

**Remember**: There's no wrong way to explore. Use `/sg:index` whenever you need guidance, and don't hesitate to experiment with new commands and flag combinations.
