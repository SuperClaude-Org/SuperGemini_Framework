---
name: build
description: "Build, compile, and package projects with comprehensive error handling, optimization, and automated validation"
allowed-tools: [Read, Bash, Grep, Glob, Write]

# Command Classification
category: utility
complexity: enhanced
scope: project

# Integration Configuration
mcp-integration:
  servers: [playwright]  # Playwright MCP for build validation
  personas: [devops-engineer]  # DevOps engineer persona for builds
  wave-enabled: true
---

# /sg:build - Project Building and Packaging

## Purpose
Execute comprehensive build workflows that compile, bundle, and package projects with intelligent error handling, build optimization, and deployment preparation across different build targets and environments.

## Usage
```
/sg:build [target] [--type dev|prod|test] [--clean] [--optimize] [--verbose]
```

## Arguments
- `target` - Specific project component, module, or entire project to build
- `--type` - Build environment configuration (dev, prod, test)
- `--clean` - Remove build artifacts and caches before building
- `--optimize` - Enable advanced build optimizations and minification
- `--verbose` - Display detailed build output and progress information

## Execution

### Standard Build Workflow (Default)
1. Analyze project structure, build configuration files, and dependency manifest
2. Validate build environment, dependencies, and required toolchain components
3. Execute build process with real-time monitoring and error detection
4. Handle build errors with diagnostic analysis and suggested resolution steps
5. Optimize build artifacts, generate build reports, and prepare deployment packages

## Gemini CLI Integration
- **Tool Usage**: Bash for build system execution, Read for configuration analysis, Grep for error parsing
- **File Operations**: Reads build configs and package manifests, writes build logs and artifact reports
- **Analysis Approach**: Configuration-driven build orchestration with dependency validation
- **Output Format**: Structured build reports with artifact sizes, timing metrics, and error diagnostics

## Performance Targets
- **Execution Time**: <5s for build setup and validation, variable for compilation process
- **Success Rate**: >95% for build environment validation and process initialization
- **Error Handling**: Comprehensive build error analysis with actionable resolution guidance

## Examples

### Basic Usage
```
/sg:build
# Builds entire project using default configuration
# Generates standard build artifacts in output directory
```

### Advanced Usage
```
/sg:build frontend --type prod --clean --optimize --verbose
# Clean production build of frontend module with optimizations
# Displays detailed build progress and generates optimized artifacts
```

## Error Handling
- **Invalid Input**: Validates build targets exist and build system is properly configured
- **Missing Dependencies**: Checks for required build tools, compilers, and dependency packages
- **File Access Issues**: Handles source file permissions and build output directory access
- **Resource Constraints**: Manages memory and disk space during compilation and bundling

## Integration Points
- **SuperGemini Framework**: Coordinates with test command for build verification and analyze for quality checks
- **Other Commands**: Precedes test and deployment workflows, integrates with git for build tagging
- **File System**: Reads source code and configurations, writes build artifacts to designated output directories

## Boundaries

**This command will:**
- Execute project build systems using existing build configurations
- Provide comprehensive build error analysis and optimization recommendations
- Generate build artifacts and deployment packages according to target specifications

**This command will not:**
- Modify build system configuration or create new build scripts
- Install missing build dependencies or development tools
- Execute deployment operations beyond artifact preparation