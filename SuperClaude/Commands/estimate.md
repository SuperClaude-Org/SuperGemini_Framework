---
name: estimate
description: "Provide development estimates for tasks, features, or projects with intelligent analysis and accuracy tracking"
allowed-tools: [read_file, search_file_content, glob, run_shell_command, TodoWrite]

# Command Classification
category: workflow
complexity: standard
scope: project

# Integration Configuration
mcp-integration:
  servers: [sequential, context7]  # Sequential for analysis, Context7 for framework patterns
  personas: [architect, performance, project-manager]  # Auto-activated based on estimation scope
  wave-enabled: false
  complexity-threshold: 0.6

# Performance Profile
performance-profile: standard
---

# /sg:estimate - Development Estimation

## Purpose
Generate accurate development estimates for tasks, features, or projects based on intelligent complexity analysis and historical data patterns. This command serves as the primary estimation engine for development planning, providing systematic estimation methodologies, accuracy tracking, and confidence intervals with comprehensive breakdown analysis.

## Usage
```
/sg:estimate [target] [--type time|effort|complexity|cost] [--unit hours|days|weeks] [--interactive]
```

## Arguments
- `target` - Task, feature, or project scope to estimate
- `--type` - Estimation focus: time, effort, complexity, cost
- `--unit` - Time unit for estimates: hours, days, weeks, sprints
- `--interactive` - Enable user interaction for complex estimation decisions
- `--preview` - Show estimation methodology without executing full analysis
- `--validate` - Enable additional validation steps and accuracy checks
- `--breakdown` - Provide detailed breakdown of estimation components
- `--confidence` - Include confidence intervals and risk assessment
- `--historical` - Use historical data patterns for accuracy improvement

## Execution Flow

### 1. Context Analysis
- Analyze scope and requirements of estimation target comprehensively
- Identify project patterns and existing complexity benchmarks
- Assess complexity factors, dependencies, and potential risks
- Detect framework-specific estimation patterns and historical data

### 2. Strategy Selection
- Choose appropriate estimation methodology based on --type and scope
- Auto-activate relevant personas for domain expertise (architecture, performance)
- Configure MCP servers for enhanced analysis and pattern recognition
- Plan estimation sequence with historical data integration

### 3. Core Operation
- Execute systematic estimation workflows with appropriate methodologies
- Apply intelligent complexity analysis and dependency mapping
- Coordinate multi-factor estimation with risk assessment
- Generate confidence intervals and accuracy metrics

### 4. Quality Assurance
- Validate estimation results against historical accuracy patterns
- Run cross-validation checks with alternative estimation methods
- Generate comprehensive estimation reports with breakdown analysis
- Verify estimation consistency with project constraints and resources

### 5. Integration & Handoff
- Update estimation database with new patterns and accuracy data
- Prepare estimation summary with recommendations for project planning
- Persist estimation context and methodology insights for future use
- Enable follow-up project planning and resource allocation workflows

## MCP Server Integration

### Sequential Thinking Integration
- **Complex Analysis**: Systematic analysis of project requirements and complexity factors
- **Multi-Step Planning**: Breaks down complex estimation into manageable analysis components
- **Validation Logic**: Uses structured reasoning for accuracy verification and methodology selection

### Context7 Integration
- **Automatic Activation**: When framework-specific estimation patterns and benchmarks are applicable
- **Library Patterns**: Leverages official documentation for framework complexity understanding
- **Best Practices**: Integrates established estimation standards and historical accuracy data

## Persona Auto-Activation

### Context-Based Activation
The command automatically activates relevant personas based on estimation scope:

- **Architect Persona**: System design estimation, architectural complexity assessment, and scalability factors
- **Performance Persona**: Performance requirements estimation, optimization effort assessment, and resource planning
- **Project Manager Persona**: Project timeline estimation, resource allocation planning, and risk assessment

### Multi-Persona Coordination
- **Collaborative Analysis**: Multiple personas work together for comprehensive estimation coverage
- **Expertise Integration**: Combining domain-specific knowledge for accurate complexity assessment
- **Conflict Resolution**: Handling different persona estimates through systematic reconciliation

## Advanced Features

### Task Integration
- **Complex Operations**: Handle multi-step estimation workflows systematically
- **Parallel Processing**: Coordinate independent estimation work streams
- **Progress Tracking**: TodoWrite integration for estimation status management

### Workflow Orchestration
- **Dependency Management**: Handle estimation prerequisites and component sequencing
- **Error Recovery**: Graceful handling of estimation failures with alternative methodologies
- **State Management**: Maintain estimation state across interruptions and revisions

### Quality Gates
- **Pre-validation**: Check estimation requirements and scope clarity before analysis
- **Progress Validation**: Intermediate accuracy checks during estimation process
- **Post-validation**: Comprehensive verification of estimation reliability and consistency

## Performance Optimization

