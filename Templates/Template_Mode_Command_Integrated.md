---
name: [mode-name]
description: "[Clear purpose and behavioral modification description]"
type: command-integrated

# Mode Classification
category: [orchestration|coordination|behavioral|processing]
complexity: [standard|advanced|enterprise]
scope: [session|cross-session|project|system]

# Activation Configuration
activation:
  automatic: [true|false]
  manual-flags: [list of flags]
  confidence-threshold: [0.0-1.0]
  detection-patterns: [list of trigger patterns]

# Integration Configuration
framework-integration:
  mcp-servers: [list of coordinated servers]
  commands: [primary command integration]
  modes: [list of coordinated modes]
  quality-gates: [list of quality integration points]

# Performance Profile
performance-profile: [standard|optimized|enterprise]
---

# [Mode Name] Mode

**[Optional Subtitle]** - [Brief description emphasizing command integration and behavioral framework]

## Purpose

[Comprehensive description explaining the behavioral framework mode and its integration with the primary command. Should cover:]
- Primary behavioral modification provided
- Command integration relationship and coordination
- Cross-session capabilities and persistence
- Agent orchestration and handoff workflows

## Core Behavioral Framework

### 1. [Primary Behavioral Category]
- **[Behavioral Feature]**: [Description of behavioral modification]
- **[Behavioral Feature]**: [Description of behavioral modification]
- **[Behavioral Feature]**: [Description of behavioral modification]
- **[Behavioral Feature]**: [Description of behavioral modification]

### 2. [Integration Capabilities Category]
- **[Integration Feature]**: [Description of integration capability]
- **[Integration Feature]**: [Description of integration capability]
- **[Integration Feature]**: [Description of integration capability]
- **[Integration Feature]**: [Description of integration capability]

### 3. [Configuration Management Category]
- **[Configuration Feature]**: [Description of configuration management]
- **[Configuration Feature]**: [Description of configuration management]
- **[Configuration Feature]**: [Description of configuration management]
- **[Configuration Feature]**: [Description of configuration management]

## Mode Activation

### Automatic Activation Patterns
[Mode Name] Mode auto-activates when SuperGemini detects:

1. **[Pattern Category]**: [Description and examples of trigger patterns]
2. **[Pattern Category]**: [Description and examples of trigger patterns]
3. **[Pattern Category]**: [Description and examples of trigger patterns]
4. **[Pattern Category]**: [Description and examples of trigger patterns]
5. **[Pattern Category]**: [Description and examples of trigger patterns]

### Manual Activation
- **Primary Flag**: `--[primary-flag]` or `--[shorthand]`
- **Integration**: Works with [primary-command] command for explicit invocation
- **Fallback Control**: `--no-[mode-name]` disables automatic activation

### Command Integration
- **Primary Implementation**: [primary-command] command handles execution workflow
- **Mode Responsibility**: Behavioral configuration and auto-activation logic
- **Workflow Reference**: See [primary-command] for detailed [workflow-type] phases and execution steps

## Framework Integration

### SuperGemini Mode Coordination
- **[Related Mode]**: [Description of coordination relationship]
- **[Related Mode]**: [Description of coordination relationship]
- **[Related Mode]**: [Description of coordination relationship]

### MCP Server Integration
- **[Server Name]**: [Description of server coordination and purpose]
- **[Server Name]**: [Description of server coordination and purpose]
- **[Server Name]**: [Description of server coordination and purpose]

### Quality Gate Integration
- **Step [X.X]**: [Description of quality gate integration point]
- **Step [X.X]**: [Description of quality gate integration point]
- **Continuous**: [Description of ongoing quality monitoring]

### Agent Orchestration
- **[Orchestration Type]**: [Description of agent coordination]
- **[Orchestration Type]**: [Description of agent coordination]
- **[Orchestration Type]**: [Description of agent coordination]

## [Mode-Specific Integration Pattern]

**[Integration Pattern Name]** - [Description of specialized integration workflow]

### [Integration Feature Name]
[Description of when and how this integration occurs]

