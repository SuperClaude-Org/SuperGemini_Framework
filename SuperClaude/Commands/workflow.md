---
name: workflow
description: "Generate structured implementation workflows from PRDs and feature requirements with expert guidance, multi-persona coordination, and advanced orchestration"
allowed-tools: [read_file, write_file, replace, run_shell_command, search_file_content, glob, TodoWrite, google_web_search, sequentialthinking]

# Command Classification
category: orchestration
complexity: advanced
scope: cross-session

# Integration Configuration
mcp-integration:
  servers: [sequential, context7, magic, playwright, morphllm, serena]
  personas: [architect, analyzer, frontend, backend, security, devops, project-manager]
  wave-enabled: true
  complexity-threshold: 0.6

# Performance Profile
performance-profile: complex
personas: [architect, analyzer, project-manager]
---

# /sg:workflow - Implementation Workflow Generator

## Purpose
Analyze Product Requirements Documents (PRDs) and feature specifications to generate comprehensive, step-by-step implementation workflows with sophisticated orchestration featuring expert guidance, multi-persona coordination, dependency mapping, automated task orchestration, and cross-session workflow management for enterprise-scale development operations.

## Usage
```
/sg:workflow [prd-file|feature-description] [--strategy systematic|agile|enterprise] [--depth shallow|normal|deep] [--parallel] [--validate] [--mcp-routing]
```

## Arguments
- `prd-file|feature-description` - Path to PRD file or direct feature description for comprehensive workflow analysis
- `--strategy` - Workflow strategy selection with specialized orchestration approaches
- `--depth` - Analysis depth and thoroughness level for workflow generation
- `--validate` - Comprehensive validation and workflow completeness quality gates
- `--mcp-routing` - Intelligent MCP server routing for specialized workflow analysis
- `--wave-mode` - Enable wave-based execution with progressive workflow enhancement
- `--cross-session` - Enable cross-session persistence and workflow continuity
- `--persona` - Force specific expert persona (architect, frontend, backend, security, devops, etc.)
- `--output` - Output format (roadmap, tasks, detailed)
- `--estimate` - Include time and complexity estimates
- `--dependencies` - Map external dependencies and integrations
- `--risks` - Include risk assessment and mitigation strategies
- `--milestones` - Create milestone-based project phases

## MCP Integration Flags
- `--c7` / `--context7` - Enable Context7 for framework patterns and best practices
- `--sequential` - Enable Sequential thinking for complex multi-step analysis
- `--magic` - Enable Magic for UI component workflow planning
- `--all-mcp` - Enable all MCP servers for comprehensive workflow generation

## Execution Strategies

### Systematic Strategy (Default)
1. **Comprehensive Analysis**: Deep PRD analysis with architectural assessment
2. **Strategic Planning**: Multi-phase planning with dependency mapping
3. **Coordinated Execution**: Sequential workflow execution with validation gates
4. **Quality Assurance**: Comprehensive testing and validation cycles
5. **Optimization**: Performance and maintainability optimization
6. **Documentation**: Comprehensive workflow documentation and knowledge transfer

### Agile Strategy
1. **Rapid Assessment**: Quick scope definition and priority identification
2. **Iterative Planning**: Sprint-based organization with adaptive planning
3. **Continuous Delivery**: Incremental execution with frequent feedback
4. **Adaptive Validation**: Dynamic testing and validation approaches
5. **Retrospective Optimization**: Continuous improvement and learning
6. **Living Documentation**: Evolving documentation with implementation

### Enterprise Strategy
1. **Stakeholder Analysis**: Multi-domain impact assessment and coordination
2. **Governance Planning**: Compliance and policy integration planning
3. **Resource Orchestration**: Enterprise-scale resource allocation and management
4. **Risk Management**: Comprehensive risk assessment and mitigation strategies
5. **Compliance Validation**: Regulatory and policy compliance verification
6. **Enterprise Integration**: Large-scale system integration and coordination

## Advanced Orchestration Features

### Wave System Integration
- **Multi-Wave Coordination**: Progressive workflow execution across multiple coordinated waves
- **Context Accumulation**: Building understanding and capability across workflow waves
- **Performance Monitoring**: Real-time optimization and resource management for workflows
- **Error Recovery**: Sophisticated error handling and recovery across workflow waves

