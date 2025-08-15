---
name: reflect
description: "Session lifecycle management with Serena MCP integration and performance requirements for task reflection and validation"
allowed-tools: [think_about_task_adherence, think_about_collected_information, think_about_whether_you_are_done, read_memory, write_memory, list_memories, TodoRead, TodoWrite]

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

# /sg:reflect - Task Reflection and Validation

## Purpose
Perform comprehensive task reflection and validation using Serena MCP reflection tools, bridging traditional TodoWrite patterns with Serena's analysis capabilities for enhanced task management with session lifecycle integration and cross-session persistence capabilities.

## Usage
```
/sg:reflect [--type task|session|completion] [--analyze] [--update-session] [--validate] [--performance] [--metadata] [--cleanup]
```

## Arguments
- `--type` - Reflection type (task, session, completion)
- `--analyze` - Perform deep analysis of collected information
- `--update-session` - Update session metadata with reflection results
- `--checkpoint` - Create checkpoint after reflection if needed
- `--validate` - Validate session integrity and data consistency
- `--performance` - Enable performance monitoring and optimization
- `--metadata` - Include comprehensive session metadata
- `--cleanup` - Perform session cleanup and optimization

## Session Lifecycle Integration

### 1. Session State Management
- Analyze current session state and context requirements
- Call `think_about_task_adherence` to validate current approach
- Check if current work aligns with project goals and session objectives
- Identify any deviations from planned approach
- Generate recommendations for course correction if needed
- Identify critical information for persistence or restoration
- Assess session integrity and continuity needs

### 2. Serena MCP Coordination with Token Efficiency
- Execute appropriate Serena MCP operations for session management
- Call `think_about_collected_information` to analyze session work with selective compression
- **Content Classification for Reflection Operations**:
  - **SuperGemini Framework** (Complete exclusion): All framework directories and components
  - **Session Data** (Apply compression): Reflection metadata, analysis results, insights only
  - **User Project Content** (Preserve fidelity): Project files, user documentation, configurations
- Evaluate completeness of information gathering with optimized memory operations
- Identify gaps or missing context using compressed reflection data
- Assess quality and relevance of collected data with framework exclusion awareness
- Handle memory organization, checkpoint creation, or state restoration with selective compression
- Manage cross-session context preservation and enhancement with optimized storage

### 3. Performance Validation
- Monitor operation performance against strict session targets
- Task reflection: <4s for comprehensive analysis (improved with Token Efficiency)
- Session reflection: <8s for full information assessment (improved with selective compression)
- Completion reflection: <2.5s for validation (improved with optimized operations)
- TodoWrite integration: <800ms for status synchronization (improved with compression)
- Token Efficiency overhead: <100ms for selective compression operations
- Validate memory efficiency and response time requirements
- Ensure session operations meet <200ms core operation targets

### 4. Context Continuity
- Maintain session context across operations and interruptions
- Call `think_about_whether_you_are_done` for completion validation
- Evaluate task completion criteria against actual progress
- Identify remaining work items or blockers
- Determine if current task can be marked as complete
- Preserve decision history, task progress, and accumulated insights
- Enable seamless continuation of complex multi-session workflows

### 5. Quality Assurance
- Validate session data integrity and completeness
- Use `TodoRead` to get current task states
- Map TodoWrite tasks to Serena reflection insights
- Update task statuses based on reflection results
- Maintain compatibility with existing TodoWrite patterns
- If --update-session flag: Load current session metadata and incorporate reflection insights
- Verify cross-session compatibility and version consistency
- Generate session analytics and performance reports

## Mandatory Serena MCP Integration

### Core Serena Operations
- **Memory Management**: `read_memory`, `write_memory`, `list_memories`
- **Reflection System**: `think_about_task_adherence`, `think_about_collected_information`, `think_about_whether_you_are_done`
- **TodoWrite Integration**: Bridge patterns for task management evolution
- **State Management**: Session state persistence and restoration capabilities

### Session Data Organization
- **Memory Hierarchy**: Structured memory organization for efficient retrieval
- **Task Reflection Patterns**: Systematic validation and progress assessment
- **Performance Metrics**: Session operation timing and efficiency tracking
- **Context Accumulation**: Building understanding across session boundaries