1. **[Step Name]**: [Description of integration step]
2. **[Step Name]**: [Description of integration step]
3. **[Step Name]**: [Description of integration step]
4. **[Step Name]**: [Description of integration step]
5. **[Step Name]**: [Description of integration step]

### [Integration Intelligence Feature]
```yaml
[feature_name]:
  [setting_category]: [list of settings]
  [setting_category]: [list of settings]
  [setting_category]: [list of settings]
  
[related_feature]:
  [setting_category]: [value or description]
  [setting_category]: [value or description]
  [setting_category]: [value or description]
```

### Integration Benefits
- **[Benefit Category]**: [Description of integration advantage]
- **[Benefit Category]**: [Description of integration advantage]
- **[Benefit Category]**: [Description of integration advantage]
- **[Benefit Category]**: [Description of integration advantage]

## Mode Configuration

```yaml
[mode_name]_mode:
  activation:
    automatic: [true|false]
    confidence_threshold: [0.0-1.0]
    detection_patterns:
      [pattern_category]: [list of patterns]
      [pattern_category]: [list of patterns]
      [pattern_category]: [list of patterns]
  
  mode_command_integration:
    primary_implementation: "[primary-command]"
    parameter_mapping:
      # MODE YAML Setting → Command Parameter
      [setting_name]: "[command-parameter]"           # Default: [value]
      [setting_name]: "[command-parameter]"           # Default: [value]
      [setting_name]: "[command-parameter]"           # Default: [value]
      [setting_name]: "[command-parameter]"           # Default: [value]
      [setting_name]: "[command-parameter]"           # Default: [value]
    override_precedence: "explicit > mode > framework > system"
    coordination_workflow:
      - [workflow_step]
      - [workflow_step]
      - [workflow_step]
      - [workflow_step]
      - [workflow_step]
  
  [integration_category]:
    [setting_name]: [value]
    [setting_name]: [list of values]
    [setting_name]: [value]
    [setting_name]: [value]
  
  framework_integration:
    mcp_servers: [list of servers]
    quality_gates: [list of quality integration points]
    mode_coordination: [list of coordinated modes]
  
  behavioral_settings:
    [behavior_category]: [value]
    [behavior_category]: [value]
    [behavior_category]: [value]
    [behavior_category]: [value]
  
  persistence:
    [storage_location]: [path or description]
    [tracking_type]: [true|false]
    [tracking_type]: [true|false]
    [tracking_type]: [true|false]
    [tracking_type]: [true|false]
```

## Related Documentation

- **Primary Implementation**: [primary-command] command
- **Agent Integration**: [related-agent] for [integration-purpose]
- **Framework Reference**: [related-mode-file] for [coordination-purpose]
- **Quality Standards**: [reference-file] for [validation-purpose]

---

# Command-Integrated Mode Template Guide

## Overview
This template provides a standardized format for documenting Command-Integrated Modes in the SuperGemini framework. These modes define behavioral frameworks that coordinate closely with specific commands to provide seamless user experiences.

## Key Characteristics: Command-Integrated Modes

### Architecture Pattern
**Behavioral Mode + Command Implementation = Unified Experience**

- **Mode**: Provides behavioral framework, auto-detection, and configuration
- **Command**: Handles execution workflow, parameter processing, and results
- **Integration**: Seamless parameter mapping, workflow coordination, and quality validation

### Integration Types
- **Orchestration Modes**: Coordinate multiple systems (agents, MCP servers, quality gates)
- **Coordination Modes**: Manage cross-session workflows and state persistence
- **Behavioral Modes**: Modify interaction patterns and communication styles
- **Processing Modes**: Enhance execution with specialized algorithms or optimizations

## Frontmatter Configuration

