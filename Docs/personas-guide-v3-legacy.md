# SuperGemini Personas User Guide 🎭

## 🎭 Personas Auto-Activate - No Need to Choose!

**The simple truth**: You don't need to pick personas or memorize what they do. SuperGemini usually tries to bring in helpful experts for each situation! 

**Here's what actually happens:**
- You type `/analyze auth.js` → Security expert usually jumps in 🛡️
- You work on React components → Frontend specialist often takes over 🎨  
- You debug performance issues → Performance optimizer often helps ⚡
- You write documentation → Professional writer usually helps out ✍️

**It's like having a smart team** that knows when to jump in and help, without you managing who does what. 

**Manual control available** when you want it (like asking specifically for a security review of frontend code), but most of the time you can just... let it work. 🪄

---

## 🚀 Just Try These (No Persona Knowledge Required)

```bash
# These automatically activate the right experts:
/sg:analyze payment-system/         # → Security + backend experts auto-activate
/sg:build react-app/               # → Frontend specialist takes over  
/sg:improve slow-queries.sql       # → Performance optimizer jumps in
/sg:troubleshoot "auth failing"    # → Debug specialist + security expert coordinate
```

**See the pattern?** You focus on what you want to do, SuperGemini figures out who should help. Everything below is for when you get curious about who's on the team.

---

Think of SuperGemini personas as having a team of specialists on demand. Each persona brings different expertise, priorities, and perspectives to help you with specific types of work.

## What Are Personas? 🤔

**Personas are AI specialists** that try to adapt SuperGemini's behavior for different types of work. Instead of generic responses, you often get expert-level help from relevant specialists.

**How they actually work in practice:**
- **Auto-activation** - SuperGemini usually tries to pick helpful experts (most of the time this works pretty well!)
- **Smart detection** - Recognizes security work, frontend tasks, performance issues, etc.
- **Seamless switching** - Different experts jump in as needed within the same conversation
- **Team coordination** - Multiple experts often coordinate on complex tasks
- **Manual override available** - You can explicitly choose with `--persona-name` flags when you want a different perspective

**Why this matters:**
- Often get expert-level advice without knowing which expert to ask
- Usually get better decision-making aligned with what you're actually working on
- More focused and relevant responses based on the task
- Access to specialized workflows that activate when useful

**The neat part**: You just work on your stuff, and helpful experts usually show up when needed. 🎯

## The SuperGemini Team 👥

### Technical Specialists 🔧

#### 🏗️ `architect` - Systems Design Specialist
**What they do**: Long-term architecture planning, system design, scalability decisions

**Priority**: Long-term maintainability > scalability > performance > quick fixes

**When they auto-activate**:
- Keywords: "architecture", "design", "scalability", "system structure"
- Complex system modifications involving multiple modules
- Planning large features or system changes

**Great for**:
- Planning new systems or major features
- Architectural reviews and improvements
- Technical debt assessment
- Design pattern recommendations
- Scalability planning

**Example workflows**:
```bash
/sg:design microservices-migration --persona-architect
/sg:analyze --focus architecture large-system/
/sg:estimate "redesign auth system" --persona-architect
```

**What they prioritize**:
- Maintainable, understandable code
- Loose coupling, high cohesion
- Future-proof design decisions
- Clear separation of concerns

---

#### 🎨 `frontend` - UI/UX & Accessibility Expert
**What they do**: User experience, accessibility, frontend performance, design systems

**Priority**: User needs > accessibility > performance > technical elegance

**When they auto-activate**:
- Keywords: "component", "responsive", "accessibility", "UI", "UX"
- Frontend development work
- User interface related tasks

**Great for**:
- Building UI components
- Accessibility compliance (WCAG 2.1 AA)
- Frontend performance optimization
- Design system work
- User experience improvements

**Performance budgets they enforce**:
- Load time: <3s on 3G, <1s on WiFi
- Bundle size: <500KB initial, <2MB total
- Accessibility: WCAG compliance target

**Example workflows**:
```bash
/sg:build dashboard --persona-frontend
/sg:improve --focus accessibility components/
/sg:analyze --persona-frontend --focus performance
```

**What they prioritize**:
- Intuitive, user-friendly interfaces
- Accessibility for all users
- Real-world performance on mobile/3G
- Clean, maintainable CSS/JS

---

#### ⚙️ `backend` - API & Infrastructure Specialist
**What they do**: Server-side development, APIs, databases, reliability engineering

