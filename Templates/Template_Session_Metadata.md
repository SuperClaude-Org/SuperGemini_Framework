# Session Metadata Template

This template defines the standard structure for session metadata used by the SuperGemini session lifecycle pattern with Serena MCP integration.

## Core Session Metadata Template

### Memory Key Format
```
session_metadata_{YYYY_MM_DD}_{session_id}
```

### YAML Structure
```yaml
# Session Metadata - SuperGemini Session Lifecycle
# Memory Key: session_metadata_{YYYY_MM_DD}_{session_id}
# Created: {ISO8601_timestamp}
# Version: 1.0

metadata:
  format_version: "1.0"
  created_by: "SuperGemini Session Lifecycle"
  template_source: "Template_Session_Metadata.md"
  
session:
  id: "session-{YYYY-MM-DD-HHMMSS}"
  project: "{project_name}"
  start_time: "{ISO8601_timestamp}"  # UTC format
  end_time: "{ISO8601_timestamp}"    # UTC format
  duration_minutes: {number}
  state: "{initializing|active|checkpointed|completed}"
  user_timezone: "{timezone}"
  claude_model: "{model_version}"
  
context:
  memories_loaded: 
    - "{memory_key_1}"
    - "{memory_key_2}"
  initial_context_size: {tokens}
  final_context_size: {tokens}
  context_growth: {percentage}
  onboarding_performed: {true|false}
  
work:
  tasks_completed:
    - id: "{task_id}"
      description: "{task_description}"
      start_time: "{ISO8601_timestamp}"
      end_time: "{ISO8601_timestamp}"
      duration_minutes: {number}
      priority: "{high|medium|low}"
      status: "{completed|failed|blocked}"
      
  files_modified:
    - path: "{absolute_path}"
      operations: ["{edit|create|delete}"]
      changes: {number}
      size_before: {bytes}
      size_after: {bytes}
      
  commands_executed:
    - command: "{command_name}"
      timestamp: "{ISO8601_timestamp}"
      duration_ms: {number}
      success: {true|false}
      
  decisions_made:
    - timestamp: "{ISO8601_timestamp}"
      decision: "{decision_description}"
      rationale: "{reasoning}"
      impact: "{architectural|functional|performance|security}"
      confidence: {0.0-1.0}
      
discoveries:
  patterns_found:
    - pattern: "{pattern_description}"
      confidence: {0.0-1.0}
      examples: ["{example_1}", "{example_2}"]
      
  insights_gained:
    - insight: "{insight_description}"
      category: "{architectural|technical|process|quality}"
      actionable: {true|false}
      
  performance_improvements:
    - improvement: "{improvement_description}"
      metric: "{metric_name}"
      before: {value}
      after: {value}
      improvement_percentage: {percentage}
      
  issues_identified:
    - issue: "{issue_description}"
      severity: "{critical|high|medium|low}"
      category: "{bug|performance|security|quality}"
      resolution_status: "{resolved|pending|deferred}"
      
checkpoints:
  automatic:
    - timestamp: "{ISO8601_timestamp}"
      type: "{task_complete|time_based|risk_based|error_recovery}"
      trigger: "{trigger_description}"
      checkpoint_id: "checkpoint-{YYYY-MM-DD-HHMMSS}"
      
  manual:
    - timestamp: "{ISO8601_timestamp}"
      user_requested: {true|false}
      checkpoint_id: "checkpoint-{YYYY-MM-DD-HHMMSS}"
      notes: "{user_notes}"
      
performance:
  operations:
    - name: "{operation_name}"
      duration_ms: {number}
      target_ms: {number}
      status: "{pass|warning|fail}"
      overhead_percentage: {percentage}
      
  session_metrics:
    - metric: "session_initialization"
      value: {milliseconds}
      target: 500
      
    - metric: "memory_operations_avg"
      value: {milliseconds}
      target: 200
      
    - metric: "tool_selection_avg"  
      value: {milliseconds}
      target: 100
      
    - metric: "context_loading"
      value: {milliseconds}
      target: 500
      
  alerts:
    - timestamp: "{ISO8601_timestamp}"
      metric: "{metric_name}"
      threshold_exceeded: {value}
      threshold_limit: {value}
      severity: "{warning|critical}"
      
integration:
  mcp_servers_used:
    - server: "serena"
      operations: {number}
      average_response_ms: {number}
      success_rate: {percentage}
      
    - server: "morphllm"
      operations: {number}
      average_response_ms: {number}
      success_rate: {percentage}
      
  hooks_triggered:
    - hook: "{hook_name}"
      timestamp: "{ISO8601_timestamp}"
      duration_ms: {number}
      success: {true|false}
      
  quality_gates_passed:
    - gate: "{gate_name}"
      timestamp: "{ISO8601_timestamp}"
      result: "{pass|fail|warning}"
      score: {0.0-1.0}
      
learning:
  patterns_evolved:
    - pattern: "{pattern_name}"
      evolution: "{improvement_description}"
      confidence_change: {percentage}
      
  knowledge_accumulated:
    - domain: "{domain_name}"
      new_concepts: {number}
      connections_made: {number}
      
  effectiveness_metrics:
    - metric: "problem_solving_efficiency"
      value: {0.0-1.0}
      trend: "{improving|stable|declining}"
      
    - metric: "context_retention"
      value: {percentage}
      target: 90
      
cross_references:
  related_sessions:
    - session_id: "{related_session_id}"
      relationship: "{continuation|related_project|similar_pattern}"
      
  memory_updates:
    - memory_key: "{memory_key}"
      update_type: "{created|updated|enhanced}"
      
  documentation_created:
    - document: "{document_path}"
      type: "{prd|brief|report|analysis}"
      
validation:
  data_integrity: {true|false}
  required_fields_present: {true|false}
  timestamp_consistency: {true|false}
  performance_targets_met: {percentage}
  
  completion_criteria:
    - criterion: "all_tasks_resolved"
      met: {true|false}
      
    - criterion: "context_preserved"
      met: {true|false}
      
    - criterion: "performance_acceptable"
      met: {true|false}
```