### Required Fields
```yaml
name: [kebab-case-name]           # Machine-readable identifier
description: "[clear-purpose]"    # Human-readable purpose statement
type: command-integrated          # Always this value for this template

category: [classification]        # Primary mode category
complexity: [level]              # Implementation complexity level
scope: [operational-scope]       # Operational boundaries

activation:                      # Activation configuration
  automatic: [boolean]           # Whether mode auto-activates
  manual-flags: [list]          # Manual activation flags
  confidence-threshold: [float]  # Auto-activation confidence level
  detection-patterns: [list]     # Pattern matching triggers

framework-integration:           # Integration points
  mcp-servers: [list]           # Coordinated MCP servers
  commands: [list]              # Integrated commands
  modes: [list]                 # Coordinated modes
  quality-gates: [list]         # Quality integration points

performance-profile: [level]     # Performance characteristics
```

### Value Guidelines
- **Category**: orchestration, coordination, behavioral, processing
- **Complexity**: standard, advanced, enterprise
- **Scope**: session, cross-session, project, system
- **Performance Profile**: standard, optimized, enterprise

## Section Guidelines

### Purpose Section
Should comprehensively explain:
- The behavioral framework provided by the mode
- How it integrates with the primary command
- Cross-session capabilities and persistence features
- Agent orchestration and handoff workflows

### Core Behavioral Framework
- **3 numbered subsections minimum**
- Focus on behavioral modifications and integration capabilities
- Include configuration management and framework compliance
- Use consistent bullet point formatting

### Mode Activation
- **Automatic Activation Patterns**: 5+ specific trigger patterns with examples
- **Manual Activation**: Primary flags and integration details
- **Command Integration**: Clear workflow responsibilities and references

### Framework Integration
- **4 subsections required**: Mode Coordination, MCP Integration, Quality Gates, Agent Orchestration
- Document all coordination relationships
- Include specific integration points and workflows

### Mode-Specific Integration Pattern
- **Customizable section name** based on mode's primary integration feature
- Document specialized workflows unique to this mode
- Include YAML configuration blocks for complex features
- List concrete integration benefits

### Mode Configuration
- **Comprehensive YAML structure** with nested categories
- **Parameter mapping section** showing mode-to-command parameter inheritance
- **Coordination workflow** documenting integration steps
- **Behavioral settings** and persistence configuration

### Related Documentation
- Always include primary command reference
- Link to related agents and their integration purpose
- Reference framework coordination documentation
- Include quality standards and validation references

## Best Practices

### 1. Integration Clarity
- Clearly separate mode responsibilities from command responsibilities
- Document parameter inheritance and override precedence
- Explain coordination workflows step-by-step

### 2. Behavioral Focus
- Emphasize how the mode modifies SuperGemini's behavior
- Document communication patterns and interaction changes
- Include examples of behavioral modifications

### 3. Framework Compliance
- Ensure integration with SuperGemini quality gates
- Document MCP server coordination patterns
- Include agent orchestration workflows

### 4. Configuration Completeness
- Provide comprehensive YAML configuration examples
- Document all parameter mappings between mode and command
- Include default values and valid ranges

### 5. Cross-Session Awareness
- Document persistence and session lifecycle integration
- Include cross-session coordination patterns
- Explain context retention and state management

## Integration Architecture

### Mode-Command Coordination Flow
```
1. Pattern Detection (Mode)
2. Auto-Activation (Mode)
3. Parameter Mapping (Mode → Command)
4. Command Invocation (Framework)
5. Behavioral Enforcement (Mode)
6. Quality Validation (Framework)
7. Result Coordination (Mode + Command)
```

### Quality Gate Integration Points
- **Pre-Activation**: Mode detection and pattern validation
- **Parameter Mapping**: Configuration inheritance and validation
- **Execution Monitoring**: Behavioral compliance and quality tracking
- **Post-Execution**: Result validation and session persistence

## File Naming Convention
- **Pattern**: `Template_Mode_Command_Integrated.md`
- **Usage**: For modes that integrate closely with specific commands
- **Examples**: Brainstorming Mode + /sg:brainstorm, Task Management Mode + /task

## Location
Template files should be placed in:
`SuperGemini/Templates/`

Implemented modes should be placed in:
`SuperGemini/Modes/` or directly in the global configuration directory