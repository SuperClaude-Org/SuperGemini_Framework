---
name: select-tool
description: "Intelligent MCP tool selection based on complexity scoring and operation analysis"
allowed-tools: [get_current_config, execute_sketched_edit, Read, Grep]

# Command Classification
category: special
complexity: high
scope: meta

# Integration Configuration
mcp-integration:
  servers: [serena, morphllm]
  personas: []
  wave-enabled: false
  complexity-threshold: 0.6

# Performance Profile
performance-profile: specialized
---

# /sg:select-tool - Intelligent MCP Tool Selection

## Purpose
Analyze requested operations and determine the optimal MCP tool (Serena or Morphllm) based on sophisticated complexity scoring, operation type classification, and performance requirements. This meta-system command provides intelligent routing to ensure optimal tool selection with <100ms decision time and >95% accuracy.

## Usage
```
/sg:select-tool [operation] [--analyze] [--explain] [--force serena|morphllm]
```

## Arguments
- `operation` - Description of the operation to perform and analyze
- `--analyze` - Show detailed complexity analysis and scoring breakdown
- `--explain` - Explain the selection decision with confidence metrics
- `--force serena|morphllm` - Override automatic selection for testing
- `--validate` - Validate selection against actual operation requirements
- `--dry-run` - Preview selection decision without tool activation

## Specialized Execution Flow

### 1. Unique Analysis Phase
- **Operation Parsing**: Extract operation type, scope, language, and complexity indicators
- **Context Evaluation**: Analyze file count, dependencies, and framework requirements
- **Performance Assessment**: Evaluate speed vs accuracy trade-offs for operation

### 2. Specialized Processing
- **Complexity Scoring Algorithm**: Apply multi-dimensional scoring based on file count, operation type, dependencies, and language complexity
- **Decision Logic Matrix**: Use sophisticated routing rules combining direct mappings and threshold-based selection
- **Tool Capability Matching**: Match operation requirements to specific tool capabilities

### 3. Custom Integration
- **MCP Server Coordination**: Seamless integration with Serena and Morphllm servers
- **Framework Routing**: Automatic integration with other SuperGemini commands
- **Performance Optimization**: Sub-100ms decision time with confidence scoring

### 4. Specialized Validation
- **Accuracy Verification**: >95% correct tool selection rate validation
- **Performance Monitoring**: Track decision time and execution success rates
- **Fallback Testing**: Verify fallback paths and error recovery

### 5. Custom Output Generation
- **Decision Explanation**: Detailed analysis output with confidence metrics
- **Performance Metrics**: Tool selection effectiveness and timing data
- **Integration Guidance**: Recommendations for command workflow optimization

## Custom Architecture Features

### Specialized System Integration
- **Multi-Tool Coordination**: Intelligent routing between Serena (LSP, symbols) and Morphllm (patterns, speed)
- **Command Integration**: Automatic selection logic used by refactor, edit, implement, and improve commands
- **Performance Monitoring**: Real-time tracking of selection accuracy and execution success

### Unique Processing Capabilities
- **Complexity Scoring**: Multi-dimensional algorithm considering file count, operation type, dependencies, and language
- **Decision Matrix**: Sophisticated routing logic with direct mappings and threshold-based selection
- **Capability Matching**: Operation requirements matched to specific tool strengths

### Custom Performance Characteristics
- **Sub-100ms Decisions**: Ultra-fast tool selection with performance guarantees
- **95%+ Accuracy**: High-precision tool selection validated through execution tracking
- **Optimal Performance**: Best tool selection for operation characteristics

## Advanced Specialized Features

### Intelligent Routing Algorithm
- **Direct Operation Mapping**: symbol_operations → Serena, pattern_edits → Morphllm, memory_operations → Serena
- **Complexity-Based Selection**: score > 0.6 → Serena, score < 0.4 → Morphllm, 0.4-0.6 → feature-based
- **Feature Requirement Analysis**: needs_lsp → Serena, needs_patterns → Morphllm, needs_semantic → Serena, needs_speed → Morphllm

### Multi-Dimensional Complexity Analysis
- **File Count Scoring**: Logarithmic scaling for multi-file operations
- **Operation Type Weighting**: Refactoring > renaming > editing complexity hierarchy
- **Dependency Analysis**: Cross-file dependencies increase complexity scores
- **Language Complexity**: Framework and language-specific complexity factors

### Performance Optimization Patterns
- **Decision Caching**: Cache frequent operation patterns for instant selection
- **Fallback Strategies**: Serena → Morphllm → Native tools fallback chain
- **Availability Checking**: Real-time tool availability with graceful degradation

## Specialized Tool Coordination

### Custom Tool Integration
- **Serena MCP**: Symbol operations, multi-file refactoring, LSP integration, semantic analysis
- **Morphllm MCP**: Pattern-based edits, token optimization, fast apply capabilities, simple modifications
- **Native Tools**: Fallback coordination when MCP servers unavailable

