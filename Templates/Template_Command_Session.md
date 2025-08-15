---
name: [command-name]
description: "[Session lifecycle management with Serena MCP integration and performance requirements]"
allowed-tools: [Read, Grep, Glob, Write, activate_project, read_memory, write_memory, list_memories, check_onboarding_performed, onboarding, think_about_*]

# Command Classification
category: session
complexity: standard
scope: cross-session

# Integration Configuration
mcp-integration:
  servers: [serena]  # Mandatory Serena MCP integration
  personas: []  # No persona activation required
  wave-enabled: false
  complexity-threshold: 0.3

# Performance Profile
performance-profile: session-critical
performance-targets:
  initialization: <500ms
  core-operations: <200ms
  checkpoint-creation: <1s
  memory-operations: <200ms
---

# /sg:[command-name] - [Session Command Title]

## Purpose
[Clear statement of the command's role in session lifecycle management. Explain how it maintains context continuity, enables cross-session persistence, and supports the SuperGemini framework's session management capabilities.]

## Usage
```
/sg:[command-name] [--type memory|checkpoint|state] [--resume] [--validate] [--performance]
```

## Arguments
- `target` - [Optional target for focused session operations]
- `--type` - [Type of session operation: memory, checkpoint, or state management]
- `--resume` - [Resume from previous session or checkpoint]
- `--validate` - [Validate session integrity and data consistency]
- `--performance` - [Enable performance monitoring and optimization]
- `--metadata` - [Include comprehensive session metadata]
- `--cleanup` - [Perform session cleanup and optimization]

## Session Lifecycle Integration

### 1. Session State Management
- Analyze current session state and context requirements
- Identify critical information for persistence or restoration
- Assess session integrity and continuity needs

### 2. Serena MCP Coordination
- Execute appropriate Serena MCP operations for session management
- Handle memory organization, checkpoint creation, or state restoration
- Manage cross-session context preservation and enhancement

### 3. Performance Validation
- Monitor operation performance against strict session targets
- Validate memory efficiency and response time requirements
- Ensure session operations meet <200ms core operation targets

### 4. Context Continuity
- Maintain session context across operations and interruptions
- Preserve decision history, task progress, and accumulated insights
- Enable seamless continuation of complex multi-session workflows

### 5. Quality Assurance
- Validate session data integrity and completeness
- Verify cross-session compatibility and version consistency
- Generate session analytics and performance reports

## Mandatory Serena MCP Integration

### Core Serena Operations
- **Memory Management**: `read_memory`, `write_memory`, `list_memories`
- **Project Management**: `activate_project`, `get_current_config`
- **Reflection System**: `think_about_*` tools for session analysis
- **State Management**: Session state persistence and restoration capabilities

### Session Data Organization
- **Memory Hierarchy**: Structured memory organization for efficient retrieval
- **Checkpoint System**: Progressive checkpoint creation with metadata
- **Context Accumulation**: Building understanding across session boundaries
- **Performance Metrics**: Session operation timing and efficiency tracking

### Advanced Session Features
- **Automatic Triggers**: Time-based, task-based, and risk-based session operations
- **Error Recovery**: Robust session recovery and state restoration mechanisms
- **Cross-Session Learning**: Accumulating knowledge and patterns across sessions
- **Performance Optimization**: Session-level caching and efficiency improvements

## Session Management Patterns

### Memory Operations
- **Memory Categories**: Project, session, checkpoint, and insight memory organization
- **Intelligent Retrieval**: Context-aware memory loading and optimization
- **Memory Lifecycle**: Creation, update, archival, and cleanup operations
- **Cross-Reference Management**: Maintaining relationships between memory entries

### Checkpoint Operations
- **Progressive Checkpoints**: Building understanding and state across checkpoints
- **Metadata Enrichment**: Comprehensive checkpoint metadata with recovery information
- **State Validation**: Ensuring checkpoint integrity and completeness
- **Recovery Mechanisms**: Robust restoration from checkpoint failures

### Context Operations
- **Context Preservation**: Maintaining critical context across session boundaries
- **Context Enhancement**: Building richer context through accumulated experience
- **Context Optimization**: Efficient context management and storage
- **Context Validation**: Ensuring context consistency and accuracy

## Performance Requirements

### Critical Performance Targets
- **Session Initialization**: <500ms for complete session setup
- **Core Operations**: <200ms for memory reads, writes, and basic operations
- **Checkpoint Creation**: <1s for comprehensive checkpoint with metadata
- **Memory Operations**: <200ms per individual memory operation
- **Context Loading**: <300ms for full context restoration

### Performance Monitoring
- **Real-Time Metrics**: Continuous monitoring of operation performance
- **Performance Analytics**: Detailed analysis of session operation efficiency
- **Optimization Recommendations**: Automated suggestions for performance improvement
- **Resource Management**: Efficient memory and processing resource utilization

### Performance Validation
- **Automated Testing**: Continuous validation of performance targets
- **Performance Regression Detection**: Monitoring for performance degradation
- **Benchmark Comparison**: Comparing against established performance baselines
- **Performance Reporting**: Detailed performance analytics and recommendations

## Error Handling & Recovery

