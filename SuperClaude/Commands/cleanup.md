---
name: cleanup
description: "Clean up code, remove dead code, and optimize project structure with intelligent analysis and safety validation"
allowed-tools: [Read, Grep, Glob, Bash, Edit, MultiEdit, TodoWrite, Task]

# Command Classification
category: workflow
complexity: standard
scope: cross-file

# Integration Configuration
mcp-integration:
  servers: [sequential, context7]  # Sequential for analysis, Context7 for framework patterns
  personas: [architect, quality, security]  # Auto-activated based on cleanup type
  wave-enabled: false
  complexity-threshold: 0.7

# Performance Profile
performance-profile: standard
---

# /sg:cleanup - Code and Project Cleanup

## Purpose
Systematically clean up code, remove dead code, optimize imports, and improve project structure through intelligent analysis and safety-validated operations. This command serves as the primary maintenance engine for codebase hygiene, providing automated cleanup workflows, dead code detection, and structural optimization with comprehensive validation.

## Usage
```
/sg:cleanup [target] [--type code|imports|files|all] [--safe|--aggressive] [--interactive]
```

## Arguments
- `target` - Files, directories, or entire project to clean
- `--type` - Cleanup focus: code, imports, files, structure, all
- `--safe` - Conservative cleanup approach (default) with minimal risk
- `--interactive` - Enable user interaction for complex cleanup decisions
- `--preview` - Show cleanup changes without applying them for review
- `--validate` - Enable additional validation steps and safety checks
- `--aggressive` - More thorough cleanup with higher risk tolerance
- `--dry-run` - Alias for --preview, shows changes without execution
- `--backup` - Create backup before applying cleanup operations

## Execution Flow

### 1. Context Analysis
- Analyze target scope for cleanup opportunities and safety considerations
- Identify project patterns and existing structural conventions
- Assess complexity and potential impact of cleanup operations
- Detect framework-specific cleanup patterns and requirements

### 2. Strategy Selection
- Choose appropriate cleanup approach based on --type and safety level
- Auto-activate relevant personas for domain expertise (architecture, quality)
- Configure MCP servers for enhanced analysis and pattern recognition
- Plan cleanup sequence with comprehensive risk assessment

### 3. Core Operation
- Execute systematic cleanup workflows with appropriate safety measures
- Apply intelligent dead code detection and removal algorithms
- Coordinate multi-file cleanup operations with dependency awareness
- Handle edge cases and complex cleanup scenarios safely

### 4. Quality Assurance
- Validate cleanup results against functionality and structural requirements
- Run automated checks and testing to ensure no functionality loss
- Generate comprehensive cleanup reports and impact documentation
- Verify integration with existing codebase patterns and conventions

### 5. Integration & Handoff
- Update related documentation and configuration to reflect cleanup
- Prepare cleanup summary with recommendations for ongoing maintenance
- Persist cleanup context and optimization insights for future operations
- Enable follow-up optimization and quality improvement workflows

## MCP Server Integration

### Sequential Thinking Integration
- **Complex Analysis**: Systematic analysis of code structure and cleanup opportunities
- **Multi-Step Planning**: Breaks down complex cleanup into manageable, safe operations
- **Validation Logic**: Uses structured reasoning for safety verification and impact assessment

### Context7 Integration
- **Automatic Activation**: When framework-specific cleanup patterns and conventions are applicable
- **Library Patterns**: Leverages official documentation for framework cleanup best practices
- **Best Practices**: Integrates established cleanup standards and structural conventions

## Persona Auto-Activation

### Context-Based Activation
The command automatically activates relevant personas based on cleanup scope:

- **Architect Persona**: System structure cleanup, architectural optimization, and dependency management
- **Quality Persona**: Code quality assessment, technical debt cleanup, and maintainability improvements
- **Security Persona**: Security-sensitive cleanup, credential removal, and secure code practices

### Multi-Persona Coordination
- **Collaborative Analysis**: Multiple personas work together for comprehensive cleanup assessment
- **Expertise Integration**: Combining domain-specific knowledge for safe and effective cleanup
- **Conflict Resolution**: Handling different persona recommendations through systematic evaluation

## Advanced Features

### Task Integration
- **Complex Operations**: Use Task tool for multi-step cleanup workflows
- **Parallel Processing**: Coordinate independent cleanup work streams safely
- **Progress Tracking**: TodoWrite integration for cleanup status management

### Workflow Orchestration
- **Dependency Management**: Handle cleanup prerequisites and safe operation sequencing
- **Error Recovery**: Graceful handling of cleanup failures with rollback capabilities
- **State Management**: Maintain cleanup state across interruptions with backup preservation

### Quality Gates
- **Pre-validation**: Check code safety and backup requirements before cleanup execution
- **Progress Validation**: Intermediate safety checks during cleanup process
- **Post-validation**: Comprehensive verification of cleanup effectiveness and safety

## Performance Optimization

