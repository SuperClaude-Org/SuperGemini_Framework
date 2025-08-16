# SuperClaude Session Management Guide

## Introduction

SuperClaude's session management system transforms Claude Code into a persistent, context-aware development partner. Unlike traditional AI interactions that reset with each conversation, SuperClaude maintains project memory, learning patterns, and development context across multiple sessions. See [Examples Cookbook](examples-cookbook.md) for practical session workflows.

### What Session Management Provides

**Persistent Context**: Your project understanding, architectural decisions, and development patterns survive session boundaries and accumulate over time.

**Cross-Session Learning**: SuperClaude builds comprehensive project knowledge, remembering code patterns, design decisions, and implementation approaches.

**Intelligent Checkpoints**: Automatic state preservation ensures you never lose progress on complex development tasks.

**Memory-Driven Workflows**: Task hierarchies, discovered patterns, and project insights are preserved and enhanced across sessions.

**Seamless Resumption**: Pick up exactly where you left off with full context restoration and intelligent state analysis.

## Core Concepts

### Session States

SuperClaude sessions exist in distinct states that determine available capabilities and behavior:

**Uninitialized Session**
- No project context loaded
- Limited to basic Claude Code capabilities
- No memory persistence or cross-session learning
- Manual project discovery required for each task

**Active Session**
- Project context loaded via `/sc:load`
- Full SuperClaude capabilities available
- Memory persistence enabled through Serena MCP
- Cross-session learning and pattern recognition active
- Automatic checkpoint creation based on activity

**Checkpointed Session**
- Critical states preserved for recovery
- Task hierarchies and progress maintained
- Discoveries and patterns archived
- Recovery points for complex operations

**Archived Session**
- Completed projects with preserved insights
- Historical context available for future reference
- Pattern libraries built from successful implementations
- Learning artifacts maintained for similar projects

### Context Types

SuperClaude manages multiple context layers:

**Project Context**
- Directory structure and file organization
- Dependency mappings and architectural patterns
- Code style preferences and team conventions
- Build systems and development workflows

**Task Context**
- Current work objectives and completion criteria
- Multi-step operations with dependency tracking
- Quality gates and validation requirements
- Progress checkpoints and recovery states

**Learning Context**
- Discovered patterns and successful approaches
- Architectural decisions and their outcomes
- Problem-solving strategies that worked
- Anti-patterns and approaches to avoid

**Session Metadata**
- Temporal information and session duration
- Tool usage patterns and efficiency metrics
- Quality assessments and reflection insights
- Cross-session relationship tracking

### Memory Organization

SuperClaude organizes persistent memory using a structured hierarchy:

```
plan_[timestamp]: Overall goals and objectives
phase_[1-5]: Major milestone descriptions  
task_[phase].[number]: Specific deliverable status
todo_[task].[number]: Atomic action completion
checkpoint_[timestamp]: State snapshots for recovery
blockers: Active impediments requiring attention
decisions: Key architectural choices made
patterns: Successful approaches discovered
insights: Cross-session learning artifacts
```

## Session Commands

### /sc:load - Project Context Loading

**Purpose**: Initialize session with project context and cross-session memory retrieval

**Syntax**:
```bash
/sc:load [target] [--type project|config|deps|checkpoint] [--refresh] [--analyze]
```

**Behavioral Flow**:
1. **Initialize**: Establish Serena MCP connection for memory management
2. **Discover**: Analyze project structure and identify context requirements
3. **Load**: Retrieve memories, checkpoints, and cross-session persistence data
4. **Activate**: Establish project context and prepare development workflow
5. **Validate**: Ensure loaded context integrity and session readiness

**Examples**:

```bash
# Basic project loading - most common usage
/sc:load
# Loads current directory with memory integration
# Establishes session context for development work

# Specific project with analysis
/sc:load /path/to/project --type project --analyze  
# Loads specific project with comprehensive analysis
# Activates context and retrieves cross-session memories

# Checkpoint restoration
/sc:load --type checkpoint --checkpoint session_123
# Restores specific checkpoint with session context
# Continues previous work with full context preservation

# Dependency context refresh
/sc:load --type deps --refresh
# Updates dependency understanding and mappings
# Refreshes project analysis with current state
```