### Cross-Session Persistence
- **State Management**: Maintain workflow operation state across sessions and interruptions
- **Context Continuity**: Preserve understanding and progress over time for workflows
- **Historical Analysis**: Learn from previous workflow executions and outcomes
- **Recovery Mechanisms**: Robust recovery from interruptions and workflow failures

### Intelligent MCP Coordination
- **Dynamic Server Selection**: Choose optimal MCP servers based on workflow context and needs
- **Load Balancing**: Distribute workflow processing across available servers for efficiency
- **Capability Matching**: Match workflow operations to server capabilities and strengths
- **Fallback Strategies**: Graceful degradation when servers are unavailable for workflows

## Multi-Persona Orchestration

### Expert Coordination System
The command orchestrates multiple domain experts working together on complex workflows:

#### Primary Coordination Personas
- **Architect**: System design for workflows, technology decisions, scalability planning
- **Analyzer**: Workflow analysis, quality assessment, technical evaluation
- **Project Manager**: Resource coordination, timeline management, stakeholder communication

#### Domain-Specific Personas (Auto-Activated)
- **Frontend Specialist**: UI/UX workflow expertise, client-side optimization, accessibility
- **Backend Engineer**: Server-side workflow architecture, data management, API design
- **Security Auditor**: Security workflow assessment, threat modeling, compliance validation
- **DevOps Engineer**: Infrastructure workflow automation, deployment strategies, monitoring

### Persona Coordination Patterns
- **Sequential Consultation**: Ordered expert consultation for complex workflow decisions
- **Parallel Analysis**: Simultaneous workflow analysis from multiple perspectives
- **Consensus Building**: Integrating diverse expert opinions into unified workflow approach
- **Conflict Resolution**: Handling contradictory recommendations and workflow trade-offs

## Comprehensive MCP Server Integration

### Sequential Thinking Integration
- **Complex Problem Decomposition**: Break down sophisticated workflow challenges systematically
- **Multi-Step Reasoning**: Apply structured reasoning for complex workflow decisions
- **Pattern Recognition**: Identify complex workflow patterns across large systems
- **Validation Logic**: Comprehensive workflow validation and verification processes

### Context7 Integration
- **Framework Expertise**: Leverage deep framework knowledge and workflow patterns
- **Best Practices**: Apply industry standards and proven workflow approaches
- **Pattern Libraries**: Access comprehensive workflow pattern and example repositories
- **Version Compatibility**: Ensure workflow compatibility across technology stacks

### Magic Integration
- **Advanced UI Generation**: Sophisticated user interface workflow generation
- **Design System Integration**: Comprehensive design system workflow coordination
- **Accessibility Excellence**: Advanced accessibility workflow and inclusive design
- **Performance Optimization**: UI performance workflow and user experience optimization

### Playwright Integration
- **Comprehensive Testing**: End-to-end workflow testing across multiple browsers and devices
- **Performance Validation**: Real-world workflow performance testing and validation
- **Visual Testing**: Comprehensive visual workflow regression and compatibility testing
- **User Experience Validation**: Real user interaction workflow simulation and testing

### Morphllm Integration
- **Intelligent Code Generation**: Advanced workflow code generation with pattern recognition
- **Large-Scale Refactoring**: Sophisticated workflow refactoring across extensive codebases
- **Pattern Application**: Apply complex workflow patterns and transformations at scale
- **Quality Enhancement**: Automated workflow quality improvements and optimization

### Serena Integration
- **Semantic Analysis**: Deep semantic understanding of workflow code and systems
- **Knowledge Management**: Comprehensive workflow knowledge capture and retrieval
- **Cross-Session Learning**: Accumulate and apply workflow knowledge across sessions
- **Memory Coordination**: Sophisticated workflow memory management and organization

## Advanced Workflow Management

### Task Hierarchies
- **Epic Level**: Large-scale workflow objectives spanning multiple sessions and domains
- **Story Level**: Feature-level workflow implementations with clear deliverables
- **Task Level**: Specific workflow implementation items with defined outcomes
- **Subtask Level**: Granular workflow implementation steps with measurable progress