**Priority**: Reliability > security > performance > features > convenience

**When they auto-activate**:
- Keywords: "API", "database", "service", "server", "reliability"
- Backend development work
- Infrastructure or data-related tasks

**Great for**:
- API design and implementation
- Database schema and optimization
- Security implementation
- Reliability and error handling
- Backend performance tuning

**Reliability budgets they enforce**:
- Uptime: 99.9% (8.7h/year downtime)
- Error rate: <0.1% for critical operations
- API response time: <200ms
- Recovery time: <5 minutes for critical services

**Example workflows**:
```bash
/sg:design user-api --persona-backend
/sg:analyze --focus security api/
/sg:improve --persona-backend database-layer/
```

**What they prioritize**:
- Rock-solid reliability and uptime
- Security by default (zero trust)
- Data integrity and consistency
- Graceful error handling

---

#### 🛡️ `security` - Threat Modeling & Vulnerability Expert
**What they do**: Security analysis, threat modeling, vulnerability assessment, compliance

**Priority**: Security > compliance > reliability > performance > convenience

**When they auto-activate**:
- Keywords: "security", "vulnerability", "auth", "compliance"
- Security scanning or assessment work
- Authentication/authorization tasks

**Great for**:
- Security audits and vulnerability scanning
- Threat modeling and risk assessment
- Secure coding practices
- Compliance requirements (OWASP, etc.)
- Authentication and authorization systems

**Threat assessment levels**:
- Critical: Immediate action required
- High: Fix within 24 hours
- Medium: Fix within 7 days
- Low: Fix within 30 days

**Example workflows**:
```bash
/sg:scan --persona-security --focus security
/sg:analyze auth-system/ --persona-security
/sg:improve --focus security --persona-security
```

**What they prioritize**:
- Security by default, fail-safe mechanisms
- Zero trust architecture principles
- Defense in depth strategies
- Clear security documentation

---

#### ⚡ `performance` - Optimization & Bottleneck Specialist
**What they do**: Performance optimization, bottleneck identification, metrics analysis

**Priority**: Measure first > optimize critical path > user experience > avoid premature optimization

**When they auto-activate**:
- Keywords: "performance", "optimization", "speed", "bottleneck"
- Performance analysis or optimization work
- When speed/efficiency is mentioned

**Great for**:
- Performance bottleneck identification
- Code optimization with metrics validation
- Database query optimization
- Frontend performance tuning
- Load testing and capacity planning

**Performance budgets they track**:
- API responses: <500ms
- Database queries: <100ms
- Bundle size: <500KB initial
- Memory usage: <100MB mobile, <500MB desktop

**Example workflows**:
```bash
/sg:analyze --focus performance --persona-performance
/sg:improve --type performance slow-endpoints/
/sg:test --benchmark --persona-performance
```

**What they prioritize**:
- Measurement-driven optimization
- Real user experience improvements
- Critical path performance
- Systematic optimization methodology

### Process & Quality Experts ✨

#### 🔍 `analyzer` - Root Cause Investigation Specialist
**What they do**: Systematic debugging, root cause analysis, evidence-based investigation

**Priority**: Evidence > systematic approach > thoroughness > speed

**When they auto-activate**:
- Keywords: "analyze", "investigate", "debug", "root cause"
- Debugging or troubleshooting sessions
- Complex problem investigation

**Great for**:
- Debugging complex issues
- Root cause analysis
- System investigation
- Evidence-based problem solving
- Understanding unknown codebases

**Investigation methodology**:
1. Evidence collection before conclusions
2. Pattern recognition in data
3. Hypothesis testing and validation
4. Root cause confirmation through tests

**Example workflows**:
```bash
/sg:troubleshoot "auth randomly fails" --persona-analyzer
/sg:analyze --persona-analyzer mysterious-bug/
/sg:explain --detailed "why is this slow" --persona-analyzer
```

**What they prioritize**:
- Evidence-based conclusions
- Systematic investigation methods
- Complete analysis before solutions
- Reproducible findings

---

#### 🧪 `qa` - Quality Assurance & Testing Expert
**What they do**: Testing strategy, quality gates, edge case detection, risk assessment

**Priority**: Prevention > detection > correction > comprehensive coverage

**When they auto-activate**:
- Keywords: "test", "quality", "validation", "coverage"
- Testing or quality assurance work
- Quality gates or edge cases mentioned

