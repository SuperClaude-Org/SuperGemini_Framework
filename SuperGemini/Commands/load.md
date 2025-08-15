---
name: load
description: "Session lifecycle management with Serena MCP integration and performance requirements for project context loading"
allowed-tools: [read_file, search_file_content, glob, write_file, activate_project, list_memories, read_memory, write_memory, check_onboarding_performed, onboarding]

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

# /sg:load - Project Context Loading with Serena

## Purpose
Load and analyze project context using Serena MCP for project activation, memory retrieval, and context management with session lifecycle integration and cross-session persistence capabilities.

## Usage
```
/sg:load [target] [--type project|config|deps|env|checkpoint] [--refresh] [--analyze] [--checkpoint ID] [--resume] [--validate] [--performance] [--metadata] [--cleanup] [--uc]
```

## Arguments
- `target` - Project directory or name (defaults to current directory)
- `--type` - Specific loading type (project, config, deps, env, checkpoint)
- `--refresh` - Force reload of project memories and context
- `--analyze` - Run deep analysis after loading
- `--onboard` - Run onboarding if not performed
- `--checkpoint` - Restore from specific checkpoint ID
- `--resume` - Resume from latest checkpoint automatically
- `--validate` - Validate session integrity and data consistency
- `--performance` - Enable performance monitoring and optimization
- `--metadata` - Include comprehensive session metadata
- `--cleanup` - Perform session cleanup and optimization
- `--uc` - Enable Token Efficiency mode for all memory operations (optional)

## Token Efficiency Integration

### Optional Token Efficiency Mode
The `/sg:load` command supports optional Token Efficiency mode via the `--uc` flag:

- **User Choice**: `--uc` flag can be explicitly specified for compression
- **Compression Strategy**: When enabled: 30-50% reduction with ≥95% information preservation
- **Content Classification**:
  - **SuperGemini Framework** (0% compression): Complete exclusion
  - **User Project Content** (0% compression): Full fidelity preservation
  - **Session Data** (30-50% compression): Optimized storage when --uc used
- **Quality Preservation**: Framework compliance with MODE_Token_Efficiency.md patterns

### Performance Benefits (when --uc used)
- Token Efficiency applies to all session memory operations
- Compression inherited by memory operations within session context
- Performance benefits: Faster session operations and reduced context usage

## Session Lifecycle Integration

### 1. Session State Management
- Analyze current session state and context requirements
- Use `activate_project` tool to activate the project
- Pass `{"project": target}` as parameters
- Automatically handles project registration if needed
- Validates project path and language detection
- Identify critical information for persistence or restoration
- Assess session integrity and continuity needs

### 2. Serena MCP Coordination with Token Efficiency
- Execute appropriate Serena MCP operations for session management
- Call `list_memories` tool to discover existing memories
- Load relevant memories based on --type parameter:
  - **project**: Load project_purpose, tech_stack memories (framework excluded from compression)
  - **config**: Load code_style_conventions, completion_tasks (framework excluded from compression)
  - **deps**: Analyze package.json/pyproject.toml (preserve user content)
  - **env**: Load environment-specific memories (framework excluded from compression)
- **Content Classification Strategy**:
  - **SuperGemini Framework** (Complete exclusion): All framework directories and components
  - **Session Data** (Apply compression): Session metadata, checkpoints, cache content only
  - **User Project Content** (Preserve fidelity): Project files, user documentation, configurations
- Handle memory organization, checkpoint creation, or state restoration with selective compression
- Manage cross-session context preservation and enhancement with optimized storage

### 3. Performance Validation
- Monitor operation performance against strict session targets
- Read memories using `read_memory` tool with `{"memory_file_name": name}`
- Build comprehensive project context from memories
- Supplement with file analysis if memories incomplete
- Validate memory efficiency and response time requirements
- Ensure session operations meet <200ms core operation targets

### 4. Context Continuity
- Maintain session context across operations and interruptions
- Call `check_onboarding_performed` tool
- If not onboarded and --onboard flag, call `onboarding` tool
- Create initial memories if project is new
- Preserve decision history, task progress, and accumulated insights
- Enable seamless continuation of complex multi-session workflows

### 5. Quality Assurance
- Validate session data integrity and completeness
- If --checkpoint flag: Load specific checkpoint via `read_memory`
- If --resume flag: Load latest checkpoint from `checkpoints/latest`
- If --type checkpoint: Restore session state from checkpoint metadata
- Display resumption summary showing:
  - Work completed in previous session
  - Open tasks and questions
  - Context changes since checkpoint
  - Estimated time to full restoration
- Verify cross-session compatibility and version consistency
- Generate session analytics and performance reports

## Mandatory Serena MCP Integration

### Core Serena Operations
- **Memory Management**: `read_memory`, `write_memory`, `list_memories`
- **Project Management**: `activate_project`, `check_onboarding_performed`, `onboarding`
- **Context Enhancement**: Build and enhance project understanding across sessions
- **State Management**: Session state persistence and restoration capabilities

### Session Data Organization
- **Memory Hierarchy**: Structured memory organization for efficient retrieval
- **Context Accumulation**: Building understanding across session boundaries
- **Performance Metrics**: Session operation timing and efficiency tracking
- **Project Activation**: Seamless project initialization and context loading

