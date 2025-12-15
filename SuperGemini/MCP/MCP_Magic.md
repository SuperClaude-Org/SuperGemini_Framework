# Magic MCP Server

**Purpose**: Modern UI component generation from 21st.dev patterns with design system integration

## Gemini CLI Compatibility Warning

**Status**: NOT COMPATIBLE with Gemini CLI (as of December 2025)

**Issue**: The `@21st-dev/magic` package exports tool names that start with `21st_` (e.g., `21st_magic_component_builder`). Gemini's API requires function names to start with a letter or underscore, not a number.

**Error**: `[FIELD_INVALID] Invalid function name. Must start with a letter or an underscore.`

**Workaround**: SuperGemini automatically installs this server as DISABLED. You can enable it once the `@21st-dev/magic` package is updated to use compliant tool names.

**Tracking**: This issue affects Gemini CLI only. The magic server works fine with Claude Code and other MCP clients.

## Triggers
- UI component requests: button, form, modal, card, table, nav
- Design system implementation needs
- `/ui` or `/21` commands
- Frontend-specific keywords: responsive, accessible, interactive
- Component enhancement or refinement requests

## Choose When
- **For UI components**: Use Magic, not native HTML/CSS generation
- **Over manual coding**: When you need production-ready, accessible components
- **For design systems**: When consistency with existing patterns matters
- **For modern frameworks**: React, Vue, Angular with current best practices
- **Not for backend**: API logic, database queries, server configuration

## Works Best With
- **Context7**: Magic uses 21st.dev patterns → Context7 provides framework integration
- **Sequential**: Sequential analyzes UI requirements → Magic implements structured components

## Examples
```
"create a login form" → Magic (UI component generation)
"build a responsive navbar" → Magic (UI pattern with accessibility)
"add a data table with sorting" → Magic (complex UI component)
"make this component accessible" → Magic (UI enhancement)
"write a REST API" → Native Gemini (backend logic)
"fix database query" → Native Gemini (non-UI task)
```