**Performance**: Target <500ms initialization, <200ms for core operations

### /sc:save - Session Context Persistence

**Purpose**: Preserve session context, discoveries, and progress for cross-session continuity

**Syntax**:
```bash
/sc:save [--type session|learnings|context|all] [--summarize] [--checkpoint]
```

**Behavioral Flow**:
1. **Analyze**: Examine session progress and identify discoveries worth preserving
2. **Persist**: Save context and learnings using Serena MCP memory management
3. **Checkpoint**: Create recovery points for complex sessions
4. **Validate**: Ensure data integrity and cross-session compatibility
5. **Prepare**: Ready context for seamless future session continuation

**Examples**:

```bash
# Basic session save - automatic checkpoint if >30min
/sc:save
# Saves discoveries and context to Serena MCP
# Creates checkpoint for sessions exceeding 30 minutes

# Comprehensive checkpoint with recovery state
/sc:save --type all --checkpoint
# Complete session preservation with recovery capability
# Includes learnings, context, and progress state

# Session summary with discovery documentation
/sc:save --summarize
# Creates session summary with discovery patterns
# Updates cross-session learning and project insights

# Discovery-only persistence
/sc:save --type learnings
# Saves only new patterns and insights
# Updates project understanding without full preservation
```

**Automatic Triggers**:
- Session duration >30 minutes
- Complex task completion
- Major architectural decisions
- Error recovery scenarios
- Quality gate completions

### /sc:reflect - Task Reflection and Validation

**Purpose**: Analyze session progress, validate task adherence, and capture learning insights

**Syntax**:
```bash
/sc:reflect [--type task|session|completion] [--analyze] [--validate]
```

**Behavioral Flow**:
1. **Analyze**: Examine task state and session progress using Serena reflection tools
2. **Validate**: Assess task adherence, completion quality, and requirement fulfillment
3. **Reflect**: Apply deep analysis of collected information and insights
4. **Document**: Update session metadata and capture learning patterns
5. **Optimize**: Provide recommendations for process improvement

**Examples**:

```bash
# Task adherence validation
/sc:reflect --type task --analyze
# Validates current approach against project goals
# Identifies deviations and recommends course corrections

# Session progress analysis  
/sc:reflect --type session --validate
# Comprehensive analysis of session work and information gathering
# Quality assessment and gap identification

# Completion criteria evaluation
/sc:reflect --type completion
# Evaluates task completion against actual progress
# Determines readiness and identifies remaining blockers
```

**Reflection Tools Integration**:
- `think_about_task_adherence`: Goal alignment validation
- `think_about_collected_information`: Session work analysis
- `think_about_whether_you_are_done`: Completion assessment

## Session Lifecycle

### Session Initialization Workflow

**Step 1: Environment Assessment**
```bash
# SuperClaude analyzes current environment
- Directory structure and project type detection
- Existing configuration and dependency analysis  
- Previous session memory availability check
- Development tool and framework identification
```

**Step 2: Context Loading**
```bash
/sc:load
# Triggers comprehensive context establishment:
- Serena MCP connection initialization
- Project memory retrieval from previous sessions
- Code pattern analysis and architectural understanding
- Development workflow preference loading
```

**Step 3: Session Activation**
```bash
# SuperClaude prepares active development environment:
- Agent specialization activation based on project type
- MCP server integration for enhanced capabilities
- Memory-driven task management preparation
- Cross-session learning pattern application
```

### Active Session Operations

**Continuous Context Management**:
- Real-time memory updates during development work
- Pattern recognition and learning capture
- Automatic checkpoint creation at critical junctures
- Cross-session insight accumulation and refinement

**Task Management Integration**:
```bash
# Task Management Mode with Memory
📋 Plan → write_memory("plan", goal_statement)
→ 🎯 Phase → write_memory("phase_X", milestone)  
  → 📦 Task → write_memory("task_X.Y", deliverable)
    → ✓ Todo → TodoWrite + write_memory("todo_X.Y.Z", status)
```

**Quality Gate Integration**:
- Validation checkpoints with memory persistence
- Reflection triggers for major decisions
- Learning capture during problem resolution
- Pattern documentation for future reference

### Session Completion and Persistence

