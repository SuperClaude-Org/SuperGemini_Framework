---
name: design
description: "Design system architecture, APIs, and component interfaces with comprehensive specifications"
allowed-tools: [Read, Bash, Grep, Glob, Write]

# Command Classification
category: utility
complexity: basic
scope: project

# Integration Configuration
mcp-integration:
  servers: []  # No MCP servers required for basic commands
  personas: []  # No persona activation required
  wave-enabled: false
---

# /sg:design - System and Component Design

## Purpose
Create comprehensive system architecture, API specifications, component interfaces, and technical design documentation with validation against requirements and industry best practices for maintainable and scalable solutions.

## Usage
```
/sg:design [target] [--type architecture|api|component|database] [--format diagram|spec|code] [--iterative]
```

## Arguments
- `target` - System, component, feature, or module to design
- `--type` - Design category (architecture, api, component, database)
- `--format` - Output format (diagram, specification, code templates)
- `--iterative` - Enable iterative design refinement with feedback cycles

## Execution
1. Analyze requirements, constraints, and existing system context through comprehensive discovery
2. Create initial design concepts with multiple alternatives and trade-off analysis
3. Develop detailed design specifications including interfaces, data models, and interaction patterns
4. Validate design against functional requirements, quality attributes, and architectural principles
5. Generate comprehensive design documentation with implementation guides and validation criteria

## Gemini CLI Integration
- **Tool Usage**: Read for requirements analysis, Write for documentation generation, Grep for pattern analysis
- **File Operations**: Reads requirements and existing code, writes design specs and architectural documentation
- **Analysis Approach**: Requirement-driven design with pattern matching and best practice validation
- **Output Format**: Structured design documents with diagrams, specifications, and implementation guides

## Performance Targets
- **Execution Time**: <5s for requirement analysis and initial design concept generation
- **Success Rate**: >95% for design specification generation and documentation formatting
- **Error Handling**: Clear feedback for unclear requirements and constraint conflicts

## Examples

### Basic Usage
```
/sg:design user-authentication --type api
# Designs authentication API with endpoints and security specifications
# Generates API documentation with request/response schemas
```

### Advanced Usage
```
/sg:design payment-system --type architecture --format diagram --iterative
# Creates comprehensive payment system architecture with iterative refinement
# Generates architectural diagrams and detailed component specifications
```

## Error Handling
- **Invalid Input**: Validates design targets are well-defined and requirements are accessible
- **Missing Dependencies**: Checks for design context and handles incomplete requirement specifications
- **File Access Issues**: Manages access to existing system documentation and output directories
- **Resource Constraints**: Optimizes design complexity based on available information and scope

## Integration Points
- **SuperGemini Framework**: Coordinates with analyze command for system assessment and document for specification generation
- **Other Commands**: Precedes implementation workflows and integrates with build for validation
- **File System**: Reads system requirements and existing architecture, writes design specifications to project documentation

## Boundaries

**This command will:**
- Create comprehensive design specifications based on stated requirements and constraints
- Generate architectural documentation with component interfaces and interaction patterns
- Validate designs against common architectural principles and best practices

**This command will not:**
- Generate executable code or detailed implementation beyond design templates
- Modify existing system architecture or database schemas without explicit requirements
- Create designs requiring external system integration without proper specification