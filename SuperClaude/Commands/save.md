---
name: save
description: "Session lifecycle management with Serena MCP integration and performance requirements for session context persistence"
allowed-tools: [Read, Grep, Glob, Write, write_memory, list_memories, read_memory, summarize_changes, think_about_collected_information]

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
  auto-flags: []  # No automatic flags

# Performance Profile
performance-profile: session-critical
performance-targets:
  initialization: <500ms
  core-operations: <200ms
  checkpoint-creation: <1s
  memory-operations: <200ms
---

# /sg:save - Session Context Persistence

## Purpose
Save session context, progress, and discoveries to Serena MCP memories, complementing the /sg:load workflow for continuous project understanding with comprehensive session lifecycle management and cross-session persistence capabilities.

## Usage
```
/sg:save [--type session|learnings|context|all] [--summarize] [--checkpoint] [--validate] [--performance] [--metadata] [--cleanup] [--uc]
```

## Arguments
- `--type` - What to save (session, learnings, context, all)
- `--summarize` - Generate session summary using Serena's summarize_changes
- `--checkpoint` - Create a session checkpoint for recovery
- `--prune` - Remove outdated or redundant memories
- `--validate` - Validate session integrity and data consistency
- `--performance` - Enable performance monitoring and optimization
- `--metadata` - Include comprehensive session metadata
- `--cleanup` - Perform session cleanup and optimization
- `--uc` - Enable Token Efficiency mode for all memory operations (optional)

## Token Efficiency Integration

### Optional Token Efficiency Mode
The `/sg:save` command supports optional Token Efficiency mode via the `--uc` flag:

- **User Choice**: `--uc` flag can be explicitly specified for compression
- **Compression Strategy**: When enabled: 30-50% reduction with ≥95% information preservation
- **Content Classification**:
  - **SuperGemini Framework** (0% compression): Complete exclusion
  - **User Project Content** (0% compression): Full fidelity preservation
  - **Session Data** (30-50% compression): Optimized storage when --uc used
- **Quality Preservation**: Framework compliance with MODE_Token_Efficiency.md patterns

### Session Persistence Benefits (when --uc used)
- **Optimized Storage**: Session data compressed for efficient persistence
- **Faster Restoration**: Reduced memory footprint enables faster session loading
- **Context Preservation**: ≥95% information fidelity maintained across sessions
- **Performance Improvement**: 30-50% reduction in session data storage requirements

## Session Lifecycle Integration

### 1. Session State Management
- Analyze current session state and context requirements
- Call `think_about_collected_information` to analyze session work
- Identify new discoveries, patterns, and insights
- Determine what should be persisted
- Identify critical information for persistence or restoration
- Assess session integrity and continuity needs

### 2. Serena MCP Coordination with Token Efficiency
- Execute appropriate Serena MCP operations for session management
- Call `list_memories` to check existing memories
- Identify which memories need updates with selective compression
- **Content Classification Strategy**:
  - **SuperGemini Framework** (Complete exclusion): All framework directories and components
  - **Session Data** (Apply compression): Session metadata, checkpoints, cache content only
  - **User Project Content** (Preserve fidelity): Project files, user documentation, configurations
- Organize new information by category:
  - **session_context**: Current work and progress (compressed)
  - **code_patterns**: Discovered patterns and conventions (compressed)
  - **project_insights**: New understanding about the project (compressed)
  - **technical_decisions**: Architecture and design choices (compressed)
- Handle memory organization, checkpoint creation, or state restoration with selective compression
- Manage cross-session context preservation and enhancement with optimized storage

### 3. Performance Validation
- Monitor operation performance against strict session targets
- Record operation timings in session metadata
- Compare against PRD performance targets (Enhanced with Token Efficiency):
  - Memory operations: <150ms (improved from <200ms with compression)
  - Session save: <1.5s total (improved from <2s with selective compression)
  - Tool selection: <100ms
  - Compression overhead: <50ms additional processing time
- Generate performance alerts if thresholds exceeded
- Update performance_metrics memory with trending data
- Validate memory efficiency and response time requirements
- Ensure session operations meet <200ms core operation targets

