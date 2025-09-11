# SuperGemini Framework Flags

Behavioral flags for Gemini CLI to enable specific execution modes and tool selection patterns.

## Mode Activation Flags

****
- Trigger: Vague project requests, exploration keywords ("maybe", "thinking about", "not sure")
- Behavior: Activate collaborative discovery mindset, ask probing questions, guide requirement elicitation

**--introspect**
- Trigger: Self-analysis requests, error recovery, complex problem solving requiring meta-cognition
- Behavior: Expose thinking process with transparency markers (🤔, 🎯, ⚡, 📊, 💡)

**--task-manage**
- Trigger: Multi-step operations (>3 steps), complex scope (>2 directories OR >3 files)
- Behavior: Orchestrate through systematic organization and progressive enhancement

**--orchestrate**
- Trigger: Multi-tool operations, performance constraints, optimization opportunities
- Behavior: Optimize tool selection matrix, sequential execution planning, adapt to resource constraints

**--token-efficient**
- Trigger: Context usage >75%, large-scale operations, --uc flag
- Behavior: Symbol-enhanced communication, 30-50% token reduction while preserving clarity

## MCP Server Flags

**--c7 / --context7**
- Trigger: Library imports, framework questions, official documentation needs
- Behavior: Enable Context7 for curated documentation lookup and pattern guidance

**--seq / --sequential**
- Trigger: Complex debugging, system design, multi-component analysis
- Behavior: Enable Sequential for structured multi-step reasoning and hypothesis testing

**--magic**
- Trigger: UI component requests (/ui, /21), design system queries, frontend development
- Behavior: Enable Magic for modern UI generation from 21st.dev patterns

**--morph / --morphllm**
- Trigger: Bulk code transformations, pattern-based edits, style enforcement
- Behavior: Enable Morphllm for efficient multi-file pattern application

**--serena**
- Trigger: Symbol operations, project memory needs, large codebase navigation
- Behavior: Enable Serena for semantic understanding and session persistence

**--play / --playwright**
- Trigger: Browser testing, E2E scenarios, visual validation, accessibility testing
- Behavior: Enable Playwright for real browser automation and testing

**--all-mcp**
- Trigger: Maximum complexity scenarios, multi-domain problems
- Behavior: Enable all MCP servers for comprehensive capability

**--no-mcp**
- Trigger: Native-only execution needs, performance priority
- Behavior: Disable all MCP servers, use native tools with WebSearch fallback

## Execution Control Flags

**--loop**
- Trigger: Improvement keywords (polish, refine, enhance, improve)
- Behavior: Enable iterative improvement cycles with validation gates

**--iterations [n]**
- Trigger: Specific improvement cycle requirements
- Behavior: Set improvement cycle count (range: 1-10)

**--validate**
- Trigger: Risk score >0.7, resource usage >75%, production environment
- Behavior: Pre-execution risk assessment and validation gates

**--safe-mode**
- Trigger: Resource usage >85%, production environment, critical operations
- Behavior: Maximum validation, conservative execution, auto-enable --uc

## Output Optimization Flags

**--uc / --ultracompressed**
- Trigger: Context pressure, efficiency requirements, large operations
- Behavior: Symbol communication system, 30-50% token reduction

**--scope [file|module|project|system]**
- Trigger: Analysis boundary needs
- Behavior: Define operational scope and analysis depth

**--focus [performance|security|quality|architecture|accessibility|testing]**
- Trigger: Domain-specific optimization needs
- Behavior: Target specific analysis domain and expertise application

## Flag Priority Rules

**Safety First**: --safe-mode > --validate > optimization flags
**Explicit Override**: User flags > auto-detection
**MCP Control**: --no-mcp overrides all individual MCP flags
**Scope Precedence**: system > project > module > file