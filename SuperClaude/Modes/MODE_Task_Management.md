---
name: task-management
description: "Multi-layer task orchestration with wave systems, delegation patterns, and comprehensive analytics"
type: system-architecture
category: orchestration
complexity: advanced
scope: framework
activation:
  automatic: true
  manual-flags: ["--delegate", "--wave-mode", "--loop", "--concurrency", "--wave-strategy", "--wave-delegation", "--iterations", "--interactive"]
  confidence-threshold: 0.8
  detection-patterns: ["multi-step operations", "build/implement/create keywords", "system/feature/comprehensive scope"]
framework-integration:
  mcp-servers: [task-coordination, wave-orchestration]
  commands: ["/task", "/spawn", "/loop", "TodoWrite"]
  modes: [all modes for orchestration]
  quality-gates: [task_management_validation, session_completion_verification, real_time_metrics]
performance-profile: intensive
performance-targets:
  delegation-efficiency: "40-70% time savings"
  wave-coordination: "30-50% better results"
  resource-utilization: ">0.7 optimization"
---

# Task Management Mode

## Core Principles
- **Evidence-Based Progress**: Measurable outcomes with quantified task completion metrics
- **Single Focus Protocol**: One active task at a time with strict state management
- **Real-Time Updates**: Immediate status changes with comprehensive tracking
- **Quality Gates**: Validation before completion with multi-step verification cycles

## Architecture Layers

### Layer 1: TodoRead/TodoWrite (Session Tasks)
- **Scope**: Current Gemini CLI session with real-time state management
- **States**: pending, in_progress, completed, blocked with strict transitions
- **Capacity**: 3-20 tasks per session with dynamic load balancing
- **Integration**: Foundation layer connecting to project and orchestration systems

### Layer 2: /task Command (Project Management)
- **Scope**: Multi-session features spanning days to weeks with persistence
- **Structure**: Hierarchical organization (Epic → Story → Task) with dependency mapping
- **Persistence**: Cross-session state management with comprehensive tracking
- **Coordination**: Inter-layer communication with session lifecycle integration

### Layer 3: /spawn Command (Meta-Orchestration)
- **Scope**: Complex multi-domain operations with system-wide coordination
- **Features**: Parallel/sequential coordination with intelligent tool management
- **Management**: Resource allocation and dependency resolution across domains
- **Intelligence**: Advanced decision-making with compound intelligence coordination

### Layer 4: /loop Command (Iterative Enhancement)
- **Scope**: Progressive refinement workflows with validation cycles
- **Features**: Iteration cycles with comprehensive validation and quality gates
- **Optimization**: Performance improvements through iterative analysis
- **Analytics**: Measurement and feedback loops with continuous learning

## Task Detection and Creation

### Automatic Triggers
- **Multi-step Operations**: 3+ step sequences with dependency analysis
- **Keywords**: build, implement, create, fix, optimize, refactor with context awareness
- **Scope Indicators**: system, feature, comprehensive, complete with complexity assessment
- **Complexity Thresholds**: Operations exceeding 0.4 complexity score with multi-domain impact
- **File Count Triggers**: 3+ files for delegation, 2+ directories for coordination
- **Performance Opportunities**: Auto-detect parallelizable operations with time estimates

### Task State Management
- **pending** 📋: Ready for execution with dependency validation
- **in_progress** 🔄: Currently active (ONE per session) with progress tracking
- **blocked** 🚧: Waiting on dependency with automated resolution monitoring
- **completed** ✅: Successfully finished with quality validation and evidence

## Related Flags

### Sub-Agent Delegation Flags
**`--delegate [files|folders|auto]`**
- Enable Task tool sub-agent delegation for parallel processing optimization
- **files**: Delegate individual file analysis to sub-agents with granular control
- **folders**: Delegate directory-level analysis to sub-agents with hierarchical organization
- **auto**: Auto-detect delegation strategy based on scope and complexity analysis
- Auto-activates: >2 directories or >3 files with complexity assessment
- 40-70% time savings for suitable operations with proven efficiency metrics

**`--concurrency [n]`**
- Control max concurrent sub-agents and tasks (default: 7, range: 1-15)
- Dynamic allocation based on resources and complexity with intelligent load balancing
- Prevents resource exhaustion in complex scenarios with proactive monitoring

