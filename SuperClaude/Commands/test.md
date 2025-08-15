---
name: test
description: "Execute tests, generate test reports, and maintain test coverage standards with AI-powered automated testing"
allowed-tools: [read_file, run_shell_command, search_file_content, glob, write_file]

# Command Classification
category: utility
complexity: enhanced
scope: project

# Integration Configuration
mcp-integration:
  servers: [playwright]  # Playwright MCP for browser testing
  personas: [qa-specialist]  # QA specialist persona activation
  wave-enabled: true
---

# /sg:test - Testing and Quality Assurance

## Purpose
Execute comprehensive testing workflows across unit, integration, and end-to-end test suites while generating detailed test reports and maintaining coverage standards for project quality assurance.

## Usage
```
/sg:test [target] [--type unit|integration|e2e|all] [--coverage] [--watch] [--fix]
```

## Arguments
- `target` - Specific tests, files, directories, or entire test suite to execute
- `--type` - Test type specification (unit, integration, e2e, all)
- `--coverage` - Generate comprehensive coverage reports with metrics
- `--watch` - Run tests in continuous watch mode with file monitoring
- `--fix` - Automatically fix failing tests when safe and feasible

## Execution

### Traditional Testing Workflow (Default)
1. Discover and categorize available tests using test runner patterns and file conventions
2. Execute tests with appropriate configuration, environment setup, and parallel execution
3. Monitor test execution, collect real-time metrics, and track progress
4. Generate comprehensive test reports with coverage analysis and failure diagnostics
5. Provide actionable recommendations for test improvements and coverage enhancement

## Gemini CLI Integration
- **Tool Usage**: Bash for test runner execution, Glob for test discovery, Grep for result parsing
- **File Operations**: Reads test configurations, writes coverage reports and test summaries
- **Analysis Approach**: Pattern-based test categorization with execution metrics collection
- **Output Format**: Structured test reports with coverage percentages and failure analysis

## Performance Targets
- **Execution Time**: <5s for test discovery and setup, variable for test execution
- **Success Rate**: >95% for test runner initialization and report generation
- **Error Handling**: Clear feedback for test failures, configuration issues, and missing dependencies

## Examples

### Basic Usage
```
/sg:test
# Executes all available tests with standard configuration
# Generates basic test report with pass/fail summary
```

### Advanced Usage
```
/sg:test src/components --type unit --coverage --fix
# Runs unit tests for components directory with coverage reporting
# Automatically fixes simple test failures where safe to do so
```

### Browser Testing Usage
```
/sg:test --type e2e
# Runs end-to-end tests using Playwright for browser automation
# Comprehensive UI testing with cross-browser compatibility

/sg:test src/components --coverage --watch
# Unit tests for components with coverage reporting in watch mode
# Continuous testing during development with live feedback
```

## Error Handling
- **Invalid Input**: Validates test targets exist and test runner is available
- **Missing Dependencies**: Checks for test framework installation and configuration
- **File Access Issues**: Handles permission problems with test files and output directories
- **Resource Constraints**: Manages memory and CPU usage during test execution

## Integration Points
- **SuperGemini Framework**: Integrates with build and analyze commands for CI/CD workflows
- **Other Commands**: Commonly follows build command and precedes deployment operations
- **File System**: Reads test configurations, writes reports to project test output directories

## Boundaries

**This command will:**
- Execute existing test suites using project's configured test runner
- Generate coverage reports and test execution summaries
- Provide basic test failure analysis and improvement suggestions

**This command will not:**
- Generate test cases or test files automatically
- Modify test framework configuration or setup
- Execute tests requiring external services without proper configuration