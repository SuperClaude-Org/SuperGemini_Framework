# Changelog

All notable changes to SuperGemini will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.2.3] - 2025-08-16

### Changed
- Removed `allowed-tools` entries from all command TOML files for better Gemini CLI compatibility
- Updated hyunjae-labs author email to correct address (thecurrent.lim@gmail.com)

### Fixed
- Author metadata properly configured in pyproject.toml for PyPI display

## [3.2.2] - 2025-08-16

### Added
- **hyunjae-labs** added to authors list in pyproject.toml

## [3.2.1] - 2025-08-16

### Added
- **Internal Processing Philosophy** in PRINCIPLES.md - Prevents verbose file content output
- **Progress Transparency Philosophy** in PRINCIPLES.md - Provides status updates during long operations
- **Contextual Intelligence** in Core Philosophy - Improves semantic understanding and flexible problem solving
- **Document State Verification Philosophy** in PRINCIPLES.md - Ensures read_file tool usage when documents are modified

### Improved
- AI behavior to process files internally without displaying entire contents
- Long operation feedback with 30-60 second progress updates
- Semantic file discovery in subdirectories when initial path fails
- Document freshness verification with mandatory read_file tool usage on change signals

## [3.2.0] - 2025-08-16

### Removed
- Removed `spawn`, `task`, `workflow` commands - not compatible with Gemini CLI
- Removed hooks component - Gemini CLI does not support hooks functionality

### Changed
- Commands now use TOML format for Gemini CLI compatibility
- Organization changed from SuperGemini-Org to SuperClaude-Org

### Fixed
- Installation errors related to missing command files

## [3.1.4] - 2025-08-07

### Fixed
- **Issue #1**: Command files validation error - Added explicit `_get_command_files()` method to properly list all 17 command files
- **Issue #2**: `/sg:analyze --seq` not triggering sequential-thinking MCP server - Enhanced TOML conversion with MCP activation instructions  
- **Version output**: Fixed `--version` flag not displaying properly on Windows systems
- **Package structure**: Fixed missing `setup`, `config`, and `profiles` packages in wheel distribution
- **Cross-platform**: Improved Windows/Mac compatibility with proper `which`/`where` command handling

### Changed
- Updated `pyproject.toml` to include all necessary packages in wheel distribution
- Improved error handling with proper fallback mechanisms for missing imports
- Enhanced MCP server configuration in generated TOML files
- Commands properly installed in `~/.gemini/commands/sg/` subdirectory

### Added
- Comprehensive test suite for installation validation
- Better support for MCP server auto-installation via npm
- Explicit MCP triggers for commands when using `--seq` flag

## [3.1.2] - 2025-07-20

### Changed
- Commands now use `/sg:` namespace to avoid conflicts
- All 17 commands migrated to new namespace

## [3.0.0] - 2025-07-14

### Added
- Initial release of SuperGemini v3.0
- 17 specialized slash commands for development tasks
- Smart persona auto-activation system
- MCP server integration (Context7, Sequential, Playwright)
- Unified CLI installer with multiple installation profiles
- Comprehensive documentation and user guides
- Token optimization framework
- Task management system

### Features
- **Commands**: analyze, build, cleanup, design, document, estimate, explain, git, implement, improve, index, load, spawn, task, test, troubleshoot, workflow
- **Personas**: architect, frontend, backend, analyzer, security, mentor, refactorer, performance, qa, devops, scribe
- **MCP Servers**: Official library documentation, complex analysis, browser automation
- **Installation**: Quick, minimal, and developer profiles with component selection