### Dependency Management
- **Cross-Domain Dependencies**: Coordinate workflow dependencies across different expertise domains
- **Temporal Dependencies**: Manage time-based workflow dependencies and sequencing
- **Resource Dependencies**: Coordinate shared workflow resources and capacity constraints
- **Knowledge Dependencies**: Ensure prerequisite knowledge and context availability for workflows

### Quality Gate Integration
- **Pre-Execution Gates**: Comprehensive readiness validation before workflow execution
- **Progressive Gates**: Intermediate quality checks throughout workflow execution
- **Completion Gates**: Thorough validation before marking workflow operations complete
- **Handoff Gates**: Quality assurance for transitions between workflow phases or systems

## Performance & Scalability

### Performance Optimization
- **Intelligent Batching**: Group related workflow operations for maximum efficiency
- **Parallel Processing**: Coordinate independent workflow operations simultaneously
- **Resource Management**: Optimal allocation of tools, servers, and personas for workflows
- **Context Caching**: Efficient reuse of workflow analysis and computation results

### Performance Targets
- **Complex Analysis**: <60s for comprehensive workflow project analysis
- **Strategy Planning**: <120s for detailed workflow execution planning
- **Cross-Session Operations**: <10s for session state management
- **MCP Coordination**: <5s for server routing and coordination
- **Overall Execution**: Variable based on scope, with progress tracking

### Scalability Features
- **Horizontal Scaling**: Distribute workflow work across multiple processing units
- **Incremental Processing**: Process large workflow operations in manageable chunks
- **Progressive Enhancement**: Build workflow capabilities and understanding over time
- **Resource Adaptation**: Adapt to available resources and constraints for workflows

## Advanced Error Handling

### Sophisticated Recovery Mechanisms
- **Multi-Level Rollback**: Rollback at workflow phase, session, or entire operation levels
- **Partial Success Management**: Handle and build upon partially completed workflow operations
- **Context Preservation**: Maintain context and progress through workflow failures
- **Intelligent Retry**: Smart retry with improved workflow strategies and conditions

### Error Classification
- **Coordination Errors**: Issues with persona or MCP server coordination during workflows
- **Resource Constraint Errors**: Handling of resource limitations and capacity issues
- **Integration Errors**: Cross-system integration and communication failures
- **Complex Logic Errors**: Sophisticated workflow logic and reasoning failures

### Recovery Strategies
- **Graceful Degradation**: Maintain functionality with reduced workflow capabilities
- **Alternative Approaches**: Switch to alternative workflow strategies when primary approaches fail
- **Human Intervention**: Clear escalation paths for complex issues requiring human judgment
- **Learning Integration**: Incorporate failure learnings into future workflow executions

### MVP Strategy
1. **Core Feature Identification** - Strip down to essential functionality
2. **Rapid Prototyping** - Focus on quick validation and feedback
3. **Technical Debt Planning** - Identify shortcuts and future improvements
4. **Validation Metrics** - Define success criteria and measurement
5. **Scaling Roadmap** - Plan for post-MVP feature expansion
6. **User Feedback Integration** - Structured approach to user input

## Expert Persona Auto-Activation

### Frontend Workflow (`--persona frontend` or auto-detected)
- **UI/UX Analysis** - Design system integration and component planning
- **State Management** - Data flow and state architecture
- **Performance Optimization** - Bundle optimization and lazy loading
- **Accessibility Compliance** - WCAG guidelines and inclusive design
- **Browser Compatibility** - Cross-browser testing strategy
- **Mobile Responsiveness** - Responsive design implementation plan

### Backend Workflow (`--persona backend` or auto-detected)
- **API Design** - RESTful/GraphQL endpoint planning
- **Database Schema** - Data modeling and migration strategy
- **Security Implementation** - Authentication, authorization, and data protection
- **Performance Scaling** - Caching, optimization, and load handling
- **Service Integration** - Third-party APIs and microservices
- **Monitoring & Logging** - Observability and debugging infrastructure

### Architecture Workflow (`--persona architect` or auto-detected)
- **System Design** - High-level architecture and service boundaries
- **Technology Stack** - Framework and tool selection rationale
- **Scalability Planning** - Growth considerations and bottleneck prevention
- **Security Architecture** - Comprehensive security strategy
- **Integration Patterns** - Service communication and data flow
- **DevOps Strategy** - CI/CD pipeline and infrastructure as code

