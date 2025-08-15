---
name: task
description: "Execute complex tasks with intelligent workflow management, cross-session persistence, hierarchical task organization, and advanced wave system orchestration"
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Grep, Glob, TodoWrite, Task, WebSearch, sequentialthinking]

# Command Classification
category: orchestration
complexity: advanced
scope: cross-session

# Integration Configuration
mcp-integration:
  servers: [sequential, context7, magic, playwright, morphllm, serena]
  personas: [architect, analyzer, frontend, backend, security, devops, project-manager]
  wave-enabled: true
  complexity-threshold: 0.7

# Performance Profile
performance-profile: complex
personas: [architect, analyzer, project-manager]
---

# /sg:task - Enhanced Task Management

## Purpose
Execute complex tasks with intelligent workflow management, cross-session persistence, hierarchical task organization, and advanced orchestration capabilities.

## Usage  
```
/sg:task [action] [target] [--strategy systematic|agile|enterprise] [--depth shallow|normal|deep] [--parallel] [--validate] [--mcp-routing]
```

## Arguments
- `action` - Task management action (create, execute, status, analytics, optimize, delegate, validate)
- `target` - Task description, project scope, or existing task ID for comprehensive management
- `--strategy` - Task execution strategy selection with specialized orchestration approaches
- `--depth` - Task analysis depth and thoroughness level
- `--validate` - Comprehensive validation and task completion quality gates
- `--mcp-routing` - Intelligent MCP server routing for specialized task analysis
- `--wave-mode` - Enable wave-based execution with progressive task enhancement
- `--cross-session` - Enable cross-session persistence and task continuity
- `--persist` - Enable cross-session task persistence
- `--hierarchy` - Create hierarchical task breakdown

## Actions
- `create` - Create new project-level task hierarchy with advanced orchestration
- `execute` - Execute task with intelligent orchestration and wave system integration
- `status` - View task status across sessions with comprehensive analytics
- `analytics` - Task performance and analytics dashboard with optimization insights
- `optimize` - Optimize task execution strategies with wave system coordination
- `delegate` - Delegate tasks across multiple agents with intelligent coordination
- `validate` - Validate task completion with evidence and quality assurance

## Execution Modes

### Systematic Strategy
1. **Discovery Phase**: Comprehensive project analysis and scope definition
2. **Planning Phase**: Hierarchical task breakdown with dependency mapping
3. **Execution Phase**: Sequential execution with validation gates
4. **Validation Phase**: Evidence collection and quality assurance
5. **Optimization Phase**: Performance analysis and improvement recommendations

### Agile Strategy
1. **Sprint Planning**: Priority-based task organization
2. **Iterative Execution**: Short cycles with continuous feedback
3. **Adaptive Planning**: Dynamic task adjustment based on outcomes
4. **Continuous Integration**: Real-time validation and testing
5. **Retrospective Analysis**: Learning and process improvement

### Enterprise Strategy
1. **Stakeholder Analysis**: Multi-domain impact assessment
2. **Resource Allocation**: Optimal resource distribution across tasks
3. **Risk Management**: Comprehensive risk assessment and mitigation
4. **Compliance Validation**: Regulatory and policy compliance checks
5. **Governance Reporting**: Detailed progress and compliance reporting

## Advanced Features

### Task Hierarchy Management
- **Epic Level**: Large-scale project objectives (weeks to months)
- **Story Level**: Feature-specific implementations (days to weeks)
- **Task Level**: Specific actionable items (hours to days)
- **Subtask Level**: Granular implementation steps (minutes to hours)

### Intelligent Task Orchestration
- **Dependency Resolution**: Automatic dependency detection and sequencing
- **Parallel Execution**: Independent task parallelization
- **Resource Optimization**: Intelligent resource allocation and scheduling
- **Context Sharing**: Cross-task context and knowledge sharing

### Cross-Session Persistence
- **Task State Management**: Persistent task states across sessions
- **Context Continuity**: Preserved context and progress tracking
- **Historical Analytics**: Task execution history and learning
- **Recovery Mechanisms**: Automatic recovery from interruptions

