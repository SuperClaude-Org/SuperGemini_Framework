# SuperGemini Agents Guide 🤖

## Overview

SuperGemini V4 Beta features 13 specialized domain expert agents that automatically activate based on your task context. These intelligent agents replace the previous persona system with more advanced, focused capabilities that provide expert-level assistance across all aspects of software development.

**The simple truth**: You don't need to pick agents or memorize what they do. SuperGemini automatically brings in the right experts for each situation!

**Here's what actually happens:**
- You type `/analyze auth.js` → Security auditor automatically jumps in 🛡️
- You work on React components → Frontend specialist often takes over 🎨  
- You debug performance issues → Performance optimizer often helps ⚡
- You write documentation → Technical writer usually helps out ✍️

**It's like having a smart team** that knows when to jump in and help, without you managing who does what.

## 🚀 Just Try These (No Agent Knowledge Required)

```bash
# These automatically activate the right experts:
/sg:analyze payment-system/         # → Security + backend experts auto-activate
/sg:build react-app/               # → Frontend specialist takes over  
/sg:improve slow-queries.sql       # → Performance optimizer jumps in
/sg:troubleshoot "auth failing"    # → Root cause analyzer + security expert coordinate
/sg:brainstorm "task manager app"  # → Brainstorm-PRD agent guides discovery
```

**See the pattern?** You focus on what you want to do, SuperGemini figures out who should help.

---

## The SuperGemini Agent Team 👥

### Core Development Agents 🔧

#### 🐍 `python-ultimate-expert` - Master Python Architect
**What they do**: Production-ready Python development with SOLID principles, clean architecture, and comprehensive testing

**Auto-activation triggers**:
- Python file detection (.py, requirements.txt, pyproject.toml)
- Keywords: "python", "django", "fastapi", "flask", "asyncio"
- Python-specific patterns and frameworks

**Specialized capabilities**:
- **Production Standards**: SOLID principles, clean architecture, domain-driven design
- **Testing Excellence**: TDD with 95%+ coverage, pytest, property-based testing
- **Security First**: OWASP compliance, input validation, secrets management
- **Performance Optimization**: Profiling, async programming, memory management
- **Modern Tooling**: uv/poetry, black, ruff, mypy, pre-commit hooks

**Example use cases**:
```bash
/sg:build python-api --focus security     # → Production-ready FastAPI with security
/sg:improve legacy-python/ --focus quality # → Refactor to SOLID principles
/sg:test python-service/ --comprehensive   # → Full test suite with coverage
```

**Integration with MCP servers**:
- **Context7**: Python framework documentation and best practices
- **Sequential**: Complex architecture analysis and system design
- **Magic**: Python web framework UI components

---

#### ⚙️ `backend-engineer` - Reliable Systems Specialist
**What they do**: Server-side development, APIs, databases, and reliability engineering

**Auto-activation triggers**:
- Keywords: "API", "database", "server", "microservices", "reliability"
- Backend file patterns (server.js, app.py, database schemas)
- Infrastructure and service-related tasks

**Specialized capabilities**:
- **Reliability First**: 99.9% uptime targets, fault tolerance, graceful degradation
- **API Excellence**: RESTful design, GraphQL, comprehensive validation
- **Database Mastery**: Schema design, query optimization, ACID compliance
- **Security Implementation**: Authentication, authorization, zero trust architecture
- **Observable Systems**: Structured logging, monitoring, alerting

**Quality standards**:
- Primary: 99.9% uptime with zero data loss tolerance
- Secondary: <200ms API response time, comprehensive error handling
- Success: Fault-tolerant systems meeting all reliability requirements

**Example use cases**:
```bash
/sg:design user-management-api        # → Reliable API with proper auth
/sg:optimize database-queries/        # → Performance tuning and indexing
/sg:implement payment-processing      # → Secure, reliable payment system
```

**Integration with MCP servers**:
- **Context7**: Backend framework patterns and database documentation
- **Sequential**: System architecture analysis and reliability planning
- **Serena**: Cross-service dependency analysis and integration testing

---

#### 🎨 `frontend-specialist` - Accessible UI Expert
**What they do**: User interface development with focus on accessibility, performance, and user experience

**Auto-activation triggers**:
- Keywords: "component", "responsive", "accessibility", "UI", "UX", "react", "vue"
- Frontend file patterns (.jsx, .vue, .component.ts, CSS files)
- User interface and design-related tasks

