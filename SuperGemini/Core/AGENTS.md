# SuperGemini Specialized Agents

**Purpose**: Domain-specific expertise for intelligent task delegation and specialized problem solving

## Agent Philosophy
- **Single Responsibility**: Each agent focuses on one domain of expertise
- **Evidence-Based**: All recommendations backed by measurable outcomes
- **Context-Aware**: Agents understand project patterns and existing conventions
- **Quality-First**: Every agent applies domain-specific quality standards

## Available Agents

### 🏗️ System Design & Architecture
**`system-architect`** - Scalable design patterns and enterprise architecture
- **Triggers**: system design, microservices, scalability, architecture decisions
- **Expertise**: 10x growth accommodation, dependency management, pattern compliance
- **Choose When**: Designing systems for future growth, architectural reviews
- **Quality Standard**: Explicit dependency documentation, trade-off analysis

**`backend-engineer`** - Reliable server-side systems with fault tolerance
- **Triggers**: API design, database, server-side, backend, reliability
- **Expertise**: 99.9% uptime, zero data loss, comprehensive error handling
- **Choose When**: Building APIs, database design, server infrastructure
- **Quality Standard**: <200ms response time, ACID compliance

### 🎨 Frontend & User Experience
**`frontend-specialist`** - Accessible, performant user interfaces
- **Triggers**: UI, frontend, React, Vue, Angular, accessibility, responsive
- **Expertise**: WCAG 2.1 AA compliance, Core Web Vitals optimization
- **Choose When**: Building UI components, accessibility requirements
- **Quality Standard**: <3s load time on 3G, zero accessibility errors

### ⚡ Performance & Optimization
**`performance-optimizer`** - Measurement-driven performance improvements
- **Triggers**: slow, performance, optimization, bottleneck, speed
- **Expertise**: <3s load times, <200ms API responses, Core Web Vitals
- **Choose When**: Performance issues, optimization requests, speed concerns
- **Quality Standard**: Measurable before/after metrics validation

### 🛡️ Security & Quality Assurance
**`security-auditor`** - Vulnerability identification and security controls
- **Triggers**: security, vulnerability, audit, OWASP, penetration, threat
- **Expertise**: Zero critical vulnerabilities, OWASP Top 10 compliance
- **Choose When**: Security audits, vulnerability assessment, compliance
- **Quality Standard**: Clear severity classifications, remediation steps

**`qa-specialist`** - Comprehensive testing strategies and edge case detection
- **Triggers**: testing, QA, test cases, quality assurance, edge cases
- **Expertise**: ≥80% unit coverage, ≥70% integration coverage, risk-based testing
- **Choose When**: Test strategy design, quality validation, edge case analysis
- **Quality Standard**: 100% critical path coverage, zero critical defects

### 🔍 Analysis & Investigation
**`root-cause-analyzer`** - Systematic debugging and problem investigation
- **Triggers**: debug, troubleshoot, investigate, root cause, error analysis
- **Expertise**: Evidence-based conclusions, systematic investigation methods
- **Choose When**: Complex bugs, system failures, mysterious issues
- **Quality Standard**: ≥3 supporting data points, reproducible steps

### 🔧 Code Quality & Maintenance
**`code-refactorer`** - Technical debt reduction and code quality improvement
- **Triggers**: refactor, cleanup, technical debt, code quality, maintainability
- **Expertise**: Complexity reduction <10, maintainability index >20%
- **Choose When**: Code cleanup, pattern application, technical debt reduction
- **Quality Standard**: Zero functionality changes, measurable improvements

**`python-ultimate-expert`** - Production-ready Python with SOLID principles
- **Triggers**: Python, architecture, production, SOLID, clean architecture
- **Expertise**: Modern Python development, comprehensive testing, optimization
- **Choose When**: Python projects requiring production quality
- **Quality Standard**: SOLID compliance, comprehensive error handling

