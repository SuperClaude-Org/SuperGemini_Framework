# ORCHESTRATOR.md - SuperGemini Intelligent Routing System

Streamlined routing and coordination guide for Gemini CLI operations.

## 🎯 Quick Pattern Matching

Match user requests to appropriate tools and strategies:

```yaml
ui_component: [component, design, frontend, UI] → Magic + frontend persona
deep_analysis: [architecture, complex, system-wide] → Sequential + think modes  
quick_tasks: [simple, basic, straightforward] → Morphllm + Direct execution
large_scope: [many files, entire codebase] → Serena + Enable delegation
symbol_operations: [rename, refactor, extract, move] → Serena + LSP precision
pattern_edits: [framework, style, cleanup] → Morphllm + token optimization
performance: [optimize, slow, bottleneck] → Performance persona + profiling
security: [vulnerability, audit, secure] → Security persona + validation
documentation: [document, README, guide] → Scribe persona + Context7
brainstorming: [explore, figure out, not sure, new project] → MODE_Brainstorming + /sg:brainstorm
memory_operations: [save, load, checkpoint] → Serena + session management
session_lifecycle: [init, work, checkpoint, complete] → /sg:load + /sg:save + /sg:reflect
task_reflection: [validate, analyze, complete] → /sg:reflect + Serena reflection tools
```

## 🚦 Resource Management

Simple zones for resource-aware operation:

```yaml
green_zone (0-75%):
  - Full capabilities available
  - Proactive caching enabled
  - Normal verbosity

yellow_zone (75-85%):
  - Activate efficiency mode
  - Reduce verbosity
  - Defer non-critical operations

red_zone (85%+):
  - Essential operations only
  - Minimize output verbosity  
  - Fail fast on complex requests
```

## 🔧 Tool Selection Guide

### When to use MCP Servers:
- **Context7**: Library docs, framework patterns, best practices
- **Sequential**: Multi-step problems, complex analysis, debugging
- **Magic**: UI components, design systems, frontend generation
- **Playwright**: Browser testing, E2E validation, visual testing
- **Morphllm**: Pattern-based editing, token optimization, fast edits
- **Serena**: Symbol-level operations, large refactoring, multi-language projects

### Hybrid Intelligence Routing:
**Serena vs Morphllm Decision Matrix**:
```yaml
serena_triggers:
  file_count: >10
  symbol_operations: [rename, extract, move, analyze]
  multi_language: true
  lsp_required: true
  shell_integration: true
  complexity_score: >0.6

morphllm_triggers:
  framework_patterns: true
  token_optimization: required
  simple_edits: true
  fast_apply_suitable: true
  complexity_score: ≤0.6
```

### Simple Fallback Strategy:
```
Serena unavailable → Morphllm → Native Gemini CLI tools → Explain limitations if needed
```

## ⚡ Auto-Activation Rules

Clear triggers for automatic enhancements:

```yaml
enable_sequential:
  - Complexity appears high (multi-file, architectural)
  - User explicitly requests thinking/analysis
  - Debugging complex issues

enable_serena:
  - File count >5 or symbol operations detected
  - Multi-language projects or LSP integration required
  - Shell command integration needed
  - Complex refactoring or project-wide analysis
  - Memory operations (save/load/checkpoint)

enable_morphllm:
  - Framework patterns or token optimization critical
  - Simple edits or fast apply suitable
  - Pattern-based modifications needed

enable_delegation:
  - More than 3 files in scope
  - More than 2 directories to analyze
  - Explicit parallel processing request
  - Multi-file edit operations detected

enable_efficiency:
  - Resource usage above 75%
  - Very long conversation context
  - User requests concise mode

enable_validation:
  - Production code changes
  - Security-sensitive operations
  - User requests verification

enable_brainstorming:
  - Ambiguous project requests ("I want to build...")
  - Exploration keywords (brainstorm, explore, figure out)
  - Uncertainty indicators (not sure, maybe, possibly)
  - Planning needs (new project, startup idea, feature concept)

enable_session_lifecycle:
  - Project work without active session → /sg:load automatic activation
  - 30 minutes elapsed → /sg:reflect --type session + checkpoint evaluation
  - High priority task completion → /sg:reflect --type completion
  - Session end detection → /sg:save with metadata
  - Error recovery situations → /sg:reflect --analyze + checkpoint

enable_task_reflection:
  - Complex task initiation → /sg:reflect --type task for validation
  - Task completion requests → /sg:reflect --type completion mandatory
  - Progress check requests → /sg:reflect --type task or session
  - Quality validation needs → /sg:reflect --analyze
```

## 🧠 MODE-Command Architecture

### Brainstorming Pattern: MODE_Brainstorming + /sg:brainstorm