### 4. Context Continuity
- Maintain session context across operations and interruptions
- Based on --type parameter:
  - **session**: Save current session work and progress using `write_memory` with key "session/{timestamp}"
  - **learnings**: Save new discoveries and insights, update existing knowledge memories
  - **context**: Save enhanced project understanding, update project_purpose, tech_stack, etc.
  - **all**: Comprehensive save of all categories
- Preserve decision history, task progress, and accumulated insights
- Enable seamless continuation of complex multi-session workflows

### 5. Quality Assurance
- Validate session data integrity and completeness
- Check if any automatic triggers are met:
  - Time elapsed ≥30 minutes since last checkpoint
  - High priority task completed (via TodoRead check)
  - High risk operation pending or completed
  - Error recovery performed
- Create checkpoint if triggered or --checkpoint flag provided
- Include comprehensive restoration data with current task states, open questions, context needed for resumption, and performance metrics snapshot
- Verify cross-session compatibility and version consistency
- Generate session analytics and performance reports

## Mandatory Serena MCP Integration

### Core Serena Operations
- **Memory Management**: `read_memory`, `write_memory`, `list_memories`
- **Analysis System**: `think_about_collected_information`, `summarize_changes`
- **Session Persistence**: Comprehensive session state and context preservation
- **State Management**: Session state persistence and restoration capabilities

### Session Data Organization
- **Memory Hierarchy**: Structured memory organization for efficient retrieval
- **Progressive Checkpoints**: Building understanding and state across checkpoints
- **Performance Metrics**: Session operation timing and efficiency tracking
- **Context Accumulation**: Building understanding across session boundaries

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

## Memory Keys Used

### Session Memories
- `session/{timestamp}` - Individual session records with comprehensive metadata
- `session/current` - Latest session state pointer
- `session_metadata/{date}` - Daily session aggregations

### Knowledge Memories  
- `code_patterns` - Coding patterns and conventions discovered
- `project_insights` - Accumulated project understanding
- `technical_decisions` - Architecture and design decisions
- `performance_metrics` - Operation timing and efficiency data

### Checkpoint Memories
- `checkpoints/{timestamp}` - Full session checkpoints with restoration data
- `checkpoints/latest` - Most recent checkpoint pointer
- `checkpoints/task-{task-id}-{timestamp}` - Task-specific checkpoints
- `checkpoints/risk-{operation}-{timestamp}` - Risk-based checkpoints

### Summary Memories
- `summaries/{date}` - Daily work summaries with session links
- `summaries/weekly/{week}` - Weekly aggregations with insights
- `summaries/insights/{topic}` - Topical learning summaries

## Session Metadata Structure

### Core Session Metadata
```yaml
# Memory key: session_metadata_{YYYY_MM_DD}
session:
  id: "session-{YYYY-MM-DD-HHMMSS}"
  project: "{project_name}"
  start_time: "{ISO8601_timestamp}"
  end_time: "{ISO8601_timestamp}"
  duration_minutes: {number}
  state: "initializing|active|checkpointed|completed"
  
context:
  memories_loaded: [list_of_memory_keys]
  initial_context_size: {tokens}
  final_context_size: {tokens}
  
work:
  tasks_completed:
    - id: "{task_id}"
      description: "{task_description}"
      duration_minutes: {number}
      priority: "high|medium|low"
  
  files_modified:
    - path: "{absolute_path}"
      operations: [edit|create|delete]
      changes: {number}
      
  decisions_made:
    - timestamp: "{ISO8601_timestamp}"
      decision: "{decision_description}"
      rationale: "{reasoning}"
      impact: "architectural|functional|performance|security"
      
discoveries:
  patterns_found: [list_of_patterns]
  insights_gained: [list_of_insights]
  performance_improvements: [list_of_optimizations]
  
checkpoints:
  automatic:
    - timestamp: "{ISO8601_timestamp}"
      type: "task_complete|time_based|risk_based|error_recovery"
      trigger: "{trigger_description}"
      
performance:
  operations:
    - name: "{operation_name}"
      duration_ms: {number}
      target_ms: {number}
      status: "pass|warning|fail"
```