**Specialized capabilities**:
- **Accessibility by Default**: WCAG 2.1 AA compliance, screen reader support
- **Performance Budget**: Core Web Vitals optimization, bundle size management
- **Responsive Design**: Mobile-first approach, progressive enhancement
- **Modern Frameworks**: React, Vue, Angular with best practices
- **Design Systems**: Component libraries, design tokens, consistent patterns

**Quality standards**:
- Primary: WCAG 2.1 AA compliance (100%) with Core Web Vitals in green zone
- Secondary: <3s load time on 3G networks, zero accessibility errors
- Success: Accessible, performant UI meeting all compliance standards

**Example use cases**:
```bash
/sg:build dashboard-components/       # → Accessible React components
/sg:improve --focus accessibility ui/ # → WCAG compliance and optimization
/sg:optimize bundle-performance       # → Core Web Vitals improvement
```

**Integration with MCP servers**:
- **Magic**: Advanced UI component generation and design system integration
- **Context7**: Frontend framework documentation and accessibility patterns
- **Playwright**: Cross-browser testing and visual regression detection

---

#### 🚀 `devops-engineer` - Infrastructure Automation Expert
**What they do**: Infrastructure automation, deployment pipelines, monitoring, and reliability engineering

**Auto-activation triggers**:
- Keywords: "deploy", "infrastructure", "CI/CD", "docker", "kubernetes", "monitoring"
- DevOps file patterns (Dockerfile, docker-compose.yml, .github/workflows)
- Infrastructure and deployment-related tasks

**Specialized capabilities**:
- **Infrastructure as Code**: Terraform, CloudFormation, automated provisioning
- **CI/CD Excellence**: GitHub Actions, automated testing, deployment pipelines
- **Container Orchestration**: Docker, Kubernetes, microservices deployment
- **Monitoring & Observability**: Logging, metrics, alerting, performance tracking
- **Security Operations**: Security scanning, compliance, vulnerability management

**Quality standards**:
- Primary: Zero-downtime deployments with automated rollback capability
- Secondary: Infrastructure as code, comprehensive monitoring coverage
- Success: Fully automated, observable, secure deployment infrastructure

**Example use cases**:
```bash
/sg:deploy production-app             # → Zero-downtime deployment pipeline
/sg:build monitoring-stack           # → Comprehensive observability setup
/sg:secure infrastructure/           # → Security hardening and compliance
```

**Integration with MCP servers**:
- **Context7**: DevOps tools documentation and best practices
- **Sequential**: Infrastructure architecture analysis and optimization
- **Playwright**: Deployment validation and smoke testing

### Analysis & Quality Agents 🔍

#### 🛡️ `security-auditor` - Threat Modeling Expert
**What they do**: Security vulnerability identification, threat modeling, and compliance verification

**Auto-activation triggers**:
- Keywords: "security", "vulnerability", "auth", "compliance", "penetration", "audit"
- Security-sensitive code patterns (authentication, data handling, API endpoints)
- Security assessment and review requests

**Specialized capabilities**:
- **Vulnerability Assessment**: OWASP Top 10, CWE compliance, penetration testing mindset
- **Threat Modeling**: Attack vector analysis, security risk assessment
- **Compliance Verification**: Industry standards, regulatory requirements
- **Security Architecture**: Zero trust principles, defense in depth
- **Remediation Guidance**: Specific fixes with security rationale

**Quality standards**:
- Primary: Zero critical vulnerabilities in production with OWASP Top 10 compliance
- Secondary: All findings include remediation steps, clear severity classifications
- Success: Complete security assessment with actionable remediation plan

**Example use cases**:
```bash
/sg:scan --focus security auth-system/ # → Comprehensive security audit
/sg:analyze payment-flow --security     # → Threat modeling and risk assessment
/sg:improve --fix vulnerabilities api/  # → Security hardening and fixes
```

**Integration with MCP servers**:
- **Context7**: Security framework documentation and compliance standards
- **Sequential**: Complex threat modeling and vulnerability chain analysis
- **Playwright**: Security testing and penetration validation

---

#### ⚡ `performance-optimizer` - Bottleneck Detection Expert
**What they do**: Performance analysis, optimization, and bottleneck identification across all system layers

**Auto-activation triggers**:
- Keywords: "performance", "optimization", "slow", "bottleneck", "latency", "memory"
- Performance-related issues and optimization requests
- System profiling and benchmarking tasks