**Step 1: Progress Assessment**
```bash
/sc:reflect --type completion
# Evaluates session outcomes:
- Task completion against original objectives
- Quality assessment of delivered work
- Learning insights and pattern discoveries
- Blockers and remaining work identification
```

**Step 2: Context Preservation**
```bash
/sc:save --type all --summarize
# Comprehensive session archival:
- Complete context state preservation
- Discovery documentation and pattern capture
- Cross-session learning artifact creation
- Recovery checkpoint establishment
```

**Step 3: Session Closure**
```bash
# SuperClaude completes session lifecycle:
- Memory optimization and cleanup
- Temporary state removal
- Cross-session relationship establishment
- Future session preparation
```

### Session Resumption Workflow

**Context Restoration**:
```bash
/sc:load
# Intelligent session restoration:
1. list_memories() → Display available context
2. read_memory("current_plan") → Resume primary objectives
3. think_about_collected_information() → Understand progress state
4. Project context reactivation with full capability restoration
```

**State Analysis**:
```bash
# SuperClaude analyzes restoration context:
- Progress evaluation against previous session objectives
- Context gap identification and resolution
- Workflow continuation strategy determination
- Enhanced capability activation based on accumulated learning
```

## Context Management

### Project Context Layers

**File System Context**:
- Directory structure and organization patterns
- File naming conventions and categorization
- Configuration file relationships and dependencies
- Build artifact and output directory management

**Code Context**:
- Architectural patterns and design principles
- Code style and formatting preferences
- Dependency usage patterns and import conventions
- Testing strategies and quality assurance approaches

**Development Context**:
- Workflow patterns and tool preferences
- Debugging strategies and problem-solving approaches
- Performance optimization patterns and techniques
- Security considerations and implementation strategies

**Team Context**:
- Collaboration patterns and communication preferences
- Code review standards and quality criteria
- Documentation approaches and maintenance strategies
- Deployment and release management patterns

### Context Persistence Strategies

**Incremental Context Building**:
- Session-by-session context enhancement
- Pattern recognition and abstraction
- Anti-pattern identification and avoidance
- Success strategy documentation and refinement

**Context Validation**:
- Regular context integrity checks
- Outdated information identification and removal
- Context relationship validation and maintenance
- Cross-session consistency enforcement

**Context Optimization**:
- Memory usage optimization for large projects
- Context relevance scoring and prioritization
- Selective context loading based on task requirements
- Performance-critical context caching strategies

### Memory Management Patterns

**Memory Types**:

**Temporary Memory**: Session-specific, cleanup after completion
```bash
checkpoint_[timestamp]: Recovery states
todo_[task].[number]: Atomic action tracking  
blockers: Current impediments
working_context: Active development state
```

**Persistent Memory**: Cross-session preservation
```bash
plan_[timestamp]: Project objectives
decisions: Architectural choices
patterns: Successful approaches
insights: Learning artifacts
```

**Archived Memory**: Historical reference
```bash
completed_phases: Finished milestone documentation
resolved_patterns: Successful problem solutions
performance_optimizations: Applied improvements
security_implementations: Implemented protections
```

## Checkpointing

### Automatic Checkpoint Creation

**Time-Based Triggers**:
- Session duration exceeding 30 minutes
- Continuous development work >45 minutes
- Complex task sequences >1 hour
- Daily development session boundaries

**Event-Based Triggers**:
- Major architectural decision implementation
- Significant code refactoring completion
- Error recovery and problem resolution
- Quality gate completion and validation

**Progress-Based Triggers**:
- Task phase completion in complex workflows
- Multi-file operation completion
- Testing milestone achievement
- Documentation generation completion

### Manual Checkpoint Strategies

**Strategic Checkpoints**:
```bash
/sc:save --checkpoint --type all
# Before risky operations:
- Major refactoring initiatives
- Architectural pattern changes
- Dependency updates or migrations
- Performance optimization attempts
```

**Milestone Checkpoints**:
```bash
/sc:save --summarize --checkpoint  
# At development milestones:
- Feature completion and testing
- Integration points and API implementations
- Security feature implementations
- Performance target achievements
```

**Recovery Checkpoints**:
```bash
/sc:save --type context --checkpoint
# Before complex debugging:
- Multi-component failure investigation
- Performance bottleneck analysis
- Security vulnerability remediation
- Integration issue resolution
```

