---
name: git
description: "Git operations with intelligent commit messages, branch management, and workflow optimization"
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

# /sg:git - Git Operations and Workflow Management

## Purpose
Execute comprehensive Git operations with intelligent commit message generation, automated branch management, workflow optimization, and integration with development processes while maintaining repository best practices.

## Usage
```
/sg:git [operation] [args] [--smart-commit] [--branch-strategy] [--interactive]
```

## Arguments
- `operation` - Git command (add, commit, push, pull, merge, branch, status, log, diff)
- `args` - Operation-specific arguments and file specifications
- `--smart-commit` - Enable intelligent commit message generation based on changes
- `--branch-strategy` - Apply consistent branch naming conventions and workflow patterns
- `--interactive` - Enable interactive mode for complex operations requiring user input

## Execution
1. Analyze current Git repository state, working directory changes, and branch context
2. Execute requested Git operations with comprehensive validation and error checking
3. Apply intelligent commit message generation based on change analysis and conventional patterns
4. Handle merge conflicts, branch management, and repository state consistency
5. Provide clear operation feedback, next steps guidance, and workflow recommendations

## Gemini CLI Integration
- **Tool Usage**: Bash for Git command execution, Read for repository analysis, Grep for log parsing
- **File Operations**: Reads repository state and configuration, writes commit messages and branch documentation
- **Analysis Approach**: Change analysis with pattern recognition for conventional commit formatting
- **Output Format**: Structured Git operation reports with status summaries and recommended actions

## Performance Targets
- **Execution Time**: <5s for repository analysis and standard Git operations
- **Success Rate**: >95% for Git command execution and repository state validation
- **Error Handling**: Comprehensive handling of merge conflicts, permission issues, and network problems

## Examples

### Basic Usage
```
/sg:git status
# Displays comprehensive repository status with change analysis
# Provides recommendations for next steps and workflow optimization
```

### Advanced Usage
```
/sg:git commit --smart-commit --branch-strategy --interactive
# Interactive commit with intelligent message generation
# Applies branch naming conventions and workflow best practices
```

## Error Handling
- **Invalid Input**: Validates Git repository exists and operations are appropriate for current state
- **Missing Dependencies**: Checks Git installation and repository initialization status
- **File Access Issues**: Handles file permissions, lock files, and concurrent Git operations
- **Resource Constraints**: Manages large repository operations and network connectivity issues

## Integration Points
- **SuperGemini Framework**: Integrates with build for release tagging and test for pre-commit validation
- **Other Commands**: Coordinates with analyze for code quality gates and troubleshoot for repository issues
- **File System**: Reads Git configuration and history, writes commit messages and branch documentation

## Boundaries

**This command will:**
- Execute standard Git operations with intelligent automation and best practice enforcement
- Generate conventional commit messages based on change analysis and repository patterns
- Provide comprehensive repository status analysis and workflow optimization recommendations

**This command will not:**
- Modify Git repository configuration or hooks without explicit user authorization
- Execute destructive operations like force pushes or history rewriting without confirmation
- Handle complex merge scenarios requiring manual intervention beyond basic conflict resolution