### Session-Critical Error Handling
- **Data Integrity Errors**: Comprehensive validation and recovery procedures
- **Memory Access Failures**: Robust fallback and retry mechanisms
- **Context Corruption**: Recovery strategies for corrupted session context
- **Performance Degradation**: Automatic optimization and resource management

### Recovery Strategies
- **Graceful Degradation**: Maintaining core functionality under adverse conditions
- **Automatic Recovery**: Intelligent recovery from common failure scenarios
- **Manual Recovery**: Clear escalation paths for complex recovery situations
- **State Reconstruction**: Rebuilding session state from available information

### Error Categories
- **Serena MCP Errors**: Specific handling for Serena server communication issues
- **Memory System Errors**: Memory corruption, access, and consistency issues
- **Performance Errors**: Operation timeout and resource constraint handling
- **Integration Errors**: Cross-system integration and coordination failures

## Session Analytics & Reporting

### Performance Analytics
- **Operation Timing**: Detailed timing analysis for all session operations
- **Resource Utilization**: Memory, processing, and network resource tracking
- **Efficiency Metrics**: Session operation efficiency and optimization opportunities
- **Trend Analysis**: Performance trends and improvement recommendations

### Session Intelligence
- **Usage Patterns**: Analysis of session usage and optimization opportunities
- **Context Evolution**: Tracking context development and enhancement over time
- **Success Metrics**: Session effectiveness and user satisfaction tracking
- **Predictive Analytics**: Intelligent prediction of session needs and optimization

### Quality Metrics
- **Data Integrity**: Comprehensive validation of session data quality
- **Context Accuracy**: Ensuring session context remains accurate and relevant
- **Performance Compliance**: Validation against performance targets and requirements
- **User Experience**: Session impact on overall user experience and productivity

## Integration Ecosystem

### SuperGemini Framework Integration
- **Command Coordination**: Integration with other SuperGemini commands for session support
- **Quality Gates**: Integration with validation cycles and quality assurance
- **Mode Coordination**: Support for different operational modes and contexts
- **Workflow Integration**: Seamless integration with complex workflow operations

### Cross-Session Coordination
- **Multi-Session Projects**: Managing complex projects spanning multiple sessions
- **Context Handoff**: Smooth transition of context between sessions and users
- **Collaborative Sessions**: Support for multi-user session coordination
- **Session Hierarchies**: Managing parent-child session relationships

## Examples

### Basic Session Operation
```
/sg:[command-name] --type memory
# Standard memory management operation
```

### Session Checkpoint
```
/sg:[command-name] --type checkpoint --metadata
# Create comprehensive checkpoint with metadata
```

### Session Recovery
```
/sg:[command-name] --resume --validate
# Resume from previous session with validation
```

### Performance Monitoring
```
/sg:[command-name] --performance --validate
# Session operation with performance monitoring
```

## Boundaries

**This session command will:**
- [Provide robust session lifecycle management with strict performance requirements]
- [Integrate seamlessly with Serena MCP for comprehensive session capabilities]
- [Maintain context continuity and cross-session persistence effectively]
- [Support complex multi-session workflows with intelligent state management]
- [Deliver session operations within strict performance targets consistently]

**This session command will not:**
- [Operate without proper Serena MCP integration and connectivity]
- [Compromise performance targets for additional functionality]
- [Proceed without proper session state validation and integrity checks]
- [Function without adequate error handling and recovery mechanisms]

---

# Template Usage Guidelines

## Implementation Requirements
This template is designed for session management commands that require:
- Mandatory Serena MCP integration for all core functionality
- Strict performance targets for session-critical operations
- Cross-session context persistence and continuity
- Comprehensive session lifecycle management
- Advanced error handling and recovery capabilities

## Serena MCP Integration Requirements

### Mandatory Tools
All session commands must integrate with these Serena MCP tools:
- **Memory Management**: read_memory, write_memory, list_memories, delete_memory
- **Project Management**: activate_project, get_current_config
- **Reflection System**: think_about_* tools for session analysis and validation
- **State Management**: Session state persistence and restoration capabilities

### Integration Patterns
- **Memory-First Approach**: All operations should leverage Serena memory system
- **Performance Validation**: Continuous monitoring against strict performance targets
- **Context Preservation**: Maintaining rich context across session boundaries
- **Error Recovery**: Robust recovery mechanisms for session-critical failures

## Performance Validation Requirements

### Critical Performance Targets
Session commands must meet these non-negotiable performance requirements:
- Session initialization: <500ms for complete setup
- Core operations: <200ms for memory and basic operations
- Checkpoint creation: <1s for comprehensive checkpoints
- Memory operations: <200ms per individual operation

### Performance Monitoring
- Real-time performance tracking and validation
- Automated performance regression detection
- Detailed performance analytics and reporting
- Resource optimization and efficiency recommendations

## Quality Standards

### Session Command Requirements
- [ ] Mandatory Serena MCP integration is properly implemented
- [ ] All performance targets are realistic and consistently achievable
- [ ] Cross-session context persistence works reliably
- [ ] Error handling covers all session-critical failure scenarios
- [ ] Memory organization follows established patterns
- [ ] Session lifecycle integration is comprehensive
- [ ] Performance monitoring and analytics are functional

---

*This template is specifically designed for session management commands that provide critical session lifecycle capabilities with mandatory Serena MCP integration and strict performance requirements.*