### Efficiency Features
- **Intelligent Batching**: Group related cleanup operations for efficiency and safety
- **Context Caching**: Reuse analysis results within session for related cleanup operations
- **Parallel Execution**: Independent cleanup operations run concurrently with safety coordination
- **Resource Management**: Optimal tool and MCP server utilization for cleanup analysis

### Performance Targets
- **Analysis Phase**: <20s for comprehensive cleanup opportunity assessment
- **Cleanup Phase**: <60s for standard code and import cleanup operations
- **Validation Phase**: <15s for safety verification and functionality testing
- **Overall Command**: <120s for complex multi-file cleanup workflows

## Examples

### Safe Code Cleanup
```
/sg:cleanup src/ --type code --safe --backup
# Conservative code cleanup with automatic backup
```

### Import Optimization
```
/sg:cleanup project --type imports --preview --validate
# Import cleanup with preview and validation
```

### Aggressive Project Cleanup
```
/sg:cleanup entire-project --type all --aggressive --interactive
# Comprehensive cleanup with user interaction for safety
```

### Dead Code Removal
```
/sg:cleanup legacy-modules --type code --dry-run
# Dead code analysis with preview of removal operations
```

## Error Handling & Recovery

### Graceful Degradation
- **MCP Server Unavailable**: Falls back to native analysis capabilities with basic cleanup patterns
- **Persona Activation Failure**: Continues with general cleanup guidance and conservative operations
- **Tool Access Issues**: Uses alternative analysis methods and provides manual cleanup guidance

### Error Categories
- **Input Validation Errors**: Clear feedback for invalid targets or conflicting cleanup parameters
- **Process Execution Errors**: Handling of cleanup failures with automatic rollback capabilities
- **Integration Errors**: MCP server or persona coordination issues with fallback strategies
- **Resource Constraint Errors**: Behavior under resource limitations with optimization suggestions

### Recovery Strategies
- **Automatic Retry**: Retry failed cleanup operations with adjusted parameters and reduced scope
- **User Intervention**: Request clarification when cleanup requirements are ambiguous
- **Partial Success Handling**: Complete partial cleanup and document remaining work safely
- **State Cleanup**: Ensure clean codebase state after cleanup failures with backup restoration

## Integration Patterns

### Command Coordination
- **Preparation Commands**: Often follows /sg:analyze or /sg:improve for cleanup planning
- **Follow-up Commands**: Commonly followed by /sg:test, /sg:improve, or /sg:validate
- **Parallel Commands**: Can run alongside /sg:optimize for comprehensive codebase maintenance

### Framework Integration
- **SuperGemini Ecosystem**: Integrates with quality gates and validation cycles
- **Quality Gates**: Participates in the 8-step validation process for cleanup verification
- **Session Management**: Maintains cleanup context across session boundaries

### Tool Coordination
- **Multi-Tool Operations**: Coordinates Grep/Glob/Edit/MultiEdit for complex cleanup operations
- **Tool Selection Logic**: Dynamic tool selection based on cleanup scope and safety requirements
- **Resource Sharing**: Efficient use of shared MCP servers and persona expertise

## Customization & Configuration

### Configuration Options
- **Default Behavior**: Conservative cleanup with comprehensive safety validation
- **User Preferences**: Cleanup aggressiveness levels and backup requirements
- **Project-Specific Settings**: Project conventions and cleanup exclusion patterns

### Extension Points
- **Custom Workflows**: Integration with project-specific cleanup standards and patterns
- **Plugin Integration**: Support for additional static analysis and cleanup tools
- **Hook Points**: Pre/post cleanup validation and custom safety checks

## Quality Standards

### Validation Criteria
- **Functional Correctness**: Cleanup preserves all existing functionality and behavior
- **Performance Standards**: Meeting cleanup effectiveness targets without functionality loss
- **Integration Compliance**: Proper integration with existing codebase and structural patterns
- **Error Handling Quality**: Comprehensive validation and rollback capabilities

### Success Metrics
- **Completion Rate**: >95% for well-defined cleanup targets and parameters
- **Performance Targets**: Meeting specified timing requirements for cleanup phases
- **User Satisfaction**: Clear cleanup results with measurable structural improvements
- **Integration Success**: Proper coordination with MCP servers and persona activation

## Boundaries

**This command will:**
- Systematically clean up code, remove dead code, and optimize project structure
- Auto-activate relevant personas and coordinate MCP servers for enhanced analysis
- Provide comprehensive safety validation with backup and rollback capabilities
- Apply intelligent cleanup algorithms with framework-specific pattern recognition

**This command will not:**
- Remove code without thorough safety analysis and validation
- Override project-specific cleanup exclusions or architectural constraints
- Apply cleanup operations that compromise functionality or introduce bugs
- Bypass established safety gates or validation requirements

---

*This cleanup command provides comprehensive codebase maintenance capabilities with intelligent analysis and systematic cleanup workflows while maintaining strict safety and validation standards.*