# [Mode Name] Mode

**[Optional Subtitle]** - [Brief description of the mode's primary function]

## Purpose

[Clear, comprehensive description of what this mode enables and why it exists. Should explain the operational behavior change this mode provides.]

## Core Capabilities

### 1. [Capability Category]
- **[Specific Feature]**: [Description of what it does]
- **[Specific Feature]**: [Description of what it does]
- **[Specific Feature]**: [Description of what it does]

### 2. [Capability Category]
- **[Specific Feature]**: [Description of what it does]
- **[Specific Feature]**: [Description of what it does]

[Continue numbering as needed]

## Activation

### Manual Activation
- **Primary Flag**: `--[shorthand]` or `--[fullname]`
- **Context**: [When users would manually activate this]

### Automatic Activation
1. **[Trigger Condition]**: [Description of what triggers activation]
2. **[Trigger Condition]**: [Description of what triggers activation]
3. **[Trigger Condition]**: [Description of what triggers activation]
[Continue as needed]

## [Mode-Specific Section]

[This section varies by mode type. Examples:]
- For state-based modes: ## States
- For communication modes: ## Communication Markers
- For optimization modes: ## Techniques
- For analysis modes: ## Analysis Types

## Communication Style

[How this mode affects interaction with the user]

### [Subsection if needed]
[Details about specific communication patterns]

## Integration Points

### Related Flags
- **`--[flag]`**: [How it interacts with this mode]
- **`--[flag]`**: [How it interacts with this mode]

### [Other Integration Categories]
[Commands, Agents, MCP Servers, Tools, etc.]

## Configuration

```yaml
[mode_name]:
  activation:
    automatic: [true/false]
    [threshold_name]: [value]
  [category]:
    [setting]: [value]
    [setting]: [value]
  [category]:
    [setting]: [value]
```

---

# Mode Template Guide

## Overview
This template provides a standardized format for documenting Modes in the SuperGemini framework. Modes define HOW Claude operates, as opposed to Agents which define WHO Claude becomes.

## Key Differences: Modes vs Agents
- **Modes**: Operational behaviors, interaction patterns, processing methods
- **Agents**: Domain expertise, persona, specialized knowledge
- **Example**: Brainstorming Mode (interactive dialogue) + brainstorm-PRD Agent (requirements expertise)

## Section Guidelines

### Purpose
- Focus on operational behavior changes
- Explain what interaction pattern or processing method is enabled
- Keep it clear and action-oriented

### Core Capabilities
- Group related capabilities under numbered categories
- Use bold formatting for feature names
- Be specific about behavioral changes

### Activation
- Document both manual (flag-based) and automatic triggers
- Automatic triggers should be observable patterns
- Include confidence thresholds where applicable

### Mode-Specific Sections
Choose based on mode type:
- **State-Based**: Document states, transitions, and exit conditions
- **Communication**: Define markers, styles, and patterns
- **Processing**: Explain techniques, optimizations, and algorithms
- **Analysis**: Describe types, methods, and outputs

### Communication Style
- How the mode changes Claude's interaction
- Include examples of communication patterns
- Note any special markers or formatting

### Integration Points
- List all related flags with their interactions
- Include relevant commands, agents, or tools
- Note any mode combinations or conflicts

### Configuration
- YAML block showing configurable settings
- Include defaults and valid ranges
- Group settings logically

## Best Practices

1. **Clarity**: Write for developers who need quick reference
2. **Specificity**: Focus on observable behavior changes
3. **Examples**: Include concrete examples where helpful
4. **Consistency**: Follow this template structure exactly
5. **Completeness**: Cover all major behavioral aspects

## File Naming
- Use prefix: `MODE_ModeName.md`
- Be descriptive but concise with MODE_ prefix
- Examples: `MODE_Brainstorming.md`, `MODE_Introspection.md`, `MODE_Token_Efficiency.md`

## Location
All Mode documentation files should be placed in:
`SuperGemini/Modes/`