# SuperGemini Session Lifecycle Pattern

## Overview

The Session Lifecycle Pattern defines how SuperGemini manages work sessions through integration with Serena MCP, enabling continuous learning and context preservation across sessions.

## Core Concept

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  /sg:load   │────▶│    WORK     │────▶│  /sg:save   │────▶│    NEXT     │
│  (INIT)     │     │  (ACTIVE)   │     │ (CHECKPOINT)│     │  SESSION    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                                                              │
       └──────────────────── Enhanced Context ───────────────────────┘
```

## Session States

### 1. INITIALIZING
- **Trigger**: `/sg:load` command execution
- **Actions**:
  - Activate project via `activate_project`
  - Load existing memories via `list_memories`
  - Check onboarding status
  - Build initial context with framework exclusion
  - Initialize session context and memory structures
- **Content Management**:
  - **Session Data**: Session metadata, checkpoints, cache content
  - **Framework Content**: All SuperGemini framework components loaded
  - **User Content**: Project files, user docs, configurations loaded
- **Duration**: <500ms target
- **Next State**: ACTIVE

### 2. ACTIVE
- **Description**: Working session with full context
- **Characteristics**:
  - Project memories loaded
  - Context available for all operations
  - Changes tracked for persistence
  - Decisions logged for replay
- **Checkpoint Triggers**:
  - Manual: User requests via `/sg:save --checkpoint`
  - Automatic: See Automatic Checkpoint Triggers section
- **Next State**: CHECKPOINTED or COMPLETED

### 3. CHECKPOINTED
- **Trigger**: `/sg:save` command or automatic trigger
- **Actions**:
  - Analyze session changes via `think_about_collected_information`
  - Persist discoveries to appropriate memories
  - Create checkpoint record with session metadata
  - Generate summary if requested
- **Storage Strategy**:
  - **Framework Content**: All framework components stored
  - **Session Metadata**: Session operational data stored
  - **User Work Products**: Full fidelity preservation
- **Memory Keys Created**:
  - `session/{timestamp}` - Session record with metadata
  - `checkpoints/{timestamp}` - Checkpoint with session data
  - `summaries/{date}` - Daily summary (optional)
- **Next State**: ACTIVE (continue) or COMPLETED

### 4. RESUMED
- **Trigger**: `/sg:load` after previous checkpoint
- **Actions**:
  - Load latest checkpoint via `read_memory`
  - Restore session context and data
  - Display resumption summary
  - Continue from last state
- **Restoration Strategy**:
  - **Framework Content**: Load framework content directly
  - **Session Context**: Restore session operational data
  - **User Context**: Load preserved user content
- **Special Features**:
  - Shows work completed in previous session
  - Highlights open tasks/questions
  - Restores decision context with full fidelity
- **Next State**: ACTIVE

### 5. COMPLETED
- **Trigger**: Session end or explicit completion
- **Actions**:
  - Final checkpoint creation
  - Session summary generation
  - Memory consolidation
  - Cleanup operations
- **Final Outputs**:
  - Session summary in memories
  - Updated project insights
  - Enhanced context for next session

## Checkpoint Mechanisms

### Manual Checkpoints
```bash
/sg:save --checkpoint                  # Basic checkpoint
/sg:save --checkpoint --summarize      # With summary
/sg:save --checkpoint --type all       # Comprehensive
```

### Automatic Checkpoint Triggers

#### 1. Task-Based Triggers
- **Condition**: Major task marked complete
- **Implementation**: Hook into TodoWrite status changes
- **Frequency**: On task completion with priority="high"
- **Memory Key**: `checkpoints/task-{task-id}-{timestamp}`

#### 2. Time-Based Triggers
- **Condition**: Every 30 minutes of active work
- **Implementation**: Session timer with activity detection
- **Frequency**: 30-minute intervals
- **Memory Key**: `checkpoints/auto-{timestamp}`

#### 3. Risk-Based Triggers
- **Condition**: Before high-risk operations
- **Examples**:
  - Major refactoring (>50 files)
  - Deletion operations
  - Architecture changes
  - Security-sensitive modifications
- **Memory Key**: `checkpoints/risk-{operation}-{timestamp}`

#### 4. Error Recovery Triggers
- **Condition**: After recovering from errors
- **Purpose**: Preserve error context and recovery steps
- **Memory Key**: `checkpoints/recovery-{timestamp}`

## Session Metadata Structure

### Core Metadata
```yaml
# Stored in: session/{timestamp}
session:
  id: "session-2025-01-31-14:30:00"
  project: "SuperGemini"
  start_time: "2025-01-31T14:30:00Z"
  end_time: "2025-01-31T16:45:00Z"
  duration_minutes: 135
  
context:
  memories_loaded:
    - project_purpose
    - tech_stack
    - code_style_conventions
  initial_context_size: 15420
  final_context_size: 23867
  context_stats:
    session_data_size: 3450      # Session metadata size
    framework_content_size: 12340 # Framework content size
    user_content_size: 16977      # User content size
    total_context_bytes: 32767
    retention_ratio: 0.92
  
