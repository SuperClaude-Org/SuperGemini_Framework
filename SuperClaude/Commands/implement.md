---
name: implement
description: "Feature and code implementation with intelligent persona activation and comprehensive MCP integration for development workflows"
allowed-tools: [read_file, write_file, replace, run_shell_command, search_file_content, glob]

# Command Classification
category: workflow
complexity: standard
scope: cross-file

# Integration Configuration
mcp-integration:
  servers: [context7, sequential, magic, playwright]  # Enhanced capabilities for implementation
  personas: [architect, frontend, backend, security, qa-specialist]  # Auto-activated based on context
  wave-enabled: false
  complexity-threshold: 0.5

# Performance Profile
performance-profile: standard
---

# /sg:implement - Feature Implementation

## Purpose
Implement features, components, and code functionality with intelligent expert activation and comprehensive development support. This command serves as the primary implementation engine in development workflows, providing automated persona activation, MCP server coordination, and best practices enforcement throughout the implementation process.

## Usage
```
/sg:implement [feature-description] [--type component|api|service|feature] [--framework react|vue|express|etc] [--safe] [--interactive]
```

## Arguments
- `feature-description` - Description of what to implement (required)
- `--type` - Implementation type: component, api, service, feature, module
- `--framework` - Target framework or technology stack
- `--safe` - Use conservative implementation approach with minimal risk
- `--interactive` - Enable user interaction for complex implementation decisions
- `--preview` - Show implementation plan without executing
- `--validate` - Enable additional validation steps and quality checks
- `--iterative` - Enable iterative development with validation steps
- `--with-tests` - Include test implementation alongside feature code
- `--documentation` - Generate documentation alongside implementation

## Execution Flow

### 1. Context Analysis
- Analyze implementation requirements and detect technology context
- Identify project patterns and existing conventions
- Assess complexity and potential impact of implementation
- Detect framework and library dependencies automatically

### 2. Strategy Selection
- Choose appropriate implementation approach based on --type and context
- Auto-activate relevant personas for domain expertise (frontend, backend, security)
- Configure MCP servers for enhanced capabilities (Magic for UI, Context7 for patterns)
- Plan implementation sequence and dependency management

### 3. Core Operation
- Generate implementation code with framework-specific best practices
- Apply security and quality validation throughout development
- Coordinate multi-file implementations with proper integration
- Handle edge cases and error scenarios proactively

### 4. Quality Assurance
- Validate implementation against requirements and standards
- Run automated checks and linting where applicable
- Verify integration with existing codebase patterns
- Generate comprehensive feedback and improvement recommendations

### 5. Integration & Handoff
- Update related documentation and configuration files
- Provide testing recommendations and validation steps
- Prepare for follow-up commands or next development phases
- Persist implementation context for future operations

## MCP Server Integration

### Context7 Integration
- **Automatic Activation**: When external frameworks or libraries are detected in implementation requirements
- **Library Patterns**: Leverages official documentation for React, Vue, Angular, Express, and other frameworks
- **Best Practices**: Integrates established patterns and conventions from framework documentation

### Sequential Thinking Integration
- **Complex Analysis**: Applies systematic analysis for multi-component implementations
- **Multi-Step Planning**: Breaks down complex features into manageable implementation steps
- **Validation Logic**: Uses structured reasoning for quality checks and integration verification

### Magic Integration
- **UI Component Generation**: Automatically activates for frontend component implementations
- **Design System Integration**: Applies design tokens and component patterns
- **Responsive Implementation**: Ensures mobile-first and accessibility compliance

## Persona Auto-Activation

### Context-Based Activation
The command automatically activates relevant personas based on detected context:

- **Architect Persona**: System design, module structure, architectural decisions, and scalability considerations
- **Frontend Persona**: UI components, React/Vue/Angular development, client-side logic, and user experience
- **Backend Persona**: APIs, services, database integration, server-side logic, and data processing
- **Security Persona**: Authentication, authorization, data protection, input validation, and security best practices

### Multi-Persona Coordination
- **Collaborative Analysis**: Multiple personas work together for full-stack implementations
- **Expertise Integration**: Combining domain-specific knowledge for comprehensive solutions
- **Conflict Resolution**: Handling different persona recommendations through systematic evaluation

## Advanced Features

### Task Integration
- **Complex Operations**: Handle multi-step implementation workflows systematically
- **Parallel Processing**: Coordinate independent implementation work streams
- **Progress Tracking**: TodoWrite integration for implementation status management

### Workflow Orchestration
- **Dependency Management**: Handle prerequisites and implementation sequencing
- **Error Recovery**: Graceful handling of implementation failures and rollbacks
- **State Management**: Maintain implementation state across interruptions

