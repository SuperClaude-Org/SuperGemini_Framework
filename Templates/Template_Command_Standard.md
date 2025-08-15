---
name: [command-name]
description: "[Clear description for help systems and auto-activation patterns with workflow context]"
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Grep, Glob, TodoWrite, Task]

# Command Classification
category: workflow
complexity: standard
scope: [project|cross-file]

# Integration Configuration
mcp-integration:
  servers: [context7, sequential]  # Optional MCP servers for enhanced capabilities
  personas: [architect, frontend, backend, security]  # Auto-activated based on context
  wave-enabled: false
  complexity-threshold: 0.5

# Performance Profile
performance-profile: standard
---

# /sg:[command-name] - [Command Title]

## Purpose
[Clear statement of what this command does in the context of development workflows. Explain how it fits into typical development processes and when it provides the most value.]

## Usage
```
/sg:[command-name] [target] [--type option1|option2|option3] [--safe] [--interactive]
```

## Arguments
- `target` - [Description of the target: files, directories, or project scope]
- `--type` - [Workflow type or approach selection]
- `--safe` - [Conservative approach with minimal risk]
- `--interactive` - [Enable user interaction for complex decisions]
- `--preview` - [Show changes without applying them]
- `--validate` - [Enable additional validation steps]

## Execution Flow

### 1. Context Analysis
- Analyze target scope and detect relevant technologies
- Identify project patterns and existing conventions
- Assess complexity and potential impact of operation

### 2. Strategy Selection
- Choose appropriate approach based on --type and context
- Auto-activate relevant personas for domain expertise
- Configure MCP servers for enhanced capabilities

### 3. Core Operation
- Execute primary workflow with appropriate validation
- Apply domain-specific best practices and patterns
- Monitor progress and handle edge cases

### 4. Quality Assurance  
- Validate results against requirements and standards
- Run automated checks and testing where applicable
- Generate comprehensive feedback and recommendations

### 5. Integration & Handoff
- Update related documentation and configuration
- Prepare for follow-up commands or next steps
- Persist relevant context for future operations

## MCP Server Integration

### Context7 Integration
- **Automatic Activation**: [When Context7 enhances command capabilities]
- **Library Patterns**: [How the command leverages framework documentation]
- **Best Practices**: [Integration with established patterns and conventions]

### Sequential Thinking Integration  
- **Complex Analysis**: [When Sequential thinking provides systematic analysis]
- **Multi-Step Planning**: [How Sequential breaks down complex operations]
- **Validation Logic**: [Use of Sequential for verification and quality checks]

## Persona Auto-Activation

### Context-Based Activation
The command automatically activates relevant personas based on detected context:

- **Architect Persona**: [When architectural decisions or system design are involved]
- **Frontend Persona**: [For UI/UX related operations and client-side concerns]
- **Backend Persona**: [For server-side logic, APIs, and data operations]
- **Security Persona**: [When security considerations are paramount]

### Multi-Persona Coordination
- **Collaborative Analysis**: [How multiple personas work together]
- **Expertise Integration**: [Combining domain-specific knowledge]
- **Conflict Resolution**: [Handling different persona recommendations]

## Advanced Features

### Task Integration
- **Complex Operations**: Use Task tool for multi-step workflows
- **Parallel Processing**: Coordinate independent work streams
- **Progress Tracking**: TodoWrite integration for status management

### Workflow Orchestration
- **Dependency Management**: Handle prerequisites and sequencing
- **Error Recovery**: Graceful handling of failures and rollbacks  
- **State Management**: Maintain operation state across interruptions

### Quality Gates
- **Pre-validation**: Check requirements before execution
- **Progress Validation**: Intermediate quality checks
- **Post-validation**: Comprehensive results verification

## Performance Optimization

### Efficiency Features
- **Intelligent Batching**: Group related operations for efficiency
- **Context Caching**: Reuse analysis results within session
- **Parallel Execution**: Independent operations run concurrently
- **Resource Management**: Optimal tool and server utilization

### Performance Targets
- **Analysis Phase**: <10s for project-level analysis
- **Execution Phase**: <30s for standard operations
- **Validation Phase**: <5s for quality checks
- **Overall Command**: <60s for complex workflows

## Examples

### Basic Workflow
```
/sg:[command-name] src/components --type standard
# Standard workflow with automatic persona activation
```

### Safe Mode Operation
```
/sg:[command-name] entire-project --safe --preview
# Conservative approach with preview of changes
```

