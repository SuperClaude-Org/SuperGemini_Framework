---
name: [mode-name]
description: "[Clear purpose and behavioral modification description]"
type: behavioral

# Mode Classification  
category: [optimization|analysis]
complexity: basic
scope: [session|framework]

# Activation Configuration
activation:
  automatic: [true|false]
  manual-flags: [list of flags]
  confidence-threshold: [0.0-1.0]
  detection-patterns: [list of trigger patterns]

# Integration Configuration
framework-integration:
  mcp-servers: [list of coordinated servers]
  commands: [list of integrated commands]
  modes: [list of coordinated modes]
  quality-gates: [list of quality integration points]

# Performance Profile
performance-profile: lightweight
---

# [Mode Name] Mode

**[Optional Subtitle]** - [Brief description focusing on behavioral modification and framework impact]

## Purpose

[Clear description of the behavioral framework this mode provides. Focus on:
- What operational behavior changes it enables
- How it modifies Gemini CLI's approach to tasks
- Why this behavioral modification is valuable
- What problems it solves in the SuperGemini framework]

## Core [Capabilities|Framework]

### 1. [Primary Framework Category]
- **[Core Feature]**: [Specific behavioral modification it provides]
- **[Core Feature]**: [How it changes Claude's operational approach]
- **[Core Feature]**: [Framework integration point or enhancement]
- **[Core Feature]**: [Quality or performance improvement provided]

### 2. [Secondary Framework Category]
- **[Supporting Feature]**: [Additional behavioral enhancement]
- **[Supporting Feature]**: [Integration with other framework components]
- **[Supporting Feature]**: [Cross-cutting concern or optimization]

### 3. [Integration Framework Category]
- **[Integration Feature]**: [How it coordinates with MCP servers]
- **[Integration Feature]**: [How it enhances command execution]
- **[Integration Feature]**: [How it supports quality gates]

[Continue with additional categories as needed for the specific mode]

## Activation Patterns

### Automatic Activation
[Mode] auto-activates when SuperGemini detects:

1. **[Primary Trigger Category]**: [Description of detection pattern]
2. **[Secondary Trigger Category]**: [Specific conditions or keywords]
3. **[Context Trigger Category]**: [Environmental or situational triggers]
4. **[Performance Trigger Category]**: [Resource or performance-based triggers]
5. **[Integration Trigger Category]**: [Framework or quality-based triggers]

### Manual Activation
- **Primary Flag**: `--[shorthand]` or `--[fullname]`
- **Context**: [When users would explicitly request this behavioral mode]
- **Integration**: [How it works with other flags or commands]
- **Fallback Control**: `--no-[shorthand]` disables automatic activation

## [Mode-Specific Framework Section]

[This section varies by behavioral mode type:]

### For Optimization Modes: Optimization Framework
[Include frameworks like symbol systems, compression strategies, resource management, etc.]

### For Analysis Modes: Analysis Framework
[Include analysis markers, communication patterns, assessment categories, etc.]

### Framework Components
[Document the core framework elements this mode provides:]

## Framework Integration

### SuperGemini Mode Coordination
- **[Related Mode]**: [How this mode coordinates with other behavioral modes]
- **[Related Mode]**: [Shared configuration or mutual enhancement]
- **[Related Mode]**: [Conflict resolution or priority handling]

### MCP Server Integration
- **[Server Name]**: [How this mode enhances or coordinates with MCP servers]
- **[Server Name]**: [Specific integration points or optimizations]
- **[Server Name]**: [Performance improvements or behavioral modifications]

### Quality Gate Integration
- **[Gate Step]**: [How this mode contributes to validation process]
- **[Gate Step]**: [Specific quality enhancements provided]
- **[Gate Type]**: [Continuous monitoring or checkpoint integration]

### Command Integration
- **[Command Category]**: [How this mode modifies command execution]
- **[Command Category]**: [Behavioral enhancements during command flow]
- **[Command Category]**: [Performance or quality improvements]

## Communication Style

### [Primary Communication Pattern]
1. **[Style Element]**: [How this mode changes Claude's communication]
2. **[Style Element]**: [Specific behavioral modifications in responses]
3. **[Style Element]**: [Integration with SuperGemini communication standards]
4. **[Style Element]**: [Quality or efficiency improvements in dialogue]

### [Secondary Communication Pattern]
1. **[Pattern Element]**: [Additional communication behaviors]
2. **[Pattern Element]**: [Framework compliance in communication]
3. **[Pattern Element]**: [Cross-mode communication consistency]

[Include mode-specific communication elements like symbols, markers, abbreviations, etc.]

## Configuration

```yaml
[mode_name]_mode:
  activation:
    automatic: [true|false]
    confidence_threshold: [0.0-1.0]
    detection_patterns:
      [pattern_category]: [list of patterns]
      [pattern_category]: [list of patterns]
  
  [framework_category]:
    [setting]: [value]
    [setting]: [value]
    [threshold_name]: [threshold_value]
  
  framework_integration:
    mcp_servers: [list of coordinated servers]
    quality_gates: [list of integration points]
    mode_coordination: [list of coordinated modes]
  
  behavioral_settings:
    [behavior_aspect]: [configuration]
    [behavior_aspect]: [configuration]
  
  performance:
    [performance_metric]: [target_value]
    [performance_metric]: [target_value]
```

## Integration Ecosystem

### SuperGemini Framework Compliance

```yaml
framework_integration:
  quality_gates: [specific quality integration points]
  mcp_coordination: [server coordination patterns]
  mode_orchestration: [cross-mode behavioral coordination]
  document_persistence: [how behavioral changes are documented]
  
behavioral_consistency:
  communication_patterns: [standardized behavioral modifications]
  performance_standards: [performance targets and monitoring]
  quality_enforcement: [framework standards maintained]
  integration_protocols: [coordination with other components]
```

### Cross-Mode Behavioral Coordination

```yaml
mode_interactions:
  [related_mode]: [specific coordination pattern]
  [related_mode]: [shared behavioral modifications]
  [related_mode]: [conflict resolution strategy]
  
orchestration_principles:
  behavioral_consistency: [how consistency is maintained]
  configuration_harmony: [shared settings and coordination]
  quality_enforcement: [SuperGemini standards preserved]
  performance_optimization: [efficiency gains through coordination]
```

## Related Documentation

- **Framework Reference**: [ORCHESTRATOR.md or other relevant framework docs]
- **Integration Patterns**: [specific command or MCP integration docs]
- **Quality Standards**: [quality gate or validation references]
- **Performance Targets**: [performance monitoring or optimization docs]

---

# Template Guide: Basic Behavioral Modes

## Overview

This template is designed for **basic behavioral framework modes** that provide lightweight, session-scoped behavioral modifications to Gemini CLI's operation. These modes focus on optimizing specific aspects of the SuperGemini framework through global behavioral changes.

## Behavioral Mode Characteristics

### Key Features
- **Lightweight Performance Profile**: Minimal resource overhead with maximum behavioral impact
- **Global Behavioral Modification**: Changes that apply consistently across all operations
- **Framework Integration**: Deep integration with SuperGemini's quality gates and orchestration
- **Adaptive Intelligence**: Context-aware behavioral adjustments based on task complexity
- **Evidence-Based Operation**: All behavioral modifications validated with metrics

### Mode Types Supported

#### Optimization Modes
- **Focus**: Performance, efficiency, resource management, token optimization
- **Examples**: Token Efficiency, Resource Management, Performance Optimization
- **Framework**: Symbol systems, compression strategies, threshold management
- **Metrics**: Performance targets, efficiency gains, resource utilization

#### Analysis Modes  
- **Focus**: Meta-cognitive analysis, introspection, framework troubleshooting
- **Examples**: Introspection, Quality Analysis, Framework Compliance
- **Framework**: Analysis markers, assessment categories, communication patterns
- **Metrics**: Analysis depth, insight quality, framework compliance

## Template Sections

### Required Sections
1. **YAML Frontmatter**: Structured metadata for mode classification and configuration
2. **Purpose**: Clear behavioral modification description
3. **Core Framework**: The specific framework this mode provides
4. **Activation Patterns**: Auto-detection and manual activation
5. **Framework Integration**: SuperGemini ecosystem integration
6. **Configuration**: YAML configuration structures

### Optional Sections
- **Communication Style**: For modes that modify interaction patterns
- **Mode-Specific Framework**: Custom framework elements (symbols, markers, etc.)
- **Integration Ecosystem**: Advanced coordination patterns

## Usage Guidelines

### When to Use This Template
- **Simple behavioral modifications** that don't require complex state management
- **Global optimizations** that apply across all operations
- **Framework enhancements** that integrate with SuperGemini's core systems
- **Lightweight modes** with minimal performance overhead

### When NOT to Use This Template
- **Complex workflow modes** with multiple states (use Template_Mode_Advanced.md)
- **Agent-like modes** with domain expertise (use Template_Agent.md)
- **Command-integrated modes** with execution workflows (use Template_Command_Session.md)

## Customization Points

### For Optimization Modes
- Focus on **performance metrics** and **efficiency frameworks**
- Include **symbol systems** or **compression strategies**
- Emphasize **resource management** and **threshold configurations**
- Document **integration with MCP servers** for performance gains

### For Analysis Modes
- Focus on **analysis frameworks** and **assessment categories**
- Include **communication markers** and **transparency patterns**
- Emphasize **meta-cognitive capabilities** and **framework compliance**
- Document **troubleshooting patterns** and **insight generation**

## Best Practices

1. **Clear Behavioral Focus**: Each mode should have a single, clear behavioral modification
2. **Framework Integration**: Deep integration with SuperGemini's quality gates and orchestration
3. **Performance Awareness**: Document performance impact and optimization benefits
4. **Evidence-Based Design**: Include metrics and validation for all behavioral changes
5. **Consistent Communication**: Maintain SuperGemini's communication standards

## File Naming Convention
- **Prefix**: `MODE_`
- **Format**: `MODE_{ModeName}.md`
- **Examples**: `MODE_Token_Efficiency.md`, `MODE_Introspection.md`

## Location
All Basic Behavioral Mode files should be placed in: `SuperGemini/Modes/`