### Advanced Session Features
- **TodoWrite Evolution**: Bridge patterns for transitioning from TodoWrite to Serena reflection
- **Cross-Session Learning**: Accumulating knowledge and patterns across sessions
- **Performance Optimization**: Session-level caching and efficiency improvements
- **Quality Gates Integration**: Validation checkpoints during reflection phases

## Session Management Patterns

### Memory Operations
- **Memory Categories**: Project, session, checkpoint, and insight memory organization
- **Intelligent Retrieval**: Context-aware memory loading and optimization
- **Memory Lifecycle**: Creation, update, archival, and cleanup operations
- **Cross-Reference Management**: Maintaining relationships between memory entries

### Reflection Operations
- **Task Reflection**: Current task validation and progress assessment
- **Session Reflection**: Overall session progress and information quality
- **Completion Reflection**: Task and session completion readiness
- **TodoWrite Bridge**: Integration patterns for traditional task management

### Context Operations
- **Context Preservation**: Maintaining critical context across session boundaries
- **Context Enhancement**: Building richer context through accumulated experience
- **Context Optimization**: Efficient context management and storage
- **Context Validation**: Ensuring context consistency and accuracy

## Reflection Types

### Task Reflection (--type task)
**Focus**: Current task validation and progress assessment

**Tools Used**: 
- `think_about_task_adherence`
- `TodoRead` for current state
- `TodoWrite` for status updates

**Output**:
- Task alignment assessment
- Progress validation
- Next steps recommendations
- Risk assessment

### Session Reflection (--type session)
**Focus**: Overall session progress and information quality

**Tools Used**:
- `think_about_collected_information`
- Session metadata analysis

**Output**:
- Information completeness assessment
- Session progress summary
- Knowledge gaps identification
- Learning insights extraction

### Completion Reflection (--type completion)
**Focus**: Task and session completion readiness

**Tools Used**:
- `think_about_whether_you_are_done`
- Final validation checks

**Output**:
- Completion readiness assessment
- Outstanding items identification
- Quality validation results
- Handoff preparation status

## Integration Patterns

### With TodoWrite System
```yaml
# Bridge pattern for TodoWrite integration
traditional_pattern:
  - TodoRead() → Assess tasks
  - Work on tasks
  - TodoWrite() → Update status

enhanced_pattern:
  - TodoRead() → Get current state
  - /sg:reflect --type task → Validate approach
  - Work on tasks with Serena guidance
  - /sg:reflect --type completion → Validate completion
  - TodoWrite() → Update with reflection insights
```

### With Session Lifecycle
```yaml
# Integration with /sg:load and /sg:save
session_integration:
  - /sg:load → Initialize session
  - Work with periodic /sg:reflect --type task
  - /sg:reflect --type session → Mid-session analysis
  - /sg:reflect --type completion → Pre-save validation
  - /sg:save → Persist with reflection insights
```

### With Automatic Checkpoints
```yaml
# Checkpoint integration
checkpoint_triggers:
  - High priority task completion → /sg:reflect --type completion
  - 30-minute intervals → /sg:reflect --type session
  - Before risk operations → /sg:reflect --type task
  - Error recovery → /sg:reflect --analyze
```

## Performance Requirements

### Critical Performance Targets
- **Session Initialization**: <500ms for complete session setup
- **Core Operations**: <200ms for memory reads, writes, and basic operations
- **Memory Operations**: <200ms per individual memory operation
- **Task Reflection**: <5s for comprehensive analysis
- **Session Reflection**: <10s for full information assessment
- **Completion Reflection**: <3s for validation
- **TodoWrite Integration**: <1s for status synchronization

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

### Quality Metrics
- Task adherence accuracy: >90%
- Information completeness: >85%
- Completion readiness: >95%
- Session continuity: >90%

## Error Handling & Recovery

### Session-Critical Error Handling
- **Data Integrity Errors**: Comprehensive validation and recovery procedures
- **Memory Access Failures**: Robust fallback and retry mechanisms
- **Context Corruption**: Recovery strategies for corrupted session context
- **Performance Degradation**: Automatic optimization and resource management
- **Serena MCP Unavailable**: Fall back to TodoRead/TodoWrite patterns
- **Reflection Inconsistencies**: Cross-validate reflection results

