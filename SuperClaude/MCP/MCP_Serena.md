# Serena MCP Server

## Purpose
Powerful coding agent toolkit providing semantic retrieval, intelligent editing capabilities, project-aware context management, and comprehensive memory operations for SuperGemini integration

## Activation Patterns

**Automatic Activation**:
- Complex semantic code analysis requests
- Project-wide symbol navigation and referencing
- Advanced editing operations requiring context awareness
- Multi-file refactoring with semantic understanding
- Code exploration and discovery workflows

**Manual Activation**:
- Flag: `--serena`, `--semantic`

**Smart Detection**:
- Symbol lookup and reference analysis keywords
- Complex code exploration requests
- Project-wide navigation and analysis
- Semantic search and context-aware editing
- Memory-driven development workflows

## Flags

**`--serena` / `--semantic`**
- Enable Serena for semantic code analysis and intelligent editing
- Auto-activates: Complex symbol analysis, project exploration, semantic search
- Detection: find/symbol/reference keywords, project navigation, semantic analysis
- Workflow: Project activation → Semantic analysis → Intelligent editing → Context preservation

**`--no-serena`**
- Disable Serena server
- Fallback: Standard file operations and basic search
- Performance: 10-30% faster when semantic analysis not needed

## Workflow Process

1. **Project Activation**: Initialize project context and load semantic understanding
2. **Symbol Analysis**: Deep symbol discovery and reference mapping across codebase
3. **Context Gathering with Selective Compression**: Collect relevant code context with content classification
   - **SuperGemini Framework** (Complete exclusion): All framework directories and components
   - **Session Data** (Apply compression): Session metadata, checkpoints, cache content only
   - **User Content**: Preserve full fidelity for project code, user-specific content, configurations
4. **Server Coordination**: Sync with Morphllm for hybrid editing, Sequential for analysis
5. **Semantic Search**: Intelligent pattern matching and code discovery
6. **Memory Management with Selective Compression**: Store and retrieve development context with optimized storage
   - **SuperGemini Framework Content**: Complete exclusion from compression (0% compression)
   - **Session Data**: Compressed storage for session metadata and operational data only
   - **Project Memories**: Full preservation for user project insights and context
7. **Intelligent Editing**: Context-aware code modifications with semantic understanding
8. **Reference Tracking**: Maintain symbol relationships and dependency awareness
9. **Language Server Integration**: Real-time language analysis and validation
10. **Dashboard Monitoring**: Web-based interface for agent status and metrics

## Integration Points

**Commands**: `analyze`, `implement`, `refactor`, `explore`, `find`, `edit`, `improve`, `design`, `load`, `save`

**Thinking Modes**: 
- Works with all thinking flags for semantic analysis
- `--seq`: Symbol-level context analysis with Sequential coordination
- `--systematic`: Project-wide semantic understanding with structured approach
- `--deep`: Complex architectural semantic analysis with comprehensive coverage

**Other MCP Servers**: 
- **Morphllm**: Hybrid intelligence for advanced editing operations
- **Sequential**: Complex semantic analysis coordination
- **Context7**: Framework-specific semantic patterns
- **Magic**: UI component semantic understanding
- **Playwright**: Testing semantic validation

## Core Capabilities

### Semantic Retrieval
- **Symbol Discovery**: Deep symbol search across entire codebase
- **Reference Analysis**: Find all references and usages of symbols
- **Context-Aware Search**: Semantic pattern matching beyond simple text search
- **Project Navigation**: Intelligent code exploration and discovery

### Intelligent Editing
- **Context-Aware Modifications**: Edits that understand surrounding code semantics
- **Symbol-Based Refactoring**: Rename and restructure with full dependency tracking
- **Semantic Code Generation**: Generate code that fits naturally into existing patterns
- **Multi-File Coordination**: Maintain consistency across related files

### Memory Management
- **Development Context**: Store and retrieve project insights and decisions
- **Pattern Recognition**: Learn and apply project-specific coding patterns
- **Context Preservation**: Maintain semantic understanding across sessions
- **Knowledge Base**: Build cumulative understanding of codebase architecture

### Language Server Integration
- **Real-Time Analysis**: Live language server integration for immediate feedback
- **Symbol Information**: Rich symbol metadata and type information
- **Error Detection**: Semantic error identification and correction suggestions
- **Code Completion**: Context-aware code completion and suggestions

### Project Management
- **Multi-Project Support**: Handle multiple codebases with context switching
- **Configuration Management**: Project-specific settings and preferences
- **Mode Switching**: Adaptive behavior based on development context
- **Dashboard Interface**: Web-based monitoring and control interface

## Use Cases