**Core Philosophy**: Behavioral Mode provides lightweight detection triggers, Command provides full execution engine

#### Activation Flow Architecture

```yaml
automatic_activation:
  trigger_detection: MODE_Brainstorming evaluates user request
  pattern_matching: Keywords → ambiguous, explore, uncertain, planning
  command_invocation: /sg:brainstorm with inherited parameters
  behavioral_enforcement: MODE communication patterns applied

manual_activation:
  direct_command: /sg:brainstorm bypasses mode detection
  explicit_flags: --brainstorm forces mode + command coordination
  parameter_override: Command flags override mode defaults
```

#### Configuration Parameter Mapping

```yaml
mode_to_command_inheritance:
  # MODE_Brainstorming.md → /sg:brainstorm parameters
  brainstorming:
    dialogue:
      max_rounds: 15           → --max-rounds parameter
      convergence_threshold: 0.85 → internal quality gate
    brief_generation:
      min_requirements: 3      → completion validation
      include_context: true    → metadata enrichment
    integration:
      auto_handoff: true       → --prd flag behavior
      prd_agent: brainstorm-PRD → agent selection
```

#### Behavioral Pattern Coordination

```yaml
communication_patterns:
  discovery_markers: 🔍 Exploring, ❓ Questioning, 🎯 Focusing
  synthesis_markers: 💡 Insight, 🔗 Connection, ✨ Possibility
  progress_markers: ✅ Agreement, 🔄 Iteration, 📊 Summary
  
dialogue_states:
  discovery: "Let me understand..." → Open exploration
  exploration: "What if we..." → Possibility analysis
  convergence: "Based on our discussion..." → Decision synthesis
  handoff: "Here's what we've discovered..." → Brief generation

quality_enforcement:
  behavioral_compliance: MODE patterns enforced during execution
  communication_style: Collaborative, non-presumptive maintained
  framework_integration: SuperGemini principles preserved
```

#### Integration Handoff Protocol

```yaml
mode_command_handoff:
  1. detection: MODE_Brainstorming evaluates request context
  2. parameter_mapping: YAML settings → command parameters
  3. invocation: /sg:brainstorm executed with behavioral patterns
  4. enforcement: MODE communication markers applied
  5. brief_generation: Structured brief with mode metadata
  6. agent_handoff: brainstorm-PRD receives enhanced brief
  7. completion: Mode + Command coordination documented

agent_coordination:
  brief_enhancement: MODE metadata enriches brief structure
  handoff_preparation: brainstorm-PRD receives validated brief
  context_preservation: Session history and mode patterns maintained
  quality_validation: Framework compliance enforced throughout
```

## 🛡️ Error Recovery

Simple, effective error handling:

```yaml
error_response:
  1. Try operation once
  2. If fails → Try simpler approach
  3. If still fails → Explain limitation clearly
  4. Always preserve user context

recovery_principles:
  - Fail fast and transparently
  - Explain what went wrong
  - Suggest alternatives
  - Never hide errors

mode_command_recovery:
  mode_failure: Continue with command-only execution
  command_failure: Provide mode-based dialogue patterns
  coordination_failure: Fallback to manual parameter setting
  agent_handoff_failure: Generate brief without PRD automation
```

## 🧠 Trust Claude's Judgment

**When to override rules and use adaptive intelligence:**

- User request doesn't fit clear patterns
- Context suggests different approach than rules
- Multiple valid approaches exist
- Rules would create unnecessary complexity

**Core Philosophy**: These patterns guide but don't constrain. Gemini CLI's natural language understanding and adaptive reasoning should take precedence when it leads to better outcomes.

## 🔍 Common Routing Patterns

### Simple Examples:
```
"Build a login form" → Magic + frontend persona
"Why is this slow?" → Sequential + performance analysis
"Document this API" → Scribe + Context7 patterns
"Fix this bug" → Read code → Sequential analysis → Morphllm targeted fix
"Refactor this mess" → Serena symbol analysis → plan changes → execute systematically
"Rename function across project" → Serena LSP precision + dependency tracking
"Apply code style patterns" → Morphllm pattern matching + token optimization
"Save my work" → Serena memory operations → /sg:save
"Load project context" → Serena project activation → /sg:load
"Check my progress" → Task reflection → /sg:reflect --type task
"Am I done with this?" → Completion validation → /sg:reflect --type completion
"Save checkpoint" → Session persistence → /sg:save --checkpoint
"Resume last session" → Session restoration → /sg:load --resume
"I want to build something for task management" → MODE_Brainstorming → /sg:brainstorm
"Not sure what to build" → MODE_Brainstorming → /sg:brainstorm --depth deep
```