**Great for**:
- Test strategy and planning
- Quality assurance processes
- Edge case identification
- Risk-based testing
- Test automation

**Quality risk assessment**:
- Critical path analysis for user journeys
- Failure impact evaluation
- Defect probability assessment
- Recovery difficulty estimation

**Example workflows**:
```bash
/sg:test --persona-qa comprehensive-suite
/sg:analyze --focus quality --persona-qa
/sg:review --persona-qa critical-features/
```

**What they prioritize**:
- Preventing defects over finding them
- Comprehensive test coverage
- Risk-based testing priorities
- Quality built into the process

---

#### 🔄 `refactorer` - Code Quality & Cleanup Specialist
**What they do**: Code quality improvement, technical debt management, clean code practices

**Priority**: Simplicity > maintainability > readability > performance > cleverness

**When they auto-activate**:
- Keywords: "refactor", "cleanup", "quality", "technical debt"
- Code improvement or cleanup work
- Maintainability concerns

**Great for**:
- Code refactoring and cleanup
- Technical debt reduction
- Code quality improvements
- Design pattern application
- Legacy code modernization

**Code quality metrics they track**:
- Cyclomatic complexity
- Code readability scores
- Technical debt ratio
- Test coverage

**Example workflows**:
```bash
/sg:improve --type quality --persona-refactorer
/sg:cleanup legacy-module/ --persona-refactorer
/sg:analyze --focus maintainability --persona-refactorer
```

**What they prioritize**:
- Simple, readable solutions
- Consistent patterns and conventions
- Maintainable code structure
- Technical debt management

---

#### 🚀 `devops` - Infrastructure & Deployment Expert
**What they do**: Infrastructure automation, deployment, monitoring, reliability engineering

**Priority**: Automation > observability > reliability > scalability > manual processes

**When they auto-activate**:
- Keywords: "deploy", "infrastructure", "CI/CD", "monitoring"
- Deployment or infrastructure work
- DevOps or automation tasks

**Great for**:
- Deployment automation and CI/CD
- Infrastructure as code
- Monitoring and alerting setup
- Performance monitoring
- Container and cloud infrastructure

**Infrastructure automation priorities**:
- Zero-downtime deployments
- Automated rollback capabilities
- Infrastructure as code
- Comprehensive monitoring

**Example workflows**:
```bash
/sg:deploy production --persona-devops
/sg:analyze infrastructure/ --persona-devops
/sg:improve deployment-pipeline --persona-devops
```

**What they prioritize**:
- Automated over manual processes
- Comprehensive observability
- Reliable, repeatable deployments
- Infrastructure as code practices

### Knowledge & Communication 📚

#### 👨‍🏫 `mentor` - Educational Guidance Specialist
**What they do**: Teaching, knowledge transfer, educational explanations, learning facilitation

**Priority**: Understanding > knowledge transfer > teaching > task completion

**When they auto-activate**:
- Keywords: "explain", "learn", "understand", "teach"
- Educational or knowledge transfer tasks
- Step-by-step guidance requests

**Great for**:
- Learning new technologies
- Understanding complex concepts
- Code explanations and walkthroughs
- Best practices education
- Team knowledge sharing

**Learning optimization approach**:
- Skill level assessment
- Progressive complexity building
- Learning style adaptation
- Knowledge retention reinforcement

**Example workflows**:
```bash
/sg:explain React hooks --persona-mentor
/sg:document --type guide --persona-mentor
/sg:analyze complex-algorithm.js --persona-mentor
```

**What they prioritize**:
- Clear, accessible explanations
- Complete conceptual understanding
- Engaging learning experiences
- Practical skill development

---

#### ✍️ `scribe` - Professional Documentation Expert
**What they do**: Professional writing, documentation, localization, cultural communication

**Priority**: Clarity > audience needs > cultural sensitivity > completeness > brevity

**When they auto-activate**:
- Keywords: "document", "write", "guide", "README"
- Documentation or writing tasks
- Professional communication needs

**Great for**:
- Technical documentation
- User guides and tutorials
- README files and wikis
- API documentation
- Professional communications

**Language support**: English (default), Spanish, French, German, Japanese, Chinese, Portuguese, Italian, Russian, Korean

**Content types**: Technical docs, user guides, API docs, commit messages, PR descriptions

**Example workflows**:
```bash
/sg:document api/ --persona-scribe
/sg:git commit --persona-scribe
/sg:explain --persona-scribe=es complex-feature
```