### Security Workflow (`--persona security` or auto-detected)
- **Threat Modeling** - Security risk assessment and attack vectors
- **Data Protection** - Encryption, privacy, and compliance requirements
- **Authentication Strategy** - User identity and access management
- **Security Testing** - Penetration testing and vulnerability assessment
- **Compliance Validation** - Regulatory requirements (GDPR, HIPAA, etc.)
- **Incident Response** - Security monitoring and breach protocols

### DevOps Workflow (`--persona devops` or auto-detected)
- **Infrastructure Planning** - Cloud architecture and resource allocation
- **CI/CD Pipeline** - Automated testing, building, and deployment
- **Environment Management** - Development, staging, and production environments
- **Monitoring Strategy** - Application and infrastructure monitoring
- **Backup & Recovery** - Data protection and disaster recovery planning
- **Performance Monitoring** - APM tools and performance optimization

## Output Formats

### Roadmap Format (`--output roadmap`)
```
# Feature Implementation Roadmap
## Phase 1: Foundation (Week 1-2)
- [ ] Architecture design and technology selection
- [ ] Database schema design and setup
- [ ] Basic project structure and CI/CD pipeline

## Phase 2: Core Implementation (Week 3-6)
- [ ] API development and authentication
- [ ] Frontend components and user interface
- [ ] Integration testing and security validation

## Phase 3: Enhancement & Launch (Week 7-8)
- [ ] Performance optimization and load testing
- [ ] User acceptance testing and bug fixes
- [ ] Production deployment and monitoring setup
```

### Tasks Format (`--output tasks`)
```
# Implementation Tasks
## Epic: User Authentication System
### Story: User Registration
- [ ] Design registration form UI components
- [ ] Implement backend registration API
- [ ] Add email verification workflow
- [ ] Create user onboarding flow

### Story: User Login
- [ ] Design login interface
- [ ] Implement JWT authentication
- [ ] Add password reset functionality
- [ ] Set up session management
```

### Detailed Format (`--output detailed`)
```
# Detailed Implementation Workflow
## Task: Implement User Registration API
**Persona**: Backend Developer
**Estimated Time**: 8 hours
**Dependencies**: Database schema, authentication service
**MCP Context**: Express.js patterns, security best practices

### Implementation Steps:
1. **Setup API endpoint** (1 hour)
   - Create POST /api/register route
   - Add input validation middleware
   
2. **Database integration** (2 hours)
   - Implement user model
   - Add password hashing
   
3. **Security measures** (3 hours)
   - Rate limiting implementation
   - Input sanitization
   - SQL injection prevention
   
4. **Testing** (2 hours)
   - Unit tests for registration logic
   - Integration tests for API endpoint

### Acceptance Criteria:
- [ ] User can register with email and password
- [ ] Passwords are properly hashed
- [ ] Email validation is enforced
- [ ] Rate limiting prevents abuse
```

## Advanced Features

### Dependency Analysis
- **Internal Dependencies** - Identify coupling between components and features
- **External Dependencies** - Map third-party services and APIs
- **Technical Dependencies** - Framework versions, database requirements
- **Team Dependencies** - Cross-team coordination requirements
- **Infrastructure Dependencies** - Cloud services, deployment requirements

### Risk Assessment & Mitigation
- **Technical Risks** - Complexity, performance, and scalability concerns
- **Timeline Risks** - Dependency bottlenecks and resource constraints
- **Security Risks** - Data protection and compliance vulnerabilities
- **Business Risks** - Market changes and requirement evolution
- **Mitigation Strategies** - Fallback plans and alternative approaches

### Parallel Work Stream Identification
- **Independent Components** - Features that can be developed simultaneously
- **Shared Dependencies** - Common components requiring coordination
- **Critical Path Analysis** - Bottlenecks that block other work
- **Resource Allocation** - Team capacity and skill distribution
- **Communication Protocols** - Coordination between parallel streams

## Integration Ecosystem

