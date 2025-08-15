---
name: index
description: "Generate comprehensive project documentation and knowledge base with intelligent organization and cross-referencing"
allowed-tools: [Read, Grep, Glob, Bash, Write, TodoWrite, Task]

# Command Classification
category: workflow
complexity: standard
scope: project

# Integration Configuration
mcp-integration:
  servers: [sequential, context7]  # Sequential for analysis, Context7 for documentation patterns
  personas: [architect, scribe, quality]  # Auto-activated based on documentation scope
  wave-enabled: false
  complexity-threshold: 0.5

# Performance Profile
performance-profile: standard
---

# /sg:index - Project Documentation

## Purpose
Create and maintain comprehensive project documentation, indexes, and knowledge bases with intelligent organization and cross-referencing capabilities. This command serves as the primary documentation generation engine, providing systematic documentation workflows, knowledge organization patterns, and automated maintenance with comprehensive project understanding.

## Usage
```
/sg:index [target] [--type docs|api|structure|readme] [--format md|json|yaml] [--interactive]
```

## Arguments
- `target` - Project directory or specific component to document
- `--type` - Documentation focus: docs, api, structure, readme, knowledge-base
- `--format` - Output format: md, json, yaml, html
- `--interactive` - Enable user interaction for complex documentation decisions
- `--preview` - Show documentation structure without generating full content
- `--validate` - Enable additional validation steps for documentation completeness
- `--update` - Update existing documentation while preserving manual additions
- `--cross-reference` - Generate comprehensive cross-references and navigation
- `--templates` - Use project-specific documentation templates and patterns

## Execution Flow

### 1. Context Analysis
- Analyze project structure and identify key documentation components
- Identify existing documentation patterns and organizational conventions
- Assess documentation scope and complexity requirements
- Detect framework-specific documentation patterns and standards

### 2. Strategy Selection
- Choose appropriate documentation approach based on --type and project structure
- Auto-activate relevant personas for domain expertise (architect, scribe)
- Configure MCP servers for enhanced analysis and documentation pattern access
- Plan documentation sequence with cross-referencing and navigation structure

### 3. Core Operation
- Execute systematic documentation workflows with appropriate organization patterns
- Apply intelligent content extraction and documentation generation algorithms
- Coordinate multi-component documentation with logical structure and flow
- Generate comprehensive cross-references and navigation systems

### 4. Quality Assurance
- Validate documentation completeness against project structure and requirements
- Run accuracy checks and consistency validation across documentation
- Generate comprehensive documentation with proper organization and formatting
- Verify documentation integration with project conventions and standards

### 5. Integration & Handoff
- Update documentation index and navigation systems
- Prepare documentation summary with maintenance recommendations
- Persist documentation context and organizational insights for future updates
- Enable follow-up documentation maintenance and knowledge management workflows

## MCP Server Integration

### Sequential Thinking Integration
- **Complex Analysis**: Systematic analysis of project structure and documentation requirements
- **Multi-Step Planning**: Breaks down complex documentation into manageable generation components
- **Validation Logic**: Uses structured reasoning for completeness verification and organization assessment

### Context7 Integration
- **Automatic Activation**: When framework-specific documentation patterns and conventions are applicable
- **Library Patterns**: Leverages official documentation for framework documentation standards
- **Best Practices**: Integrates established documentation standards and organizational patterns

## Persona Auto-Activation

### Context-Based Activation
The command automatically activates relevant personas based on documentation scope:

- **Architect Persona**: System documentation, architectural decision records, and structural organization
- **Scribe Persona**: Content creation, documentation standards, and knowledge organization optimization
- **Quality Persona**: Documentation quality assessment, completeness verification, and maintenance planning

### Multi-Persona Coordination
- **Collaborative Analysis**: Multiple personas work together for comprehensive documentation coverage
- **Expertise Integration**: Combining domain-specific knowledge for accurate and well-organized documentation
- **Conflict Resolution**: Handling different persona recommendations through systematic documentation evaluation

## Advanced Features

### Task Integration
- **Complex Operations**: Use Task tool for multi-step documentation workflows
- **Parallel Processing**: Coordinate independent documentation work streams
- **Progress Tracking**: TodoWrite integration for documentation completeness management

### Workflow Orchestration
- **Dependency Management**: Handle documentation prerequisites and logical sequencing
- **Error Recovery**: Graceful handling of documentation failures with alternative approaches
- **State Management**: Maintain documentation state across interruptions and updates

### Quality Gates
- **Pre-validation**: Check documentation requirements and project structure before generation
- **Progress Validation**: Intermediate completeness and accuracy checks during documentation process
- **Post-validation**: Comprehensive verification of documentation quality and organizational effectiveness

## Performance Optimization