- **Code Exploration**: Navigate and understand large, complex codebases
- **Semantic Refactoring**: Rename variables, functions, classes with full impact analysis
- **Pattern Discovery**: Find similar code patterns and implementation examples
- **Context-Aware Development**: Write code that naturally fits existing architecture
- **Cross-Reference Analysis**: Understand how components interact and depend on each other
- **Intelligent Code Search**: Find code based on semantic meaning, not just text matching
- **Project Onboarding**: Quickly understand and navigate new codebases
- **Memory Replacement**: Complete replacement of ClaudeDocs file-based system
- **Session Management**: Save/load project context and session state
- **Task Reflection**: Intelligent task tracking and validation

## Error Recovery & Resilience

### Primary Recovery Strategies
- **Connection lost** → Graceful degradation with cached context → Automatic reconnection attempts
- **Project activation failed** → Manual setup with guided configuration → Alternative analysis pathways
- **Symbol lookup timeout** → Use cached semantic data → Fallback to intelligent text search
- **Language server error** → Automatic restart with state preservation → Manual validation backup
- **Memory corruption** → Intelligent memory reconstruction → Selective context recovery

### Advanced Recovery Orchestration
- **Context Preservation**: Critical project context automatically saved for disaster recovery
- **Multi-Language Fallback**: When LSP fails, fallback to language-specific text analysis
- **Semantic Cache Management**: Intelligent cache invalidation and reconstruction strategies
- **Cross-Session Recovery**: Session state recovery from multiple checkpoint sources
- **Hybrid Intelligence Failover**: Seamless coordination with Morphllm when semantic analysis unavailable

## Caching Strategy

- **Cache Type**: Semantic analysis results, symbol maps, and project context
- **Cache Duration**: Project-based with intelligent invalidation
- **Cache Key**: Project path + file modification timestamps + symbol signature

## Quality Gates Integration

Serena contributes to the following validation steps:

- **Step 2 - Type Analysis**: Deep semantic type checking and compatibility validation
- **Step 3 - Code Quality**: Semantic code quality assessment and pattern compliance
- **Step 4 - Security Assessment**: Semantic security pattern analysis
- **Step 6 - Performance Analysis**: Semantic performance pattern identification

## Hybrid Intelligence with Morphllm

**Complementary Capabilities**:
- **Serena**: Provides semantic understanding and project context
- **Morphllm**: Delivers precise editing execution and natural language processing
- **Combined**: Creates powerful hybrid editing engine with both intelligence and precision

**Coordination Patterns**:
- Serena analyzes semantic context → Morphllm executes precise edits
- Morphllm identifies edit requirements → Serena provides semantic validation
- Joint validation ensures both syntax correctness and semantic consistency


## Strategic Orchestration

### When to Use Serena
- **Large Codebase Analysis**: Projects >50 files requiring semantic understanding
- **Symbol-Level Refactoring**: Rename, extract, move operations with dependency tracking
- **Project Context Management**: Session persistence and cross-session learning
- **Multi-Language Projects**: Complex polyglot codebases requiring LSP integration
- **Architectural Analysis**: System-wide understanding and pattern recognition

### Memory-Driven Development Strategy
**Session Lifecycle Integration**:
- Project activation → Context loading → Work session → Context persistence
- Automatic checkpoints on high-risk operations and task completion
- Cross-session knowledge accumulation and pattern learning

**Memory Organization Strategy**:
- Replace file-based ClaudeDocs with intelligent memory system
- Hierarchical memory structure: session → checkpoints → summaries → insights
- Semantic indexing for efficient context retrieval and pattern matching

### Advanced Semantic Intelligence
- **Project-Wide Understanding**: Complete codebase context maintained across sessions
- **Dependency Graph Analysis**: Real-time tracking of symbol relationships and impacts
- **Pattern Evolution Tracking**: Code patterns learned and adapted over time
- **Cross-Language Integration**: Unified understanding across multiple programming languages
- **Architectural Change Impact**: System-wide implications analyzed for all modifications

## Project Management

Essential tools for SuperGemini integration:
- `activate_project`: Initialize project context and semantic understanding
- `list_memories` / `read_memory` / `write_memory`: Memory-based development context
- `onboarding` / `check_onboarding_performed`: Project setup and validation

## SuperGemini Integration

**Session Lifecycle Commands**:
- `/sg:load` → `activate_project` + `list_memories` + context loading  
- `/sg:save` → `write_memory` + session persistence + checkpoint creation

## Error Recovery

- **Connection lost** → Graceful degradation with cached context
- **Project activation failed** → Manual setup with guided configuration
- **Symbol lookup timeout** → Use cached semantic data → Fallback to intelligent text search