### Interactive Complex Operation
```
/sg:[command-name] src --interactive --validate --type advanced
# Interactive mode with enhanced validation
```

### Framework-Specific Operation
```
/sg:[command-name] frontend-app --type react --c7
# Leverage Context7 for React-specific patterns
```

## Error Handling & Recovery

### Graceful Degradation
- **MCP Server Unavailable**: [Fallback behavior when servers are offline]
- **Persona Activation Failure**: [Default behavior without persona enhancement]
- **Tool Access Issues**: [Alternative approaches when tools are unavailable]

### Error Categories
- **Input Validation Errors**: [Clear feedback for invalid inputs]
- **Process Execution Errors**: [Handling of runtime failures]
- **Integration Errors**: [MCP server or persona coordination issues]
- **Resource Constraint Errors**: [Behavior under resource limitations]

### Recovery Strategies
- **Automatic Retry**: [When and how automatic retry is attempted]
- **User Intervention**: [When user input is required for recovery]
- **Partial Success Handling**: [Managing partially completed operations]
- **State Cleanup**: [Ensuring clean state after failures]

## Integration Patterns

### Command Coordination
- **Preparation Commands**: [Commands typically run before this one]
- **Follow-up Commands**: [Commands that commonly follow this one]
- **Parallel Commands**: [Commands that can run simultaneously]

### Framework Integration
- **SuperGemini Ecosystem**: [How this fits into the broader framework]
- **Quality Gates**: [Integration with validation cycles]
- **Session Management**: [Interaction with session lifecycle]

### Tool Coordination
- **Multi-Tool Operations**: [How different tools work together]
- **Tool Selection Logic**: [Dynamic tool selection based on context]
- **Resource Sharing**: [Efficient use of shared resources]

## Customization & Configuration

### Configuration Options
- **Default Behavior**: [Standard operation mode]
- **User Preferences**: [How user preferences affect behavior]
- **Project-Specific Settings**: [Project-level customization]

### Extension Points
- **Custom Workflows**: [How to extend with custom logic]
- **Plugin Integration**: [Integration with external tools]
- **Hook Points**: [Where custom logic can be inserted]

## Quality Standards

### Validation Criteria
- **Functional Correctness**: [Ensuring the command achieves its purpose]
- **Performance Standards**: [Meeting performance targets]
- **Integration Compliance**: [Proper integration with ecosystem]
- **Error Handling Quality**: [Comprehensive error management]

### Success Metrics
- **Completion Rate**: >95% for well-formed inputs
- **Performance Targets**: Meeting specified timing requirements
- **User Satisfaction**: Clear feedback and expected outcomes
- **Integration Success**: Proper coordination with other components

## Boundaries

**This command will:**
- [Primary capability with workflow integration]
- [Secondary capability with persona support]
- [Quality assurance and validation capability]
- [Integration and handoff capability]

**This command will not:**
- [Limitation related to scope boundaries]
- [Limitation related to complexity boundaries]
- [Limitation related to safety boundaries]
- [Limitation related to tool boundaries]

---

# Template Usage Guidelines

## Implementation Steps
1. **Copy Template**: Use this for workflow commands requiring moderate complexity
2. **Configure Integration**: Set up MCP servers and persona activation patterns
3. **Define Workflows**: Specify the main execution flow and edge cases
4. **Test Integration**: Validate MCP server coordination and persona activation
5. **Performance Validation**: Ensure the command meets performance targets

## MCP Integration Guidelines

### Context7 Integration
- Use for framework-specific patterns and best practices
- Leverage library documentation and example patterns
- Enable automatic activation for technology-specific contexts

### Sequential Integration
- Apply for complex multi-step analysis and planning
- Use for systematic validation and quality checking
- Enable for operations requiring structured reasoning

### Persona Coordination
- Define clear activation criteria for each persona
- Handle multi-persona scenarios with coordination logic
- Provide fallback behavior when personas are unavailable

## Quality Checklist
- [ ] All MCP integration points are documented
- [ ] Persona activation logic is clearly defined
- [ ] Performance targets are realistic and measurable
- [ ] Error handling covers all integration failure modes
- [ ] Tool coordination is efficient and resource-aware
- [ ] Examples demonstrate real-world usage patterns

---

*This template is designed for standard workflow commands that benefit from MCP integration and persona activation while maintaining moderate complexity. Use higher-tier templates for advanced orchestration or session management needs.*