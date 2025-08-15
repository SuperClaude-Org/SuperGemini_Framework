---
name: document
description: "Generate focused documentation for specific components, functions, or features"
allowed-tools: [Read, Bash, Grep, Glob, Write]

# Command Classification
category: utility
complexity: basic
scope: file

# Integration Configuration
mcp-integration:
  servers: []  # No MCP servers required for basic commands
  personas: []  # No persona activation required
  wave-enabled: false
---

# /sg:document - Focused Documentation Generation

## Purpose
Generate precise, well-structured documentation for specific components, functions, APIs, or features with appropriate formatting, comprehensive coverage, and integration with existing documentation ecosystems.

## Usage
```
/sg:document [target] [--type inline|external|api|guide] [--style brief|detailed] [--template standard|custom]
```

## Arguments
- `target` - Specific file, function, class, module, or component to document
- `--type` - Documentation format (inline code comments, external files, api reference, user guide)
- `--style` - Documentation depth and verbosity (brief summary, detailed comprehensive)
- `--template` - Template specification (standard format, custom organization)

## Execution
1. Analyze target component structure, interfaces, and functionality through comprehensive code inspection
2. Identify documentation requirements, target audience, and integration context within project
3. Generate appropriate documentation content based on type specifications and style preferences
4. Apply consistent formatting, structure, and organizational patterns following documentation standards
5. Integrate generated documentation with existing project documentation and ensure cross-reference consistency

## Gemini CLI Integration
- **Tool Usage**: Read for component analysis, Write for documentation creation, Grep for reference extraction
- **File Operations**: Reads source code and existing docs, writes documentation files with proper formatting
- **Analysis Approach**: Code structure analysis with API extraction and usage pattern identification
- **Output Format**: Structured documentation with consistent formatting, cross-references, and examples

## Performance Targets
- **Execution Time**: <5s for component analysis and documentation generation
- **Success Rate**: >95% for documentation extraction and formatting across supported languages
- **Error Handling**: Graceful handling of complex code structures and incomplete information

## Examples

### Basic Usage
```
/sg:document src/auth/login.js --type inline
# Generates inline code comments for login function
# Adds JSDoc comments with parameter and return descriptions
```

### Advanced Usage
```
/sg:document src/api --type api --style detailed --template standard
# Creates comprehensive API documentation for entire API module
# Generates detailed external documentation with examples and usage guidelines
```

## Error Handling
- **Invalid Input**: Validates documentation targets exist and contain documentable code structures
- **Missing Dependencies**: Handles cases where code analysis is incomplete or context is insufficient
- **File Access Issues**: Manages read access to source files and write permissions for documentation output
- **Resource Constraints**: Optimizes documentation generation for large codebases with progress feedback

## Integration Points
- **SuperGemini Framework**: Coordinates with analyze for code understanding and design for specification documentation
- **Other Commands**: Follows development workflows and integrates with build for documentation publishing
- **File System**: Reads project source code and existing documentation, writes formatted docs to appropriate locations

## Boundaries

**This command will:**
- Generate comprehensive documentation based on code analysis and existing patterns
- Create properly formatted documentation following project conventions and standards
- Extract API information, usage examples, and integration guidance from source code

**This command will not:**
- Modify source code structure or add functionality beyond documentation
- Generate documentation for external dependencies or third-party libraries
- Create documentation requiring runtime analysis or dynamic code execution