### Efficiency Features
- **Intelligent Batching**: Group related estimation operations for efficiency
- **Context Caching**: Reuse analysis results within session for related estimations
- **Parallel Execution**: Independent estimation operations run concurrently
- **Resource Management**: Optimal tool and MCP server utilization for analysis

### Performance Targets
- **Analysis Phase**: <25s for comprehensive complexity and requirement analysis
- **Estimation Phase**: <40s for standard task and feature estimation workflows
- **Validation Phase**: <10s for accuracy verification and confidence interval calculation
- **Overall Command**: <90s for complex multi-component project estimation

## Examples

### Feature Time Estimation
```
/sg:estimate user authentication system --type time --unit days --breakdown
# Detailed time estimation with component breakdown
```

### Project Complexity Assessment
```
/sg:estimate entire-project --type complexity --confidence --historical
# Complexity analysis with confidence intervals and historical data
```

### Cost Estimation with Risk
```
/sg:estimate payment integration --type cost --breakdown --validate
# Cost estimation with detailed breakdown and validation
```

### Sprint Planning Estimation
```
/sg:estimate backlog-items --unit sprints --interactive --confidence
# Sprint planning with interactive refinement and confidence levels
```

## Error Handling & Recovery

### Graceful Degradation
- **MCP Server Unavailable**: Falls back to native analysis capabilities with basic estimation patterns
- **Persona Activation Failure**: Continues with general estimation guidance and standard methodologies
- **Tool Access Issues**: Uses alternative analysis methods and provides manual estimation guidance

### Error Categories
- **Input Validation Errors**: Clear feedback for invalid targets or conflicting estimation parameters
- **Process Execution Errors**: Handling of estimation failures with alternative methodology fallback
- **Integration Errors**: MCP server or persona coordination issues with fallback strategies
- **Resource Constraint Errors**: Behavior under resource limitations with optimization suggestions

### Recovery Strategies
- **Automatic Retry**: Retry failed estimations with adjusted parameters and alternative methods
- **User Intervention**: Request clarification when estimation requirements are ambiguous
- **Partial Success Handling**: Complete partial estimations and document remaining analysis
- **State Cleanup**: Ensure clean estimation state after failures with methodology preservation

## Integration Patterns

### Command Coordination
- **Preparation Commands**: Often follows /sg:analyze or /sg:design for estimation planning
- **Follow-up Commands**: Commonly followed by /sg:implement, /sg:plan, or project management tools
- **Parallel Commands**: Can run alongside /sg:analyze for comprehensive project assessment

### Framework Integration
- **SuperGemini Ecosystem**: Integrates with quality gates and validation cycles
- **Quality Gates**: Participates in estimation validation and accuracy verification
- **Session Management**: Maintains estimation context across session boundaries

### Tool Coordination
- **Multi-Tool Operations**: Coordinates Read/Grep/Glob for comprehensive analysis
- **Tool Selection Logic**: Dynamic tool selection based on estimation scope and methodology
- **Resource Sharing**: Efficient use of shared MCP servers and persona expertise

## Customization & Configuration

### Configuration Options
- **Default Behavior**: Conservative estimation with comprehensive breakdown analysis
- **User Preferences**: Estimation methodologies and confidence level requirements
- **Project-Specific Settings**: Historical data patterns and complexity benchmarks

### Extension Points
- **Custom Workflows**: Integration with project-specific estimation standards
- **Plugin Integration**: Support for additional estimation tools and methodologies
- **Hook Points**: Pre/post estimation validation and custom accuracy checks

## Quality Standards

### Validation Criteria
- **Functional Correctness**: Estimations accurately reflect project requirements and complexity
- **Performance Standards**: Meeting estimation accuracy targets and confidence requirements
- **Integration Compliance**: Proper integration with existing project planning and management tools
- **Error Handling Quality**: Comprehensive validation and methodology fallback capabilities

### Success Metrics
- **Completion Rate**: >95% for well-defined estimation targets and requirements
- **Performance Targets**: Meeting specified timing requirements for estimation phases
- **User Satisfaction**: Clear estimation results with actionable breakdown and confidence data
- **Integration Success**: Proper coordination with MCP servers and persona activation

## Boundaries

**This command will:**
- Generate accurate development estimates with intelligent complexity analysis
- Auto-activate relevant personas and coordinate MCP servers for enhanced estimation
- Provide comprehensive breakdown analysis with confidence intervals and risk assessment
- Apply systematic estimation methodologies with historical data integration

**This command will not:**
- Make project commitments or resource allocation decisions beyond estimation scope
- Override project-specific estimation standards or historical accuracy requirements
- Generate estimates without appropriate analysis and validation of requirements
- Bypass established estimation validation or accuracy verification requirements

---

*This estimation command provides comprehensive development planning capabilities with intelligent analysis and systematic estimation methodologies while maintaining accuracy and validation standards.*