**What they prioritize**:
- Clear, professional communication
- Audience-appropriate language
- Cultural sensitivity and adaptation
- High writing standards

## When Each Persona Shines ⭐

### Development Phase Mapping

**Planning & Design Phase**:
- 🏗️ `architect` - System design and architecture planning
- 🎨 `frontend` - UI/UX design and user experience
- ✍️ `scribe` - Requirements documentation and specifications

**Implementation Phase**:
- 🎨 `frontend` - UI component development
- ⚙️ `backend` - API and service implementation
- 🛡️ `security` - Security implementation and hardening

**Testing & Quality Phase**:
- 🧪 `qa` - Test strategy and quality assurance
- ⚡ `performance` - Performance testing and optimization
- 🔍 `analyzer` - Bug investigation and root cause analysis

**Maintenance & Improvement Phase**:
- 🔄 `refactorer` - Code cleanup and refactoring
- ⚡ `performance` - Performance optimization
- 👨‍🏫 `mentor` - Knowledge transfer and documentation

**Deployment & Operations Phase**:
- 🚀 `devops` - Deployment automation and infrastructure
- 🛡️ `security` - Security monitoring and compliance
- ✍️ `scribe` - Operations documentation and runbooks

### Problem Type Mapping

**"My code is slow"** → ⚡ `performance`
**"Something's broken and I don't know why"** → 🔍 `analyzer`
**"Need to design a new system"** → 🏗️ `architect`
**"UI looks terrible"** → 🎨 `frontend`
**"Is this secure?"** → 🛡️ `security`
**"Code is messy"** → 🔄 `refactorer`
**"Need better tests"** → 🧪 `qa`
**"Deployment keeps failing"** → 🚀 `devops`
**"I don't understand this"** → 👨‍🏫 `mentor`
**"Need documentation"** → ✍️ `scribe`

## Persona Combinations 🤝

Personas often work together automatically. Here are common collaboration patterns:

### Design & Implementation
```bash
/sg:design user-dashboard
# Auto-activates: 🏗️ architect (system design) + 🎨 frontend (UI design)
```

### Security Review
```bash
/sg:analyze --focus security api/
# Auto-activates: 🛡️ security (primary) + ⚙️ backend (API expertise)
```

### Performance Optimization
```bash
/sg:improve --focus performance slow-app/
# Auto-activates: ⚡ performance (primary) + 🎨 frontend (if UI) or ⚙️ backend (if API)
```

### Quality Improvement
```bash
/sg:improve --focus quality legacy-code/
# Auto-activates: 🔄 refactorer (primary) + 🧪 qa (testing) + 🏗️ architect (design)
```

### Documentation & Learning
```bash
/sg:document complex-feature --type guide
# Auto-activates: ✍️ scribe (writing) + 👨‍🏫 mentor (educational approach)
```

## Practical Examples 💡

### Before/After: Generic vs Persona-Specific

**Before** (generic):
```bash
/sg:analyze auth.js
# → Basic analysis, generic advice
```

**After** (security persona):
```bash
/sg:analyze auth.js --persona-security
# → Security-focused analysis
# → Threat modeling perspective
# → OWASP compliance checking
# → Vulnerability pattern detection
```

### Auto-Activation in Action

**Frontend work detection**:
```bash
/sg:build react-components/
# Auto-activates: 🎨 frontend
# → UI-focused build optimization
# → Accessibility checking
# → Performance budgets
# → Bundle size analysis
```

**Complex debugging**:
```bash
/sg:troubleshoot "payment processing randomly fails"
# Auto-activates: 🔍 analyzer
# → Systematic investigation approach
# → Evidence collection methodology
# → Pattern analysis
# → Root cause identification
```

### Manual Override Examples

**Force security perspective**:
```bash
/sg:analyze react-app/ --persona-security
# Even though it's frontend code, analyze from security perspective
# → XSS vulnerability checking
# → Authentication flow analysis
# → Data exposure risks
```

**Get architectural advice on small changes**:
```bash
/sg:improve small-utility.js --persona-architect
# Apply architectural thinking to small code
# → Design pattern opportunities
# → Future extensibility
# → Coupling analysis
```

## Advanced Usage 🚀

### Manual Persona Control

**When to override auto-activation**:
- You want a different perspective on the same problem
- Auto-activation chose wrong persona for your specific needs
- You're learning and want to see how different experts approach problems

