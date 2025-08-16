# SuperClaude Commands Guide 🛠️

## 💡 Don't Overthink It - SuperClaude Tries to Help

**The truth about these 21 commands**: You don't need to memorize them. Just start with `/sc:analyze` or `/sc:implement` and see what happens! 

**Here's how it usually works:**
- Type `/` in Claude Code → See available commands
- Use basic ones like `/sc:analyze`, `/sc:build`, `/sc:improve` 
- **SuperClaude tries to pick helpful tools and experts** for each situation
- More commands become useful as you get comfortable

**Auto-activation is pretty neat** 🪄 - SuperClaude attempts to detect what you're trying to do and activate relevant specialists (security expert, performance optimizer, etc.) without you managing it. Usually works well! 😊

## Core Philosophy

SuperClaude commands work by:
- **Intelligent activation**: Right experts and tools activated automatically
- **Context awareness**: Understanding your project and frameworks
- **Safe operations**: Quality gates and validation throughout
- **Progressive enhancement**: Building from simple to complex solutions

---

## Quick "Just Try These" List 🚀

**Start here** (no reading required):
```bash
/sc:index                    # See what's available
/sc:analyze src/            # Tries to analyze your code smartly 
/sc:brainstorm "app idea"   # Interactive help for exploring ideas
/sc:workflow feature-100-prd.md  # Creates step-by-step implementation workflow from PRD
/sc:implement user-auth     # Creates features and components (replaces v2 /build)
/sc:build                   # Attempts intelligent project building
/sc:improve messy-file.js   # Tries to clean up code 
/sc:troubleshoot "error"    # Attempts to help with problems
/sc:save --checkpoint       # Save your work and progress
```

**That's honestly enough to get started.** Everything else below is here when you get curious about what other tools are available. For step-by-step examples, see [Examples Cookbook](examples-cookbook.md). 🛠️

---

A practical guide to all 21 SuperClaude v4.0.0 slash commands. We'll be honest about what works well and what's still rough around the edges.

## Quick Reference 📋

