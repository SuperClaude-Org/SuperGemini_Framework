---
name: [command-name]
description: "[Clear, concise description for help systems and auto-activation patterns]"
allowed-tools: [Read, Bash, Grep, Glob, Write]

# Command Classification
category: utility
complexity: basic
scope: [file|project]

# Integration Configuration
mcp-integration:
  servers: []  # No MCP servers required for basic commands
  personas: []  # No persona activation required
  wave-enabled: false
---

# /sg:[command-name] - [Command Title]

## Purpose
[Clear statement of what this command does and when to use it. Focus on the primary goal and value proposition.]

## Usage
```
/sg:[command-name] [arguments] [--flag1] [--flag2]
```

## Arguments
- `argument1` - Description of the argument and its purpose
- `argument2` - Description of the argument and its purpose
- `--flag1` - Description of the flag and its impact
- `--flag2` - Description of the flag and its impact

## Execution
1. [First step - what the command does initially]
2. [Second step - core processing or analysis]
3. [Third step - main operation or transformation]
4. [Fourth step - validation or output generation]
5. [Fifth step - final results and feedback]

## Gemini CLI Integration
- **Tool Usage**: [Describe how the command uses its allowed tools]
- **File Operations**: [Explain file reading, writing, or manipulation patterns]
- **Analysis Approach**: [Detail how the command analyzes or processes input]
- **Output Format**: [Describe the expected output and formatting]

## Performance Targets
- **Execution Time**: <5s for typical operations
- **Success Rate**: >95% for well-formed inputs
- **Error Handling**: Clear feedback for common failure modes

## Examples

### Basic Usage
```
/sg:[command-name] [simple-example]
# Expected outcome description
```

### Advanced Usage
```
/sg:[command-name] [complex-example] --flag1 --flag2
# Expected outcome description
```

## Error Handling
- **Invalid Input**: [How the command handles bad input]
- **Missing Dependencies**: [What happens when prerequisites are missing]
- **File Access Issues**: [How file permission or access problems are handled]
- **Resource Constraints**: [Behavior under resource limitations]

## Integration Points
- **SuperGemini Framework**: [How this command fits into the broader framework]
- **Other Commands**: [Commands that commonly precede or follow this one]
- **File System**: [File system interactions and expectations]

## Boundaries

**This command will:**
- [Specific capability 1]
- [Specific capability 2]
- [Specific capability 3]

**This command will not:**
- [Specific limitation 1]
- [Specific limitation 2]
- [Specific limitation 3]

---

# Template Usage Guidelines

## Quick Start
1. Copy this template to `SuperGemini/Commands/[command-name].md`
2. Fill in the frontmatter with appropriate values
3. Replace all placeholder text with command-specific content
4. Test the command with various inputs
5. Validate integration with Gemini CLI

## Tool Selection Guidelines
Basic commands should use minimal, focused tool sets:
- **Read**: For analyzing input files and configuration
- **Bash**: For executing system commands and operations
- **Grep**: For pattern matching and text search
- **Glob**: For file discovery and path matching
- **Write**: For generating output files when needed

## Section Guidelines

### Purpose Section
- Single paragraph explaining the command's primary function
- Focus on when and why a user would invoke this command
- Avoid technical implementation details

### Usage Section
- Clear command syntax with argument placeholders
- Use consistent formatting for optional arguments
- Include common flag combinations

### Execution Section
- 5 numbered steps describing the command's workflow
- Focus on what happens, not how it's implemented
- Use action-oriented language

### Gemini CLI Integration Section
- Explain how the command leverages its allowed tools
- Detail file system interactions
- Describe error handling approach
- Mention any special integration patterns

### Examples Section
- Provide at least 2 realistic examples
- Show both simple and complex usage patterns
- Include expected outcomes for each example

## Quality Standards

### Consistency Requirements
- All sections must be present and properly formatted
- Frontmatter must include all required fields
- Tool usage must align with allowed-tools list
- Examples must be realistic and testable

### Content Standards
- Clear, concise language appropriate for developers
- Technical accuracy in all descriptions
- Consistent terminology throughout
- Proper markdown formatting

### Integration Standards
- Must work within Gemini CLI environment
- Should integrate cleanly with other SuperGemini commands
- Must handle errors gracefully
- Should provide clear user feedback

## Common Patterns

### File Processing Commands
```yaml
typical_tools: [Read, Grep, Glob, Write]
typical_flow: 
  1. Discover/validate input files
  2. Analyze file content or structure
  3. Process according to command logic
  4. Generate output or modify files
  5. Report results and next steps
```

### Analysis Commands
```yaml
typical_tools: [Read, Grep, Glob, Bash]
typical_flow:
  1. Parse target and scope
  2. Collect relevant data
  3. Apply analysis techniques
  4. Generate findings with severity
  5. Present recommendations
```

### System Operation Commands
```yaml
typical_tools: [Bash, Read, Write]
typical_flow:
  1. Validate system state
  2. Execute system operations
  3. Monitor execution results
  4. Handle errors and edge cases
  5. Report completion status
```

## Testing Guidelines

### Validation Checklist
- [ ] Command syntax is properly documented
- [ ] All arguments and flags are explained
- [ ] Examples work as described
- [ ] Error cases are handled gracefully
- [ ] Tool usage aligns with allowed-tools
- [ ] Integration points are documented
- [ ] Performance expectations are realistic

### Common Test Cases
- Valid input with expected output
- Invalid input with appropriate error messages
- Edge cases (empty files, large inputs, etc.)
- Missing dependencies or permissions
- Integration with other SuperGemini commands

---

*This template is designed for basic utility commands that perform focused operations with minimal complexity. For more sophisticated commands requiring MCP integration or advanced orchestration, use the appropriate higher-tier templates.*