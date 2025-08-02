# Changelog

All notable changes to SuperGemini will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- **BREAKING**: Commands now use `/sg:` namespace to avoid conflicts with user custom commands
- Commands are now installed in `~/.gemini/commands/sc/` subdirectory
- All 16 commands updated: `/analyze` � `/sg:analyze`, `/build` � `/sg:build`, etc.
- Automatic migration from old command locations to new `sc/` subdirectory

### Added
- **NEW COMMAND**: `/sg:implement` for feature and code implementation (addresses v2 user feedback)
- Migration logic to move existing commands to new namespace automatically
- Enhanced uninstaller to handle both old and new command locations
- Improved command conflict prevention
- Better command organization and discoverability

### Technical Details
- Commands now accessible as `/sg:analyze`, `/sg:build`, `/sg:improve`, etc.
- Migration preserves existing functionality while preventing naming conflicts
- Installation process detects and migrates existing commands automatically
- Tab completion support for `/sg:` prefix to discover all SuperGemini commands

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