### Advanced Session Features
- **Checkpoint Restoration**: Resume from specific checkpoints with full context
- **Cross-Session Learning**: Accumulating knowledge and patterns across sessions
- **Performance Optimization**: Session-level caching and efficiency improvements
- **Onboarding Integration**: Automatic onboarding for new projects

## Session Management Patterns

### Memory Operations
- **Memory Categories**: Project, session, checkpoint, and insight memory organization
- **Intelligent Retrieval**: Context-aware memory loading and optimization
- **Memory Lifecycle**: Creation, update, archival, and cleanup operations
- **Cross-Reference Management**: Maintaining relationships between memory entries

### Context Enhancement Operations with Selective Compression
- Analyze project structure if --analyze flag
- Create/update memories with new discoveries using selective compression
- Save enhanced context using `write_memory` tool with compression awareness
- Initialize session metadata with start time and optimized context loading
- Build comprehensive project understanding from compressed and preserved memories
- Enhance context through accumulated experience and insights with efficient storage
- **Compression Application**:
  - SuperGemini framework components: 0% compression (complete exclusion)
  - User project files and custom configurations: 0% compression (full preservation)
  - Session operational data only: 40-70% compression for storage optimization

### Memory Categories Used
- `project_purpose` - Overall project goals and architecture
- `tech_stack` - Technologies, frameworks, dependencies
- `code_style_conventions` - Coding standards and patterns
- `completion_tasks` - Build/test/deploy commands
- `suggested_commands` - Common development workflows
- `session/*` - Session records and continuity data
- `checkpoints/*` - Checkpoint data for restoration

### Context Operations
- **Context Preservation**: Maintaining critical context across session boundaries
- **Context Enhancement**: Building richer context through accumulated experience
- **Context Optimization**: Efficient context management and storage
- **Context Validation**: Ensuring context consistency and accuracy

## Performance Requirements

### Critical Performance Targets (Enhanced with Compression)
- **Session Initialization**: <500ms for complete session setup (improved with compression: <400ms)
- **Core Operations**: <200ms for memory reads, writes, and basic operations (improved: <150ms)
- **Memory Operations**: <200ms per individual memory operation (optimized: <150ms)
- **Context Loading**: <300ms for full context restoration (enhanced: <250ms)
- **Project Activation**: <100ms for project activation (maintained: <100ms)
- **Deep Analysis**: <3s for large projects (optimized: <2.5s)
- **Compression Overhead**: <50ms additional processing time for selective compression
- **Storage Efficiency**: 30-50% reduction in internal content storage requirements

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
- **Serena Unavailable**: Use traditional file analysis with local caching
- **Onboarding Failures**: Graceful degradation with manual onboarding options

### Recovery Strategies
- **Graceful Degradation**: Maintaining core functionality under adverse conditions
- **Automatic Recovery**: Intelligent recovery from common failure scenarios
- **Manual Recovery**: Clear escalation paths for complex recovery situations
- **State Reconstruction**: Rebuilding session state from available information
- **Fallback Mechanisms**: Backward compatibility with existing workflow patterns

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

### Integration with /sg:save
- Context loaded by /sg:load is enhanced during session
- Use /sg:save to persist session changes back to Serena
- Maintains session lifecycle: load → work → save
- Session continuity through checkpoint and restoration mechanisms

## Examples

### Basic Project Load
```
/sg:load
# Activates current directory project and loads all memories
```

### Specific Project with Analysis
```
/sg:load ~/projects/webapp --analyze
# Activates webapp project and runs deep analysis
```

### Refresh Configuration
```
/sg:load --type config --refresh
# Reloads configuration memories and updates context
```

### New Project Onboarding
```
/sg:load ./new-project --onboard
# Activates and onboards new project, creating initial memories
```

### Session Checkpoint
```
/sg:load --type checkpoint --metadata
# Create comprehensive checkpoint with metadata
```

### Session Recovery
```
/sg:load --resume --validate
# Resume from previous session with validation
```

### Performance Monitoring with Compression
```
/sg:load --performance --validate
# Session operation with performance monitoring

/sg:load --optimize-internal --performance
# Enable selective compression with performance tracking
```

### Checkpoint Restoration
```
/sg:load --resume
# Automatically resume from latest checkpoint

/sg:load --checkpoint checkpoint-2025-01-31-16:00:00  
# Restore from specific checkpoint ID

/sg:load --type checkpoint MyProject
# Load project and restore from latest checkpoint
```

### Session Continuity Examples
```
# Previous session workflow:
/sg:load MyProject              # Initialize session
# ... work on project ...
/sg:save --checkpoint          # Create checkpoint

# Next session workflow:
/sg:load MyProject --resume    # Resume from checkpoint
# ... continue work ...
/sg:save --summarize          # Save with summary
```

## Boundaries

**This session command will:**
- Provide robust session lifecycle management with strict performance requirements
- Integrate seamlessly with Serena MCP for comprehensive session capabilities
- Maintain context continuity and cross-session persistence effectively
- Support complex multi-session workflows with intelligent state management
- Deliver session operations within strict performance targets consistently
- Enable seamless project activation and context loading across sessions

**This session command will not:**
- Operate without proper Serena MCP integration and connectivity
- Compromise performance targets for additional functionality
- Proceed without proper session state validation and integrity checks
- Function without adequate error handling and recovery mechanisms
- Ignore onboarding requirements for new projects
- Skip context validation and enhancement procedures