---
name: improve
description: "Apply systematic improvements to code quality, performance, and maintainability with intelligent analysis and refactoring patterns"
allowed-tools: [read_file, search_file_content, glob, replace, TodoWrite]

# Command Classification
category: workflow
complexity: standard
scope: cross-file

# Integration Configuration
mcp-integration:
  servers: [sequential, context7]  # Sequential for analysis, Context7 for best practices
  personas: [architect, performance, quality, security]  # Auto-activated based on improvement type
  wave-enabled: false
  complexity-threshold: 0.6

# Performance Profile
performance-profile: standard
---

# /sg:improve - Code Improvement

## Purpose
Apply systematic improvements to code quality, performance, maintainability, and best practices through intelligent analysis and targeted refactoring. This command serves as the primary quality enhancement engine, providing automated assessment workflows, quality metrics analysis, and systematic improvement application with safety validation.

## Usage
```
/sg:improve [target] [--type quality|performance|maintainability|style] [--safe] [--interactive]
```

## Arguments
- `target` - Files, directories, or project scope to improve
- `--type` - Improvement focus: quality, performance, maintainability, style, security
- `--safe` - Apply only safe, low-risk improvements with minimal impact
- `--interactive` - Enable user interaction for complex improvement decisions
- `--preview` - Show improvements without applying them for review
- `--validate` - Enable additional validation steps and quality verification
- `--metrics` - Generate detailed quality metrics and improvement tracking
- `--iterative` - Apply improvements in multiple passes with validation

## Execution Flow

### 1. Context Analysis
- Analyze codebase for improvement opportunities and quality issues
- Identify project patterns and existing quality standards
- Assess complexity and potential impact of proposed improvements
- Detect framework-specific optimization opportunities

### 2. Strategy Selection
- Choose appropriate improvement approach based on --type and context
- Auto-activate relevant personas for domain expertise (performance, security, quality)
- Configure MCP servers for enhanced analysis capabilities
- Plan improvement sequence with risk assessment and validation

### 3. Core Operation
- Execute systematic improvement workflows with appropriate validation
- Apply domain-specific best practices and optimization patterns
- Monitor progress and handle complex refactoring scenarios
- Coordinate multi-file improvements with dependency awareness

### 4. Quality Assurance
- Validate improvements against quality standards and requirements
- Run automated checks and testing to ensure functionality preservation
- Generate comprehensive metrics and improvement documentation
- Verify integration with existing codebase patterns and conventions

### 5. Integration & Handoff
- Update related documentation and configuration to reflect improvements
- Prepare improvement summary and recommendations for future work
- Persist improvement context and quality metrics for tracking
- Enable follow-up optimization and maintenance workflows

## MCP Server Integration

### Sequential Thinking Integration
- **Complex Analysis**: Systematic analysis of code quality issues and improvement opportunities
- **Multi-Step Planning**: Breaks down complex refactoring into manageable improvement steps
- **Validation Logic**: Uses structured reasoning for quality verification and impact assessment

### Context7 Integration
- **Automatic Activation**: When framework-specific improvements and best practices are applicable
- **Library Patterns**: Leverages official documentation for framework optimization patterns
- **Best Practices**: Integrates established quality standards and coding conventions

## Persona Auto-Activation

### Context-Based Activation
The command automatically activates relevant personas based on improvement type:

- **Architect Persona**: System design improvements, architectural refactoring, and structural optimization
- **Performance Persona**: Performance optimization, bottleneck analysis, and scalability improvements
- **Quality Persona**: Code quality assessment, maintainability improvements, and technical debt reduction
- **Security Persona**: Security vulnerability fixes, secure coding practices, and data protection improvements

### Multi-Persona Coordination
- **Collaborative Analysis**: Multiple personas work together for comprehensive quality improvements
- **Expertise Integration**: Combining domain-specific knowledge for holistic optimization
- **Conflict Resolution**: Handling different persona recommendations through systematic evaluation

## Advanced Features

### Task Integration
- **Complex Operations**: Handle multi-step improvement workflows systematically
- **Parallel Processing**: Coordinate independent improvement work streams
- **Progress Tracking**: TodoWrite integration for improvement status management

### Workflow Orchestration
- **Dependency Management**: Handle improvement prerequisites and sequencing
- **Error Recovery**: Graceful handling of improvement failures and rollbacks
- **State Management**: Maintain improvement state across interruptions

### Quality Gates
- **Pre-validation**: Check code quality baseline before improvement execution
- **Progress Validation**: Intermediate quality checks during improvement process
- **Post-validation**: Comprehensive verification of improvement effectiveness