**How to override**:
```bash
# Explicit persona selection
/sg:analyze frontend-code/ --persona-security  # Security view of frontend
/sg:improve backend-api/ --persona-performance # Performance view of backend

# Multiple persona flags (last one wins)
/sg:analyze --persona-frontend --persona-security # Uses security persona
```

### Persona-Specific Flags and Settings

**Security persona + validation**:
```bash
/sg:analyze --persona-security --focus security --validate
# → Maximum security focus with validation
```

**Performance persona + benchmarking**:
```bash
/sg:test --persona-performance --benchmark --focus performance
# → Performance-focused testing with metrics
```

**Mentor persona + detailed explanations**:
```bash
/sg:explain complex-concept --persona-mentor --verbose
# → Educational explanation with full detail
```

### Cross-Domain Expertise

**When you need multiple perspectives**:
```bash
# Sequential analysis with different personas
/sg:analyze --persona-security api/auth.js
/sg:analyze --persona-performance api/auth.js  
/sg:analyze --persona-refactorer api/auth.js

# Or let SuperGemini coordinate automatically
/sg:analyze --focus quality api/auth.js
# Auto-coordinates: security + performance + refactorer insights
```

## Common Workflows by Persona 💼

### 🏗️ Architect Workflows
```bash
# System design
/sg:design microservices-architecture --persona-architect
/sg:estimate "migrate monolith to microservices" --persona-architect

# Architecture review
/sg:analyze --focus architecture --persona-architect large-system/
/sg:review --persona-architect critical-components/
```

### 🎨 Frontend Workflows
```bash
# Component development
/sg:build dashboard-components/ --persona-frontend
/sg:improve --focus accessibility --persona-frontend ui/

# Performance optimization
/sg:analyze --focus performance --persona-frontend bundle/
/sg:test --persona-frontend --focus performance
```

### ⚙️ Backend Workflows
```bash
# API development
/sg:design rest-api --persona-backend
/sg:build api-endpoints/ --persona-backend

# Reliability improvements
/sg:improve --focus reliability --persona-backend services/
/sg:analyze --persona-backend --focus security api/
```

### 🛡️ Security Workflows
```bash
# Security assessment
/sg:scan --persona-security --focus security entire-app/
/sg:analyze --persona-security auth-flow/

# Vulnerability fixing
/sg:improve --focus security --persona-security vulnerable-code/
/sg:review --persona-security --focus security critical-paths/
```

### 🔍 Analyzer Workflows
```bash
# Bug investigation
/sg:troubleshoot "intermittent failures" --persona-analyzer
/sg:analyze --persona-analyzer --focus debugging problem-area/

# System understanding
/sg:explain --persona-analyzer complex-system/
/sg:load --persona-analyzer unfamiliar-codebase/
```

## Quick Reference 📋

### Persona Cheat Sheet

| Persona | Best For | Auto-Activates On | Manual Flag |
|---------|----------|-------------------|-------------|
| 🏗️ architect | System design, architecture | "architecture", "design", "scalability" | `--persona-architect` |
| 🎨 frontend | UI/UX, accessibility | "component", "responsive", "UI" | `--persona-frontend` |
| ⚙️ backend | APIs, databases, reliability | "API", "database", "service" | `--persona-backend` |
| 🛡️ security | Security, compliance | "security", "vulnerability", "auth" | `--persona-security` |
| ⚡ performance | Optimization, speed | "performance", "optimization", "slow" | `--persona-performance` |
| 🔍 analyzer | Debugging, investigation | "analyze", "debug", "investigate" | `--persona-analyzer` |
| 🧪 qa | Testing, quality | "test", "quality", "validation" | `--persona-qa` |
| 🔄 refactorer | Code cleanup, refactoring | "refactor", "cleanup", "quality" | `--persona-refactorer` |
| 🚀 devops | Deployment, infrastructure | "deploy", "infrastructure", "CI/CD" | `--persona-devops` |
| 👨‍🏫 mentor | Learning, explanation | "explain", "learn", "understand" | `--persona-mentor` |
| ✍️ scribe | Documentation, writing | "document", "write", "guide" | `--persona-scribe` |

### Most Useful Combinations

**Security-focused development**:
```bash
--persona-security --focus security --validate
```

**Performance optimization**:
```bash
--persona-performance --focus performance --benchmark
```

**Learning and understanding**:
```bash
--persona-mentor --verbose --explain
```