### Checkpoint Metadata Structure  
```yaml
# Memory key: checkpoints/{timestamp}
checkpoint:
  id: "checkpoint-{YYYY-MM-DD-HHMMSS}"
  session_id: "{session_id}"
  type: "manual|automatic|risk|recovery"
  trigger: "{trigger_description}"
  
state:
  active_tasks:
    - id: "{task_id}"
      status: "pending|in_progress|blocked"
      progress: "{percentage}"
  open_questions: [list_of_questions]
  blockers: [list_of_blockers]
  
context_snapshot:
  size_bytes: {number}
  key_memories: [list_of_memory_keys]
  recent_changes: [list_of_changes]
  
recovery_info:
  restore_command: "/sg:load --checkpoint {checkpoint_id}"
  dependencies_check: "all_clear|issues_found"
  estimated_restore_time_ms: {number}
```

## Automatic Checkpoint Triggers

### 1. Task-Based Triggers
- **Condition**: Major task marked complete via TodoWrite
- **Implementation**: Monitor TodoWrite status changes for priority="high"
- **Memory Key**: `checkpoints/task-{task-id}-{timestamp}`

### 2. Time-Based Triggers  
- **Condition**: Every 30 minutes of active work
- **Implementation**: Check elapsed time since last checkpoint
- **Memory Key**: `checkpoints/auto-{timestamp}`

### 3. Risk-Based Triggers
- **Condition**: Before high-risk operations
- **Examples**: Major refactoring (>50 files), deletion operations, architecture changes
- **Memory Key**: `checkpoints/risk-{operation}-{timestamp}`

### 4. Error Recovery Triggers
- **Condition**: After recovering from errors or failures
- **Purpose**: Preserve error context and recovery steps
- **Memory Key**: `checkpoints/recovery-{timestamp}`

## Performance Requirements

### Critical Performance Targets
- **Session Initialization**: <500ms for complete session setup
- **Core Operations**: <200ms for memory reads, writes, and basic operations
- **Checkpoint Creation**: <1s for comprehensive checkpoint with metadata
- **Memory Operations**: <200ms per individual memory operation
- **Session Save**: <2s for typical session
- **Summary Generation**: <500ms

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
- **Serena Unavailable**: Queue saves locally for later sync
- **Memory Conflicts**: Merge intelligently or prompt user

### Recovery Strategies
- **Graceful Degradation**: Maintaining core functionality under adverse conditions
- **Automatic Recovery**: Intelligent recovery from common failure scenarios
- **Manual Recovery**: Clear escalation paths for complex recovery situations
- **State Reconstruction**: Rebuilding session state from available information
- **Local Queueing**: Local save queueing when Serena unavailable

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

### Integration with /sg:load

#### Session Lifecycle
1. `/sg:load` - Activate project and load context
2. Work on project (make changes, discover patterns)
3. `/sg:save` - Persist discoveries and progress
4. Next session: `/sg:load` retrieves enhanced context

#### Continuous Learning
- Each session builds on previous knowledge
- Patterns and insights accumulate over time
- Project understanding deepens with each cycle

## Examples

### Basic Session Save
```
/sg:save
# Saves current session context and discoveries
```

### Session Checkpoint
```
/sg:save --type checkpoint --metadata
# Create comprehensive checkpoint with metadata
```

### Session Recovery
```
/sg:save --checkpoint --validate
# Create checkpoint with validation
```

### Performance Monitoring
```
/sg:save --performance --validate
# Session operation with performance monitoring
```

### Save with Summary
```
/sg:save --summarize
# Saves session and generates summary
```

### Create Checkpoint
```
/sg:save --checkpoint --type all
# Creates comprehensive checkpoint for session recovery
```

### Save Only Learnings
```
/sg:save --type learnings
# Updates only discovered patterns and insights
```

## Boundaries

**This session command will:**
- Provide robust session lifecycle management with strict performance requirements
- Integrate seamlessly with Serena MCP for comprehensive session capabilities
- Maintain context continuity and cross-session persistence effectively
- Support complex multi-session workflows with intelligent state management
- Deliver session operations within strict performance targets consistently
- Enable comprehensive session context persistence and checkpoint creation

**This session command will not:**
- Operate without proper Serena MCP integration and connectivity
- Compromise performance targets for additional functionality
- Proceed without proper session state validation and integrity checks
- Function without adequate error handling and recovery mechanisms
- Skip automatic checkpoint evaluation and creation when triggered
- Ignore session metadata structure and performance monitoring requirements