### Wave Orchestration Flags
**`--wave-mode [auto|force|off]`**
- Control wave orchestration activation with intelligent threshold detection
- **auto**: Auto-activates based on complexity >0.4 AND file_count >3 AND operation_types >2
- **force**: Override auto-detection and force wave mode for borderline cases
- **off**: Disable wave mode, use Sub-Agent delegation instead with fallback coordination
- 30-50% better results through compound intelligence and progressive enhancement

**`--wave-strategy [progressive|systematic|adaptive|enterprise]`**
- Select wave orchestration strategy with context-aware optimization
- **progressive**: Iterative enhancement for incremental improvements with validation cycles
- **systematic**: Comprehensive methodical analysis for complex problems with full coverage
- **adaptive**: Dynamic configuration based on varying complexity with real-time adjustment
- **enterprise**: Large-scale orchestration for >100 files with >0.7 complexity threshold

**`--wave-delegation [files|folders|tasks]`**
- Control how Wave system delegates work to Sub-Agent with strategic coordination
- **files**: Sub-Agent delegates individual file analysis across waves with precision targeting
- **folders**: Sub-Agent delegates directory-level analysis across waves with structural organization
- **tasks**: Sub-Agent delegates by task type (security, performance, quality, architecture) with domain specialization

### Iterative Enhancement Flags
**`--loop`**
- Enable iterative improvement mode for commands with automatic validation
- Auto-activates: Quality improvement requests, refinement operations, polish tasks with pattern detection
- Compatible operations: /improve, /refine, /enhance, /fix, /cleanup, /analyze with full integration
- Default: 3 iterations with automatic validation and quality gate enforcement

**`--iterations [n]`**
- Control number of improvement cycles (default: 3, range: 1-10)
- Overrides intelligent default based on operation complexity with adaptive optimization

**`--interactive`**
- Enable user confirmation between iterations with comprehensive review cycles
- Pauses for review and approval before each cycle with detailed progress reporting
- Allows manual guidance and course correction with decision point integration

## Auto-Activation Thresholds
- **Sub-Agent Delegation**: >2 directories OR >3 files OR complexity >0.4 with multi-condition evaluation
- **Wave Mode**: complexity ≥0.4 AND files >3 AND operation_types >2 with sophisticated logic
- **Loop Mode**: polish, refine, enhance, improve keywords detected with contextual analysis

## Document Persistence

**Comprehensive task management documentation system** with automated session completion summaries and orchestration analytics.

### Directory Structure
```
ClaudeDocs/Task/Management/
├── Orchestration/           # Wave orchestration reports
├── Delegation/             # Sub-agent delegation analytics
├── Performance/            # Task execution metrics
├── Coordination/           # Multi-layer coordination results
└── Archives/              # Historical task management data
```

### Summary Documents
```
ClaudeDocs/Summary/
├── session-completion-{session-id}-{YYYY-MM-DD-HHMMSS}.md
├── task-orchestration-{project}-{YYYY-MM-DD-HHMMSS}.md
├── delegation-summary-{project}-{YYYY-MM-DD-HHMMSS}.md
└── performance-summary-{session-id}-{YYYY-MM-DD-HHMMSS}.md
```

### File Naming Convention
```
{task-operation}-management-{YYYY-MM-DD-HHMMSS}.md

Examples:
- orchestration-management-2024-12-15-143022.md
- delegation-management-2024-12-15-143045.md
- wave-coordination-management-2024-12-15-143108.md
- performance-analytics-management-2024-12-15-143131.md
```

### Session Completion Summaries
```
session-completion-{session-id}-{YYYY-MM-DD-HHMMSS}.md
task-orchestration-{project}-{YYYY-MM-DD-HHMMSS}.md
delegation-summary-{project}-{YYYY-MM-DD-HHMMSS}.md
performance-summary-{session-id}-{YYYY-MM-DD-HHMMSS}.md
```

### Metadata Format
```yaml
---
operation_type: [orchestration|delegation|coordination|performance]
timestamp: 2024-12-15T14:30:22Z
session_id: session_abc123
task_complexity: 0.85
orchestration_metrics:
  wave_strategy: progressive
  wave_count: 3
  delegation_efficiency: 0.78
  coordination_success: 0.92
delegation_analytics:
  sub_agents_deployed: 5
  parallel_efficiency: 0.65
  resource_utilization: 0.72
  completion_rate: 0.88
performance_analytics:
  execution_time_reduction: 0.45
  quality_preservation: 0.96
  resource_optimization: 0.71
  throughput_improvement: 0.38
---
```