### Quality Gates
- **Pre-validation**: Check requirements and dependencies before implementation
- **Progress Validation**: Intermediate quality checks during development
- **Post-validation**: Comprehensive results verification and integration testing

## Performance Optimization

### Efficiency Features
- **Intelligent Batching**: Group related implementation operations for efficiency
- **Context Caching**: Reuse analysis results within session for related implementations
- **Parallel Execution**: Independent implementation operations run concurrently
- **Resource Management**: Optimal tool and MCP server utilization

### Performance Targets
- **Analysis Phase**: <10s for feature requirement analysis
- **Implementation Phase**: <30s for standard component/API implementations
- **Validation Phase**: <5s for quality checks and integration verification
- **Overall Command**: <60s for complex multi-component implementations

## Examples

### Basic Component Implementation
```
/sg:implement user profile component --type component --framework react
# React component with persona activation and Magic integration
```

### API Service Implementation
```
/sg:implement user authentication API --type api --safe --with-tests
# Backend API with security persona and comprehensive validation
```

### Full Feature Implementation
```
/sg:implement payment processing system --type feature --iterative --documentation
# Complex feature with multi-persona coordination and iterative development
```

### Framework-Specific Implementation
```
/sg:implement dashboard widget --type component --framework vue --c7
# Vue component leveraging Context7 for Vue-specific patterns
```

## Error Handling & Recovery

### Graceful Degradation
- **MCP Server Unavailable**: Falls back to native Gemini CLI capabilities with reduced automation
- **Persona Activation Failure**: Continues with general development guidance and best practices
- **Tool Access Issues**: Uses alternative tools and provides manual implementation guidance

### Error Categories
- **Input Validation Errors**: Clear feedback for invalid feature descriptions or conflicting parameters
- **Process Execution Errors**: Handling of implementation failures with rollback capabilities
- **Integration Errors**: MCP server or persona coordination issues with fallback strategies
- **Resource Constraint Errors**: Behavior under resource limitations with optimization suggestions

### Recovery Strategies
- **Automatic Retry**: Retry failed operations with adjusted parameters and reduced complexity
- **User Intervention**: Request clarification when implementation requirements are ambiguous
- **Partial Success Handling**: Complete partial implementations and document remaining work
- **State Cleanup**: Ensure clean codebase state after implementation failures

## Integration Patterns

### Command Coordination
- **Preparation Commands**: Often follows /sg:design or /sg:analyze for implementation planning
- **Follow-up Commands**: Commonly followed by /sg:test, /sg:improve, or /sg:document
- **Parallel Commands**: Can run alongside /sg:estimate for development planning

### Framework Integration
- **SuperGemini Ecosystem**: Integrates with quality gates and validation cycles
- **Quality Gates**: Participates in the 8-step validation process
- **Session Management**: Maintains implementation context across session boundaries

### Tool Coordination
- **Multi-Tool Operations**: Coordinates Write/Edit/MultiEdit for complex implementations
- **Tool Selection Logic**: Dynamic tool selection based on implementation scope and complexity
- **Resource Sharing**: Efficient use of shared MCP servers and persona expertise

## Customization & Configuration

### Configuration Options
- **Default Behavior**: Automatic persona activation with conservative implementation approach
- **User Preferences**: Framework preferences and coding style enforcement
- **Project-Specific Settings**: Project conventions and architectural patterns

### Extension Points
- **Custom Workflows**: Integration with project-specific implementation patterns
- **Plugin Integration**: Support for additional frameworks and libraries
- **Hook Points**: Pre/post implementation validation and custom quality checks

## Quality Standards

### Validation Criteria
- **Functional Correctness**: Implementation meets specified requirements and handles edge cases
- **Performance Standards**: Meeting framework-specific performance targets and best practices
- **Integration Compliance**: Proper integration with existing codebase and architectural patterns
- **Error Handling Quality**: Comprehensive error management and graceful degradation

### Success Metrics
- **Completion Rate**: >95% for well-formed feature descriptions and requirements
- **Performance Targets**: Meeting specified timing requirements for implementation phases
- **User Satisfaction**: Clear implementation results with expected functionality
- **Integration Success**: Proper coordination with MCP servers and persona activation

## Boundaries

**This command will:**
- Implement features, components, and code functionality with intelligent automation
- Auto-activate relevant personas and coordinate MCP servers for enhanced capabilities
- Apply framework-specific best practices and security validation throughout development
- Provide comprehensive implementation with testing recommendations and documentation

**This command will not:**
- Make architectural decisions without appropriate persona consultation and validation
- Implement features that conflict with existing security policies or architectural constraints
- Override user-specified safety constraints or project-specific implementation guidelines
- Create implementations that bypass established quality gates or validation requirements

---

*This implementation command provides comprehensive development capabilities with intelligent persona activation and MCP integration while maintaining safety and quality standards throughout the implementation process.*