### Quality Gates and Validation
- **Evidence Collection**: Systematic evidence gathering during execution
- **Validation Criteria**: Customizable completion criteria
- **Quality Metrics**: Comprehensive quality assessment
- **Compliance Checks**: Automated compliance validation

## Integration Points

### Wave System Integration
- **Wave Coordination**: Multi-wave task execution strategies
- **Context Accumulation**: Progressive context building across waves
- **Performance Monitoring**: Real-time performance tracking and optimization
- **Error Recovery**: Graceful error handling and recovery mechanisms

### MCP Server Coordination
- **Context7**: Framework patterns and library documentation
- **Sequential**: Complex analysis and multi-step reasoning
- **Magic**: UI component generation and design systems
- **Playwright**: End-to-end testing and performance validation

### Persona Integration
- **Architect**: System design and architectural decisions
- **Analyzer**: Code analysis and quality assessment
- **Project Manager**: Resource allocation and progress tracking
- **Domain Experts**: Specialized expertise for specific task types

## Performance Optimization

### Execution Efficiency
- **Batch Operations**: Grouped execution for related tasks
- **Parallel Processing**: Independent task parallelization
- **Context Caching**: Reusable context and analysis results
- **Resource Pooling**: Shared resource utilization

### Intelligence Features
- **Predictive Planning**: AI-driven task estimation and planning
- **Adaptive Execution**: Dynamic strategy adjustment based on progress
- **Learning Systems**: Continuous improvement from execution patterns
- **Optimization Recommendations**: Data-driven improvement suggestions

## Examples

### Comprehensive Project Analysis
```
/sg:task create "enterprise authentication system" --strategy systematic --depth deep --validate --mcp-routing
# Comprehensive analysis with full orchestration capabilities
```

### Agile Multi-Sprint Coordination
```
/sg:task execute "feature backlog" --strategy agile --parallel --cross-session
# Agile coordination with cross-session persistence
```

### Enterprise-Scale Operation
```
/sg:task create "digital transformation" --strategy enterprise --wave-mode --all-personas
# Enterprise-scale coordination with full persona orchestration
```

### Complex Integration Project
```  
/sg:task execute "microservices platform" --depth deep --parallel --validate --sequential
# Complex integration with sequential thinking and validation
```

### Create Project-Level Task Hierarchy
```
/sg:task create "Implement user authentication system" --hierarchy --persist --strategy systematic
```

### Execute with Multi-Agent Delegation
```
/sg:task execute AUTH-001 --wave-mode --validate
```

### Analytics and Optimization
```
/sg:task analytics --project AUTH --optimization-recommendations
```

### Cross-Session Task Management
```
/sg:task status --all-sessions --detailed-breakdown
```

## Boundaries

**This advanced command will:**
- Orchestrate complex multi-domain task operations with expert coordination
- Provide sophisticated analysis and strategic task planning capabilities
- Coordinate multiple MCP servers and personas for optimal task outcomes
- Maintain cross-session persistence and progressive enhancement for task continuity
- Apply comprehensive quality gates and validation throughout task execution
- Execute complex tasks with intelligent workflow management and wave system integration
- Create hierarchical task breakdown with advanced orchestration capabilities
- Track task performance and analytics with optimization recommendations

**This advanced command will not:**
- Execute without proper analysis and planning phases for task management
- Operate without appropriate error handling and recovery mechanisms for tasks
- Proceed without stakeholder alignment and clear success criteria for task completion
- Compromise quality standards for speed or convenience in task execution

---

## Gemini CLI Integration
- **TodoWrite Integration**: Seamless session-level task coordination
- **Wave System**: Advanced multi-stage execution orchestration
- **Hook System**: Real-time task monitoring and optimization
- **MCP Coordination**: Intelligent server routing and resource utilization
- **Performance Monitoring**: Sub-100ms execution targets with comprehensive metrics

## Success Criteria
- **Task Completion Rate**: >95% successful task completion
- **Performance Targets**: <100ms hook execution, <5s task creation
- **Quality Metrics**: >90% validation success rate
- **Cross-Session Continuity**: 100% task state preservation
- **Intelligence Effectiveness**: >80% accurate predictive planning