# FLAGS.md - Gemini CLI Behavior Flags

Quick reference for flags that modify how I approach tasks. **Remember: These guide but don't constrain - I'll use judgment when patterns don't fit.**

## 🎯 Flag Categories

### MCP Server Flags
```yaml
--seq           # Enable Sequential for complex analysis
--c7            # Enable Context7 for documentation
--magic         # Enable Magic for UI components
--play          # Enable Playwright for testing
--morph         # Enable Morphllm for fast edits
--serena        # Enable Serena for semantic analysis
```

### Execution Control
```yaml
--plan          # Show what I'll do before starting
--validate      # Check risks before operations
--answer-only   # Skip automation, just respond directly
```

### Delegation & Parallelism
```yaml
--delegate [auto|files|folders]  # Split work across agents (auto-detects best approach)
--concurrency [n]                # Control parallel operations (default: 7)
```

### MCP Servers
```yaml
--all-mcp       # Enable all MCP servers (Context7, Sequential, Magic, Playwright, Morphllm, Serena)
--no-mcp        # Disable all MCP servers, use native tools
# Individual server flags: see MCP/*.md docs
```

### Scope & Focus
```yaml
--scope [file|module|project|system]         # Analysis scope
--focus [performance|security|quality|architecture|testing]  # Domain focus
```

### Iteration
```yaml
--loop          # Iterative improvement mode (default: 3 cycles)
--iterations n  # Set specific number of iterations
--interactive   # Pause for confirmation between iterations
```

## ⚡ Auto-Activation

I'll automatically enable appropriate flags when I detect:

```yaml
mcp_server_activation:
  complex_analysis → Sequential
  library_docs → Context7
  ui_components → Magic
  browser_testing → Playwright

parallel_work:
  many_files (>50) → --delegate auto
  many_dirs (>7) → --delegate folders

mcp_servers:
  ui_components → Magic
  library_docs → Context7
  complex_analysis → Sequential
  browser_testing → Playwright

safety:
  high_risk → --validate
  production_code → --validate
```

## 📋 Simple Precedence

When flags conflict, I follow this order:

1. **Your explicit flags** > auto-detection
2. **Safety** > performance  
3. **Deeper analysis** > shallow analysis
4. **Specific scope** > general scope
5. **--no-mcp** overrides individual server flags

## 💡 Common Patterns

Quick examples of flag combinations:

```
"analyze this architecture" → Sequential server (auto)
"build a login form" → Magic server (auto)
"fix this bug" → Sequential + focused analysis
"process entire codebase" → --delegate auto
"just explain this" → --answer-only
"make this code better" → --loop (auto)
```

## 🧠 Advanced Features

For complex scenarios, additional flags available:

- **Wave orchestration**: For enterprise-scale operations (see MODE_Task_Management.md)
- **Token efficiency**: Compression modes (see MODE_Token_Efficiency.md)
- **Introspection**: Self-analysis mode (see MODE_Introspection.md)

---

*These flags help me work more effectively, but my natural understanding of your needs takes precedence. When in doubt, I'll choose the approach that best serves your goal.*