### Checkpoint Management

**Checkpoint Naming Conventions**:
```bash
session_[timestamp]: Regular session preservation
milestone_[feature]: Feature completion states
recovery_[issue]: Problem resolution points
decision_[architecture]: Major choice documentation
```

**Checkpoint Validation**:
- Context integrity verification
- Memory consistency checking
- Cross-session compatibility validation
- Recovery state functionality testing

**Checkpoint Cleanup**:
- Automatic removal of outdated temporary checkpoints
- Consolidation of related checkpoint sequences
- Archive creation for completed project phases
- Memory optimization through selective retention

## Cross-Session Workflows

### Long-Term Project Development

**Project Initiation Session**:
```bash
Session 1: Project Analysis and Planning
/sc:load                                    # Initialize new project
/sc:analyze .                              # Comprehensive project analysis
/sc:brainstorm "modernization strategy"     # Interactive requirement discovery
/sc:save --type all --summarize            # Preserve initial insights
```

**Implementation Sessions**:
```bash
Session 2-N: Iterative Development
/sc:load                                   # Resume with full context
/sc:reflect --type session               # Validate progress continuation
[Development work with automatic checkpointing]
/sc:save --checkpoint                     # Preserve progress state
```

**Completion Session**:
```bash
Final Session: Project Completion
/sc:load                                  # Final context restoration
/sc:reflect --type completion            # Comprehensive completion assessment
/sc:save --type all --summarize          # Archive complete project insights
```

### Collaborative Development Patterns

**Context Sharing Strategies**:
- Team-specific memory organization
- Shared pattern libraries and conventions
- Collaborative checkpoint management
- Cross-team insight documentation

**Handoff Workflows**:
```bash
Developer A Completion:
/sc:save --type all --summarize
# Complete context documentation for handoff

Developer B Resumption:  
/sc:load --analyze
# Context restoration with comprehension validation
```

### Multi-Project Context Management

**Project Isolation**:
- Separate memory namespaces per project
- Context switching with state preservation
- Project-specific pattern libraries
- Independent checkpoint management

**Cross-Project Learning**:
- Pattern sharing between related projects
- Architecture decision documentation
- Solution library accumulation
- Best practice consolidation

### Complex Task Continuation

**Multi-Session Task Management**:
```bash
Session 1: Task Initiation
write_memory("plan_auth", "Implement JWT authentication")
write_memory("phase_1", "Analysis and design")
TodoWrite: Create detailed task breakdown

Session 2: Implementation Continuation  
list_memories() → Shows previous context
read_memory("plan_auth") → Resume objectives
think_about_collected_information() → Progress assessment
Continue implementation with full context
```

**Cross-Session Quality Gates**:
- Validation checkpoints across session boundaries
- Quality criteria persistence and evaluation
- Cross-session testing strategy continuation
- Performance monitoring across development phases

## Session Optimization

### Best Practices for Effective Sessions

**Session Initialization Optimization**:
```bash
# Efficient session startup pattern
/sc:load --analyze                        # Load with immediate analysis
/sc:reflect --type session               # Validate continuation strategy  
[Focused development work]
/sc:save --checkpoint                     # Regular progress preservation
```

**Memory Management Optimization**:
- Regular memory cleanup of temporary artifacts
- Strategic memory organization for quick retrieval
- Context relevance validation and maintenance
- Performance monitoring for large project contexts

**Task Management Optimization**:
- Clear objective definition and persistence
- Progress tracking with meaningful checkpoints
- Quality gate integration with validation
- Learning capture and pattern documentation

### Performance Considerations

**Session Startup Performance**:
- Target <500ms for context loading
- <200ms for memory operations
- <1s for checkpoint creation
- Optimal balance between completeness and speed

**Memory Performance**:
- Efficient storage patterns for large codebases
- Selective context loading based on task scope
- Memory compression for archived sessions
- Cache optimization for frequently accessed patterns

**Cross-Session Performance**:
- Context relationship optimization
- Pattern matching acceleration
- Learning algorithm efficiency
- Cleanup automation for memory optimization

### Session Efficiency Patterns

**Focused Session Design**:
- Clear session objectives and success criteria
- Scope limitation for manageable complexity
- Quality gate integration for validation
- Learning capture for future efficiency

