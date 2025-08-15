---
name: explain
description: "Provide clear explanations of code, concepts, or system behavior with educational clarity and interactive learning patterns"
allowed-tools: [Read, Grep, Glob, Bash, TodoWrite, Task]

# Command Classification
category: workflow
complexity: standard
scope: cross-file

# Integration Configuration
mcp-integration:
  servers: [sequential, context7]  # Sequential for analysis, Context7 for framework documentation
  personas: [educator, architect, security]  # Auto-activated based on explanation context
  wave-enabled: false
  complexity-threshold: 0.4

# Performance Profile
performance-profile: standard
---

# /sg:explain - Code and Concept Explanation

## Purpose
Deliver clear, comprehensive explanations of code functionality, concepts, or system behavior with educational clarity and interactive learning support. This command serves as the primary knowledge transfer engine, providing adaptive explanation frameworks, clarity assessment, and progressive learning patterns with comprehensive context understanding.

## Usage
```
/sg:explain [target] [--level basic|intermediate|advanced] [--format text|diagram|examples] [--interactive]
```

## Arguments
- `target` - Code file, function, concept, or system to explain
- `--level` - Explanation complexity: basic, intermediate, advanced, expert
- `--format` - Output format: text, diagram, examples, interactive
- `--interactive` - Enable user interaction for clarification and deep-dive exploration
- `--preview` - Show explanation outline without full detailed content
- `--validate` - Enable additional validation steps for explanation accuracy
- `--context` - Additional context scope for comprehensive understanding
- `--examples` - Include practical examples and use cases
- `--diagrams` - Generate visual representations and system diagrams

## Execution Flow

### 1. Context Analysis
- Analyze target code or concept thoroughly for comprehensive understanding
- Identify key components, relationships, and complexity factors
- Assess audience level and appropriate explanation depth
- Detect framework-specific patterns and documentation requirements

### 2. Strategy Selection
- Choose appropriate explanation approach based on --level and --format
- Auto-activate relevant personas for domain expertise (educator, architect)
- Configure MCP servers for enhanced analysis and documentation access
- Plan explanation sequence with progressive complexity and clarity

### 3. Core Operation
- Execute systematic explanation workflows with appropriate clarity frameworks
- Apply educational best practices and structured learning patterns
- Coordinate multi-component explanations with logical flow
- Generate relevant examples, diagrams, and interactive elements

### 4. Quality Assurance
- Validate explanation accuracy against source code and documentation
- Run clarity checks and comprehension validation
- Generate comprehensive explanation with proper structure and flow
- Verify explanation completeness with context understanding

### 5. Integration & Handoff
- Update explanation database with reusable patterns and insights
- Prepare explanation summary with recommendations for further learning
- Persist explanation context and educational insights for future use
- Enable follow-up learning and documentation workflows

## MCP Server Integration

### Sequential Thinking Integration
- **Complex Analysis**: Systematic analysis of code structure and concept relationships
- **Multi-Step Planning**: Breaks down complex explanations into manageable learning components
- **Validation Logic**: Uses structured reasoning for accuracy verification and clarity assessment

### Context7 Integration
- **Automatic Activation**: When framework-specific explanations and official documentation are relevant
- **Library Patterns**: Leverages official documentation for accurate framework understanding
- **Best Practices**: Integrates established explanation standards and educational patterns

## Persona Auto-Activation

### Context-Based Activation
The command automatically activates relevant personas based on explanation scope:

- **Educator Persona**: Learning optimization, clarity assessment, and progressive explanation design
- **Architect Persona**: System design explanations, architectural pattern descriptions, and complexity breakdown
- **Security Persona**: Security concept explanations, vulnerability analysis, and secure coding practice descriptions

### Multi-Persona Coordination
- **Collaborative Analysis**: Multiple personas work together for comprehensive explanation coverage
- **Expertise Integration**: Combining domain-specific knowledge for accurate and clear explanations
- **Conflict Resolution**: Handling different persona approaches through systematic educational evaluation

## Advanced Features

### Task Integration
- **Complex Operations**: Handle multi-step explanation workflows systematically
- **Parallel Processing**: Coordinate independent explanation work streams
- **Progress Tracking**: TodoWrite integration for explanation completeness management

### Workflow Orchestration
- **Dependency Management**: Handle explanation prerequisites and logical sequencing
- **Error Recovery**: Graceful handling of explanation failures with alternative approaches
- **State Management**: Maintain explanation state across interruptions and refinements

### Quality Gates
- **Pre-validation**: Check explanation requirements and target clarity before analysis
- **Progress Validation**: Intermediate clarity and accuracy checks during explanation process
- **Post-validation**: Comprehensive verification of explanation completeness and educational value

## Performance Optimization

