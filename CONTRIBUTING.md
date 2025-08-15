# Contributing to SuperGemini Framework

Thanks for your interest in contributing! 🙏

SuperGemini is a community-driven project that enhances Gemini CLI through modular hooks, intelligent orchestration, specialized agents, and behavioral modes. Every contribution helps make the framework more useful for developers.

## 🚀 Quick Start

### Prerequisites
- Python 3.12+ (standard library only)
- Node.js 18+ (for MCP servers)
- Gemini CLI installed and authenticated
- uv package manager (recommended for development)

### Development Setup

```bash
# Clone the repository
git clone https://github.com/SuperClaude-Org/SuperGemini_Framework.git
cd SuperGemini_Framework

# Install dependencies with uv
uv sync

# Install SuperGemini V4 Beta
python -m pip install -e .

# Run tests
python Tests/comprehensive_test.py
python Tests/v4_integration_test.py
```

## 🎯 Ways to Contribute

### 🐛 Bug Reports
- Use GitHub Issues with the "bug" label
- Include system info (OS, Python/Node versions)
- Provide minimal reproduction steps
- Include relevant hook logs from `~/.claude/`

### 💡 Feature Requests
- Check existing issues and roadmap first
- Use GitHub Issues with the "enhancement" label
- Describe the use case and expected behavior
- Consider if it fits the framework's modular philosophy

### 📝 Documentation
- Fix typos or unclear explanations
- Add examples and use cases
- Improve installation guides
- Translate documentation (especially for Scribe persona)

### 🔧 Code Contributions
- Focus on hooks, commands, agents, modes, or core framework components
- Follow existing patterns and conventions
- Include tests for new functionality
- Update documentation as needed

### 🤖 Agents & Modes
- Create specialized agents for domain expertise
- Develop behavioral modes for enhanced workflow patterns
- Ensure proper integration with MCP servers
- Follow the SuperGemini orchestration principles

## 🏗️ Architecture Overview

### Core Components
```
SuperGemini_Framework/
├── SuperGemini/
│   ├── Agents/         # 13 specialized domain agents
│   ├── Commands/       # 21 slash commands (/sg:load, /sg:save, etc.)
│   ├── Core/          # Framework documentation and rules
│   ├── Config/        # Configuration management
│   ├── Hooks/         # 22+ Python hooks (main extension points)
│   ├── MCP/           # 6 MCP server integrations
│   └── Modes/         # 4 behavioral modes
├── SuperGemini-Lite/  # Lightweight framework variant
├── Templates/         # Document and code templates
└── Tests/            # Comprehensive test suite
```

### V4 Beta Architecture

#### Agents System
Domain-specialized agents for expert capabilities:
- **system-architect.md**: System design and architecture
- **performance-optimizer.md**: Performance analysis and optimization
- **security-auditor.md**: Security assessment and hardening
- **frontend-specialist.md**: UI/UX and frontend development

#### Modes System
Behavioral modes that modify Claude's operational approach:
- **MODE_Task_Management.md**: Multi-layer task orchestration
- **MODE_Token_Efficiency.md**: Intelligent compression and optimization
- **MODE_Introspection.md**: Meta-cognitive analysis and troubleshooting

#### MCP Integration
Advanced server coordination for enhanced capabilities:
- **MCP_Serena.md**: Semantic code analysis and memory management
- **MCP_Sequential.md**: Multi-step problem solving
- **MCP_Magic.md**: UI component generation
- **MCP_Context7.md**: Library documentation lookup
- **MCP_Morphllm.md**: Intelligent file editing
- **MCP_Playwright.md**: Browser automation and testing

#### Hook System
Enhanced hooks with session lifecycle and performance monitoring:
- **Session Lifecycle**: Load, checkpoint, save operations
- **Performance Monitoring**: Real-time metrics and optimization
- **Quality Gates**: 8-step validation framework
- **Framework Coordination**: Agent and mode orchestration

## 🧪 Testing

### Running Tests
```bash
# Full V4 test suite
python Tests/comprehensive_test.py
python Tests/v4_integration_test.py

# Component-specific tests
python Tests/agent_system_test.py
python Tests/mode_coordination_test.py
python Tests/mcp_integration_test.py
python Tests/session_lifecycle_test.py

# Hook integration tests
python SuperGemini/Hooks/test_orchestration_integration.py
python SuperGemini/Hooks/test_session_lifecycle.py
python SuperGemini/Hooks/test_performance_monitoring.py
```

