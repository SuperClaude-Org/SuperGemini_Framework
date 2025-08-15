# [Flag Name] Flag

**`--[flag-name]` / `--[alias]`** *(if applicable)*

## Metadata
```yaml
name: --[flag-name]
aliases: [--[alias1], --[alias2]]  # Optional
category: [Planning|Efficiency|MCP Control|Delegation|Scope|Focus|Iteration|Introspection]
priority: [1-10]  # Higher number = higher precedence
token_impact: [low|medium|high|variable]
```

## Purpose
[One-line description of what this flag does and when to use it]

## Behavior
[Detailed explanation of flag behavior in 2-3 sentences. Include what happens when the flag is active, any side effects, and performance implications.]

## Auto-Activation Rules

**Conditions**:
- [Condition 1 that triggers auto-activation]
- [Condition 2 that triggers auto-activation]
- [Threshold or metric if applicable]

**Detection Patterns**:
- Keywords: `[keyword1]`, `[keyword2]`, `[keyword3]`
- File patterns: `[pattern1]`, `[pattern2]`
- Complexity indicators: [describe complexity metrics]
- Resource thresholds: [describe resource conditions]

**Precedence**: [Describe any special precedence rules]

## Token Impact
- **Base Usage**: [Estimated token usage]
- **Scaling Factor**: [How usage scales with project size]
- **Optimization**: [Any token-saving features when active]

## Conflicts & Resolution

**Incompatible With**:
- `--[flag1]`: [Reason for incompatibility]
- `--[flag2]`: [Reason for incompatibility]

**Resolution Strategy**:
1. [Step 1 for conflict resolution]
2. [Step 2 for conflict resolution]

**Overrides**:
- Overridden by: `--[higher-priority-flag]`
- Overrides: `--[lower-priority-flag]`

## Integration Points

### Compatible Commands
- `/sg:[command1]` - [How the flag enhances this command]
- `/sg:[command2]` - [How the flag enhances this command]
- `/sg:[command3]` - [How the flag enhances this command]

### MCP Servers
- **[Server Name]**: [How this flag interacts with the server]
- **[Server Name]**: [How this flag interacts with the server]

### Synergistic Flags
- `--[flag1]`: [How they work together]
- `--[flag2]`: [How they work together]

## Usage Examples

### Basic Usage
```bash
claude "your request here" --[flag-name]
```

### With Parameters *(if applicable)*
```bash
claude "your request here" --[flag-name] [parameter]
```

### Combined with Other Flags
```bash
claude "your request here" --[flag-name] --[other-flag]
```

### Real-World Scenario
```bash
# [Describe a real use case]
claude "[specific request example]" --[flag-name]
```

## Implementation Notes

**Performance Considerations**:
- [Note about performance impact]
- [Resource usage patterns]

**Best Practices**:
- [When to use this flag]
- [When NOT to use this flag]
- [Common pitfalls to avoid]

---

# Flag Template Usage Guide

## Overview
This template provides a standardized format for documenting flags in the SuperGemini framework. Each flag should have its own section in FLAGS.md following this structure.

## Creating a New Flag

### 1. Choose Appropriate Naming
- Use lowercase with hyphens: `--flag-name`
- Be descriptive but concise
- Consider aliases for common variations
- Examples: `--seq`, `--safe-mode`, `--wave-mode`

### 2. Select Category
Choose from these standard categories:
- **Planning & Analysis**: Thinking modes, analysis depth
- **Compression & Efficiency**: Token optimization, output control
- **MCP Control**: Server activation/deactivation
- **Delegation**: Sub-agent and task distribution
- **Scope & Focus**: Operation boundaries and domains
- **Iteration**: Loop and refinement controls
- **Wave Orchestration**: Multi-stage execution
- **Introspection**: Transparency and debugging

### 3. Set Priority (1-10)
Priority determines precedence in conflicts:
- **10**: Safety flags (--safe-mode)
- **8-9**: Explicit user flags
- **6-7**: Performance and efficiency flags
- **4-5**: Feature flags
- **1-3**: Convenience flags

