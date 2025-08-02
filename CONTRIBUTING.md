# Contributing to SuperGemini Framework

Thanks for your interest in contributing! 🙏

SuperGemini is a community-driven project that enhances Gemini Code through modular hooks and intelligent orchestration. Every contribution helps make the framework more useful for developers.

## 🚀 Quick Start

### Prerequisites
- Python 3.12+ (standard library only)
- Node.js 18+ (for MCP servers)
- Gemini Code installed and authenticated

### Development Setup

```bash
# Clone the repository
git clone https://github.com/your-username/SuperGemini.git
cd SuperGemini

# Install SuperGemini
./install.sh --standard

# Run tests
python Tests/comprehensive_test.py
```

## 🎯 Ways to Contribute

### 🐛 Bug Reports
- Use GitHub Issues with the "bug" label
- Include system info (OS, Python/Node versions)
- Provide minimal reproduction steps
- Include relevant hook logs from `~/.gemini/`

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
- Focus on hooks, commands, or core framework components
- Follow existing patterns and conventions
- Include tests for new functionality
- Update documentation as needed

## 🏗️ Architecture Overview

### Core Components
```
SuperGemini/
├── SuperGemini/
│   ├── Hooks/          # 15 Python hooks (main extension points)
│   ├── Commands/       # 14 slash commands
│   ├── Core/          # Framework documentation
│   └── Settings/      # Configuration files
├── Scripts/           # Installation and utility scripts
└── Tests/            # Test suite
```

### Hook System
Hooks are the primary extension mechanism:
- **PreToolUse**: Intercept before tool execution
- **PostToolUse**: Process after tool completion  
- **SubagentStop**: Handle sub-agent lifecycle
- **Stop**: Session cleanup and synthesis
- **Notification**: Real-time event processing

## 🧪 Testing

### Running Tests
```bash
# Full test suite
python Tests/comprehensive_test.py

# Specific components
python Tests/task_management_test.py
python Tests/performance_test_suite.py

# Hook integration tests
python SuperGemini/Hooks/test_orchestration_integration.py
```

### Writing Tests
- Test hook behavior with mock data
- Include performance benchmarks
- Test error conditions and recovery
- Validate cross-component integration

## 📋 Code Standards

### Python Code (Hooks)
```python
#!/usr/bin/env python3
"""
Brief description of hook purpose.
Part of SuperGemini Framework v3.0
"""

import json
import sys
from typing import Dict, Any

def process_hook_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Process hook data with proper error handling."""
    try:
        # Implementation here
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # Standard hook entry point
    input_data = json.loads(sys.stdin.read())
    result = process_hook_data(input_data)
    print(json.dumps(result))
```

### Documentation (Markdown)
- Use clear headings and structure
- Include code examples where helpful
- Add emoji sparingly for clarity 🎯
- Keep language humble and developer-focused

### Commit Messages
```
type(scope): brief description

Longer explanation if needed.

- Specific changes made
- Why the change was needed
- Any breaking changes noted
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `chore`

## 🔄 Development Workflow

### 1. Fork & Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Develop & Test
- Make focused, atomic changes
- Test locally with `--standard` installation
- Ensure hooks don't break existing functionality

### 3. Submit Pull Request
- Clear title and description
- Reference related issues
- Include test results
- Update documentation if needed

### 4. Code Review
- Address feedback promptly
- Keep discussions focused and respectful
- Be open to suggestions and improvements

## 📦 Release Process

### Version Management
- Follow [Semantic Versioning](https://semver.org/)
- Update `VERSION` file
- Document changes in `CHANGELOG.md`
- Tag releases: `git tag v3.0.1`

### Release Checklist
- [ ] All tests pass
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped
- [ ] Installation tested on clean system

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

**Q: How do I debug hook execution?**
A: Check logs in `~/.gemini/` and use verbose logging for detailed output.

**Q: Can I add new MCP servers?**
A: Yes! Follow the pattern in `settings.json` and add integration hooks.

**Q: How do I test changes without affecting my global setup?**
A: Use a separate test environment or backup your `~/.gemini` directory before testing.

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Acknowledgments

Thanks to all contributors who help make SuperGemini better for the development community!