## Usage Instructions

### 1. Session Initialization
- Copy template structure
- Replace all `{placeholder}` values with actual data
- Use UTC timestamps in ISO8601 format
- Set initial state to "initializing"

### 2. During Session
- Update work.tasks_completed as tasks finish
- Add files_modified entries for each file operation
- Record decisions_made with full context
- Track performance.operations for timing

### 3. Session Completion
- Set end_time and final state
- Calculate duration_minutes
- Ensure all performance metrics recorded
- Validate completion criteria

### 4. Memory Storage
Use Serena MCP `write_memory` tool:
```
write_memory
{
  "memory_name": "session_metadata_2025_01_31_143022",
  "content": "{YAML_content_above}"
}
```

## Integration Points

### With /sg:load Command
- Initialize session metadata on project activation
- Load checkpoint metadata for session restoration
- Track context loading performance

### With /sg:save Command  
- Update session metadata throughout work
- Create checkpoint metadata when triggered
- Record final session state and metrics

### With Hooks System
- Track hook execution in integration.hooks_triggered
- Record quality gate results
- Monitor performance impact of hooks

## Validation Rules

1. **Required Fields**: session.id, session.project, session.start_time must be present
2. **Timestamp Format**: All timestamps must be ISO8601 UTC format
3. **Performance Targets**: All operations must record duration and compare to targets
4. **State Consistency**: Session state must follow lifecycle pattern
5. **Cross-References**: All memory_updates must reference valid memory keys

## Template Versioning

- **Version 1.0**: Initial template supporting basic session lifecycle
- **Future Versions**: Will extend with additional metrics and integration points
- **Backward Compatibility**: New versions will maintain core structure compatibility