**Specialized capabilities**:
- **Bottleneck Identification**: Systematic performance profiling and analysis
- **Optimization Strategy**: Database queries, application code, infrastructure tuning
- **Performance Monitoring**: Metrics collection, alerting, continuous optimization
- **Load Testing**: Capacity planning, stress testing, scalability analysis
- **Resource Management**: Memory optimization, CPU utilization, I/O efficiency

**Quality standards**:
- Primary: Measurable performance improvements with baseline metrics
- Secondary: Comprehensive profiling, optimization rationale documentation
- Success: Performance targets met with sustainable optimization strategies

**Example use cases**:
```bash
/sg:analyze --focus performance slow-api/ # → Bottleneck identification and fixes
/sg:optimize database-queries/            # → Query performance tuning
/sg:benchmark application-performance     # → Load testing and capacity planning
```

**Integration with MCP servers**:
- **Sequential**: Complex performance analysis and systematic optimization
- **Context7**: Performance optimization patterns and best practices
- **Playwright**: Performance testing and real-world load simulation

---

#### 🔍 `root-cause-analyzer` - Systematic Investigation Expert
**What they do**: Debugging, root cause analysis, and evidence-based problem solving

**Auto-activation triggers**:
- Keywords: "debug", "investigate", "troubleshoot", "root cause", "analyze", "broken"
- Bug reports, system failures, and complex problem investigation
- Unknown system behavior and mysterious issues

**Specialized capabilities**:
- **Systematic Investigation**: Evidence collection, hypothesis testing, pattern analysis
- **Debug Methodology**: Step-by-step problem isolation and reproduction
- **Root Cause Identification**: Deep analysis beyond surface symptoms
- **Solution Validation**: Testing fixes and preventing regression
- **Knowledge Transfer**: Documenting findings and prevention strategies

**Quality standards**:
- Primary: Evidence-based conclusions with reproducible findings
- Secondary: Systematic investigation methodology, complete analysis
- Success: Root cause identified with validated solution and prevention

**Example use cases**:
```bash
/sg:troubleshoot "payment processing fails randomly" # → Systematic investigation
/sg:analyze mysterious-bug/                          # → Evidence-based debugging
/sg:investigate system-outage-logs/                  # → Root cause analysis
```

**Integration with MCP servers**:
- **Sequential**: Complex problem decomposition and systematic analysis
- **Serena**: Code analysis and symbol-level investigation
- **Context7**: Debugging patterns and troubleshooting methodologies

---

#### 🧪 `qa-specialist` - Quality Assurance Expert
**What they do**: Testing strategy, quality gates, edge case detection, and comprehensive validation

**Auto-activation triggers**:
- Keywords: "test", "quality", "validation", "QA", "edge case", "coverage"
- Testing-related tasks and quality assurance requests
- Quality gate implementation and validation processes

**Specialized capabilities**:
- **Testing Strategy**: Comprehensive test planning, risk-based testing
- **Quality Assurance**: Edge case identification, failure mode analysis
- **Test Automation**: Unit, integration, and end-to-end testing frameworks
- **Quality Gates**: Automated quality validation and compliance checking
- **Risk Assessment**: Quality risk analysis and mitigation strategies

**Quality standards**:
- Primary: Comprehensive test coverage with edge case validation
- Secondary: Automated quality gates, risk-based testing priorities
- Success: Quality assurance processes preventing defects in production

**Example use cases**:
```bash
/sg:test --comprehensive user-service/     # → Full testing strategy and implementation
/sg:validate --quality critical-features/  # → Quality gate implementation
/sg:analyze --focus testing legacy-code/   # → Testing strategy for existing code
```

**Integration with MCP servers**:
- **Playwright**: End-to-end testing and cross-browser validation
- **Sequential**: Complex testing strategy and quality analysis
- **Context7**: Testing framework documentation and QA best practices

### Architecture & Code Quality Agents 🏗️

#### 🏗️ `system-architect` - Large-Scale Design Expert
**What they do**: System architecture, design patterns, and scalability planning

**Auto-activation triggers**:
- Keywords: "architecture", "design", "scalability", "system", "patterns", "microservices"
- Large-scale system design and architectural decisions
- Cross-system integration and design pattern implementation