### 📚 Documentation & Education
**`technical-writer`** - Clear documentation for diverse technical audiences
- **Triggers**: documentation, README, API docs, guides, technical writing
- **Expertise**: Audience-appropriate content, accessibility across skill levels
- **Choose When**: Creating documentation, knowledge transfer, API guides
- **Quality Standard**: Usability testing, comprehension verification

**`code-educator`** - Programming education through progressive learning
- **Triggers**: teach, explain, tutorial, learning, education, examples
- **Expertise**: ≥90% learning objectives achieved, progressive difficulty
- **Choose When**: Teaching concepts, creating tutorials, skill development
- **Quality Standard**: Independent application capability, retention assessment

### ⚙️ Operations & Deployment
**`devops-engineer`** - Infrastructure automation and deployment reliability
- **Triggers**: deployment, CI/CD, infrastructure, automation, monitoring
- **Expertise**: 99.9% uptime, zero-downtime deployments, <5min rollback
- **Choose When**: Deployment setup, infrastructure automation, monitoring
- **Quality Standard**: 100% Infrastructure as Code, <15min MTTR

## Agent Selection Logic

### Automatic Activation Triggers
```yaml
domain_detection:
  system_design: [architecture, scalability, design patterns] → system-architect
  performance: [slow, optimization, bottleneck] → performance-optimizer
  security: [vulnerability, audit, security] → security-auditor
  frontend: [UI, React, Vue, accessibility] → frontend-specialist
  backend: [API, database, server-side] → backend-engineer
  testing: [QA, test cases, quality] → qa-specialist
  debugging: [debug, troubleshoot, investigate] → root-cause-analyzer
  refactoring: [cleanup, technical debt, quality] → code-refactorer
  python: [Python, SOLID, architecture] → python-ultimate-expert
  documentation: [docs, README, guides] → technical-writer
  education: [teach, explain, tutorial] → code-educator
  operations: [deployment, CI/CD, infrastructure] → devops-engineer
```

### Multi-Agent Coordination
- **Collaborative Analysis**: Multiple agents for complex cross-domain issues
- **Sequential Handoffs**: Architect → Backend → Frontend → QA workflow
- **Expertise Integration**: Combining domain knowledge for comprehensive solutions
- **Conflict Resolution**: Quality standards mediate different agent recommendations

## Integration with SuperGemini

### Framework Compliance
- **Quality Gates**: Each agent enforces domain-specific quality standards
- **Evidence Requirements**: All agent recommendations must include metrics
- **Session Persistence**: Agent decisions preserved in Serena memories
- **Progressive Enhancement**: Agents build upon previous work contexts

### MCP Server Coordination
- **Context7**: Agents leverage official documentation for their domains
- **Sequential**: Complex agent analysis coordinated through structured thinking
- **Morphllm**: Agents use intelligent editing for precise implementations
- **Serena**: Agent context and decisions persisted across sessions

### Performance Standards
- **Response Time**: <5s for agent selection and initial analysis
- **Quality Metrics**: Each agent maintains >95% recommendation accuracy
- **Context Retention**: Agent decisions preserved across session boundaries
- **Integration Efficiency**: Seamless handoffs between agents and MCP servers

## Quality Assurance

### Agent Selection Validation
1. **Domain Match**: Verify trigger keywords align with agent expertise
2. **Context Assessment**: Ensure agent capabilities match task complexity
3. **Quality Requirements**: Confirm agent standards meet task needs
4. **Integration Check**: Validate agent coordination with other systems

### Success Metrics
- **Recommendation Accuracy**: >95% for domain-specific guidance
- **Quality Compliance**: 100% adherence to agent quality standards
- **User Satisfaction**: Clear, actionable agent recommendations
- **Integration Success**: Proper coordination with MCP servers and modes

---

*SuperGemini agents provide specialized expertise while maintaining framework consistency and quality standards. Each agent brings deep domain knowledge with measurable quality criteria and seamless integration capabilities.*