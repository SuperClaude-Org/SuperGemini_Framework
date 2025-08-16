# Changelog

All notable changes to SuperGemini will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- **BREAKING**: Commands now use `/sg:` namespace to avoid conflicts with user custom commands
- Commands are now installed in `~/.claude/commands/sc/` subdirectory
- All 16 commands updated: `/analyze` � `/sg:analyze`, `/build` � `/sg:build`, etc.
- Automatic migration from old command locations to new `sc/` subdirectory
- **BREAKING**: Documentation reorganization - Docs/ directory renamed to Guides/

### Added
- **NEW COMMAND**: `/sg:implement` for feature and code implementation (addresses v2 user feedback)
- Migration logic to move existing commands to new namespace automatically
- Enhanced uninstaller to handle both old and new command locations
- Improved command conflict prevention
- Better command organization and discoverability
- Comprehensive PyPI publishing infrastructure
- API key management during SuperClaude MCP setup

### Removed
- **BREAKING**: Removed Templates/ directory (legacy templates no longer needed)
- **BREAKING**: Removed legacy agents and replaced with enhanced 13-agent system

### Improved
- Refactored Modes and MCP documentation for concise behavioral guidance
- Enhanced project cleanup and gitignore for PyPI publishing
- Implemented uninstall and update safety enhancements
- Better agent specialization and domain expertise focus

### Technical Details
- Commands now accessible as `/sg:analyze`, `/sg:build`, `/sg:improve`, etc.
- Migration preserves existing functionality while preventing naming conflicts
- Installation process detects and migrates existing commands automatically
- Tab completion support for `/sg:` prefix to discover all SuperGemini commands

## [4.0.0-beta.1] - 2025-02-05

### Added
- **Agent System**: 13 specialized domain experts replacing personas
- **Behavioral Modes**: 3 intelligent modes for different workflows (Introspection, Task Management, Token Efficiency)
- **Session Lifecycle**: /sg:load and /sg:save for cross-session persistence with Serena MCP
- **New Commands**: /sg:reflect, /sg:save, /sg:select-tool (20 total commands)
- **Serena MCP**: Semantic code analysis and memory management
- **Morphllm MCP**: Intelligent file editing with Fast Apply capability
- **Hooks System**: Python-based framework integration (completely redesigned and implemented)
- **SuperGemini-Lite**: Minimal implementation with YAML configuration
- **Templates**: Comprehensive templates for creating new components
- **Python-Ultimate-Expert Agent**: Master Python architect for production-ready code

### Changed
- Commands expanded from 16 to 21 specialized commands
- Personas replaced with 13 specialized Agents
- Enhanced MCP integration (6 servers total)
- Improved token efficiency (30-50% reduction with Token Efficiency Mode)
- Session management now uses Serena integration for persistence
- Framework structure reorganized for better modularity

### Improved
- Task management with multi-layer orchestration (TodoWrite, /task, /spawn, /loop)
- Quality gates with 8-step validation cycle
- Performance monitoring and optimization
- Cross-session context preservation
- Intelligent routing with ORCHESTRATOR.md enhancements

## [3.0.0] - 2025-07-14

### Added
- Initial release of SuperGemini v3.0
- 15 specialized slash commands for development tasks
- Smart persona auto-activation system
- MCP server integration (Context7, Sequential, Magic, Playwright)
- Unified CLI installer with multiple installation profiles
- Comprehensive documentation and user guides
- Token optimization framework
- Task management system

### Features
- **Commands**: analyze, build, cleanup, design, document, estimate, explain, git, improve, index, load, spawn, task, test, troubleshoot
- **Personas**: architect, frontend, backend, analyzer, security, mentor, refactorer, performance, qa, devops, scribe
- **MCP Servers**: Official library documentation, complex analysis, UI components, browser automation
- **Installation**: Quick, minimal, and developer profiles with component selection