### Efficiency Features
- **Intelligent Batching**: Group related explanation operations for coherent learning flow
- **Context Caching**: Reuse analysis results within session for related explanations
- **Parallel Execution**: Independent explanation operations run concurrently with coordination
- **Resource Management**: Optimal tool and MCP server utilization for analysis and documentation

### Performance Targets
- **Analysis Phase**: <15s for comprehensive code or concept analysis
- **Explanation Phase**: <30s for standard explanation generation with examples
- **Validation Phase**: <8s for accuracy verification and clarity assessment
- **Overall Command**: <60s for complex multi-component explanation workflows

## Examples

### Basic Code Explanation
```
/sg:explain authentication.js --level basic --examples
# Clear explanation with practical examples for beginners
```

### Advanced System Architecture
```
/sg:explain microservices-system --level advanced --diagrams --interactive
# Advanced explanation with visual diagrams and interactive exploration
```

### Framework Concept Explanation
```
/sg:explain react-hooks --level intermediate --format examples --c7
# Framework-specific explanation with Context7 documentation integration
```

### Security Concept Breakdown
```
/sg:explain jwt-authentication --context security --level basic --validate
# Security-focused explanation with validation and clear context
```

## Error Handling & Recovery

### Graceful Degradation
- **MCP Server Unavailable**: Falls back to native analysis capabilities with basic explanation patterns
- **Persona Activation Failure**: Continues with general explanation guidance and standard educational patterns
- **Tool Access Issues**: Uses alternative analysis methods and provides manual explanation guidance

### Error Categories
- **Input Validation Errors**: Clear feedback for invalid targets or conflicting explanation parameters
- **Process Execution Errors**: Handling of explanation failures with alternative educational approaches
- **Integration Errors**: MCP server or persona coordination issues with fallback strategies
- **Resource Constraint Errors**: Behavior under resource limitations with optimization suggestions

### Recovery Strategies
- **Automatic Retry**: Retry failed explanations with adjusted parameters and alternative methods
- **User Intervention**: Request clarification when explanation requirements are ambiguous
- **Partial Success Handling**: Complete partial explanations and document remaining analysis
- **State Cleanup**: Ensure clean explanation state after failures with educational content preservation

## Integration Patterns

### Command Coordination
- **Preparation Commands**: Often follows /sg:analyze or /sg:document for explanation preparation
- **Follow-up Commands**: Commonly followed by /sg:implement, /sg:improve, or /sg:test
- **Parallel Commands**: Can run alongside /sg:document for comprehensive knowledge transfer

### Framework Integration
- **SuperGemini Ecosystem**: Integrates with quality gates and validation cycles
- **Quality Gates**: Participates in explanation accuracy and clarity verification
- **Session Management**: Maintains explanation context across session boundaries

### Tool Coordination
- **Multi-Tool Operations**: Coordinates Read/Grep/Glob for comprehensive analysis
- **Tool Selection Logic**: Dynamic tool selection based on explanation scope and complexity
- **Resource Sharing**: Efficient use of shared MCP servers and persona expertise

## Customization & Configuration

### Configuration Options
- **Default Behavior**: Adaptive explanation with comprehensive examples and context
- **User Preferences**: Explanation depth preferences and learning style adaptations
- **Project-Specific Settings**: Framework conventions and domain-specific explanation patterns

### Extension Points
- **Custom Workflows**: Integration with project-specific explanation standards
- **Plugin Integration**: Support for additional documentation and educational tools
- **Hook Points**: Pre/post explanation validation and custom clarity checks

## Quality Standards

### Validation Criteria
- **Functional Correctness**: Explanations accurately reflect code behavior and system functionality
- **Performance Standards**: Meeting explanation clarity targets and educational effectiveness
- **Integration Compliance**: Proper integration with existing documentation and educational resources
- **Error Handling Quality**: Comprehensive validation and alternative explanation approaches

### Success Metrics
- **Completion Rate**: >95% for well-defined explanation targets and requirements
- **Performance Targets**: Meeting specified timing requirements for explanation phases
- **User Satisfaction**: Clear explanation results with effective knowledge transfer
- **Integration Success**: Proper coordination with MCP servers and persona activation

## Boundaries

**This command will:**
- Provide clear, comprehensive explanations with educational clarity and progressive learning
- Auto-activate relevant personas and coordinate MCP servers for enhanced analysis
- Generate accurate explanations with practical examples and interactive learning support
- Apply systematic explanation methodologies with framework-specific documentation integration

**This command will not:**
- Generate explanations without thorough analysis and accuracy verification
- Override project-specific documentation standards or educational requirements
- Provide explanations that compromise security or expose sensitive implementation details
- Bypass established explanation validation or educational quality requirements

---

*This explanation command provides comprehensive knowledge transfer capabilities with intelligent analysis and systematic educational workflows while maintaining accuracy and clarity standards.*