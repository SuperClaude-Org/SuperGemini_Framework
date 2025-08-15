---
name: troubleshoot
description: "Diagnose and resolve issues in code, builds, deployments, or system behavior"
allowed-tools: [read_file, run_shell_command, search_file_content, glob, write_file]

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

# /sg:troubleshoot - Issue Diagnosis and Resolution

## Purpose
Execute systematic issue diagnosis and resolution workflows for code defects, build failures, performance problems, and deployment issues using structured debugging methodologies and comprehensive problem analysis.

## Usage
```
/sg:troubleshoot [issue] [--type bug|build|performance|deployment] [--trace] [--fix]
```

## Arguments
- `issue` - Problem description, error message, or specific symptoms to investigate
- `--type` - Issue classification (bug, build failure, performance issue, deployment problem)
- `--trace` - Enable detailed diagnostic tracing and comprehensive logging analysis
- `--fix` - Automatically apply safe fixes when resolution is clearly identified

## Execution
1. Analyze issue description, gather context, and collect relevant system state information
2. Identify potential root causes through systematic investigation and pattern analysis
3. Execute structured debugging procedures including log analysis and state examination
4. Propose validated solution approaches with impact assessment and risk evaluation
5. Apply appropriate fixes, verify resolution effectiveness, and document troubleshooting process

## Gemini CLI Integration
- **Tool Usage**: Read for log analysis, Bash for diagnostic commands, Grep for error pattern detection
- **File Operations**: Reads error logs and system state, writes diagnostic reports and resolution documentation
- **Analysis Approach**: Systematic root cause analysis with hypothesis testing and evidence collection
- **Output Format**: Structured troubleshooting reports with findings, solutions, and prevention recommendations

## Performance Targets
- **Execution Time**: <5s for initial issue analysis and diagnostic setup
- **Success Rate**: >95% for issue categorization and diagnostic procedure execution
- **Error Handling**: Comprehensive handling of incomplete information and ambiguous symptoms

## Examples

### Basic Usage
```
/sg:troubleshoot "Build failing with TypeScript errors"
# Analyzes build logs and identifies TypeScript compilation issues
# Provides specific error locations and recommended fixes
```

### Advanced Usage
```
/sg:troubleshoot "Performance degradation in API responses" --type performance --trace --fix
# Deep performance analysis with detailed tracing enabled
# Identifies bottlenecks and applies safe performance optimizations
```

## Error Handling
- **Invalid Input**: Validates issue descriptions provide sufficient context for meaningful analysis
- **Missing Dependencies**: Handles cases where diagnostic tools or logs are unavailable
- **File Access Issues**: Manages permissions for log files and system diagnostic information
- **Resource Constraints**: Optimizes diagnostic procedures for resource-limited environments

## Integration Points
- **SuperGemini Framework**: Coordinates with analyze for code quality issues and test for validation
- **Other Commands**: Integrates with build for compilation issues and git for version-related problems
- **File System**: Reads system logs and error reports, writes diagnostic summaries and resolution guides

## Boundaries

**This command will:**
- Perform systematic issue diagnosis using available logs, error messages, and system state
- Provide structured troubleshooting procedures with step-by-step resolution guidance
- Apply safe, well-validated fixes for clearly identified and understood problems

**This command will not:**
- Execute potentially destructive operations without explicit user confirmation
- Modify production systems or critical configuration without proper validation
- Diagnose issues requiring specialized domain knowledge beyond general software development