**Context Reuse Strategies**:
- Pattern library development and maintenance
- Solution template creation and application
- Architecture decision documentation and reuse
- Best practice consolidation and application

**Automation Integration**:
- Automatic checkpoint creation based on activity
- Quality gate automation with context persistence
- Pattern recognition and application automation
- Learning capture automation for efficiency

## Advanced Session Patterns

### Multi-Layer Context Management

**Context Hierarchies**:
```bash
Global Context: Organization patterns and standards
Project Context: Specific project architecture and decisions
Feature Context: Feature-specific patterns and implementations  
Task Context: Immediate work objectives and constraints
```

**Context Inheritance Patterns**:
- Global patterns inherited by projects
- Project decisions applied to features
- Feature patterns available to tasks
- Task insights contributed to higher levels

**Context Specialization**:
- Domain-specific context layers (frontend, backend, security)
- Technology-specific patterns and conventions
- Quality-specific criteria and validation approaches
- Performance-specific optimization strategies

### Adaptive Session Management

**Context-Aware Session Adaptation**:
- Session behavior modification based on project type
- Tool selection optimization based on context history
- Agent activation patterns based on accumulated learning
- Quality gate customization based on project requirements

**Learning-Driven Session Evolution**:
- Session pattern optimization based on success metrics
- Context organization improvement through usage analysis
- Memory management refinement through performance monitoring
- Checkpoint strategy optimization through recovery analysis

**Predictive Session Features**:
- Next-step suggestion based on context patterns
- Resource requirement prediction based on task analysis
- Quality issue prediction based on historical patterns
- Performance bottleneck prediction based on context analysis

### Power User Techniques

**Session Orchestration**:
```bash
# Complex multi-session orchestration
/sc:load --type checkpoint --analyze      # Strategic restoration
/sc:reflect --type task --validate        # Comprehensive validation
[Orchestrated development with multiple agents and tools]
/sc:save --type all --summarize          # Complete preservation
```

**Memory Pattern Development**:
- Custom memory schemas for specialized workflows
- Pattern template creation for repeated tasks
- Context relationship modeling for complex projects
- Learning acceleration through pattern recognition

**Cross-Session Analytics**:
- Session efficiency analysis and optimization
- Context usage pattern analysis and refinement
- Quality outcome correlation with session patterns
- Performance optimization through session analytics

**Advanced Integration Patterns**:
- Multi-MCP server coordination with context awareness
- Agent specialization with session-specific optimization
- Tool selection matrix optimization based on session history
- Quality gate customization with context-aware validation

## Troubleshooting Sessions

### Common Session Issues

**Context Loading Problems**:

**Symptom**: Session fails to load project context
```bash
Error: "Failed to activate project context"
Solution:
1. Verify Serena MCP server connection
2. Check project directory permissions
3. Validate memory integrity with list_memories()
4. Reinitialize with /sc:load --refresh
```

**Symptom**: Incomplete context restoration
```bash
Issue: Missing project patterns or decisions
Diagnosis:
1. /sc:reflect --type session --analyze
2. Check memory completeness with list_memories()
3. Validate context relationships
Resolution:
1. Manual context restoration from checkpoints
2. Pattern rediscovery through analysis
3. Context rebuild with /sc:load --analyze
```

**Memory Management Issues**:

**Symptom**: Memory operations timeout or fail
```bash
Error: "Memory operation exceeded timeout"
Solution:
1. Check Serena MCP server health
2. Optimize memory size through cleanup
3. Validate memory schema consistency
4. Reinitialize session with fresh context
```

**Symptom**: Context inconsistency across sessions
```bash
Issue: Different behavior between sessions
Diagnosis:
1. Compare memory states with list_memories()
2. Validate context integrity
3. Check for corrupted checkpoints
Resolution:
1. Restore from known-good checkpoint
2. Rebuild context through fresh analysis
3. Consolidate memory with cleanup
```

### Performance Troubleshooting

**Slow Session Initialization**:

**Diagnosis**:
```bash
# Performance analysis
/sc:load --analyze                        # Time context loading
list_memories()                          # Check memory size
/sc:reflect --type session --analyze     # Assess context complexity
```