### Writing Tests
- Test hook behavior with mock data and session context
- Include performance benchmarks for V4 features
- Test error conditions and recovery mechanisms
- Validate cross-component integration (agents, modes, MCP)
- Test session lifecycle operations (/sg:load, /sg:save)
- Validate mode coordination and behavioral patterns

## 📋 Code Standards

### Python Code (Hooks)
```python
#!/usr/bin/env python3
"""
Brief description of hook purpose.
Part of SuperGemini Framework V4 Beta
"""

import json
import sys
from typing import Dict, Any, Optional
from pathlib import Path

def process_hook_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Process hook data with V4 session lifecycle support."""
    try:
        # V4 features: session context, performance metrics
        session_id = data.get('session_id')
        context = data.get('context', {})
        
        # Implementation here with V4 patterns
        result = {
            "status": "success",
            "data": result_data,
            "session_id": session_id,
            "metrics": {"execution_time_ms": elapsed_time}
        }
        return result
    except Exception as e:
        return {
            "status": "error", 
            "message": str(e),
            "session_id": data.get('session_id')
        }

if __name__ == "__main__":
    # V4 standard hook entry point with session support
    input_data = json.loads(sys.stdin.read())
    result = process_hook_data(input_data)
    print(json.dumps(result))
```

### Agent Documentation (Markdown)
```markdown
---
name: agent-name
description: "Brief description of agent's domain expertise"
type: domain-specialist
category: [architecture|performance|security|frontend|backend]
complexity: [basic|standard|advanced|expert]
scope: [module|system|enterprise]

# Integration Configuration
framework-integration:
  mcp-servers: [serena, sequential, context7]
  commands: [relevant-commands]
  modes: [relevant-modes]
  quality-gates: [relevant-validation-steps]

# Performance Profile
performance-profile: [lightweight|standard|intensive]
---

# Agent Name

**Domain expertise description** with specific capabilities.

## Core Capabilities
- Specific technical expertise
- Domain-specific analysis
- Integration patterns

## Integration Points
- MCP server coordination
- Command workflows
- Mode interactions
```

### Mode Documentation (YAML + Markdown)
```markdown
---
name: mode-name
description: "Behavioral modification description"
type: behavioral

# Mode Classification
category: [orchestration|optimization|analysis]
complexity: [basic|standard|advanced]
scope: [session|project|framework]

# Activation Configuration
activation:
  automatic: true
  manual-flags: ["--flag"]
  confidence-threshold: 0.7
  detection-patterns: ["pattern keywords"]

# Integration Configuration
framework-integration:
  mcp-servers: [relevant-servers]
  commands: [relevant-commands]
  modes: [coordinated-modes]
  quality-gates: [validation-steps]

# Performance Profile
performance-profile: [lightweight|standard|intensive]
---

# Mode Name

Mode description and behavioral patterns.
```

### Documentation (Markdown)
- Use clear headings and structure with V4 component organization
- Include code examples for agents, modes, and MCP integration
- Add emoji sparingly for clarity 🎯
- Keep language humble and developer-focused
- Follow YAML frontmatter standards for agents and modes
- Document integration points and behavioral patterns

