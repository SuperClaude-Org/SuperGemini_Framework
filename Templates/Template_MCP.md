# [Server Name] MCP Server

## Purpose
[One-line description of what this MCP server provides]

## Activation Patterns

**Automatic Activation**:
- [Condition 1 that triggers automatic activation]
- [Condition 2 that triggers automatic activation]

**Manual Activation**:
- Flag: `--[shorthand]`, `--[fullname]`

**Smart Detection**:
- [Context-aware activation patterns]
- [Keywords or patterns that suggest server usage]

## Workflow Process

1. **[Step Name]**: [Description of what happens]
2. **[Step Name]**: [Description of what happens]
3. **[Step Name]**: [Description of what happens]
[Continue numbering as needed]

## Integration Points

**Commands**: [List of commands that commonly use this server]

**Analysis Modes**: [How it integrates with --seq and other analysis flags if applicable]

**Other MCP Servers**: [Which other servers it coordinates with]

## Core Capabilities

### [Capability Category 1]
- [Specific capability]
- [Specific capability]

### [Capability Category 2]
- [Specific capability]
- [Specific capability]

## Use Cases

- **[Use Case 1]**: [Description]
- **[Use Case 2]**: [Description]
- **[Use Case 3]**: [Description]

## Error Recovery

- **[Error Scenario 1]** → [Recovery Strategy] → [Fallback]
- **[Error Scenario 2]** → [Recovery Strategy] → [Fallback]
- **[Error Scenario 3]** → [Recovery Strategy] → [Fallback]

## Caching Strategy

- **Cache Type**: [What gets cached]
- **Cache Duration**: [How long cache persists]
- **Cache Key**: [How cache entries are identified]

## Configuration

```yaml
[server_name]:
  activation:
    automatic: [true/false]
    complexity_threshold: [0.0-1.0]
  performance:
    timeout: [milliseconds]
    max_retries: [number]
  cache:
    enabled: [true/false]
    ttl: [seconds]
```

---

# MCP Server Template Guide

## Overview
This template provides a standardized format for documenting MCP (Model Context Protocol) servers in the SuperGemini framework. Each MCP server should have its own file following this structure.

## Section Guidelines

### Purpose
- Keep it to one clear, concise line
- Focus on the primary value the server provides
- Example: "Official library documentation, code examples, and best practices"

### Activation Patterns
Document three types of activation:
1. **Automatic**: Conditions that trigger without user intervention
2. **Manual**: Explicit flags users can specify
3. **Smart**: Context-aware patterns Gemini CLI detects

### Workflow Process
- Number each step sequentially
- Use bold formatting for step names
- Keep descriptions action-oriented
- Include coordination with other servers if applicable

### Integration Points
- List relevant commands without the `/` prefix
- Specify which thinking modes apply
- Note other MCP servers this one coordinates with

### Core Capabilities
- Group related capabilities under categories
- Use bullet points for specific features
- Be concrete and specific

### Use Cases
- Provide 3-5 real-world examples
- Use bold formatting for use case names
- Keep descriptions brief but clear

### Error Recovery
- Format: **Error** → Recovery → Fallback
- Include common failure scenarios
- Provide actionable recovery strategies

### Caching Strategy
- Specify what gets cached
- Include cache duration/TTL
- Explain cache key structure

### Rules
- Specify mandatory rules for this server
- Use bullet points for clarity
- Only simple, actionable rules

## Best Practices

1. **Consistency**: Follow this template structure exactly
2. **Clarity**: Write for developers who need quick reference
3. **Completeness**: Cover all major functionality
4. **Examples**: Use concrete examples where helpful
5. **Updates**: Keep documentation synchronized with implementation

## File Naming
- Use prefix: `MCP_ServerName.md`
- Match the server's official name with MCP_ prefix
- Examples: `MCP_Context7.md`, `MCP_Sequential.md`, `MCP_Magic.md`

## Location
All MCP server documentation files should be placed in:
`SuperGemini/MCP/`