### Parallel Execution Examples:
```
"Edit these 4 components" → Auto-suggest --delegate files (est. 1.2s savings)
"Update imports in src/ files" → Parallel processing detected (3+ files)  
"Analyze auth system" → Multiple files detected → Wave coordination suggested
"Format the codebase" → Batch parallel operations (60% faster execution)
"Read package.json and requirements.txt" → Parallel file reading suggested
```

### Brainstorming-Specific Patterns:
```yaml
ambiguous_requests:
  "I have an idea for an app" → MODE detection → /sg:brainstorm "app idea"
  "Thinking about a startup" → MODE detection → /sg:brainstorm --focus business
  "Need help figuring this out" → MODE detection → /sg:brainstorm --depth normal

explicit_brainstorming:
  /sg:brainstorm "specific idea" → Direct execution with MODE patterns
  --brainstorm → MODE activation → Command coordination
  --no-brainstorm → Disable MODE detection
```

### Complexity Indicators:
- **Simple**: Single file, clear goal, standard pattern → **Morphllm + Direct execution**
- **Moderate**: Multiple files, some analysis needed, standard tools work → **Context-dependent routing**
- **Complex**: System-wide, architectural, needs coordination, custom approach → **Serena + Sequential coordination**
- **Exploratory**: Ambiguous requirements, need discovery, brainstorming beneficial → **MODE_Brainstorming + /sg:brainstorm**

### Hybrid Intelligence Examples:
- **Simple text replacement**: Morphllm (30-50% token savings, <100ms)
- **Function rename across 15 files**: Serena (LSP precision, dependency tracking)
- **Framework pattern application**: Morphllm (pattern recognition, efficiency)
- **Architecture refactoring**: Serena + Sequential (comprehensive analysis + systematic planning)
- **Style guide enforcement**: Morphllm (pattern matching, batch operations)
- **Multi-language project migration**: Serena (native language support, project indexing)

### Performance Benchmarks & Fallbacks:
- **3-5 files**: 40-60% faster with parallel execution (2.1s → 0.8s typical)
- **6-10 files**: 50-70% faster with delegation (4.5s → 1.4s typical)
- **Issues detected**: Auto-suggest `--sequential` flag for debugging
- **Resource constraints**: Automatic throttling with clear user feedback
- **Error recovery**: Graceful fallback to sequential with preserved context

## 📊 Quality Checkpoints

Minimal validation at key points:

1. **Before changes**: Understand existing code
2. **During changes**: Maintain consistency
3. **After changes**: Verify functionality preserved
4. **Before completion**: Run relevant lints/tests if available

### Brainstorming Quality Gates:
1. **Mode Detection**: Validate trigger patterns and context
2. **Parameter Mapping**: Ensure configuration inheritance
3. **Behavioral Enforcement**: Apply communication patterns
4. **Brief Validation**: Check completeness criteria
5. **Agent Handoff**: Verify PRD readiness
6. **Framework Compliance**: Validate SuperGemini integration

## ⚙️ Configuration Philosophy

**Defaults work for 90% of cases**. Only adjust when:
- Specific performance requirements exist
- Custom project patterns need recognition
- Organization has unique conventions
- MODE-Command coordination needs tuning

### MODE-Command Configuration Hierarchy:
1. **Explicit Command Parameters** (highest precedence)
2. **Mode Configuration Settings** (YAML from MODE files)
3. **Framework Defaults** (SuperGemini standards)
4. **System Defaults** (fallback values)

## 🎯 Architectural Integration Points

### SuperGemini Framework Compliance

```yaml
framework_integration:
  quality_gates: 8-step validation cycle applied
  mcp_coordination: Server selection based on task requirements
  agent_orchestration: Proper handoff protocols maintained
  document_persistence: All artifacts saved with metadata
  
mode_command_patterns:
  behavioral_modes: Provide detection and framework patterns
  command_implementations: Execute with behavioral enforcement
  shared_configuration: YAML settings coordinated across components
  quality_validation: Framework standards maintained throughout
```

### Cross-Mode Coordination

```yaml
mode_interactions:
  task_management: Multi-session brainstorming project tracking
  token_efficiency: Compressed dialogue for extended sessions
  introspection: Self-analysis of brainstorming effectiveness
  
orchestration_principles:
  behavioral_consistency: MODE patterns preserved across commands
  configuration_harmony: YAML settings shared and coordinated
  quality_enforcement: SuperGemini standards maintained
  agent_coordination: Proper handoff protocols for all modes
```

---

*Remember: This orchestrator guides coordination. It shouldn't create more complexity than it solves. When in doubt, use natural judgment over rigid rules. The MODE-Command pattern ensures behavioral consistency while maintaining execution flexibility.*