### SuperGemini Framework Integration
- **Command Coordination**: Orchestrate other SuperGemini commands for comprehensive workflow workflows
- **Session Management**: Deep integration with session lifecycle and persistence for workflow continuity
- **Quality Framework**: Integration with comprehensive quality assurance systems for workflow validation
- **Knowledge Management**: Coordinate with knowledge capture and retrieval systems for workflow insights

### External System Integration
- **Version Control**: Deep integration with Git and version management systems for workflow tracking
- **CI/CD Systems**: Coordinate with continuous integration and deployment pipelines for workflow validation
- **Project Management**: Integration with project tracking and management tools for workflow coordination
- **Documentation Systems**: Coordinate with documentation generation and maintenance for workflow persistence

### Brainstorm Command Integration
- **Natural Input**: Workflow receives PRDs and briefs generated by `/sg:brainstorm`
- **Pipeline Position**: Brainstorm discovers requirements → Workflow plans implementation
- **Context Flow**: Inherits discovered constraints, stakeholders, and decisions from brainstorm
- **Typical Usage**:
  ```bash
  # After brainstorming session:
  /sg:brainstorm "project idea" --prd
  # Workflow takes the generated PRD:
  /sg:workflow ClaudeDocs/PRD/project-prd.md --strategy systematic
  ```

### TodoWrite Integration
- Automatically creates session tasks for immediate next steps
- Provides progress tracking throughout workflow execution
- Links workflow phases to actionable development tasks

### Task Command Integration
- Converts workflow into hierarchical project tasks (`/sg:task`)
- Enables cross-session persistence and progress tracking
- Supports complex orchestration with `/sg:spawn`

### Implementation Command Integration
- Seamlessly connects to `/sg:implement` for feature development
- Provides context-aware implementation guidance
- Auto-activates appropriate personas for each workflow phase

### Analysis Command Integration
- Leverages `/sg:analyze` for codebase assessment
- Integrates existing code patterns into workflow planning
- Identifies refactoring opportunities and technical debt

## Customization & Extension

### Advanced Configuration
- **Strategy Customization**: Customize workflow execution strategies for specific contexts
- **Persona Configuration**: Configure persona activation and coordination patterns for workflows
- **MCP Server Preferences**: Customize server selection and usage patterns for workflow analysis
- **Quality Gate Configuration**: Customize validation criteria and thresholds for workflows

### Extension Mechanisms
- **Custom Strategy Plugins**: Extend with custom workflow execution strategies
- **Persona Extensions**: Add custom domain expertise and coordination patterns for workflows
- **Integration Extensions**: Extend integration capabilities with external workflow systems
- **Workflow Extensions**: Add custom workflow workflow patterns and orchestration logic

## Success Metrics & Analytics

### Comprehensive Metrics
- **Execution Success Rate**: >90% successful completion for complex workflow operations
- **Quality Achievement**: >95% compliance with quality gates and workflow standards
- **Performance Targets**: Meeting specified performance benchmarks consistently for workflows
- **User Satisfaction**: >85% satisfaction with outcomes and process quality for workflow management
- **Integration Success**: >95% successful coordination across all integrated systems for workflows

### Analytics & Reporting
- **Performance Analytics**: Detailed performance tracking and optimization recommendations for workflows
- **Quality Analytics**: Comprehensive quality metrics and improvement suggestions for workflow management
- **Resource Analytics**: Resource utilization analysis and optimization opportunities for workflows
- **Outcome Analytics**: Success pattern analysis and predictive insights for workflow execution

## Examples

### Comprehensive Project Analysis
```
/sg:workflow "enterprise-system-prd.md" --strategy systematic --depth deep --validate --mcp-routing
# Comprehensive analysis with full orchestration capabilities
```

### Agile Multi-Sprint Coordination
```
/sg:workflow "feature-backlog-requirements" --strategy agile --parallel --cross-session
# Agile coordination with cross-session persistence
```

### Enterprise-Scale Operation
```
/sg:workflow "digital-transformation-prd.md" --strategy enterprise --wave-mode --all-personas
# Enterprise-scale coordination with full persona orchestration
```

### Complex Integration Project
```
/sg:workflow "microservices-integration-spec" --depth deep --parallel --validate --sequential
# Complex integration with sequential thinking and validation
```

