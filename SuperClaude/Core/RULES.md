# RULES.md - SuperGemini Framework Actionable Rules

Simple actionable rules for Gemini CLI SuperGemini framework operation.

## Core Operational Rules

### Task Management Rules
- TodoRead() → TodoWrite(3+ tasks) → Execute → Track progress
- Use batch tool calls when possible, sequential only when dependencies exist
- Always validate before execution, verify after completion
- Run lint/typecheck before marking tasks complete
- Use /spawn and /task for complex multi-session workflows
- Maintain ≥90% context retention across operations

### File Operation Security
- Always use Read tool before Write or Edit operations
- Use absolute paths only, prevent path traversal attacks
- Prefer batch operations and transaction-like behavior
- Never commit automatically unless explicitly requested

### Framework Compliance
- Check package.json/pyproject.toml before using libraries
- Follow existing project patterns and conventions
- Use project's existing import styles and organization
- Respect framework lifecycles and best practices

### Systematic Codebase Changes
- **MANDATORY**: Complete project-wide discovery before any changes
- Search ALL file types for ALL variations of target terms
- Document all references with context and impact assessment
- Plan update sequence based on dependencies and relationships
- Execute changes in coordinated manner following plan
- Verify completion with comprehensive post-change search
- Validate related functionality remains working
- Use systematic approach for comprehensive searches when scope uncertain

### Knowledge Management Rules
- **Check Serena memories first**: Search for relevant previous work before starting new operations
- **Build upon existing work**: Reference and extend Serena memory entries when applicable
- **Update with new insights**: Enhance Serena memories when discoveries emerge during operations
- **Cross-reference related content**: Link to relevant Serena memory entries in new documents
- **Leverage knowledge patterns**: Use established patterns from similar previous operations
- **Maintain knowledge network**: Ensure memory relationships reflect actual operation dependencies

### Session Lifecycle Rules
- **Always use /sg:load**: Initialize every project session via /sg:load command with Serena activation
- **Session metadata**: Create and maintain session metadata using Template_Session_Metadata.md structure
- **Automatic checkpoints**: Trigger checkpoints based on time (30min), task completion (high priority), or risk level
- **Performance monitoring**: Track and record all operation timings against PRD targets (<200ms memory, <500ms load)
- **Session persistence**: Use /sg:save regularly and always before session end
- **Context continuity**: Maintain ≥90% context retention across checkpoints and session boundaries

### Task Reflection Rules (Serena Integration)
- **Replace TodoWrite patterns**: Use Serena reflection tools for task validation and progress tracking
- **think_about_task_adherence**: Call before major task execution to validate approach
- **think_about_collected_information**: Use for session analysis and checkpoint decisions
- **think_about_whether_you_are_done**: Mandatory before marking complex tasks complete
- **Session-task linking**: Connect task outcomes to session metadata for continuous learning

## Quick Reference

### Do
✅ Initialize sessions with /sg:load (Serena activation required)
✅ Read before Write/Edit/Update
✅ Use absolute paths and UTC timestamps
✅ Batch tool calls when possible
✅ Validate before execution using Serena reflection tools
✅ Check framework compatibility
✅ Track performance against PRD targets (<200ms memory ops)
✅ Trigger automatic checkpoints (30min/high-priority tasks/risk)
✅ Preserve context across operations (≥90% retention)
✅ Use quality gates (see ORCHESTRATOR.md)
✅ Complete discovery before codebase changes
✅ Verify completion with evidence
✅ Check Serena memories for relevant previous work
✅ Build upon existing Serena memory entries
✅ Cross-reference related Serena memory content
✅ Use session metadata template for all sessions
✅ Call /sg:save before session end

### Don't
❌ Start work without /sg:load project activation
❌ Skip Read operations or Serena memory checks
❌ Use relative paths or non-UTC timestamps
❌ Auto-commit without permission
❌ Ignore framework patterns or session lifecycle
❌ Skip validation steps or reflection tools
❌ Mix user-facing content in config
❌ Override safety protocols or performance targets
❌ Make reactive codebase changes without checkpoints
❌ Mark complete without Serena think_about_whether_you_are_done
❌ Start operations without checking Serena memories
❌ Ignore existing relevant Serena memory entries
❌ Create duplicate work when Serena memories exist
❌ End sessions without /sg:save
❌ Use TodoWrite without Serena integration patterns

### Auto-Triggers
- Wave mode: complexity ≥0.4 + multiple domains + >3 files
- Sub-agent delegation: >3 files OR >2 directories OR complexity >0.4
- Gemini CLI agents: automatic delegation based on task context  
- MCP servers: task type + performance requirements
- Quality gates: all operations apply 8-step validation
- Parallel suggestions: Multi-file operations with performance estimates