### Recovery Strategies
- **Graceful Degradation**: Maintaining core functionality under adverse conditions
- **Automatic Recovery**: Intelligent recovery from common failure scenarios
- **Manual Recovery**: Clear escalation paths for complex recovery situations
- **State Reconstruction**: Rebuilding session state from available information
- **Cache Reflection**: Cache reflection insights locally
- **Retry Integration**: Retry Serena integration when available

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
- **Session Hierarchies**: Managing parent-child session relationships
- **Continuous Learning**: Each session builds on previous knowledge and insights

### Integration with Hooks

#### Hook Integration Points
- `task_validator` hook: Enhanced with reflection insights
- `state_synchronizer` hook: Uses reflection for state management
- `quality_gate_trigger` hook: Incorporates reflection validation
- `evidence_collector` hook: Captures reflection outcomes

#### Performance Monitoring
- Track reflection timing in session metadata
- Monitor reflection accuracy and effectiveness
- Alert if reflection processes exceed performance targets
- Integrate with overall session performance metrics

## Examples

### Basic Task Reflection
```
/sg:reflect --type task
# Validates current task approach and progress
```

### Session Checkpoint
```
/sg:reflect --type session --metadata
# Create comprehensive session analysis with metadata
```

### Session Recovery
```
/sg:reflect --type completion --validate
# Completion validation with integrity checks
```

### Performance Monitoring
```
/sg:reflect --performance --validate
# Session operation with performance monitoring
```

### Comprehensive Session Analysis
```
/sg:reflect --type session --analyze --update-session
# Deep session analysis with metadata update
```

### Pre-Completion Validation
```
/sg:reflect --type completion
# Validates readiness to mark tasks complete
```

### Checkpoint-Triggered Reflection
```
/sg:reflect --type session --checkpoint
# Session reflection with automatic checkpoint creation
```

## Output Format

### Task Reflection Output
```yaml
task_reflection:
  adherence_score: 0.92
  alignment_status: "on_track"
  deviations_identified: []
  recommendations:
    - "Continue current approach"
    - "Consider performance optimization"
  risk_level: "low"
  next_steps:
    - "Complete implementation"
    - "Run validation tests"
```

### Session Reflection Output
```yaml
session_reflection:
  information_completeness: 0.87
  gaps_identified:
    - "Missing error handling patterns"
    - "Performance benchmarks needed"
  insights_gained:
    - "Framework integration successful"
    - "Session lifecycle pattern validated"
  learning_opportunities:
    - "Advanced Serena patterns"
    - "Performance optimization techniques"
```

### Completion Reflection Output
```yaml
completion_reflection:
  readiness_score: 0.95
  outstanding_items: []
  quality_validation: "pass"
  completion_criteria:
    - criterion: "functionality_complete"
      status: "met"
    - criterion: "tests_passing"
      status: "met"
    - criterion: "documentation_updated"
      status: "met"
  handoff_ready: true
```

## Future Evolution

### Python Hooks Integration
When Python hooks system is implemented:
- Automatic reflection triggers based on task state changes
- Real-time reflection insights during work sessions
- Intelligent checkpoint decisions based on reflection analysis
- Enhanced TodoWrite replacement with full Serena integration

### Advanced Reflection Patterns
- Cross-session reflection for project-wide insights
- Collaborative reflection for team workflows
- Predictive reflection for proactive issue identification
- Automated reflection scheduling based on work patterns

## Boundaries

**This session command will:**
- Provide robust session lifecycle management with strict performance requirements
- Integrate seamlessly with Serena MCP for comprehensive session capabilities
- Maintain context continuity and cross-session persistence effectively
- Support complex multi-session workflows with intelligent state management
- Deliver session operations within strict performance targets consistently
- Bridge TodoWrite patterns with advanced Serena reflection capabilities

**This session command will not:**
- Operate without proper Serena MCP integration and connectivity
- Compromise performance targets for additional functionality
- Proceed without proper session state validation and integrity checks
- Function without adequate error handling and recovery mechanisms
- Skip TodoWrite integration and compatibility maintenance
- Ignore reflection quality metrics and validation requirements