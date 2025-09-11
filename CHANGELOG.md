# Changelog

All notable changes to SuperGemini will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [4.0.9] - 2025-08-24

### Removed
- **AGENTS.md reference-only file**: Removed from installation and git tracking per v4.0.8 architecture
- **Agent file imports**: Removed @AGENTS.md from Core Framework imports in GEMINI.md

### Technical Details
- AGENTS.md excluded from component file discovery (setup/core/base.py)
- Added AGENTS.md to .gitignore and removed from git tracking
- Core component now installs 3 files instead of 4 (FLAGS.md, PRINCIPLES.md, RULES.md only)
- Agent expertise remains integrated in TOML command prompts as designed

## [4.0.8] - 2025-08-24

### Fixed
- **Serena folder auto-creation**: Removed unnecessary directory creation during MCP installation
- **Logger error during uninstall**: Fixed custom Logger wrapper attribute access issue preventing clean uninstall
- **Uninstall completeness**: Enhanced file removal process with proper log handler cleanup

### Technical Details
- MCP component no longer creates serena directory unnecessarily (setup/components/mcp.py)
- Uninstall command properly accesses internal logger handlers through wrapper (setup/cli/commands/uninstall.py)
- Both issues identified and resolved through root cause analysis

## [4.0.7] - 2025-08-24

### Changed
- **BREAKING**: Agent System revolutionized from simple personas to 13 specialized domain experts
- **BREAKING**: Commands now use `/sg:` namespace optimized for Gemini CLI integration  
- **BREAKING**: Architecture shifted to single-agent with expert knowledge integration for Gemini optimization
- Commands expanded from 14 to 17 specialized commands (+3 new commands)
- Agent expertise now directly integrated into TOML command prompts for Gemini efficiency
- Enhanced MCP integration from 3 to 6 servers with intelligent tool selection
- Session management completely redesigned with cross-session persistence capabilities

### Added
- **NEW AGENTS**: 13 specialized domain experts with deep expertise integration
  - system-architect, backend-architect, frontend-architect, devops-architect
  - security-engineer, performance-engineer, quality-engineer, refactoring-expert
  - requirements-analyst, root-cause-analyst, python-expert, technical-writer, learning-guide
- **NEW BEHAVIORAL MODES**: 5 intelligent workflow adaptation modes
  - analysis mode for collaborative discovery and requirements exploration
  - Introspection Mode for meta-cognitive analysis and reasoning optimization
  - Orchestration Mode for intelligent tool selection and resource efficiency
  - Task Management Mode for hierarchical organization with persistent memory
  - Token Efficiency Mode for symbol-enhanced communication (30-50% reduction)
- **NEW COMMANDS**: 3 powerful workflow commands
  - `/sg:reflect` for task validation using Serena MCP analysis
  - `/sg:save` for session context persistence with cross-session memory
  - `/sg:select-tool` for intelligent MCP tool selection system
- **NEW MCP SERVERS**: 3 advanced integration servers
  - Serena MCP for semantic code analysis and memory management
  - Morphllm MCP for pattern-based edits and bulk transformations
  - Magic MCP for modern UI component generation
- **SESSION LIFECYCLE**: Complete session management with `/sg:load` → work → checkpoint → `/sg:save`
- **PERFORMANCE OPTIMIZATION**: Enhanced tool selection and session management efficiency
- **COMPREHENSIVE DOCUMENTATION**: Complete reorganization with Getting-Started, User-Guide, Developer-Guide, Reference sections

### Enhanced
- **Command Intelligence**: All 17 commands completely rewritten with multi-agent perspectives
- **MCP Decision Matrix**: Intelligent routing between 6 MCP servers based on operation requirements
- **Cross-Session Persistence**: Memory management preserving context and technical decisions
- **Agent Coordination**: Multi-persona operations with specialized domain expertise
- **Performance Optimization**: Tool selection optimization with speed vs accuracy trade-offs
- **Gemini CLI Integration**: Native optimization for single-agent architecture patterns

### Removed  
- **BREAKING**: Simple persona system replaced with specialized agent architecture
- **BREAKING**: Basic MCP integration replaced with advanced 6-server ecosystem
- Legacy hook system removed (Gemini CLI incompatibility)
- SuperGemini/Core/ complexity reduced from 9 files to 4 files for streamlined operation

### Technical Details
- Commands accessible as `/sg:analyze`, `/sg:build`, `/sg:improve`, `/sg:implement`, etc.
- Agent expertise integrated directly into command execution for Gemini single-agent optimization
- MCP servers auto-selected based on operation type: Serena (semantic), Morphllm (bulk), Magic (UI)
- Behavioral modes activate automatically based on context: complexity, scope, performance needs
- Session workflow: `/sg:load` → work → periodic checkpoints → `/sg:save` for continuity
- Memory schema supports plan/phase/task/todo hierarchy with cross-session preservation

### Migration Guide
- **Command Migration**: All `/sg:` commands maintain backward compatibility with enhanced functionality
- **Agent Learning**: 13 specialized agents replace simple personas - review agent capabilities for optimal usage
- **Session Workflow**: Adopt `/sg:load` → work → `/sg:save` pattern for cross-session continuity
- **MCP Integration**: Install Serena and Morphllm MCP servers for advanced semantic and bulk operations
- **Performance**: Leverage behavioral modes for improved efficiency in complex operations

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