## Performance Optimization

### Efficiency Features
- **Intelligent Batching**: Group related improvement operations for efficiency
- **Context Caching**: Reuse analysis results within session for related improvements
- **Parallel Execution**: Independent improvement operations run concurrently
- **Resource Management**: Optimal tool and MCP server utilization

### Performance Targets
- **Analysis Phase**: <15s for comprehensive code quality assessment
- **Improvement Phase**: <45s for standard quality and performance improvements
- **Validation Phase**: <10s for quality verification and testing
- **Overall Command**: <90s for complex multi-file improvement workflows

## Examples

### Quality Improvement
```
/sg:improve src/ --type quality --safe --metrics
# Safe quality improvements with detailed metrics tracking
```

### Performance Optimization
```
/sg:improve backend/api --type performance --iterative --validate
# Performance improvements with iterative validation
```

### Style and Maintainability
```
/sg:improve entire-project --type maintainability --preview
# Project-wide maintainability improvements with preview
```

### Security Hardening
```
/sg:improve auth-module --type security --interactive --validate
# Security improvements with interactive validation
```

## Error Handling & Recovery

### Graceful Degradation
- **MCP Server Unavailable**: Falls back to native analysis capabilities with basic improvement patterns
- **Persona Activation Failure**: Continues with general improvement guidance and standard practices
- **Tool Access Issues**: Uses alternative analysis methods and provides manual guidance

### Error Categories
- **Input Validation Errors**: Clear feedback for invalid targets or conflicting improvement parameters
- **Process Execution Errors**: Handling of improvement failures with rollback capabilities
- **Integration Errors**: MCP server or persona coordination issues with fallback strategies
- **Resource Constraint Errors**: Behavior under resource limitations with optimization suggestions

### Recovery Strategies
- **Automatic Retry**: Retry failed improvements with adjusted parameters and reduced scope
- **User Intervention**: Request clarification when improvement requirements are ambiguous
- **Partial Success Handling**: Complete partial improvements and document remaining work
- **State Cleanup**: Ensure clean codebase state after improvement failures

## Integration Patterns

### Command Coordination
- **Preparation Commands**: Often follows /sg:analyze or /sg:estimate for improvement planning
- **Follow-up Commands**: Commonly followed by /sg:test, /sg:validate, or /sg:document
- **Parallel Commands**: Can run alongside /sg:cleanup for comprehensive codebase enhancement

### Framework Integration
- **SuperGemini Ecosystem**: Integrates with quality gates and validation cycles
- **Quality Gates**: Participates in the 8-step validation process for improvement verification
- **Session Management**: Maintains improvement context across session boundaries

### Tool Coordination
- **Multi-Tool Operations**: Coordinates Read/Edit/MultiEdit for complex improvements
- **Tool Selection Logic**: Dynamic tool selection based on improvement scope and complexity
- **Resource Sharing**: Efficient use of shared MCP servers and persona expertise

## Customization & Configuration

### Configuration Options
- **Default Behavior**: Conservative improvements with comprehensive validation
- **User Preferences**: Quality standards and improvement priorities
- **Project-Specific Settings**: Project conventions and architectural guidelines

### Extension Points
- **Custom Workflows**: Integration with project-specific quality standards
- **Plugin Integration**: Support for additional linting and quality tools
- **Hook Points**: Pre/post improvement validation and custom quality checks

## Quality Standards

### Validation Criteria
- **Functional Correctness**: Improvements preserve existing functionality and behavior
- **Performance Standards**: Meeting quality improvement targets and metrics
- **Integration Compliance**: Proper integration with existing codebase and patterns
- **Error Handling Quality**: Comprehensive validation and rollback capabilities

### Success Metrics
- **Completion Rate**: >95% for well-defined improvement targets and parameters
- **Performance Targets**: Meeting specified timing requirements for improvement phases
- **User Satisfaction**: Clear improvement results with measurable quality gains
- **Integration Success**: Proper coordination with MCP servers and persona activation

## Boundaries

**This command will:**
- Apply systematic improvements to code quality, performance, and maintainability
- Auto-activate relevant personas and coordinate MCP servers for enhanced analysis
- Provide comprehensive quality assessment with metrics and improvement tracking
- Ensure safe improvement application with validation and rollback capabilities

**This command will not:**
- Make breaking changes without explicit user approval and validation
- Override project-specific quality standards or architectural constraints
- Apply improvements that compromise security or introduce technical debt
- Bypass established quality gates or validation requirements

---

*This improvement command provides comprehensive code quality enhancement capabilities with intelligent analysis and systematic improvement workflows while maintaining safety and validation standards.*