*(You really don't need to memorize this - just pick what sounds useful)*

| Command | Purpose | Auto-Activates | Best For |
|---------|---------|-----------------|----------|
| `/sc:analyze` | Smart code analysis | Security/performance experts | Finding issues, understanding codebases |
| `/sc:build` | Intelligent building | Frontend/backend specialists | Compilation, bundling, deployment prep |
| `/sc:implement` | Feature implementation | Domain-specific experts | Creating features, components, APIs, services |
| `/sc:improve` | Automatic code cleanup | Quality experts | Refactoring, optimization, quality fixes |
| `/sc:troubleshoot` | Problem investigation | Debug specialists | Debugging, issue investigation ([Troubleshooting Guide](troubleshooting-guide.md)) |
| `/sc:test` | Smart testing | QA experts | Running tests, coverage analysis |
| `/sc:document` | Auto documentation | Writing specialists | README files, code comments, guides |
| `/sc:git` | Enhanced git workflows | DevOps specialists | Smart commits, branch management |
| `/sc:design` | System design help | Architecture experts | Architecture planning, API design |
| `/sc:explain` | Learning assistant | Teaching specialists | Learning concepts, understanding code |
| `/sc:cleanup` | Debt reduction | Refactoring experts | Removing dead code, organizing files |
| `/sc:load` | Context understanding | Analysis experts | Project analysis, session initialization ([Session Management Guide](session-management.md)) |
| `/sc:estimate` | Smart estimation | Planning experts | Time/effort planning, complexity analysis |
| `/sc:spawn` | Complex workflows | Orchestration system | Multi-step operations, workflow automation |
| `/sc:task` | Project management | Planning system | Long-term feature planning, task tracking |
| `/sc:workflow` | Implementation planning | Workflow system | Creating step-by-step workflows from PRDs |
| `/sc:index` | Command navigation | Help system | Finding the right command for your task |
| `/sc:brainstorm` | Interactive discovery | Socratic dialogue | Requirements gathering, idea exploration |
| `/sc:reflect` | Task validation | Serena intelligence | Progress checking, completion validation |
| `/sc:save` | Session persistence | Checkpoint system | Context saving, session management |
| `/sc:select-tool` | Tool selection | Intelligence routing | Complex operation optimization |

**Pro tip**: Just try the ones that sound useful. SuperClaude usually tries to activate helpful experts and tools for each situation! 🎯

## Development Commands 🔨

### `/workflow` - Implementation Workflow Generator 🗺️
**What it does**: Analyzes PRDs and feature requirements to create comprehensive step-by-step implementation workflows.

**The helpful part**: Takes your PRD and breaks it down into a structured implementation plan with expert guidance, dependency mapping, and task orchestration! 🎯

**When to use it**:
- Starting a new feature from a PRD or specification
- Need a clear implementation roadmap
- Want expert guidance on implementation strategy
- Planning complex features with multiple dependencies

**The magic**: Auto-activates appropriate expert agents (architect, security, frontend, backend) and MCP servers (Context7 for patterns, Sequential for complex analysis) based on your feature requirements.

**Examples**:
```bash
/sc:workflow docs/feature-100-prd.md --strategy systematic --c7 --sequential
/sc:workflow "user authentication system" --agent security --output detailed
/sc:workflow payment-api --strategy mvp --risks --dependencies
```

**What you get**:
- **Roadmap Format**: Phase-based implementation plan with timelines
- **Tasks Format**: Organized epics, stories, and actionable tasks  
- **Detailed Format**: Step-by-step instructions with time estimates
- **Risk Assessment**: Potential issues and mitigation strategies
- **Dependency Mapping**: Internal and external dependencies
- **Expert Guidance**: Domain-specific best practices and patterns

### `/implement` - Feature Implementation
**What it does**: Implements features, components, and functionality with intelligent expert activation.

**The helpful part**: SuperClaude auto-activates the right experts (frontend, backend, security) and tools based on what you're implementing! 🎯

**When to use it**:
- Creating new features or components (replaces v2's `/build` functionality)
- Implementing APIs, services, or modules
- Building UI components with modern frameworks
- Developing business logic and integrations

**Basic syntax**:
```bash
/sc:implement user authentication system      # Implement complete feature
/sc:implement --type component LoginForm      # Create specific component  
/sc:implement --type api user-management      # Build API endpoints
/sc:implement --framework react dashboard     # Framework-specific implementation
```

**Useful flags**:
- `--type component|api|service|feature|module` - Implementation type
- `--framework react|vue|express|django|etc` - Target framework
- `--safe` - Conservative implementation approach
- `--iterative` - Step-by-step development with validation
- `--with-tests` - Include test implementation
- `--documentation` - Generate docs alongside code

**Real examples**:
```bash
/sc:implement user authentication --type feature --with-tests
/sc:implement dashboard component --type component --framework react
/sc:implement REST API for orders --type api --safe
/sc:implement payment processing --type service --iterative
/sc:implement search functionality --framework vue --documentation
```

**Auto-activation patterns**:
- **Frontend**: UI components, React/Vue/Angular → frontend agent + Magic MCP
- **Backend**: APIs, services, databases → backend agent + Context7
- **Security**: Auth, payments, sensitive data → security agent + validation
- **Complex features**: Multi-step implementations → Sequential MCP + architect agent

**Gotchas**:
- Specify `--type` for better results (component vs service vs feature)
- Use `--framework` when working with specific tech stacks
- Try `--safe` for production code or `--iterative` for complex features
- Remember: this replaces v2's `/build` for actual code implementation

---

### `/build` - Project Building
**What it does**: Builds, compiles, and packages projects with smart error handling.

**The easy way**: Just type `/sc:build` and SuperClaude tries to figure out your build system! 🎯

**When to use it**:
- You need to compile/bundle your project (just try `/sc:build`)
- Build process is failing and you want help debugging  
- Setting up build optimization (it tries to detect what you need)
- Preparing for deployment

**Basic syntax**:
```bash
/sc:build                          # Build current project
/sc:build --type prod              # Production build
/sc:build --clean                  # Clean build (remove old artifacts)
/sc:build --optimize               # Enable optimizations
/sc:build src/                     # Build specific directory
```

**Useful flags**:
- `--type dev|prod|test` - Build type
- `--clean` - Clean before building  
- `--optimize` - Enable build optimizations
- `--verbose` - Show detailed build output

**Real examples**:
```bash
/sc:build --type prod --optimize   # Production build with optimizations
/sc:build --clean --verbose        # Clean build with detailed output
/sc:build src/components           # Build just the components folder
```

**Gotchas**:
- Works best with common build tools (npm, webpack, etc.)
- May struggle with very custom build setups
- Check your build tool is in PATH

---

### `/design` - System & Component Design
**What it does**: Creates system architecture, API designs, and component specifications.

**When to use it**:
- Planning new features or systems
- Need API or database design
- Creating component architecture
- Documenting system relationships

**Basic syntax**:
```bash
/sc:design user-auth-system        # Design a user authentication system
/sc:design --type api auth         # Design just the API part
/sc:design --format spec payment   # Create formal specification
```

**Useful flags**:
- `--type architecture|api|component|database` - Design focus
- `--format diagram|spec|code` - Output format
- `--iterative` - Refine design through iterations

**Real examples**:
```bash
/sc:design --type api user-management    # Design user management API
/sc:design --format spec chat-system     # Create chat system specification
/sc:design --type database ecommerce     # Design database schema
```

**Gotchas**:
- More conceptual than code-generating
- Output quality depends on how clearly you describe requirements
- Great for planning phase, less for implementation details

## Analysis Commands 🔍

### `/analyze` - Code Analysis  
**What it does**: Comprehensive analysis of code quality, security, performance, and architecture.

**The helpful part**: SuperClaude tries to detect what kind of analysis you need and usually picks relevant experts! 🔍

**When to use it**:
- Understanding unfamiliar codebases (just point it at any folder)
- Finding security vulnerabilities (security expert usually jumps in)
- Performance bottleneck hunting (performance expert usually helps)
- Code quality assessment (quality specialist often takes over)

**Basic syntax**:
```bash
/sc:analyze src/                   # Analyze entire src directory
/sc:analyze --focus security       # Focus on security issues
/sc:analyze --depth deep app.js    # Deep analysis of specific file
```

**Useful flags**:
- `--focus quality|security|performance|architecture` - Analysis focus
- `--depth quick|deep` - Analysis thoroughness
- `--format text|json|report` - Output format

**Real examples**:
```bash
/sc:analyze --focus security --depth deep     # Deep security analysis
/sc:analyze --focus performance src/api/      # Performance analysis of API
/sc:analyze --format report .                 # Generate analysis report
```

**Gotchas**:
- Can take a while on large codebases
- Security analysis is pretty good, performance analysis varies
- Works best with common languages (JS, Python, etc.)

---

### `/troubleshoot` - Problem Investigation
**What it does**: Systematic debugging and problem investigation.

**When to use it**:
- Something's broken and you're not sure why
- Need systematic debugging approach
- Error messages are confusing
- Performance issues investigation

**Basic syntax**:
```bash
/sc:troubleshoot "login not working"     # Investigate login issue
/sc:troubleshoot --logs error.log        # Analyze error logs
/sc:troubleshoot performance             # Performance troubleshooting
```

**Useful flags**:
- `--logs <file>` - Include log file analysis
- `--seq` - Use structured debugging approach
- `--focus network|database|frontend` - Focus area

**Real examples**:
```bash
/sc:troubleshoot "API returning 500" --logs server.log
/sc:troubleshoot --focus database "slow queries"
/sc:troubleshoot "build failing" --seq
```

**Gotchas**:
- Works better with specific error descriptions
- Include relevant error messages and logs when possible
- May suggest obvious things first (that's usually good!)

---

### `/explain` - Educational Explanations
**What it does**: Explains code, concepts, and technologies in an educational way.

**When to use it**:
- Learning new technologies or patterns
- Understanding complex code
- Need clear explanations for team members
- Documenting tricky concepts

**Basic syntax**:
```bash
/sc:explain async/await               # Explain async/await concept
/sc:explain --code src/utils.js       # Explain specific code file
/sc:explain --beginner React hooks    # Beginner-friendly explanation
```

**Useful flags**:
- `--beginner` - Simpler explanations
- `--advanced` - Technical depth
- `--code <file>` - Explain specific code
- `--examples` - Include practical examples

**Real examples**:
```bash
/sc:explain --beginner "what is REST API"
/sc:explain --code src/auth.js --advanced
/sc:explain --examples "React context patterns"
```

**Gotchas**:
- Great for well-known concepts, may struggle with very niche topics
- Better with specific questions than vague "explain this codebase"
- Include context about your experience level

## Quality Commands ✨

### `/improve` - Code Enhancement
**What it does**: Systematic improvements to code quality, performance, and maintainability.

**When to use it**:
- Refactoring messy code
- Performance optimization
- Applying best practices
- Modernizing old code

**Basic syntax**:
```bash
/sc:improve src/legacy/            # Improve legacy code
/sc:improve --type performance     # Focus on performance
/sc:improve --safe src/utils.js    # Safe, low-risk improvements only
```

**Useful flags**:
- `--type quality|performance|maintainability|style` - Improvement focus
- `--safe` - Only apply low-risk changes
- `--preview` - Show what would be changed without doing it

**Real examples**:
```bash
/sc:improve --type performance --safe src/api/
/sc:improve --preview src/components/LegacyComponent.js
/sc:improve --type style . --safe
```

**Gotchas**:
- Always use `--preview` first to see what it wants to change
- `--safe` is your friend - prevents risky refactoring
- Works best on smaller files/modules rather than entire codebases

---

### `/cleanup` - Technical Debt Reduction
**What it does**: Removes dead code, unused imports, and organizes file structure.

**When to use it**:
- Codebase feels cluttered
- Lots of unused imports/variables
- File organization is messy
- Before major refactoring

**Basic syntax**:
```bash
/sc:cleanup src/                   # Clean up src directory
/sc:cleanup --dead-code            # Focus on dead code removal
/sc:cleanup --imports package.js   # Clean up imports in specific file
```

**Useful flags**:
- `--dead-code` - Remove unused code
- `--imports` - Clean up import statements
- `--files` - Reorganize file structure
- `--safe` - Conservative cleanup only

**Real examples**:
```bash
/sc:cleanup --dead-code --safe src/utils/
/sc:cleanup --imports src/components/
/sc:cleanup --files . --safe
```

**Gotchas**:
- Can be aggressive - always review changes carefully
- May not catch all dead code (especially dynamic imports)
- Better to run on smaller sections than entire projects

---

### `/test` - Testing & Quality Assurance
**What it does**: Runs tests, generates coverage reports, and maintains test quality.

**When to use it**:
- Running test suites
- Checking test coverage
- Generating test reports
- Setting up continuous testing

**Basic syntax**:
```bash
/sc:test                           # Run all tests
/sc:test --type unit               # Run only unit tests
/sc:test --coverage                # Generate coverage report
/sc:test --watch src/              # Watch mode for development
```

**Useful flags**:
- `--type unit|integration|e2e|all` - Test type
- `--coverage` - Generate coverage reports
- `--watch` - Run tests in watch mode
- `--fix` - Try to fix failing tests automatically

**Real examples**:
```bash
/sc:test --type unit --coverage
/sc:test --watch src/components/
/sc:test --type e2e --fix
```

**Gotchas**:
- Needs your test framework to be properly configured
- Coverage reports depend on your existing test setup
- `--fix` is experimental - review what it changes

## Documentation Commands 📝

### `/document` - Focused Documentation
**What it does**: Creates documentation for specific components, functions, or features.

**When to use it**:
- Need README files
- Writing API documentation
- Adding code comments
- Creating user guides

**Basic syntax**:
```bash
/sc:document src/api/auth.js       # Document authentication module
/sc:document --type api            # API documentation
/sc:document --style brief README  # Brief README file
```

**Useful flags**:
- `--type inline|external|api|guide` - Documentation type
- `--style brief|detailed` - Level of detail
- `--template` - Use specific documentation template

**Real examples**:
```bash
/sc:document --type api src/controllers/
/sc:document --style detailed --type guide user-onboarding
/sc:document --type inline src/utils/helpers.js
```

**Gotchas**:
- Better with specific files/functions than entire projects
- Quality depends on how well-structured your code is
- May need some editing to match your project's documentation style

## Project Management Commands 📊

### `/estimate` - Project Estimation
**What it does**: Estimates time, effort, and complexity for development tasks.

**When to use it**:
- Planning new features
- Sprint planning
- Understanding project complexity
- Resource allocation

**Basic syntax**:
```bash
/sc:estimate "add user authentication"    # Estimate auth feature
/sc:estimate --detailed shopping-cart     # Detailed breakdown
/sc:estimate --complexity user-dashboard  # Complexity analysis
```

**Useful flags**:
- `--detailed` - Detailed breakdown of tasks
- `--complexity` - Focus on technical complexity
- `--team-size <n>` - Consider team size in estimates

**Real examples**:
```bash
/sc:estimate --detailed "implement payment system"
/sc:estimate --complexity --team-size 3 "migrate to microservices"
/sc:estimate "add real-time chat" --detailed
```

**Gotchas**:
- Estimates are rough - use as starting points, not gospel
- Works better with clear, specific feature descriptions
- Consider your team's experience with the tech stack

---

### `/task` - Long-term Project Management
**What it does**: Manages complex, multi-session development tasks and features.

**When to use it**:
- Planning features that take days/weeks
- Breaking down large projects
- Tracking progress across sessions
- Coordinating team work

**Basic syntax**:
```bash
/sc:task create "implement user dashboard"  # Create new task
/sc:task status                            # Check task status
/sc:task breakdown "payment integration"    # Break down into subtasks
```

**Useful flags**:
- `create` - Create new long-term task
- `status` - Check current task status
- `breakdown` - Break large task into smaller ones
- `--priority high|medium|low` - Set task priority

**Real examples**:
```bash
/sc:task create "migrate from REST to GraphQL" --priority high
/sc:task breakdown "e-commerce checkout flow"
/sc:task status
```

**Gotchas**:
- Still experimental - doesn't always persist across sessions reliably 😅
- Better for planning than actual project management
- Works best when you're specific about requirements

---

### `/spawn` - Complex Operation Orchestration
**What it does**: Coordinates complex, multi-step operations and workflows.

**When to use it**:
- Operations involving multiple tools/systems
- Coordinating parallel workflows
- Complex deployment processes
- Multi-stage data processing

**Basic syntax**:
```bash
/sc:spawn deploy-pipeline          # Orchestrate deployment
/sc:spawn --parallel migrate-data  # Parallel data migration
/sc:spawn setup-dev-environment    # Complex environment setup
```

**Useful flags**:
- `--parallel` - Run operations in parallel when possible
- `--sequential` - Force sequential execution
- `--monitor` - Monitor operation progress

**Real examples**:
```bash
/sc:spawn --parallel "test and deploy to staging"
/sc:spawn setup-ci-cd --monitor
/sc:spawn --sequential database-migration
```

**Gotchas**:
- Most complex command - expect some rough edges
- Better for well-defined workflows than ad-hoc operations
- May need multiple iterations to get right

## Version Control Commands 🔄

### `/git` - Enhanced Git Operations
**What it does**: Git operations with intelligent commit messages and workflow optimization.

**When to use it**:
- Making commits with better messages
- Branch management
- Complex git workflows
- Git troubleshooting

**Basic syntax**:
```bash
/sc:git commit                     # Smart commit with auto-generated message
/sc:git --smart-commit add .       # Add and commit with smart message
/sc:git branch feature/new-auth    # Create and switch to new branch
```

**Useful flags**:
- `--smart-commit` - Generate intelligent commit messages
- `--branch-strategy` - Apply branch naming conventions
- `--interactive` - Interactive mode for complex operations

**Real examples**:
```bash
/sc:git --smart-commit "fixed login bug"
/sc:git branch feature/user-dashboard --branch-strategy
/sc:git merge develop --interactive
```

**Gotchas**:
- Smart commit messages are pretty good but review them
- Assumes you're following common git workflows
- Won't fix bad git habits - just makes them easier

## Utility Commands 🔧

### `/index` - Command Navigation
**What it does**: Helps you find the right command for your task.

**When to use it**:
- Not sure which command to use
- Exploring available commands
- Learning about command capabilities

**Basic syntax**:
```bash
/sc:index                          # List all commands
/sc:index testing                  # Find commands related to testing
/sc:index --category analysis      # Commands in analysis category
```

**Useful flags**:
- `--category <cat>` - Filter by command category
- `--search <term>` - Search command descriptions

**Real examples**:
```bash
/sc:index --search "performance"
/sc:index --category quality
/sc:index git
```

**Gotchas**:
- Simple but useful for discovery
- Better than trying to remember all 21 commands

---

### `/load` - Project Context Loading
**What it does**: Loads and analyzes project context for better understanding.

**When to use it**:
- Starting work on unfamiliar project
- Need to understand project structure
- Before making major changes
- Onboarding team members

**Basic syntax**:
```bash
/sc:load                           # Load current project context
/sc:load src/                      # Load specific directory context
/sc:load --deep                    # Deep analysis of project structure
```

**Useful flags**:
- `--deep` - Comprehensive project analysis
- `--focus <area>` - Focus on specific project area
- `--summary` - Generate project summary

**Real examples**:
```bash
/sc:load --deep --summary
/sc:load src/components/ --focus architecture
/sc:load . --focus dependencies
```

**Gotchas**:
- Can take time on large projects
- More useful at project start than during development
- Helps with onboarding but not a replacement for good docs

## Session & Intelligence Commands 🧠

### `/brainstorm` - Interactive Requirements Discovery
**What it does**: Interactive Socratic dialogue for exploring ideas and discovering requirements.

**When to use it**:
- Starting with vague project ideas ("I want to build something...")
- Need help figuring out what to build
- Exploring requirements for new features
- Creative problem solving and ideation

**Basic syntax**:
```bash
/sc:brainstorm "mobile app idea"        # Explore app concept
/sc:brainstorm --depth deep startup     # Deep exploration of startup idea
/sc:brainstorm --focus business ecom    # Business-focused e-commerce planning
```

**Useful flags**:
- `--depth normal|deep` - Exploration thoroughness
- `--focus business|technical|user` - Conversation focus area
- `--prd` - Generate Product Requirements Document after dialogue

**Real examples**:
```bash
/sc:brainstorm "task management app" --prd
/sc:brainstorm --depth deep --focus technical "real-time chat system"
/sc:brainstorm "improve user onboarding" --focus user
```

**Gotchas**:
- Works best when you're genuinely uncertain about requirements
- Quality of output depends on engagement in the dialogue
- Can take 10-15 minutes for thorough exploration

---

### `/reflect` - Task Reflection and Validation
**What it does**: Uses Serena intelligence for task validation, progress analysis, and completion verification.

**When to use it**:
- Checking if you're on the right track with a task
- Validating task completion before marking done
- Analyzing collected information during complex work
- Getting intelligent feedback on progress

**Basic syntax**:
```bash
/sc:reflect --type task                 # Reflect on current task approach
/sc:reflect --type completion          # Validate task completion
/sc:reflect --type session            # Analyze session progress
```

**Useful flags**:
- `--type task|completion|session` - Type of reflection
- `--analyze` - Deep analysis of current context
- `--validate` - Validation-focused reflection

**Real examples**:
```bash
/sc:reflect --type completion "implemented user auth"
/sc:reflect --analyze --type session
/sc:reflect --type task --validate "refactoring approach"
```

**Gotchas**:
- Requires Serena MCP server to be available
- Most effective when you provide context about what you're working on
- Best used at natural stopping points in work

---

### `/save` - Session Persistence and Checkpointing
**What it does**: Saves session context, creates checkpoints, and manages project memory through Serena.

**When to use it**:
- Saving work progress before ending session
- Creating checkpoints before risky operations
- Preserving insights and decisions for future sessions
- Managing long-term project context

**Basic syntax**:
```bash
/sc:save                               # Basic session save
/sc:save --checkpoint                  # Create checkpoint with analysis
/sc:save --type summary               # Save with session summary
```

**Useful flags**:
- `--checkpoint` - Create detailed checkpoint
- `--type session|summary|insights` - Save type
- `--analyze` - Include session analysis in save

**Real examples**:
```bash
/sc:save --checkpoint "before major refactoring"
/sc:save --type summary --analyze
/sc:save "completed authentication implementation"
```

**Gotchas**:
- Requires Serena MCP server for full functionality
- Checkpoint creation may take a moment for analysis
- Most valuable for complex, multi-session projects

---

### `/select-tool` - Intelligent Tool Selection
**What it does**: Analyzes complex operations and recommends optimal tool combinations and approaches.

**When to use it**:
- Uncertain about best approach for complex tasks
- Want to optimize tool selection for efficiency
- Need guidance on MCP server coordination
- Planning multi-step technical operations

**Basic syntax**:
```bash
/sc:select-tool "large codebase refactoring"    # Get tool recommendations
/sc:select-tool --analyze "performance audit"   # Analyze optimal approach
/sc:select-tool --context react-app "UI testing" # Context-aware selection
```

**Useful flags**:
- `--analyze` - Deep analysis of optimal approach
- `--context <tech>` - Provide technical context
- `--efficiency` - Focus on performance optimization

**Real examples**:
```bash
/sc:select-tool --analyze "migrate 100+ files to TypeScript"
/sc:select-tool --context nodejs --efficiency "API performance testing"
/sc:select-tool "cross-browser testing setup"
```

**Gotchas**:
- Recommendations are guidance, not requirements
- Most valuable for complex, multi-faceted operations
- Consider your specific project context when following recommendations

## Command Tips & Patterns 💡

### Effective Flag Combinations
```bash
# Safe improvement workflow
/sc:improve --preview src/component.js    # See what would change
/sc:improve --safe src/component.js       # Apply safe changes only

# Comprehensive analysis
/sc:analyze --focus security --depth deep
/sc:test --coverage
/sc:document --type api

# Smart git workflow
/sc:git add .
/sc:git --smart-commit --branch-strategy

# Project understanding workflow
/sc:load --deep --summary
/sc:analyze --focus architecture
/sc:document --type guide
```

### Common Workflows

**New Project Discovery**:
```bash
/sc:brainstorm "project idea" --prd         # Explore and define requirements
/sc:load --deep --summary                   # Understand existing codebase
/sc:workflow requirements.md                # Create implementation plan
/sc:save --checkpoint "project planning"    # Save planning insights
```

**New Project Onboarding**:
```bash
/sc:load --deep --summary
/sc:analyze --focus architecture
/sc:test --coverage
/sc:document README
```

**Bug Investigation**:
```bash
/sc:troubleshoot "specific error message" --logs
/sc:analyze --focus security
/sc:test --type unit affected-component
/sc:reflect --type completion "bug analysis"
```

**Code Quality Improvement**:
```bash
/sc:analyze --focus quality
/sc:improve --preview src/
/sc:cleanup --safe
/sc:test --coverage
/sc:reflect --type completion "quality improvements"
```

**Pre-deployment Checklist**:
```bash
/sc:test --type all --coverage
/sc:analyze --focus security
/sc:build --type prod --optimize
/sc:git --smart-commit
/sc:save --checkpoint "pre-deployment validation"
```

**Complex Task Planning**:
```bash
/sc:select-tool "migrate to microservices"  # Get approach recommendations
/sc:reflect --type task "migration strategy" # Validate approach
/sc:workflow migration-plan.md              # Create detailed workflow
/sc:save "migration planning complete"      # Preserve insights
```

### Troubleshooting Command Issues

**Command not working as expected?**
- Try adding `--help` to see all options
- Use `--preview` or `--safe` flags when available
- Start with smaller scope (single file vs. entire project)

**Analysis taking too long?**
- Use `--focus` to narrow scope
- Try `--depth quick` instead of deep analysis
- Analyze smaller directories first

**Build/test commands failing?**
- Make sure your tools are in PATH
- Check that config files are in expected locations
- Try running the underlying commands directly first

**Not sure which command to use?**
- Use `/index` to browse available commands
- Look at the Quick Reference table above
- Try the most specific command first, then broader ones

---

## Final Notes 📝

**The real truth about these commands** 💯:
- **Just try them** - You don't need to study this guide first
- **Start with the basics** - `/analyze`, `/build`, `/improve` cover most needs
- **Let auto-activation work** - SuperClaude usually picks helpful experts
- **Experiment freely** - Use `--preview` if you want to see what would happen first

**Still rough around the edges:**
- Complex orchestration (spawn, task) can be a bit flaky
- Some analysis depends heavily on your project setup  
- Error handling could be better in some commands

**Getting better all the time:**
- We actively improve commands based on user feedback
- Newer commands (analyze, improve) tend to work better
- Auto-activation keeps getting smarter

**Don't stress about memorizing this** 🧘‍♂️
- SuperClaude is designed to be discoverable through use
- Type `/` to see available commands
- Commands suggest what they can do when you use `--help`
- The intelligent routing handles most of the complexity

**Need help?** Check the [Troubleshooting Guide](troubleshooting-guide.md) or GitHub issues if you're stuck! 🚀

## Related Guides

**🚀 Getting Started (Essential)**
- [Installation Guide](installation-guide.md) - Get SuperClaude set up first
- [Examples Cookbook](examples-cookbook.md) - Copy-paste working examples for all commands
- [SuperClaude User Guide](superclaude-user-guide.md) - Complete framework overview

**🤝 Understanding the Team (Recommended)**
- [Agents Guide](agents-guide.md) - The 13 specialists that work with commands
- [Behavioral Modes Guide](behavioral-modes-guide.md) - How commands adapt automatically
- [Session Management Guide](session-management.md) - Persistent context with /sc:load and /sc:save

**⚙️ Control and Optimization (Advanced)**
- [Flags Guide](flags-guide.md) - All the --flags that modify command behavior
- [Best Practices Guide](best-practices.md) - Proven command combinations and workflows

**🔧 When Commands Don't Work**
- [Troubleshooting Guide](troubleshooting-guide.md) - Common command issues and solutions

**🏗️ Technical Deep Dive (Optional)**
- [Technical Architecture Guide](technical-architecture.md) - How the command system works internally

**📖 Recommended Learning Path:**
1. [Examples Cookbook](examples-cookbook.md) - Try commands with working examples
2. [Session Management Guide](session-management.md) - Learn /sc:load and /sc:save workflow
3. [Best Practices Guide](best-practices.md) - Master effective command patterns

## Command Flags & Options

### Common Flags
- `--safe` - Conservative operations with validation
- `--interactive` - Guided operation with user input
- `--parallel` - Parallel execution where applicable
- `--preview` - Show changes without applying
- `--analyze` - Deep analysis mode
- `--validate` - Enhanced validation and verification
- `--depth shallow|normal|deep` - Analysis depth control
- `--strategy systematic|agile|enterprise` - Execution strategy

### Format Options
- `--format text|json|yaml|report|diagram` - Output format control
- `--type` - Operation type specification (varies by command)
- `--style brief|detailed` - Output verbosity control

## Expert Activation

The framework automatically activates relevant experts:

### Technical Specialists
- **Backend Architect** - Server architecture, APIs, databases
- **DevOps Architect** - Infrastructure, deployment, CI/CD  
- **Frontend Architect** - UI architecture, state management, performance
- **Learning Guide** - Educational content, knowledge transfer
- **Performance Engineer** - Optimization, profiling, scalability
- **Python Expert** - Python-specific development and best practices
- **Quality Engineer** - Testing, quality assurance, code standards
- **Refactoring Expert** - Code restructuring and technical debt
- **Requirements Analyst** - Requirements gathering and analysis
- **Root Cause Analyst** - Problem diagnosis and systematic debugging
- **Security Engineer** - Security assessment and hardening
- **Technical Writer** - Documentation and communication

### MCP Server Integration
- **Context7** - Official documentation and framework patterns
- **Magic** - Modern UI component generation
- **Morphllm** - Pattern-based code editing and transformations
- **Playwright** - Browser automation and E2E testing
- **Sequential** - Complex multi-step reasoning and analysis
- **Serena** - Project memory and session management

## Command Relationships

### Session Flow
`/sc:load` → Work with commands → `/sc:reflect` (validate) → `/sc:save`

### Development Flow  
`/sc:analyze` → `/sc:design` → `/sc:implement` → `/sc:test` → `/sc:improve`

### Project Flow
`/sc:brainstorm` → `/sc:workflow` → `/sc:estimate` → `/sc:spawn` or `/sc:task`

### Maintenance Flow
`/sc:troubleshoot` → `/sc:cleanup` → `/sc:improve` → `/sc:document`

Remember: SuperClaude adapts to your needs. Start with simple requests and let the framework's intelligence guide you to more sophisticated usage patterns!

---

*Happy coding! Just remember - you can skip most of this guide and learn by doing. 🎯*
