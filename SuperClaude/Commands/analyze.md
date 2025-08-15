---
name: analyze
description: "Analyze code quality, security, performance, and architecture with comprehensive reporting"
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

# /sg:analyze - Code Analysis and Quality Assessment

## Purpose
Execute systematic code analysis across quality, security, performance, and architecture domains to identify issues, technical debt, and improvement opportunities with detailed reporting and actionable recommendations.

## Usage
```
/sg:analyze [target] [--focus quality|security|performance|architecture] [--depth quick|deep] [--format text|json|report]
```

## Arguments
- `target` - Files, directories, modules, or entire project to analyze
- `--focus` - Primary analysis domain (quality, security, performance, architecture)
- `--depth` - Analysis thoroughness level (quick scan, deep inspection)
- `--format` - Output format specification (text summary, json data, html report)

## Execution
1. Discover and categorize source files using language detection and project structure analysis
2. Apply domain-specific analysis techniques including static analysis and pattern matching
3. Generate prioritized findings with severity ratings and impact assessment
4. Create actionable recommendations with implementation guidance and effort estimates
5. Present comprehensive analysis report with metrics, trends, and improvement roadmap

## Gemini CLI Integration
- **Tool Usage**: Glob for file discovery, Grep for pattern analysis, Read for code inspection, Bash for tool execution
- **File Operations**: Reads source files and configurations, writes analysis reports and metrics summaries
- **Analysis Approach**: Multi-domain analysis combining static analysis, pattern matching, and heuristic evaluation
- **Output Format**: Structured reports with severity classifications, metrics, and prioritized recommendations

## Performance Targets
- **Execution Time**: <5s for analysis setup and file discovery, scales with project size
- **Success Rate**: >95% for file analysis and pattern detection across supported languages
- **Error Handling**: Graceful handling of unsupported files and malformed code structures

## Examples

### Basic Usage
```
/sg:analyze
# Performs comprehensive analysis of entire project
# Generates multi-domain report with key findings and recommendations
```

### Advanced Usage
```
/sg:analyze src/security --focus security --depth deep --format report
# Deep security analysis of specific directory
# Generates detailed HTML report with vulnerability assessment
```

## Error Handling
- **Invalid Input**: Validates analysis targets exist and contain analyzable source code
- **Missing Dependencies**: Checks for analysis tools availability and handles unsupported file types
- **File Access Issues**: Manages permission restrictions and handles binary or encrypted files
- **Resource Constraints**: Optimizes memory usage for large codebases and provides progress feedback

## Integration Points
- **SuperGemini Framework**: Integrates with build command for pre-build analysis and test for quality gates
- **Other Commands**: Commonly precedes refactoring operations and follows development workflows
- **File System**: Reads project source code, writes analysis reports to designated output directories

## Boundaries

**This command will:**
- Perform static code analysis using pattern matching and heuristic evaluation
- Generate comprehensive quality, security, performance, and architecture assessments
- Provide actionable recommendations with severity ratings and implementation guidance

**This command will not:**
- Execute dynamic analysis requiring code compilation or runtime environments
- Modify source code or automatically apply fixes without explicit user consent
- Analyze external dependencies or third-party libraries beyond import analysis