**Specialized capabilities**:
- **System Architecture**: Large-scale system design, microservices architecture
- **Design Patterns**: Architectural patterns, design principle application
- **Scalability Planning**: Performance at scale, distributed system design
- **Integration Design**: Cross-system integration, API design, service mesh
- **Technology Strategy**: Technology selection, architectural decision records

**Quality standards**:
- Primary: Scalable, maintainable architecture supporting business requirements
- Secondary: Design pattern adherence, comprehensive architectural documentation
- Success: Architecture enabling development team productivity and system reliability

**Example use cases**:
```bash
/sg:design microservices-architecture     # → System architecture and service design
/sg:analyze --focus architecture system/  # → Architectural review and improvement
/sg:plan scalability-improvements         # → Scaling strategy and implementation
```

**Integration with MCP servers**:
- **Sequential**: Complex architectural analysis and design validation
- **Context7**: Architectural patterns and framework documentation
- **Serena**: Cross-system analysis and dependency management

---

#### 🔄 `code-refactorer` - Clean Code Specialist
**What they do**: Code quality improvement, technical debt management, and clean code practices

**Auto-activation triggers**:
- Keywords: "refactor", "cleanup", "quality", "technical debt", "maintainability"
- Code improvement and cleanup requests
- Legacy code modernization and quality enhancement

**Specialized capabilities**:
- **Code Quality**: Clean code principles, SOLID design patterns
- **Refactoring Strategy**: Safe refactoring, incremental improvement
- **Technical Debt**: Debt identification, prioritization, systematic reduction
- **Design Patterns**: Pattern application, code structure improvement
- **Maintainability**: Code readability, documentation, consistency

**Quality standards**:
- Primary: Improved code maintainability with reduced technical debt
- Secondary: Design pattern adherence, comprehensive test coverage
- Success: Clean, maintainable code supporting long-term development productivity

**Example use cases**:
```bash
/sg:improve --focus quality legacy-module/  # → Comprehensive code quality improvement
/sg:refactor --safe complex-functions/      # → Safe refactoring with test coverage
/sg:cleanup --technical-debt codebase/      # → Systematic technical debt reduction
```

**Integration with MCP servers**:
- **Morphllm**: Pattern-based code transformations and intelligent refactoring
- **Serena**: Symbol-level analysis and large-scale refactoring coordination
- **Sequential**: Complex refactoring strategy and impact analysis

### Communication & Knowledge Agents 📚

#### ✍️ `technical-writer` - Documentation Excellence Expert
**What they do**: Technical documentation, API references, user guides, and knowledge management

**Auto-activation triggers**:
- Keywords: "document", "README", "guide", "documentation", "API docs", "tutorial"
- Documentation creation and improvement requests
- Knowledge transfer and educational content needs

**Specialized capabilities**:
- **Technical Documentation**: API documentation, user guides, technical specifications
- **Audience Analysis**: Content tailored to different technical expertise levels
- **Information Architecture**: Structured, navigable documentation systems
- **Accessibility**: WCAG compliant documentation, inclusive design principles
- **Content Strategy**: Documentation planning, maintenance, and lifecycle management

**Quality standards**:
- Primary: Flesch Reading Score 60-70 with zero ambiguity in instructions
- Secondary: WCAG 2.1 AA compliance, complete working code examples
- Success: Documentation enabling successful task completion without external assistance

**Example use cases**:
```bash
/sg:document api-endpoints/               # → Comprehensive API documentation
/sg:write user-guide --audience beginner  # → User-friendly tutorial and guides
/sg:improve --docs project-documentation/ # → Documentation quality enhancement
```

**Integration with MCP servers**:
- **Context7**: Documentation patterns and technical writing best practices
- **Serena**: Documentation persistence and cross-reference management
- **Sequential**: Complex documentation planning and content strategy

---

#### 👨‍🏫 `code-educator` - Learning & Mentorship Expert
**What they do**: Code explanation, educational content, and knowledge transfer facilitation

**Auto-activation triggers**:
- Keywords: "explain", "learn", "understand", "teach", "tutorial", "example"
- Educational content and learning-focused requests
- Code explanation and mentorship needs

**Specialized capabilities**:
- **Educational Content**: Clear, progressive learning materials and tutorials
- **Code Explanation**: Complex concept breakdown with practical examples
- **Mentorship**: Guided learning experiences and skill development
- **Knowledge Transfer**: Best practices education and team learning facilitation
- **Interactive Learning**: Hands-on examples and practical exercises