### Commit Messages
```
type(scope): brief description

Longer explanation if needed.

- Specific changes made
- Why the change was needed
- Any breaking changes noted
- V4 component impacts (agents, modes, hooks)
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `chore`
Scopes: `agents`, `modes`, `hooks`, `mcp`, `core`, `commands`, `lifecycle`

## 🔄 Development Workflow

### 1. Fork & Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Develop & Test
- Make focused, atomic changes aligned with V4 architecture
- Test locally with V4 Beta installation (`python -m pip install -e .`)
- Ensure hooks, agents, and modes don't break existing functionality
- Test session lifecycle operations (/sg:load, /sg:save)
- Validate MCP server integration and coordination

### 3. Submit Pull Request
- Clear title and description with V4 component impact
- Reference related issues and architectural decisions
- Include test results for affected components (agents, modes, hooks)
- Update documentation for new features and integration points
- Demonstrate compatibility with existing V4 systems

### 4. Code Review
- Address feedback promptly
- Keep discussions focused and respectful
- Be open to suggestions and improvements

## 📦 Release Process

### Version Management
- Follow [Semantic Versioning](https://semver.org/)
- Update `VERSION` file and `pyproject.toml`
- Document changes in `CHANGELOG.md` with V4 component impacts
- Tag releases: `git tag v4.0.0-beta.1`
- Consider V4 Beta stability and migration path

### Release Checklist
- [ ] All V4 tests pass (comprehensive, integration, component-specific)
- [ ] Documentation updated for new agents, modes, and features
- [ ] CHANGELOG.md updated with V4 component changes
- [ ] Version bumped in `VERSION` and `pyproject.toml`
- [ ] V4 Beta installation tested on clean system
- [ ] Session lifecycle operations validated
- [ ] MCP server coordination tested
- [ ] Agent and mode integration verified

## 🤝 Community Guidelines

### Be Respectful
- Welcome newcomers and different experience levels
- Focus on the code and ideas, not personal attributes
- Help others learn and improve

### Stay Focused
- Keep discussions relevant to SuperGemini's goals
- Avoid scope creep in feature requests
- Consider if changes fit the modular philosophy

### Quality First
- Test your changes thoroughly
- Consider performance impact
- Think about maintainability

## 💬 Getting Help

### Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Documentation**: Check existing guides first

### Common Questions

**Q: How do I debug V4 hook execution and session lifecycle?**
A: Check logs in `~/.claude/` and use verbose logging. Monitor session state with `/sg:load` and `/sg:save` operations.

**Q: Can I add new MCP servers or agents?**
A: Yes! Follow the patterns in `SuperGemini/MCP/` for servers and `SuperGemini/Agents/` for domain specialists. Include proper YAML frontmatter and integration points.

**Q: How do I test V4 changes without affecting my global setup?**
A: Use a separate test environment with `python -m pip install -e .` for development installation. Backup your `~/.claude` directory and test session operations.

**Q: How do I create a new behavioral mode?**
A: Follow the pattern in `SuperGemini/Modes/` with proper YAML frontmatter, activation patterns, and framework integration configuration.

**Q: What's the difference between agents and modes?**
A: Agents provide domain expertise (system-architect, performance-optimizer), while modes modify Claude's behavioral approach (task management, token efficiency, introspection).

## 🚀 Contributing to V4 Components

### Creating New Agents
1. **Domain Research**: Identify specific expertise area and common patterns
2. **Template Usage**: Use existing agents as templates (e.g., `system-architect.md`)
3. **YAML Configuration**: Include proper frontmatter with integration points
4. **Capability Documentation**: Define core capabilities and integration patterns
5. **Testing**: Create agent-specific tests and validate MCP coordination

### Developing Behavioral Modes
1. **Behavioral Analysis**: Define how the mode modifies Claude's approach
2. **Activation Patterns**: Specify automatic and manual triggers
3. **Framework Integration**: Document MCP servers, commands, and quality gates
4. **Performance Profiling**: Define lightweight/standard/intensive characteristics
5. **Mode Coordination**: Ensure compatibility with existing modes

### Enhancing Session Lifecycle
1. **Hook Integration**: Understand session lifecycle hooks and patterns
2. **Performance Targets**: Meet <500ms load times and <200ms memory operations
3. **Context Management**: Implement proper session state preservation
4. **Error Recovery**: Handle checkpoint failures and session restoration
5. **Memory Optimization**: Follow selective compression patterns

### MCP Server Integration
1. **Server Capabilities**: Understand server specializations and coordination
2. **Performance Benchmarks**: Meet server-specific performance targets
3. **Fallback Strategies**: Implement graceful degradation patterns
4. **Quality Gates**: Integrate with validation frameworks
5. **Cross-Server Coordination**: Enable hybrid intelligence patterns

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Acknowledgments

Thanks to all contributors who help make SuperGemini V4 Beta better for the development community! Special recognition for those contributing to the new agents system, behavioral modes, session lifecycle, and MCP server coordination that make V4's intelligent orchestration possible.