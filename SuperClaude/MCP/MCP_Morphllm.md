# Morphllm MCP Server

## Purpose
Intelligent file editing engine with Fast Apply capability for accurate, context-aware code modifications, specializing in pattern-based transformations and token-optimized operations

## Activation Patterns

**Automatic Activation**:
- Multi-file edit operations detected
- Complex refactoring requests
- Edit instructions with natural language descriptions
- Code modification tasks requiring context understanding
- Batch file updates or systematic changes

**Manual Activation**:
- Flag: `--morph`, `--fast-apply`

**Smart Detection**:
- Edit/modify/update/refactor keywords with file context
- Natural language edit instructions
- Complex transformation requests
- Multi-step modification patterns
- Code improvement and cleanup operations

## Flags

**`--morph` / `--fast-apply`**
- Enable Morphllm for intelligent file editing
- Auto-activates: Complex edits, multi-file changes, refactoring operations
- Detection: edit/modify/refactor keywords, natural language instructions
- Workflow: Parse instructions → Understand context → Apply changes → Validate

**`--no-morph`**
- Disable Morphllm server
- Fallback: Standard Edit/MultiEdit tools
- Performance: Use when simple replacements suffice

## Workflow Process

1. **Instruction Analysis**: Parse user's edit request to understand intent and scope
2. **Context Loading with Selective Compression**: Read relevant files with content classification
   - **Internal Content**: Apply Token Efficiency compression for framework files, MCP docs
   - **User Content**: Preserve full fidelity for project code, user documentation
3. **Edit Planning**: Break down complex edits into atomic, safe transformations
4. **Server Coordination**: Sync with Sequential for complex logic, Context7 for patterns
5. **Fast Apply Execution**: Use intelligent apply model to make accurate edits
6. **Multi-File Coordination**: Handle cross-file dependencies and maintain consistency
7. **Validation**: Ensure syntax correctness and preserve functionality
8. **Rollback Preparation**: Maintain ability to revert changes if needed
9. **Result Verification**: Confirm edits match intended modifications
10. **Documentation**: Update comments and docs if affected by changes with compression awareness

## Integration Points

**Commands**: `edit`, `refactor`, `improve`, `fix`, `cleanup`, `implement`, `build`, `design`

**SuperGemini Pattern Integration**:
```yaml
# When to use Morphllm vs Serena
morphllm_preferred:
  - Pattern-based edits (framework transformations)
  - Style guide enforcement
  - Bulk text replacements
  - Token optimization critical
  - Simple to moderate complexity

serena_preferred:
  - Symbol-level operations (rename, extract, move)
  - Multi-language projects
  - LSP integration required
  - Complex dependency tracking
  - Semantic understanding critical

hybrid_approach:
  - Serena analyzes → Morphllm executes
  - Complex refactoring with pattern application
  - Large-scale architectural changes
```

**Thinking Modes**: 
- Works with all thinking flags for complex edit planning
- `--seq`: Analyzes edit impact across modules and plans systematic refactoring with Sequential analysis
- `--deep`: Coordinates large-scale transformations with comprehensive analysis

**Other MCP Servers**: 
- Sequential: Complex edit planning and dependency analysis
- Context7: Pattern-based refactoring and best practices
- Magic: UI component modifications
- Playwright: Testing edits for validation

## Core Capabilities

### Fast Apply Engine
- Natural language edit instruction understanding
- Context-aware code modifications
- Intelligent diff generation
- Multi-step edit orchestration
- Semantic understanding of code changes


## Strategic Orchestration

### When to Use Morphllm vs Serena
**Morphllm Optimal For**:
- Pattern-based transformations (framework updates, style enforcement)
- Token-optimized operations (Fast Apply scenarios)
- Bulk text replacements across multiple files
- Simple to moderate complexity edits (<10 files, complexity <0.6)

**Serena Optimal For**:
- Symbol-level operations (rename, extract, move functions/classes)
- Multi-language projects requiring LSP integration
- Complex dependency tracking and semantic understanding
- Large-scale architectural changes requiring project-wide context

### Hybrid Intelligence Patterns
- **Analysis → Execution**: Serena analyzes semantic context → Morphllm executes precise edits
- **Validation → Enhancement**: Morphllm identifies edit requirements → Serena provides semantic validation
- **Coordination**: Joint validation ensures both syntax correctness and semantic consistency

### Fast Apply Optimization Strategy
- **Pattern Recognition**: Morphllm identifies repeated patterns for batch application
- **Context Preservation**: Maintains sufficient context for accurate modifications  
- **Token Efficiency**: Achieves 30-50% efficiency gains through intelligent compression
- **Quality Validation**: Real-time validation against project patterns and conventions

### Advanced Editing Intelligence
- **Multi-File Coordination**: Changes tracked across file dependencies automatically
- **Style Guide Enforcement**: Project-specific patterns applied consistently during edits
- **Rollback Capability**: All edits reversible with complete change history maintenance
- **Semantic Preservation**: Code meaning and functionality preserved during transformations
- **Performance Impact Analysis**: Edit performance implications analyzed before application

## Use Cases

- **Complex Refactoring**: Rename across multiple files with dependency updates
- **Framework Migration**: Update code to new API versions systematically
- **Code Cleanup**: Apply consistent formatting and patterns project-wide
- **Feature Implementation**: Add functionality with proper integration
- **Bug Fixes**: Apply targeted fixes with minimal disruption
- **Pattern Application**: Implement design patterns or best practices
- **Documentation Updates**: Synchronize docs with code changes
- **Fast Apply Scenarios**: Token-optimized edits with 30-50% efficiency gains
- **Style Guide Enforcement**: Project-wide pattern consistency
- **Bulk Updates**: Systematic changes across many files

## Error Recovery

- **Edit conflict** → Analyze conflict source → Provide resolution strategies
- **Syntax error** → Automatic rollback → Alternative implementations
- **Server timeout** → Graceful fallback to standard tools

## Quality Gates Integration

- **Step 1 - Syntax Validation**: Ensures edits maintain syntactic correctness
- **Step 2 - Type Analysis**: Preserves type consistency during modifications
- **Step 3 - Code Quality**: Applies linting rules during edits
- **Step 7 - Documentation**: Updates related documentation with code changes