### Unique Tool Patterns
- **Hybrid Intelligence**: Serena for complex analysis, Morphllm for efficient execution
- **Progressive Fallback**: Intelligent degradation from advanced to basic tools
- **Performance-Aware Selection**: Speed vs capability trade-offs based on operation urgency

### Tool Performance Optimization
- **Sub-100ms Selection**: Lightning-fast decision making with complexity scoring
- **Accuracy Tracking**: >95% correct selection rate with continuous validation
- **Resource Awareness**: Tool availability and performance characteristic consideration

## Custom Error Handling

### Specialized Error Categories
- **Tool Unavailability**: Graceful fallback when selected MCP server unavailable
- **Selection Ambiguity**: Handling edge cases where multiple tools could work
- **Performance Degradation**: Recovery when tool selection doesn't meet performance targets

### Custom Recovery Strategies
- **Progressive Fallback**: Serena → Morphllm → Native tools with capability preservation
- **Alternative Selection**: Re-analyze with different parameters when initial selection fails
- **Graceful Degradation**: Clear explanation of limitations when optimal tools unavailable

### Error Prevention
- **Real-time Availability**: Check tool availability before selection commitment
- **Confidence Scoring**: Provide uncertainty indicators for borderline selections
- **Validation Hooks**: Pre-execution validation of tool selection appropriateness

## Integration Patterns

### SuperGemini Framework Integration
- **Automatic Command Integration**: Used by refactor, edit, implement, improve commands
- **Performance Monitoring**: Integration with framework performance tracking
- **Quality Gates**: Selection validation within SuperGemini quality assurance cycle

### Custom MCP Integration
- **Serena Coordination**: Symbol analysis, multi-file operations, LSP integration
- **Morphllm Coordination**: Pattern recognition, token optimization, fast apply operations
- **Availability Management**: Real-time server status and capability assessment

### Specialized System Coordination
- **Command Workflow**: Seamless integration with other SuperGemini commands
- **Performance Tracking**: Selection effectiveness and execution success monitoring
- **Framework Evolution**: Continuous improvement of selection algorithms

## Performance & Scalability

### Specialized Performance Requirements
- **Decision Time**: <100ms for tool selection regardless of operation complexity
- **Selection Accuracy**: >95% correct tool selection validated through execution tracking
- **Success Rate**: >90% successful execution with selected tools

### Custom Resource Management
- **Memory Efficiency**: Lightweight complexity scoring with minimal resource usage
- **CPU Optimization**: Fast decision algorithms with minimal computational overhead
- **Cache Management**: Intelligent caching of frequent operation patterns

### Scalability Characteristics
- **Operation Complexity**: Scales from simple edits to complex multi-file refactoring
- **Project Size**: Handles projects from single files to large codebases
- **Performance Consistency**: Maintains sub-100ms decisions across all scales

## Examples

### Basic Specialized Operation
```
/sg:select-tool "fix typo in README.md"
# Result: Morphllm (simple edit, single file, token optimization beneficial)
```

### Advanced Specialized Usage
```
/sg:select-tool "extract authentication logic into separate service" --analyze --explain
# Result: Serena (high complexity, architectural change, needs LSP and semantic analysis)
```

### System-Level Operation
```
/sg:select-tool "rename function getUserData to fetchUserProfile across all files" --validate
# Result: Serena (symbol operation, multi-file scope, cross-file dependencies)
```

### Meta-Operation Example
```
/sg:select-tool "convert all var declarations to const in JavaScript files" --dry-run --explain
# Result: Morphllm (pattern-based operation, token optimization, framework patterns)
```

## Quality Standards

### Specialized Validation Criteria
- **Selection Accuracy**: >95% correct tool selection validated through execution outcomes
- **Performance Guarantee**: <100ms decision time with complexity scoring and analysis
- **Success Rate Validation**: >90% successful execution with selected tools

### Custom Success Metrics
- **Decision Confidence**: Confidence scoring for selection decisions with uncertainty indicators
- **Execution Effectiveness**: Track actual performance of selected tools vs alternatives
- **Integration Success**: Seamless integration with SuperGemini command ecosystem

### Specialized Compliance Requirements
- **Framework Integration**: Full compliance with SuperGemini orchestration patterns
- **Performance Standards**: Meet or exceed specified timing and accuracy requirements
- **Quality Assurance**: Integration with SuperGemini quality gate validation cycle

## Boundaries

**This specialized command will:**
- Analyze operations and select optimal MCP tools with >95% accuracy
- Provide sub-100ms decision time with detailed complexity scoring
- Integrate seamlessly with other SuperGemini commands for automatic tool routing
- Maintain high success rates through intelligent fallback and error recovery

**This specialized command will not:**
- Execute the actual operations (only selects tools for execution)
- Override user preferences when explicit tool selection is provided
- Compromise system stability through experimental or untested tool selections
- Make selections without proper availability verification and fallback planning