**Quality improvement**:
```bash
--persona-refactorer --focus quality --safe-mode
```

**Professional documentation**:
```bash
--persona-scribe --type guide --detailed
```

### Auto-Activation Triggers

**Strong triggers** (usually work well):
- "security audit" → 🛡️ security
- "UI component" → 🎨 frontend  
- "API design" → ⚙️ backend
- "system architecture" → 🏗️ architect
- "debug issue" → 🔍 analyzer

**Moderate triggers** (often work):
- "improve performance" → ⚡ performance
- "write tests" → 🧪 qa
- "clean up code" → 🔄 refactorer
- "deployment issue" → 🚀 devops

**Context-dependent triggers** (varies):
- "document this" → ✍️ scribe or 👨‍🏫 mentor (depends on audience)
- "analyze this" → 🔍 analyzer, 🏗️ architect, or domain specialist (depends on content)

## Troubleshooting Persona Issues 🚨

### Common Problems

**"Wrong persona activated"**
- Use explicit persona flags: `--persona-security`
- Check if your keywords triggered auto-activation
- Try more specific language in your request

**"Persona doesn't seem to work"**
- Verify persona name spelling: `--persona-frontend` not `--persona-fronted`
- Some personas work better with specific commands
- Try combining with relevant flags: `--focus security --persona-security`

**"Want multiple perspectives"**
- Run same command with different personas manually
- Use broader focus flags: `--focus quality` (activates multiple personas)
- Let SuperGemini coordinate automatically with complex requests

**"Persona is too focused"**
- Try a different persona that's more general
- Use mentor persona for broader explanations
- Combine with `--verbose` for more context

### When to Override Auto-Activation

**Override when**:
- Auto-activation chose the wrong specialist
- You want to learn from a different perspective
- Working outside typical domain boundaries
- Need specific expertise for edge cases

**How to override effectively**:
```bash
# Force specific perspective
/sg:analyze frontend-code/ --persona-security  # Security view of frontend

# Combine multiple perspectives
/sg:analyze api/ --persona-security
/sg:analyze api/ --persona-performance  # Run separately for different views

# Use general analysis
/sg:analyze --no-persona  # Disable persona auto-activation
```

## Tips for Effective Persona Usage 💡

### Getting Started (The Honest Way)
1. **Just ignore personas completely at first** - Auto-activation handles everything
2. **Use basic commands normally** - `/analyze`, `/build`, `/improve` work great without persona knowledge
3. **Notice what happens** - You'll see different types of expertise emerge naturally
4. **Trust the automation** - SuperGemini usually picks better experts than manual selection

### Getting Advanced (If You Want To)
1. **Experiment with manual override** - Try `--persona-security` on frontend code for different perspectives
2. **Learn the team members** - Read about individual personas when you get curious
3. **Watch persona combinations** - See how multiple experts collaborate on complex problems
4. **Use for learning** - Ask different personas the same question to see different approaches

### Best Practices (Keep It Simple)
- **Let auto-activation work first** - Override only when you want different perspectives
- **Don't overthink it** - The right experts show up when needed
- **Use for experimentation** - Try different personas on the same problem for learning
- **Trust the intelligence** - Auto-activation learns from patterns and keeps getting better

---

## Final Notes 📝

**The real truth about personas** 💯:
- **Auto-activation usually works pretty well** compared to trying to pick experts yourself
- **You can completely ignore this guide** and still often get helpful expert assistance
- **Personas exist to help you** - not to create complexity you need to manage
- **Learning happens naturally** through use, not through studying persona descriptions 😊

**Don't feel overwhelmed by the team** 🧘‍♂️:
- You don't need to know what each persona does
- SuperGemini usually handles expert selection reasonably well
- The detailed descriptions above are for curiosity, not necessity
- You're not missing anything by letting auto-activation work

**When you might manually choose personas**:
- **Curiosity** - "What would a security expert think about this frontend code?"
- **Learning** - "How would different experts approach this problem?"
- **Experimentation** - "Let me see this through a performance lens"
- **Override** - "I want architectural advice on this small utility function"

**Keep it simple** 🎯:
- Use normal commands like `/analyze some-code/`
- Let the right experts automatically show up
- Manual persona control is available when you want it, not because you need it
- Focus on your work, not on managing who helps you

---

*Behind all this apparent complexity of having 11 specialists, SuperGemini tries to be simple to use. Just start coding and helpful experts usually show up when needed! 🚀*