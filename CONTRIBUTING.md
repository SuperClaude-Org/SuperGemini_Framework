# Contributing to SuperGemini Framework

Thanks for your interest in contributing! 🙏

SuperClaude is a community-driven project that enhances Claude Code through intelligent orchestration, specialized agents, and behavioral modes. Every contribution helps make the framework more useful for developers.

## 🚀 Quick Start

### Prerequisites
- Python 3.12+ (standard library only)
- Node.js 18+ (for MCP servers)
- Gemini CLI installed and authenticated
- uv package manager (recommended for development)

### Development Setup

```bash
# Clone the repository
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework

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
- Include relevant logs from `~/.claude/`

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
- Focus on commands, agents, modes, or core framework components
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
│   ├── MCP/           # 6 MCP server integrations
│   └── Modes/         # 5 behavioral modes
├── Guides/           # User guides and documentation
└── Tests/            # Comprehensive test suite
```

### V4 Beta Architecture

#### Agents System
Domain-specialized agents for expert capabilities:
- **system-architect.md**: System design and architecture
- **performance-engineer.md**: Performance analysis and optimization
- **security-engineer.md**: Security assessment and hardening
- **frontend-architect.md**: UI/UX and frontend development
- **requirements-analyst.md**: Requirements discovery and analysis

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

## 📝 Contribution Guidelines

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
- V4 component impacts (agents, modes, core components)
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `chore`
Scopes: `agents`, `modes`, `mcp`, `core`, `commands`, `lifecycle`

## 🔄 Development Workflow

### 1. Fork & Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Develop & Test
- Make focused, atomic changes aligned with V4 architecture
- Test locally with V4 Beta installation (`python -m pip install -e .`)
- Ensure agents and modes don't break existing functionality
- Test session lifecycle operations (/sc:load, /sc:save)
- Validate MCP server integration and coordination

### 3. Submit Pull Request
- Clear title and description with V4 component impact
- Reference related issues and architectural decisions
- Include test results for affected components (agents, modes, framework)
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

**Q: How do I debug V4 framework execution and session lifecycle?**
A: Check logs in `~/.claude/` and use verbose logging. Monitor session state with `/sc:load` and `/sc:save` operations.

**Q: Can I add new MCP servers or agents?**
A: Yes! Follow the patterns in `SuperGemini/MCP/` for servers and `SuperGemini/Agents/` for domain specialists. Include proper YAML frontmatter and integration points.

**Q: How do I test V4 changes without affecting my global setup?**
A: Use a separate test environment with `python -m pip install -e .` for development installation. Backup your `~/.claude` directory and test session operations.

**Q: How do I create a new behavioral mode?**
A: Follow the pattern in `SuperGemini/Modes/` with proper YAML frontmatter, activation patterns, and framework integration configuration.

**Q: What's the difference between agents and modes?**
A: Agents provide domain expertise (system-architect, performance-engineer), while modes modify Claude's behavioral approach (brainstorming, task management, token efficiency).

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
1. **Framework Integration**: Understand session lifecycle patterns
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