### 4. Define Auto-Activation
Specify clear, measurable conditions:
- **Threshold-based**: "complexity > 0.7"
- **Count-based**: "files > 50"
- **Pattern-based**: "import statements detected"
- **Composite**: "complexity > 0.8 AND domains > 2"

### 5. Document Token Impact
Classify token usage:
- **Low**: <1K additional tokens
- **Medium**: 1K-10K additional tokens
- **High**: 10K+ additional tokens
- **Variable**: Depends on operation scope

## Best Practices

### Do's
✅ Provide clear auto-activation conditions
✅ Document all conflicts explicitly
✅ Include real-world usage examples
✅ Specify token impact estimates
✅ List integration points comprehensively
✅ Test flag interactions thoroughly

### Don'ts
❌ Create overlapping flags without clear differentiation
❌ Use vague auto-activation conditions
❌ Ignore precedence rules
❌ Forget to update integration sections
❌ Skip conflict resolution documentation

## Testing Your Flag

### 1. Manual Testing
```bash
# Test basic functionality
claude "test request" --your-flag

# Test with parameters
claude "test request" --your-flag parameter

# Test combinations
claude "test request" --your-flag --other-flag
```

### 2. Auto-Activation Testing
- Create scenarios that should trigger activation
- Verify activation occurs at correct thresholds
- Ensure no false positives

### 3. Conflict Testing
- Test with known incompatible flags
- Verify resolution strategy works
- Check precedence ordering

### 4. Integration Testing
- Test with relevant commands
- Verify MCP server interactions
- Check synergistic flag combinations

## Common Flag Patterns

### Analysis Flags
```yaml
category: Planning & Analysis
auto_activation: complexity-based
token_impact: high
integrates_with: Sequential MCP
```

### Control Flags
```yaml
category: MCP Control
auto_activation: context-based
token_impact: variable
conflicts_with: opposite controls
```

### Performance Flags
```yaml
category: Efficiency
auto_activation: resource-based
token_impact: reduces overall
integrates_with: all operations
```

### Safety Flags
```yaml
category: Safety
priority: 10
auto_activation: risk-based
overrides: most other flags
```

## Flag Categories Reference

| Category | Purpose | Common Patterns |
|----------|---------|-----------------|
| Planning & Analysis | Deep analysis modes | --seq, --analyze |
| Efficiency | Token optimization | --uc, --compress |
| MCP Control | Server management | --seq, --no-mcp |
| Delegation | Task distribution | --delegate, --concurrency |
| Scope | Operation boundaries | --scope, --focus |
| Iteration | Refinement loops | --loop, --iterations |
| Wave | Multi-stage execution | --wave-mode, --wave-strategy |
| Introspection | Debugging/transparency | --introspect, --debug |

## Integration with FLAGS.md

When adding a new flag to FLAGS.md:

1. **Find the appropriate section** based on category
2. **Maintain alphabetical order** within sections
3. **Update the Flag System Architecture** if introducing new concepts
4. **Add to Integration Patterns** section if relevant
5. **Update any affected precedence rules**

## Version Compatibility

- Document which version introduced the flag
- Note any breaking changes in behavior
- Specify minimum Gemini CLI version required
- List deprecated flags this replaces (if any)

## Examples of Well-Documented Flags

### Example 1: Thinking Flag
```markdown
**`--seq`**
- Multi-file analysis (~4K tokens)
- Enables Sequential MCP for structured problem-solving
- Auto-activates: Import chains >5 files, cross-module calls >10 references
- Auto-enables `--seq` for systematic analysis
```

### Example 2: Delegation Flag
```markdown
**`--delegate [files|folders|auto]`**
- Enable Task tool sub-agent delegation for parallel processing
- **files**: Delegate individual file analysis to sub-agents
- **folders**: Delegate directory-level analysis to sub-agents  
- **auto**: Auto-detect delegation strategy based on scope and complexity
- Auto-activates: >7 directories or >50 files
- 40-70% time savings for suitable operations
```

### Example 3: Safety Flag
```markdown
**`--safe-mode`**
- Maximum validation with conservative execution
- Auto-activates: Resource usage >85% or production environment
- Enables validation checks, forces --uc mode, blocks risky operations
```

---

This template ensures consistent, comprehensive documentation for all SuperGemini flags, making them easy to understand, implement, and maintain.