### Persistence Workflow

#### Session Completion Summary Generation
1. **Session End Detection**: Automatically detect session completion or termination
2. **Performance Analysis**: Calculate task completion rates, efficiency metrics, orchestration success
3. **Summary Generation**: Create comprehensive session summary with key achievements and metrics
4. **Cross-Reference**: Link to related project documents and task hierarchies
5. **Knowledge Extraction**: Document patterns and lessons learned for future sessions

#### Task Orchestration Summary
1. **Orchestration Tracking**: Monitor wave execution, delegation patterns, coordination effectiveness
2. **Performance Metrics**: Track efficiency gains, resource utilization, quality preservation scores
3. **Pattern Analysis**: Identify successful orchestration strategies and optimization opportunities
4. **Summary Documentation**: Generate orchestration summary in ClaudeDocs/Summary/
5. **Best Practices**: Document effective orchestration patterns for reuse

### Integration Points

#### Quality Gates Integration
- **Step 2.5**: Task management validation during orchestration operations
- **Step 7.5**: Session completion verification and summary documentation
- **Continuous**: Real-time metrics collection and performance monitoring
- **Post-Session**: Comprehensive session analytics and completion reporting

## Integration Points

### SuperGemini Framework Integration
- **Session Lifecycle**: Deep integration with session management and checkpoint systems
- **Quality Gates**: Embedded validation throughout the 8-step quality cycle
- **MCP Coordination**: Seamless integration with all MCP servers for orchestration
- **Mode Coordination**: Cross-mode orchestration with specialized capabilities

### Cross-System Coordination
- **TodoWrite Integration**: Task completion triggers checkpoint evaluation and state transitions
- **Command Orchestration**: Multi-command coordination with /task, /spawn, /loop integration
- **Agent Delegation**: Sophisticated sub-agent coordination with performance optimization
- **Wave Systems**: Advanced wave orchestration with compound intelligence coordination

### Quality Gates Integration
- **Step 2.5**: Task management validation during orchestration operations with real-time verification
- **Step 7.5**: Session completion verification and summary documentation with comprehensive analytics
- **Continuous**: Real-time metrics collection and performance monitoring with adaptive optimization
- **Specialized**: Task-specific validation with domain expertise and quality preservation

## Configuration

```yaml
task_management:
  activation:
    automatic: true
    complexity_threshold: 0.4
    detection_patterns:
      multi_step_operations: ["3+ steps", "build", "implement"]
      keywords: [build, implement, create, fix, optimize, refactor]
      scope_indicators: [system, feature, comprehensive, complete]
  
  delegation_coordination:
    default_strategy: auto
    concurrency_options: [files, folders, auto]
    intelligent_detection: scope_and_complexity_analysis
    performance_optimization: parallel_processing_with_load_balancing
  
  wave_orchestration:
    auto_activation: true
    threshold_complexity: 0.4
    file_count_minimum: 3
    operation_types_minimum: 2
  
  iteration_enhancement:
    default_cycles: 3
    validation_approach: automatic_quality_gates
    interactive_mode: user_confirmation_cycles
    compatible_commands: [improve, refine, enhance, fix, cleanup, analyze]
  
  performance_analytics:
    delegation_efficiency_target: 0.65
    wave_coordination_target: 0.40
    resource_utilization_target: 0.70
    quality_preservation_minimum: 0.95
  
  persistence_config:
    enabled: true
    directory: "ClaudeDocs/Task/Management/"
    auto_save: true
    report_types:
      - orchestration_analytics
      - delegation_summaries
      - performance_metrics
      - session_completions
    metadata_format: yaml
    retention_days: 90
```

## Related Documentation

- **Primary Implementation**: TodoWrite integration with session-based task management
- **Secondary Integration**: /task, /spawn, /loop commands for multi-layer orchestration
- **Framework Reference**: SESSION_LIFECYCLE.md for checkpoint and persistence coordination
- **Quality Standards**: ORCHESTRATOR.md for validation checkpoints and quality gate integration

---

*This mode provides comprehensive task orchestration capabilities with multi-layer architecture, advanced delegation systems, wave orchestration, and comprehensive analytics for maximum efficiency and quality preservation.*