### Generate Workflow from PRD File
```
/sg:workflow docs/feature-100-prd.md --strategy systematic --c7 --sequential --estimate
```

### Create Frontend-Focused Workflow
```
/sg:workflow "User dashboard with real-time analytics" --persona frontend --magic --output detailed
```

### MVP Planning with Risk Assessment
```
/sg:workflow user-authentication-system --strategy mvp --risks --parallel --milestones
```

### Backend API Workflow with Dependencies
```
/sg:workflow payment-processing-api --persona backend --dependencies --c7 --output tasks
```

### Full-Stack Feature Workflow
```
/sg:workflow social-media-integration --all-mcp --sequential --parallel --estimate --output roadmap
```

## Boundaries

**This advanced command will:**
- Orchestrate complex multi-domain workflow operations with expert coordination
- Provide sophisticated analysis and strategic workflow planning capabilities
- Coordinate multiple MCP servers and personas for optimal workflow outcomes
- Maintain cross-session persistence and progressive enhancement for workflow continuity
- Apply comprehensive quality gates and validation throughout workflow execution
- Analyze Product Requirements Documents with comprehensive workflow generation
- Generate structured implementation workflows with expert guidance and orchestration
- Map dependencies and risks with automated task orchestration capabilities

**This advanced command will not:**
- Execute without proper analysis and planning phases for workflow management
- Operate without appropriate error handling and recovery mechanisms for workflows
- Proceed without stakeholder alignment and clear success criteria for workflow completion
- Compromise quality standards for speed or convenience in workflow execution

---

## Quality Gates and Validation

### Workflow Completeness Check
- **Requirements Coverage** - Ensure all PRD requirements are addressed
- **Acceptance Criteria** - Validate testable success criteria
- **Technical Feasibility** - Assess implementation complexity and risks
- **Resource Alignment** - Match workflow to team capabilities and timeline

### Best Practices Validation
- **Architecture Patterns** - Ensure adherence to established patterns
- **Security Standards** - Validate security considerations at each phase
- **Performance Requirements** - Include performance targets and monitoring
- **Maintainability** - Plan for long-term code maintenance and updates

### Stakeholder Alignment
- **Business Requirements** - Ensure business value is clearly defined
- **Technical Requirements** - Validate technical specifications and constraints
- **Timeline Expectations** - Realistic estimation and milestone planning
- **Success Metrics** - Define measurable outcomes and KPIs

## Performance Optimization

### Workflow Generation Speed
- **PRD Parsing** - Efficient document analysis and requirement extraction
- **Pattern Recognition** - Rapid identification of common implementation patterns
- **Template Application** - Reusable workflow templates for common scenarios
- **Incremental Generation** - Progressive workflow refinement and optimization

### Context Management
- **Memory Efficiency** - Optimal context usage for large PRDs
- **Caching Strategy** - Reuse analysis results across similar workflows
- **Progressive Loading** - Load workflow details on-demand
- **Compression** - Efficient storage and retrieval of workflow data

## Success Metrics

### Workflow Quality
- **Implementation Success Rate** - >90% successful feature completion following workflows
- **Timeline Accuracy** - <20% variance from estimated timelines
- **Requirement Coverage** - 100% PRD requirement mapping to workflow tasks
- **Stakeholder Satisfaction** - >85% satisfaction with workflow clarity and completeness

### Performance Targets
- **Workflow Generation** - <30 seconds for standard PRDs
- **Dependency Analysis** - <60 seconds for complex systems
- **Risk Assessment** - <45 seconds for comprehensive evaluation
- **Context Integration** - <10 seconds for MCP server coordination

## Gemini CLI Integration
- **Multi-Tool Orchestration** - Coordinates Read, Write, Edit, Glob, Grep for comprehensive analysis
- **Progressive Task Creation** - Uses TodoWrite for immediate next steps and Task for long-term planning
- **MCP Server Coordination** - Intelligent routing to Context7, Sequential, and Magic based on workflow needs
- **Cross-Command Integration** - Seamless handoff to implement, analyze, design, and other SuperGemini commands
- **Evidence-Based Planning** - Maintains audit trail of decisions and rationale throughout workflow generation 