### Efficiency Features
- **Intelligent Batching**: Group related documentation operations for coherent organization
- **Context Caching**: Reuse analysis results within session for related documentation components
- **Parallel Execution**: Independent documentation operations run concurrently with coordination
- **Resource Management**: Optimal tool and MCP server utilization for analysis and generation

### Performance Targets
- **Analysis Phase**: <30s for comprehensive project structure and requirement analysis
- **Documentation Phase**: <90s for standard project documentation generation workflows
- **Validation Phase**: <20s for completeness verification and quality assessment
- **Overall Command**: <180s for complex multi-component documentation generation

## Examples

### Project Structure Documentation
```
/sg:index project-root --type structure --format md --cross-reference
# Comprehensive project structure documentation with navigation
```

### API Documentation Generation
```
/sg:index src/api --type api --format json --validate --update
# API documentation with validation and existing documentation updates
```

### Knowledge Base Creation
```
/sg:index entire-project --type knowledge-base --interactive --templates
# Interactive knowledge base generation with project templates
```

### README Generation
```
/sg:index . --type readme --format md --c7 --cross-reference
# README generation with Context7 framework patterns and cross-references
```

## Error Handling & Recovery

### Graceful Degradation
- **MCP Server Unavailable**: Falls back to native analysis capabilities with basic documentation patterns
- **Persona Activation Failure**: Continues with general documentation guidance and standard organizational patterns
- **Tool Access Issues**: Uses alternative analysis methods and provides manual documentation guidance

### Error Categories
- **Input Validation Errors**: Clear feedback for invalid targets or conflicting documentation parameters
- **Process Execution Errors**: Handling of documentation failures with alternative generation approaches
- **Integration Errors**: MCP server or persona coordination issues with fallback strategies
- **Resource Constraint Errors**: Behavior under resource limitations with optimization suggestions

### Recovery Strategies
- **Automatic Retry**: Retry failed documentation operations with adjusted parameters and alternative methods
- **User Intervention**: Request clarification when documentation requirements are ambiguous
- **Partial Success Handling**: Complete partial documentation and document remaining analysis
- **State Cleanup**: Ensure clean documentation state after failures with content preservation

## Integration Patterns

### Command Coordination
- **Preparation Commands**: Often follows /sg:analyze or /sg:explain for documentation preparation
- **Follow-up Commands**: Commonly followed by /sg:validate, /sg:improve, or knowledge management workflows
- **Parallel Commands**: Can run alongside /sg:explain for comprehensive knowledge transfer

### Framework Integration
- **SuperGemini Ecosystem**: Integrates with quality gates and validation cycles
- **Quality Gates**: Participates in documentation completeness and quality verification
- **Session Management**: Maintains documentation context across session boundaries

### Tool Coordination
- **Multi-Tool Operations**: Coordinates Read/Grep/Glob/Write for comprehensive documentation
- **Tool Selection Logic**: Dynamic tool selection based on documentation scope and format requirements
- **Resource Sharing**: Efficient use of shared MCP servers and persona expertise

## Customization & Configuration

### Configuration Options
- **Default Behavior**: Comprehensive documentation with intelligent organization and cross-referencing
- **User Preferences**: Documentation depth preferences and organizational style adaptations
- **Project-Specific Settings**: Framework conventions and domain-specific documentation patterns

### Extension Points
- **Custom Workflows**: Integration with project-specific documentation standards
- **Plugin Integration**: Support for additional documentation tools and formats
- **Hook Points**: Pre/post documentation validation and custom organization checks

## Quality Standards

### Validation Criteria
- **Functional Correctness**: Documentation accurately reflects project structure and functionality
- **Performance Standards**: Meeting documentation completeness targets and organizational effectiveness
- **Integration Compliance**: Proper integration with existing documentation and project standards
- **Error Handling Quality**: Comprehensive validation and alternative documentation approaches

### Success Metrics
- **Completion Rate**: >95% for well-defined documentation targets and requirements
- **Performance Targets**: Meeting specified timing requirements for documentation phases
- **User Satisfaction**: Clear documentation results with effective knowledge organization
- **Integration Success**: Proper coordination with MCP servers and persona activation

## Boundaries

**This command will:**
- Generate comprehensive project documentation with intelligent organization and cross-referencing
- Auto-activate relevant personas and coordinate MCP servers for enhanced analysis
- Provide systematic documentation workflows with quality validation and maintenance support
- Apply intelligent content extraction with framework-specific documentation standards

**This command will not:**
- Override existing manual documentation without explicit update permission
- Generate documentation that conflicts with project-specific standards or security requirements
- Create documentation without appropriate analysis and validation of project structure
- Bypass established documentation validation or quality requirements

---

*This index command provides comprehensive documentation generation capabilities with intelligent analysis and systematic organization workflows while maintaining quality and standards compliance.*