work:
  tasks_completed:
    - id: "TASK-006"
      description: "Refactor /sg:load command"
      duration_minutes: 45
    - id: "TASK-007"
      description: "Implement /sg:save command"
      duration_minutes: 60
      
  files_modified:
    - path: "/SuperGemini/Commands/load.md"
      operations: ["edit"]
      changes: 6
    - path: "/SuperGemini/Commands/save.md"
      operations: ["create"]
      
  decisions_made:
    - timestamp: "2025-01-31T15:00:00Z"
      decision: "Use Serena MCP tools directly in commands"
      rationale: "Commands are orchestration instructions"
      impact: "architectural"
      
discoveries:
  patterns_found:
    - "MCP tool naming convention: direct tool names"
    - "Commands use declarative markdown format"
  insights_gained:
    - "SuperGemini as orchestration layer"
    - "Session persistence enables continuous learning"
    
checkpoints:
  - timestamp: "2025-01-31T15:30:00Z"
    type: "automatic"
    trigger: "30-minute-interval"
  - timestamp: "2025-01-31T16:00:00Z"
    type: "manual"
    trigger: "user-requested"
```

### Checkpoint Metadata
```yaml
# Stored in: checkpoints/{timestamp}
checkpoint:
  id: "checkpoint-2025-01-31-16:00:00"
  session_id: "session-2025-01-31-14:30:00"
  type: "manual|automatic|risk|recovery"
  
state:
  active_tasks:
    - id: "TASK-008"
      status: "in_progress"
      progress: "50%"
  open_questions:
    - "Should automatic checkpoints include full context?"
    - "How to handle checkpoint size limits?"
  blockers: []
  
context_snapshot:
  size_bytes: 45678
  key_memories:
    - "project_purpose"
    - "session/current"
  recent_changes:
    - "Updated /sg:load command"
    - "Created /sg:save command"
    
recovery_info:
  restore_command: "/sg:load --checkpoint checkpoint-2025-01-31-16:00:00"
  dependencies_check: "all_clear"
  estimated_restore_time_ms: 450
```

## Memory Organization

### Session Memories Hierarchy
```
memories/
├── session/
│   ├── current                    # Always points to latest session
│   ├── {timestamp}                # Individual session records
│   └── history/                   # Archived sessions (>30 days)
├── checkpoints/
│   ├── latest                     # Always points to latest checkpoint
│   ├── {timestamp}                # Individual checkpoints
│   └── task-{id}-{timestamp}      # Task-specific checkpoints
├── summaries/
│   ├── daily/{date}               # Daily work summaries
│   ├── weekly/{week}              # Weekly aggregations
│   └── insights/{topic}           # Topical insights
└── project_state/
    ├── context_enhanced           # Accumulated context
    ├── patterns_discovered        # Code patterns found
    └── decisions_log              # Architecture decisions
```

## Integration Points

### With Python Hooks (Future)
```python
# Planned hook integration points
class SessionLifecycleHooks:
    def on_session_start(self, context):
        """Called after /sg:load completes"""
        pass
        
    def on_task_complete(self, task_id, result):
        """Trigger automatic checkpoint"""
        pass
        
    def on_error_recovery(self, error, recovery_action):
        """Checkpoint after error recovery"""
        pass
        
    def on_session_end(self, summary):
        """Called during /sg:save"""
        pass
```

### With TodoWrite Integration
- Task completion triggers checkpoint evaluation
- High-priority task completion forces checkpoint
- Task state included in session metadata

### With MCP Servers
- **Serena**: Primary storage and retrieval
- **Sequential**: Session analysis and summarization
- **Morphllm**: Pattern detection in session changes

## Performance Targets

### Operation Timings
- Session initialization: <500ms
- Checkpoint creation: <1s
- Checkpoint restoration: <500ms
- Summary generation: <2s
- Memory write operations: <200ms each

### Storage Efficiency
- Session metadata: <10KB per session typical
- Checkpoint size: <50KB typical, <200KB maximum
- Summary size: <5KB per day typical
- Automatic pruning: Sessions >90 days
- **Storage Benefits**:
  - Efficient session data management
  - Fast checkpoint restoration (<500ms)
  - Optimized memory operation performance

## Error Handling

### Checkpoint Failures
- **Strategy**: Queue locally, retry on next operation
- **Fallback**: Write to local `.superclaude/recovery/` directory
- **User Notification**: Warning with manual recovery option

### Session Recovery
- **Corrupted Checkpoint**: Fall back to previous checkpoint
- **Missing Dependencies**: Load partial context with warnings
- **Serena Unavailable**: Use cached local state

### Conflict Resolution
- **Concurrent Sessions**: Last-write-wins with merge option
- **Divergent Contexts**: Present diff to user for resolution
- **Version Mismatch**: Compatibility layer for migration

## Best Practices

### For Users
1. Run `/sg:save` before major changes
2. Use `--checkpoint` flag for critical work
3. Review summaries weekly for insights
4. Clean old checkpoints periodically

### For Development
1. Include decision rationale in metadata
2. Tag checkpoints with meaningful types
3. Maintain checkpoint size limits
4. Test recovery scenarios regularly

## Future Enhancements

### Planned Features
1. **Collaborative Sessions**: Multi-user checkpoint sharing
2. **Branching Checkpoints**: Exploratory work paths
3. **Intelligent Triggers**: ML-based checkpoint timing
4. **Session Analytics**: Work pattern insights
5. **Cross-Project Learning**: Shared pattern detection

### Hook System Integration
- Automatic checkpoint on hook execution
- Session state in hook context
- Hook failure recovery checkpoints
- Performance monitoring via hooks