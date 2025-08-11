# Migration Guide: SuperClaude to SuperGemini

## Overview

SuperGemini is a fork of SuperClaude v3 adapted for Google's Gemini Code environment. Since Gemini doesn't support Task agents or sub-agent delegation features, certain functionalities have been removed or modified.

## Breaking Changes

### 1. Removed Features

#### Task Agents and Sub-Agent Delegation
- **What**: All Task agent and sub-agent delegation capabilities
- **Why**: Gemini doesn't support agent spawning or delegation
- **Migration**: Use Wave orchestration for complex multi-stage operations

#### `/spawn` Command
- **What**: The entire `/spawn` command for complex orchestration
- **Why**: Depends on agent orchestration not available in Gemini
- **Migration**: Use `/task` with wave modes for complex workflows

### 2. Modified Features

#### Delegation Flags
**Before (SuperClaude):**
```bash
/sg:analyze large-project/ --delegate auto
/sg:analyze monorepo/ --delegate folders
```

**After (SuperGemini):**
```bash
/sg:analyze large-project/ --wave-mode auto
/sg:analyze monorepo/ --wave-strategy systematic
```

#### Wave Orchestration
- Wave functionality remains but without delegation components
- Use `--wave-mode` and `--wave-strategy` for multi-stage processing
- All wave strategies work independently without sub-agents

## Migration Strategies

### For Large-Scale Analysis

**SuperClaude approach:**
```bash
/sg:analyze huge-codebase/ --delegate auto --concurrency 5
```

**SuperGemini approach:**
```bash
/sg:analyze huge-codebase/ --wave-mode force --wave-strategy systematic
```

### For Complex Operations

**SuperClaude approach:**
```bash
/sg:spawn deploy-pipeline --parallel
/sg:task execute --delegate
```

**SuperGemini approach:**
```bash
/sg:task execute --wave-mode auto
/sg:workflow deploy-pipeline --wave-strategy progressive
```

### For Performance Optimization

**SuperClaude approach:**
```bash
/sg:improve system/ --delegate folders --uc
```

**SuperGemini approach:**
```bash
/sg:improve system/ --wave-mode auto --uc
```

## Features That Remain Unchanged

### Fully Functional Components
- ✅ All 11 personas (architect, frontend, backend, etc.)
- ✅ 16 commands (all except `/spawn`)
- ✅ MCP server integrations (Context7, Sequential, Magic, Playwright)
- ✅ TodoWrite for task management
- ✅ Sequential thinking for analysis
- ✅ Token optimization (`--uc` flag)
- ✅ Introspection mode
- ✅ All focus and scope flags

### Wave Strategies Still Available
- `progressive` - Iterative enhancement
- `systematic` - Methodical analysis
- `adaptive` - Dynamic configuration
- `enterprise` - Large-scale orchestration

## Quick Reference

| SuperClaude Flag | SuperGemini Alternative | Purpose |
|-----------------|------------------------|---------|
| `--delegate auto` | `--wave-mode auto` | Automatic complexity handling |
| `--delegate folders` | `--wave-strategy systematic` | Systematic processing |
| `--delegate files` | `--wave-strategy progressive` | File-by-file processing |
| `--concurrency N` | (removed) | No parallel agents in Gemini |
| `/spawn` command | Use `/task` or `/workflow` | Complex orchestration |

## Troubleshooting

### "Command not found: /spawn"
The `/spawn` command has been removed. Use `/task` for project management or `/workflow` for complex workflows.

### "Unknown flag: --delegate"
Replace with `--wave-mode` or `--wave-strategy` depending on your use case.

### Performance Issues Without Delegation
- Use `--uc` flag for token optimization
- Apply `--wave-mode force` for systematic processing
- Consider breaking large operations into smaller chunks

## Support

For questions or issues with the migration:
1. Check this guide first
2. Review the updated CHANGELOG.md
3. Consult the modified documentation in the Docs/ folder
4. Open an issue in the SuperGemini repository

## Version Information

- Last SuperClaude version: 3.1.4
- First SuperGemini version: 4.0.0-beta
- Migration date: 2025-08-11