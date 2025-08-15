# RULES.md - SuperGemini Framework Actionable Rules

Simple actionable rules for Gemini Code SuperGemini framework operation.

## Core Operational Rules

### Task Management Rules
- Plan complex tasks step-by-step before execution
- Use sequential approach for dependent operations
- Always validate before execution, verify after completion
- Run lint/typecheck before marking tasks complete
- Use --seq for complex analysis and thinking
- Focus on clear, systematic approach

### File Operation Security
- Always use read_file before write_file or replace operations
- Use absolute paths only, prevent path traversal attacks
- Execute operations systematically and safely
- Never commit automatically unless explicitly requested

### Framework Compliance
- Check package.json/pyproject.toml before using libraries
- Follow existing project patterns and conventions
- Use project's existing import styles and organization
- Respect framework lifecycles and best practices

### Systematic Codebase Changes
- **MANDATORY**: Complete project-wide discovery before any changes
- Search ALL file types for ALL variations of target terms
- Document all references with context and impact assessment
- Plan update sequence based on dependencies and relationships
- Execute changes in coordinated manner following plan
- Verify completion with comprehensive post-change search
- Validate related functionality remains working
- Use search_file_content and glob for comprehensive searches

## Quick Reference

### Do
✅ read_file before write_file/replace
✅ Use absolute paths
✅ Sequential systematic approach
✅ Validate before execution
✅ Check framework compatibility
✅ Use --seq for complex analysis
✅ Complete discovery before codebase changes
✅ Verify completion with evidence

### Don't
❌ Skip read_file operations
❌ Use relative paths
❌ Auto-commit without permission
❌ Ignore framework patterns
❌ Skip validation steps
❌ Make reactive codebase changes
❌ Mark complete without verification

### Guidelines
- Use --seq for complex multi-step analysis
- Apply systematic approach to complex problems  
- Focus on clear, step-by-step execution
- Validate operations before and after execution