**Quality standards**:
- Primary: Clear, progressive learning experiences appropriate to audience level
- Secondary: Comprehensive examples, practical exercises, concept reinforcement
- Success: Learners successfully apply concepts and develop practical skills

**Example use cases**:
```bash
/sg:explain complex-algorithm --educational    # → Step-by-step learning guide
/sg:teach react-patterns --beginner           # → Progressive React tutorial
/sg:mentor junior-developer --focus testing   # → Personalized learning guidance
```

**Integration with MCP servers**:
- **Context7**: Educational resources and learning materials
- **Sequential**: Complex concept breakdown and progressive learning design
- **Magic**: Interactive examples and educational component creation

### Special Purpose Agents 🎯

#### 🧠 `brainstorm-PRD` - Requirements Discovery Expert
**What they do**: Transform ambiguous project ideas into concrete specifications through structured brainstorming

**Auto-activation triggers**:
- Ambiguous project requests ("I want to build something that...")
- Exploration keywords: brainstorm, explore, discuss, figure out, not sure
- PRD creation and requirements discovery needs
- `/sg:brainstorm` command usage

**Specialized capabilities**:
- **Requirements Discovery**: Socratic questioning, stakeholder analysis
- **PRD Creation**: Comprehensive product requirement documentation
- **Brainstorming Facilitation**: Creative exploration with practical constraints
- **Specification Development**: Abstract concepts to concrete requirements
- **Risk Assessment**: Early constraint and dependency identification

**Quality standards**:
- Primary: Requirements are complete and unambiguous before project handoff
- Secondary: All stakeholder perspectives integrated, feasibility validated
- Success: Comprehensive PRD enabling downstream agent execution

**Integration workflow**:
```bash
/sg:brainstorm "task management app"  # → Interactive discovery session
# → Automatic handoff to brainstorm-PRD agent
# → PRD generation with structured requirements
# → Ready for /sg:workflow implementation
```

**Integration with MCP servers**:
- **Sequential**: Complex requirements analysis and systematic discovery
- **Context7**: Industry patterns and requirement frameworks
- **Serena**: Session persistence and cross-project learning

---

## Agent Coordination & Integration 🤝

### Automatic Agent Collaboration

Agents often work together automatically. Here are common collaboration patterns:

#### **Multi-Domain Projects**
```bash
/sg:build full-stack-app/
# Auto-coordinates: backend-engineer + frontend-specialist + system-architect
```

#### **Security-Focused Development**
```bash
/sg:analyze --focus security payment-system/
# Auto-coordinates: security-auditor + backend-engineer + performance-optimizer
```

#### **Quality Improvement**
```bash
/sg:improve --focus quality legacy-codebase/
# Auto-coordinates: code-refactorer + qa-specialist + system-architect
```

### Integration with MCP Servers

Each agent leverages specific MCP servers for enhanced capabilities:

- **Context7**: Documentation patterns, framework best practices, compliance standards
- **Sequential**: Complex analysis, systematic problem solving, architectural planning
- **Magic**: UI component generation, design system integration, modern frameworks
- **Playwright**: Cross-browser testing, visual validation, performance testing
- **Morphllm**: Intelligent code transformations, pattern application, optimization
- **Serena**: Memory operations, cross-reference management, symbol-level analysis

### Integration with Commands and Modes

Agents seamlessly integrate with SuperGemini's command system:

```bash
# Commands automatically select appropriate agents
/sg:analyze → root-cause-analyzer or system-architect (context-dependent)
/sg:build → frontend-specialist, backend-engineer, or python-ultimate-expert
/sg:test → qa-specialist with domain-specific coordination
/sg:brainstorm → brainstorm-PRD for requirements discovery
/sg:document → technical-writer with audience-appropriate formatting
```

**Mode Integration**:
- **Brainstorming Mode**: Activates brainstorm-PRD for discovery sessions
- **Task Management Mode**: Coordinates multiple agents across complex workflows
- **Token Efficiency Mode**: Optimizes agent communication for resource constraints

## Quick Reference 📋

### Agent Selection Cheat Sheet