**Optimization**:
```bash
# Memory optimization
/sc:save --type learnings               # Preserve insights only
[Clean up temporary memories]
/sc:load --refresh                      # Fresh initialization
```

**Memory Performance Issues**:

**Large Project Context Management**:
- Selective context loading based on task scope
- Memory compression for archived sessions
- Context segmentation for performance
- Cleanup automation for memory optimization

**Cross-Session Performance Optimization**:
- Context relationship streamlining
- Pattern matching algorithm optimization
- Learning algorithm efficiency improvement
- Memory access pattern optimization

### Recovery Procedures

**Complete Session Recovery**:
```bash
# When session state is completely lost
1. /sc:load --type checkpoint --checkpoint [last_known_good]
2. /sc:reflect --type session --validate
3. Manual context verification and supplementation
4. /sc:save --checkpoint                  # Create new recovery point
```

**Partial Context Recovery**:
```bash
# When some context is available but incomplete
1. list_memories()                       # Assess available context
2. /sc:load --analyze                    # Attempt restoration
3. /sc:reflect --type completion         # Identify gaps
4. Manual gap filling through analysis
5. /sc:save --type all                   # Preserve recovered state
```

**Memory Corruption Recovery**:
```bash
# When memory contains inconsistent or corrupted data
1. Backup current state: /sc:save --checkpoint
2. Clean corrupted memories: delete_memory([corrupted_keys])
3. Restore from archived checkpoints
4. Rebuild context through fresh analysis
5. Validate recovery: /sc:reflect --type session --validate
```

### Session Health Monitoring

**Session Health Indicators**:
- Context loading time (<500ms target)
- Memory operation performance (<200ms target)
- Cross-session consistency validation
- Learning accumulation and pattern recognition

**Proactive Health Management**:
- Regular memory optimization and cleanup
- Context integrity validation
- Performance monitoring and optimization
- Checkpoint validation and maintenance

**Health Diagnostics**:
```bash
# Comprehensive session health check
/sc:load --analyze                       # Context loading assessment
list_memories()                         # Memory state evaluation
/sc:reflect --type session --validate   # Context integrity check
[Performance monitoring during operations]
/sc:save --summarize                    # Health documentation
```

This comprehensive session management system transforms SuperClaude from a stateless AI assistant into a persistent, learning development partner that accumulates project knowledge and improves its assistance over time. The combination of intelligent memory management, automatic checkpointing, and cross-session learning creates a development experience that truly adapts to your projects and workflows.

## Related Guides

**🚀 Foundation (Start Here First)**
- [Installation Guide](installation-guide.md) - Ensure SuperClaude is properly installed with MCP servers
- [SuperClaude User Guide](superclaude-user-guide.md) - Understanding persistent intelligence concepts
- [Examples Cookbook](examples-cookbook.md) - Working session workflows and patterns

**🛠️ Core Session Usage (Essential)**
- [Commands Guide](commands-guide.md) - Session commands (/sc:load, /sc:save, /sc:reflect)
- [Agents Guide](agents-guide.md) - How agents coordinate across sessions
- [Behavioral Modes Guide](behavioral-modes-guide.md) - Mode persistence and adaptation

**⚙️ Advanced Session Techniques (Power Users)**
- [Best Practices Guide](best-practices.md) - Session optimization and workflow patterns
- [Flags Guide](flags-guide.md) - Session-related flags and control options
- [Technical Architecture Guide](technical-architecture.md) - Memory system and checkpoint implementation

**🔧 Session Troubleshooting**
- [Troubleshooting Guide](troubleshooting-guide.md) - Session loading, memory, and persistence issues

**📖 Recommended Learning Path:**
1. [Examples Cookbook](examples-cookbook.md) - Try basic session workflows
2. [Commands Guide](commands-guide.md) - Master /sc:load, /sc:save, /sc:reflect
3. [Best Practices Guide](best-practices.md) - Learn checkpoint and workflow patterns
4. Advanced techniques in this guide for complex projects

**🎯 Session Management Mastery:**
- **Beginner**: Basic /sc:load and /sc:save usage
- **Intermediate**: Checkpoint strategies and cross-session workflows  
- **Advanced**: Memory optimization and custom session patterns
- **Expert**: Multi-project context management and session analytics