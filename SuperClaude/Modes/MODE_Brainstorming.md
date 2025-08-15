---
name: brainstorming
description: "Behavioral trigger for interactive requirements discovery"
type: command-integrated

# Mode Classification
category: orchestration
complexity: standard
scope: cross-session

# Activation Configuration
activation:
  automatic: true
  manual-flags: ["--brainstorm", "--bs"]
  confidence-threshold: 0.7
  detection-patterns: ["vague project requests", "exploration keywords", "uncertainty indicators", "PRD prerequisites", "interactive discovery needs"]

# Integration Configuration
framework-integration:
  mcp-servers: [sequential-thinking, context7, magic]
  commands: ["/sg:brainstorm"]
  modes: [task_management, token_efficiency, introspection]
  quality-gates: [requirements_clarity, brief_completeness, mode_coordination]

# Performance Profile
performance-profile: standard
---

# Brainstorming Mode

**Behavioral trigger for interactive requirements discovery** - Activates when Claude detects uncertainty or exploration needs.

## Purpose

Lightweight behavioral mode that triggers the `/sg:brainstorm` command when users need help discovering requirements through dialogue.

## Auto-Activation Patterns

Brainstorming Mode activates when detecting:

1. **Vague Project Requests**: "I want to build something that...", "Thinking about creating..."
2. **Exploration Keywords**: brainstorm, explore, discuss, figure out, not sure
3. **Uncertainty Indicators**: "maybe", "possibly", "thinking about", "could we"
4. **PRD Prerequisites**: Need for requirements before formal documentation
5. **Interactive Discovery**: Context benefits from dialogue-based exploration

## Manual Activation
- **Flags**: `--brainstorm` or `--bs`
- **Disable**: `--no-brainstorm`

## Mode Configuration

```yaml
brainstorming_mode:
  activation:
    automatic: true
    confidence_threshold: 0.7
    detection_patterns:
      vague_requests: ["want to build", "thinking about", "not sure"]
      exploration_keywords: [brainstorm, explore, discuss, figure_out]
      uncertainty_indicators: [maybe, possibly, could_we]
  
  behavioral_settings:
    dialogue_style: collaborative_non_presumptive
    discovery_depth: adaptive
    context_retention: cross_session
    handoff_automation: true
```

## Command Integration

This mode triggers `/sg:brainstorm` which handles:
- Socratic dialogue execution
- Brief generation
- PRD handoff
- Session persistence

See `/sg:brainstorm` command documentation for implementation details.

## Related Documentation

- **Command Implementation**: /sg:brainstorm
- **Agent Integration**: brainstorm-PRD
- **Framework Reference**: ORCHESTRATOR.md