| Agent | Best For | Auto-Activates On | Example Use |
|-------|----------|-------------------|-------------|
| 🐍 python-ultimate-expert | Python development | .py files, Python frameworks | Production Python APIs |
| ⚙️ backend-engineer | Server-side systems | APIs, databases, services | Reliable backend systems |
| 🎨 frontend-specialist | User interfaces | UI components, accessibility | Accessible web interfaces |
| 🚀 devops-engineer | Infrastructure | CI/CD, deployment, monitoring | Deployment automation |
| 🛡️ security-auditor | Security analysis | Security keywords, auth code | Vulnerability assessment |
| ⚡ performance-optimizer | Performance tuning | "slow", "bottleneck", profiling | System optimization |
| 🔍 root-cause-analyzer | Problem solving | "debug", "investigate", bugs | Complex bug investigation |
| 🧪 qa-specialist | Quality assurance | Testing, validation, QA | Comprehensive test strategy |
| 🏗️ system-architect | System design | Architecture, scalability | Large-scale system design |
| 🔄 code-refactorer | Code improvement | Refactoring, cleanup, quality | Clean code practices |
| ✍️ technical-writer | Documentation | Documentation requests | API documentation |
| 👨‍🏫 code-educator | Learning & teaching | "explain", "learn", tutorials | Educational content |
| 🧠 brainstorm-PRD | Requirements discovery | Ambiguous projects, brainstorming | Project specification |

### Most Useful Agent Combinations

**Full-Stack Development**:
```bash
# Automatically coordinates backend + frontend + architecture
/sg:build modern-web-app/
```

**Security & Performance Review**:
```bash
# Coordinates security + performance + quality analysis
/sg:analyze --comprehensive production-system/
```

**Learning & Development**:
```bash
# Coordinates educator + technical writer + domain expert
/sg:explain complex-system --educational
```

**Project Discovery to Implementation**:
```bash
# Brainstorm → PRD → Architecture → Implementation
/sg:brainstorm "e-commerce platform"
# → Automatic handoff through agent coordination
```

## Best Practices 💡

### Getting Started (The Simple Way)
1. **Just use normal commands** - Agents auto-activate based on your needs
2. **Trust the automation** - SuperGemini usually picks better experts than manual selection
3. **Focus on your work** - Not on managing which agent helps you
4. **Let coordination happen** - Multiple agents work together automatically

### Advanced Usage (When You Want Control)
1. **Manual agent selection** - Use agent names in commands when you want specific expertise
2. **Cross-domain perspectives** - Ask security agents about frontend code for different viewpoints
3. **Learning mode** - Use code-educator for explanation-focused assistance
4. **Quality focus** - Combine qa-specialist with domain experts for comprehensive quality

### Common Patterns

**For New Projects**:
```bash
/sg:brainstorm "your project idea"  # → Requirements discovery
# → Automatic PRD generation and handoff
# → Ready for implementation workflow
```

**For Existing Code**:
```bash
/sg:analyze existing-system/        # → Appropriate domain expert auto-selected
/sg:improve --focus quality code/   # → Quality-focused agent coordination
/sg:secure legacy-application/      # → Security-focused analysis and hardening
```

**For Learning**:
```bash
/sg:explain complex-concept --educational  # → Code educator with domain expert
/sg:document api/ --audience beginner     # → Technical writer with appropriate level
```

---

## Final Notes 📝

**The real truth about agents** 💯:
- **Auto-activation works remarkably well** - Usually better than trying to pick experts yourself
- **You can completely ignore agent details** and still get excellent expert assistance
- **Agents exist to help you** - Not to create complexity you need to manage
- **Learning happens naturally** through use, not through studying agent descriptions

**Don't feel overwhelmed by the team** 🧘‍♂️:
- You don't need to know what each agent does
- SuperGemini handles expert selection intelligently
- The detailed descriptions above are for curiosity, not necessity
- Focus on your work - the right experts will show up when needed

**When you might want to know about agents**:
- **Curiosity** - "What would a security expert think about this frontend code?"
- **Learning** - "How would different experts approach this problem?"
- **Specialization** - "I specifically need Python architecture expertise"
- **Quality focus** - "I want comprehensive quality analysis from multiple angles"

**Keep it simple** 🎯:
- Use normal commands like `/analyze some-code/` and `/build my-app/`
- Let the right experts automatically show up
- Agent coordination is available when you want it, not because you need it
- Focus on building great software - we'll handle the expertise coordination

---

*Behind this sophisticated team of 13 specialists, SuperGemini remains simple to use. Just start coding and the right experts show up when needed! 🚀*