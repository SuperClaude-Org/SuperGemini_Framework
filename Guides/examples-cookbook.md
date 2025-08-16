# SuperClaude Examples Cookbook 🍳

*A practical guide to real-world SuperClaude usage with hands-on examples*

## How to Use This Cookbook

This cookbook is your **practical reference** for using SuperClaude effectively. Unlike comprehensive guides, this focuses entirely on **working examples** and **real scenarios** you can try immediately.

**Structure:**
- **Quick Examples** - One-liner commands for common tasks
- **Development Scenarios** - Complete workflows for typical development situations
- **Troubleshooting Scenarios** - Real problem-solving examples
- **Advanced Patterns** - Complex multi-step workflows
- **Command Combinations** - Effective flag and agent combinations
- **Best Practices in Action** - Examples showing optimal SuperClaude usage

**How to read this:**
- 📋 **Copy-paste commands** - All examples are working commands you can use
- 🎯 **Expected outcomes** - What you should see after running each command
- 💡 **Why it works** - Brief explanation of the approach
- ⚠️ **Gotchas** - Common issues and how to avoid them

---

## Quick Examples - Just Try These! 🚀

### Essential One-Liners
```bash
# Initialize and understand your project
/sc:load                              # Load project context
/sc:analyze .                         # Analyze entire project
/sc:build                            # Smart build with auto-optimization

# Development workflows
/sc:implement user-auth               # Create authentication system
/sc:improve messy-file.js             # Clean up code automatically
/sc:troubleshoot "login not working"  # Debug specific issues

# Session management
/sc:save --checkpoint                 # Save progress with analysis
/sc:reflect --type completion         # Validate task completion
```

### Quick Analysis Commands
```bash
# Security focus
/sc:analyze src/auth --focus security --depth deep

# Performance analysis
/sc:analyze --focus performance --format report

# Quick quality check
/sc:analyze src/components --focus quality --depth quick

# Architecture review
/sc:analyze --focus architecture .
```

### Rapid Development Commands
```bash
# UI components (triggers Magic MCP + Frontend agent)
/sc:implement dashboard component --type component --framework react

# API development (triggers Backend agent + Context7)
/sc:implement user management API --type api --safe

# Full features (triggers multiple agents)
/sc:implement payment processing --type feature --with-tests
```

---

## Development Scenarios 📋

### Scenario 1: New Team Member Onboarding

**Situation**: New developer joining project, needs to understand codebase and setup development environment.

**Step-by-step workflow:**

```bash
# 1. Initialize session and load project context
/sc:load --deep --summary
# 🎯 Expected: Comprehensive project analysis with structure, tech stack, and key components

# 2. Understand architecture and dependencies
/sc:analyze --focus architecture
# 🎯 Expected: System design overview, dependency mapping, and component relationships

# 3. Check code quality and identify areas needing attention
/sc:analyze --focus quality --format report
# 🎯 Expected: HTML report with quality metrics, technical debt, and improvement areas

# 4. Verify test coverage and quality
/sc:test --coverage
# 🎯 Expected: Test execution results with coverage percentages and missing test areas

# 5. Generate onboarding documentation
/sc:document --type guide "getting started with this project"
# 🎯 Expected: Comprehensive getting started guide with setup instructions

# 6. Save insights for future reference
/sc:save --checkpoint "onboarding analysis complete"
# 🎯 Expected: Session saved with all analysis insights and documentation
```

**💡 Why this works:**
- `/sc:load --deep` activates comprehensive project analysis
- Multiple analysis focuses provide complete understanding
- Documentation generation creates permanent reference materials
- Session persistence preserves insights for future use

**⚠️ Gotchas:**
- Large projects may take time for deep analysis
- Test command requires existing test configuration
- Documentation quality depends on project structure clarity

---

### Scenario 2: Security Vulnerability Investigation

**Situation**: Security scan flagged potential vulnerabilities, need systematic investigation and remediation.

**Step-by-step workflow:**

```bash
# 1. Initialize focused security analysis
/sc:analyze --focus security --depth deep
# 🎯 Expected: Comprehensive security vulnerability assessment with severity ratings

# 2. Investigate specific suspicious components
/sc:troubleshoot "potential SQL injection in user queries" --type security --trace
# 🎯 Expected: Systematic analysis of SQL injection vectors and vulnerable code patterns

# 3. Analyze authentication and authorization systems
/sc:analyze src/auth --focus security --format report
# 🎯 Expected: Detailed auth security analysis with specific vulnerability details

# 4. Apply security improvements
/sc:improve auth-service --type security --safe
# 🎯 Expected: Automatic application of security best practices and vulnerability fixes

# 5. Validate security improvements with testing
/sc:test --type security
# 🎯 Expected: Security-focused test execution with validation of fixes

# 6. Document security findings and remediation
/sc:document --type report "security vulnerability assessment"
# 🎯 Expected: Comprehensive security report with findings and remediation steps

# 7. Save security analysis for compliance
/sc:save --type security-audit "vulnerability remediation complete"
# 🎯 Expected: Complete security audit trail saved for future reference
```

**💡 Why this works:**
- Security-focused analysis activates Security Engineer agent automatically
- Systematic troubleshooting provides comprehensive investigation methodology
- Safe improvements apply fixes without breaking existing functionality
- Documentation creates audit trail for compliance requirements

**⚠️ Gotchas:**
- Security analysis may flag false positives requiring manual review
- Improvements should be tested thoroughly before production deployment
- Complex security issues may require expert security engineer consultation

---

### Scenario 3: Performance Optimization Sprint

**Situation**: Application performance has degraded, need systematic optimization across frontend and backend.

**Step-by-step workflow:**

```bash
# 1. Comprehensive performance baseline analysis
/sc:analyze --focus performance --depth deep
# 🎯 Expected: Performance bottleneck identification with specific metrics and recommendations

# 2. Profile API performance issues
/sc:troubleshoot "API response times degraded" --type performance
# 🎯 Expected: Systematic analysis of API bottlenecks, database queries, and caching issues

# 3. Optimize backend performance
/sc:improve api-endpoints --type performance --interactive
# 🎯 Expected: Performance engineer provides optimization recommendations with guided implementation

# 4. Optimize frontend bundle and rendering
/sc:improve src/components --type performance --safe
# 🎯 Expected: Frontend optimization including code splitting, lazy loading, and rendering improvements

# 5. Build optimized production artifacts
/sc:build --type prod --optimize --verbose
# 🎯 Expected: Optimized production build with minification, tree-shaking, and performance analysis

# 6. Validate performance improvements with testing
/sc:test --type performance --coverage
# 🎯 Expected: Performance test execution with before/after metrics comparison

# 7. Monitor and document optimization results
/sc:reflect --type completion "performance optimization"
# 🎯 Expected: Validation of optimization effectiveness with recommendations for monitoring

# 8. Save optimization insights and metrics
/sc:save --checkpoint "performance optimization sprint complete"
# 🎯 Expected: Complete optimization documentation with metrics and ongoing monitoring recommendations
```

**💡 Why this works:**
- Performance focus automatically activates Performance Engineer agent
- Interactive improvements provide guided optimization decisions
- Production build validation ensures optimizations work in deployment
- Comprehensive testing validates improvement effectiveness

**⚠️ Gotchas:**
- Performance improvements may introduce subtle bugs requiring thorough testing
- Production builds should be tested in staging environment first
- Performance metrics should be monitored continuously after deployment

---

### Scenario 4: Legacy Code Modernization

**Situation**: Large legacy codebase needs modernization to current standards and frameworks.

**Step-by-step workflow:**

```bash
# 1. Assess legacy codebase comprehensively
/sc:load --deep --summary
# 🎯 Expected: Complete legacy system analysis with technology stack assessment

# 2. Identify modernization opportunities and technical debt
/sc:analyze --focus architecture --depth deep
# 🎯 Expected: Technical debt assessment with modernization recommendations and migration strategy

# 3. Plan systematic modernization approach
/sc:select-tool "migrate 100+ files to TypeScript" --analyze
# 🎯 Expected: Tool selection recommendations for large-scale code transformation

# 4. Begin with code quality improvements
/sc:improve legacy-modules --type maintainability --preview
# 🎯 Expected: Preview of maintainability improvements without applying changes

# 5. Apply safe modernization improvements
/sc:improve legacy-modules --type maintainability --safe
# 🎯 Expected: Application of safe refactoring and modernization patterns

# 6. Clean up technical debt systematically
/sc:cleanup src/ --dead-code --safe
# 🎯 Expected: Removal of dead code, unused imports, and outdated patterns

# 7. Validate modernization with comprehensive testing
/sc:test --type all --coverage
# 🎯 Expected: Complete test suite execution with coverage analysis

# 8. Document modernization progress and next steps
/sc:document --type report "legacy modernization progress"
# 🎯 Expected: Comprehensive modernization report with completed work and future recommendations

# 9. Save modernization insights for iterative improvement
/sc:save --checkpoint "legacy modernization phase 1"
# 🎯 Expected: Complete modernization context saved for continued iterative improvement
```

**💡 Why this works:**
- Deep analysis provides comprehensive understanding of legacy system complexity
- Tool selection optimization ensures efficient modernization approach
- Preview mode allows safe exploration of changes before application
- Iterative approach with checkpoints enables manageable modernization process

**⚠️ Gotchas:**
- Large legacy systems require multiple iteration cycles
- Preview changes carefully before applying to critical systems
- Comprehensive testing essential to prevent breaking legacy functionality
- Modernization should be planned in phases to manage risk

---

### Scenario 5: Multi-Team API Design

**Situation**: Multiple teams need to collaborate on API design requiring coordination across frontend, backend, and security concerns.

**Step-by-step workflow:**

```bash
# 1. Brainstorm API requirements with stakeholder exploration
/sc:brainstorm "multi-service API architecture" --strategy enterprise --depth deep
# 🎯 Expected: Comprehensive requirements discovery with cross-team considerations

# 2. Generate structured API implementation workflow
/sc:workflow api-requirements.md --strategy systematic --parallel
# 🎯 Expected: Detailed implementation plan with multi-team coordination and dependencies

# 3. Design API architecture with security considerations
/sc:design --type api user-management --format spec
# 🎯 Expected: Formal API specification with security, performance, and integration considerations

# 4. Implement API with multi-domain expertise
/sc:implement user management API --type api --with-tests --safe
# 🎯 Expected: Complete API implementation with automated testing and security validation

# 5. Validate API design with cross-team testing
/sc:test --type integration --coverage
# 🎯 Expected: Integration testing with frontend/backend coordination validation

# 6. Generate comprehensive API documentation
/sc:document --type api src/controllers/ --style detailed
# 🎯 Expected: Complete API documentation with usage examples and integration guidance

# 7. Reflect on multi-team coordination effectiveness
/sc:reflect --type completion "API design collaboration"
# 🎯 Expected: Analysis of coordination effectiveness with recommendations for future collaboration

# 8. Save API design insights for team knowledge sharing
/sc:save --type collaboration "multi-team API design complete"
# 🎯 Expected: Complete API design context saved for future multi-team projects
```

**💡 Why this works:**
- Brainstorming mode facilitates cross-team requirements discovery
- Workflow generation provides structured coordination approach
- Multi-persona activation ensures comprehensive domain coverage
- Documentation supports ongoing team collaboration

**⚠️ Gotchas:**
- Multi-team coordination requires clear communication channels
- API design decisions should be validated with all stakeholder teams
- Integration testing requires coordination of development environments
- Documentation should be maintained as API evolves

---

## Troubleshooting Scenarios 🔧

### Problem: Build Failures After Dependency Updates

**Symptoms**: Build process failing with cryptic error messages after updating dependencies.

**Troubleshooting workflow:**

```bash
# 1. Systematic build failure investigation
/sc:troubleshoot "TypeScript compilation errors" --type build --trace
# 🎯 Expected: Systematic analysis of build logs and TypeScript configuration issues

# 2. Analyze dependency compatibility
/sc:analyze package.json --focus dependencies
# 🎯 Expected: Dependency conflict analysis with compatibility recommendations

# 3. Attempt automatic build fixes
/sc:troubleshoot "build failing" --type build --fix
# 🎯 Expected: Application of common build fixes with validation

# 4. Clean build with optimization
/sc:build --clean --verbose
# 🎯 Expected: Clean build execution with detailed error analysis
```

**💡 Why this works:** Systematic troubleshooting provides structured diagnosis, automatic fixes handle common issues, verbose output reveals detailed error information.

---

### Problem: Authentication System Security Vulnerabilities

**Symptoms**: Security scan revealed potential authentication vulnerabilities.

**Troubleshooting workflow:**

```bash
# 1. Deep security analysis of authentication system
/sc:analyze src/auth --focus security --depth deep
# 🎯 Expected: Comprehensive security vulnerability assessment with specific findings

# 2. Investigate specific authentication vulnerabilities
/sc:troubleshoot "JWT token vulnerability" --type security --trace
# 🎯 Expected: Systematic analysis of JWT implementation with security recommendations

# 3. Apply security hardening improvements
/sc:improve auth-service --type security --safe
# 🎯 Expected: Application of security best practices and vulnerability fixes

# 4. Validate security fixes with testing
/sc:test --type security auth-tests/
# 🎯 Expected: Security-focused testing with validation of vulnerability fixes
```

**💡 Why this works:** Security-focused analysis activates security expertise, systematic troubleshooting provides comprehensive investigation, safe improvements ensure no functionality breaks.

---

### Problem: Performance Degradation in Production

**Symptoms**: Application response times increased significantly in production environment.

**Troubleshooting workflow:**

```bash
# 1. Performance bottleneck identification
/sc:troubleshoot "API response times degraded" --type performance
# 🎯 Expected: Systematic performance analysis with bottleneck identification

# 2. Analyze performance across application layers
/sc:analyze --focus performance --format report
# 🎯 Expected: Comprehensive performance report with optimization recommendations

# 3. Optimize critical performance paths
/sc:improve api-endpoints --type performance --interactive
# 🎯 Expected: Performance optimization with guided decision-making

# 4. Validate performance improvements
/sc:test --type performance --coverage
# 🎯 Expected: Performance testing with before/after metrics comparison
```

**💡 Why this works:** Performance-focused troubleshooting provides systematic bottleneck analysis, interactive improvements guide complex optimization decisions, testing validates improvement effectiveness.

---

## Advanced Patterns 🎓

### Pattern: Cross-Session Project Development

**Use case**: Working on complex features across multiple development sessions with context preservation.

```bash
# Session 1: Requirements and Planning
/sc:load                                    # Initialize project context
/sc:brainstorm "user dashboard feature" --prd # Explore requirements
/sc:workflow dashboard-requirements.md       # Generate implementation plan
/sc:save --checkpoint "dashboard planning"   # Save planning context

# Session 2: Implementation Start
/sc:load                                    # Resume project context
/sc:implement dashboard component --type component --framework react
/sc:save --checkpoint "dashboard component created"

# Session 3: Testing and Refinement  
/sc:load                                    # Resume project context
/sc:test dashboard-component --coverage     # Validate implementation
/sc:improve dashboard-component --type quality --safe
/sc:save --checkpoint "dashboard implementation complete"

# Session 4: Integration and Documentation
/sc:load                                    # Resume project context
/sc:reflect --type completion "dashboard feature"
/sc:document --type component dashboard-component
/sc:save "dashboard feature complete"
```

**💡 Why this works:** Session persistence maintains context across development cycles, checkpoints provide recovery points, progressive enhancement builds on previous work.

---

### Pattern: Multi-Tool Complex Analysis

**Use case**: Complex system analysis requiring coordination of multiple specialized tools and expertise.

```bash
# Step 1: Intelligent tool selection for complex task
/sc:select-tool "comprehensive security and performance audit" --analyze
# 🎯 Expected: Recommended tool combination and coordination strategy

# Step 2: Coordinated multi-domain analysis
/sc:analyze --focus security --depth deep &
/sc:analyze --focus performance --depth deep &
/sc:analyze --focus architecture --depth deep
# 🎯 Expected: Parallel analysis across multiple domains

# Step 3: Systematic troubleshooting with expert coordination
/sc:troubleshoot "complex system behavior" --type system --sequential
# 🎯 Expected: Structured debugging with multiple expert perspectives

# Step 4: Comprehensive improvement with validation
/sc:improve . --type quality --interactive --validate
# 🎯 Expected: Guided improvements with comprehensive validation gates
```

**💡 Why this works:** Tool selection optimization ensures efficient approach, parallel analysis maximizes efficiency, expert coordination provides comprehensive coverage.

---

### Pattern: Large-Scale Code Transformation

**Use case**: Systematic transformation of large codebase with pattern-based changes.

```bash
# Step 1: Analyze scope and plan transformation approach
/sc:select-tool "migrate 100+ files to TypeScript" --efficiency
# 🎯 Expected: Optimal tool selection for large-scale transformation

# Step 2: Systematic transformation with progress tracking
/sc:spawn migrate-typescript --parallel --monitor
# 🎯 Expected: Parallel transformation with progress monitoring

# Step 3: Validate transformation quality and completeness
/sc:test --type all --coverage
/sc:analyze --focus quality transformed-files/
# 🎯 Expected: Comprehensive validation of transformation quality

# Step 4: Cleanup and optimization post-transformation
/sc:cleanup transformed-files/ --safe
/sc:improve transformed-files/ --type maintainability --safe
# 🎯 Expected: Final cleanup and optimization of transformed code
```

**💡 Why this works:** Scope analysis ensures appropriate tool selection, parallel processing maximizes efficiency, comprehensive validation ensures quality maintenance.

---

## Command Combinations That Work Well 🔗

### Security-Focused Development Workflow
```bash
# Analysis → Improvement → Validation → Documentation
/sc:analyze --focus security --depth deep
/sc:improve src/ --type security --safe  
/sc:test --type security --coverage
/sc:document --type security-guide
```

### Performance Optimization Workflow
```bash
# Profiling → Optimization → Building → Validation
/sc:analyze --focus performance --format report
/sc:improve api/ --type performance --interactive
/sc:build --type prod --optimize
/sc:test --type performance
```

### Quality Improvement Workflow
```bash
# Assessment → Preview → Application → Cleanup → Testing
/sc:analyze --focus quality
/sc:improve src/ --type quality --preview
/sc:improve src/ --type quality --safe
/sc:cleanup src/ --safe
/sc:test --coverage
```

### New Feature Development Workflow
```bash
# Planning → Implementation → Testing → Documentation → Session Save
/sc:brainstorm "feature idea" --prd
/sc:implement feature-name --type feature --with-tests
/sc:test feature-tests/ --coverage
/sc:document --type feature feature-name
/sc:save --checkpoint "feature complete"
```

### Legacy Code Modernization Workflow
```bash
# Assessment → Planning → Safe Improvement → Cleanup → Validation
/sc:load --deep --summary
/sc:select-tool "legacy modernization" --analyze
/sc:improve legacy/ --type maintainability --preview
/sc:improve legacy/ --type maintainability --safe
/sc:cleanup legacy/ --safe
/sc:test --type all
```

---

## Best Practices in Action 🌟

### Effective Flag Usage Patterns

**Safe Development Pattern:**
```bash
# Always preview before applying changes
/sc:improve src/ --preview                    # See what would change
/sc:improve src/ --safe                       # Apply only safe changes
/sc:test --coverage                           # Validate changes work
```

**Progressive Analysis Pattern:**
```bash
# Start broad, then focus deep
/sc:analyze .                                 # Quick overview
/sc:analyze src/auth --focus security --depth deep  # Deep dive specific areas
/sc:analyze --focus performance --format report     # Detailed reporting
```

**Session Management Pattern:**
```bash
# Initialize → Work → Checkpoint → Validate → Save
/sc:load                                      # Start session
# ... work commands ...
/sc:save --checkpoint "work in progress"      # Regular checkpoints
/sc:reflect --type completion "task name"     # Validate completion
/sc:save "task complete"                      # Final save
```

### Expert Activation Optimization

**Let auto-activation work:**
```bash
# These automatically activate appropriate experts
/sc:analyze src/auth --focus security         # → Security Engineer
/sc:implement user dashboard --framework react # → Frontend Architect + Magic MCP
/sc:troubleshoot "API performance issues"     # → Performance Engineer + Backend Architect
/sc:improve legacy-code --type maintainability # → Architect + Quality Engineer
```

**Manual coordination when needed:**
```bash
# Complex scenarios benefit from explicit tool selection
/sc:select-tool "enterprise authentication system" --analyze
/sc:brainstorm "multi-service architecture" --strategy enterprise
/sc:workflow complex-feature.md --strategy systematic --parallel
```

### Error Recovery Patterns

**When commands don't work as expected:**
```bash
# 1. Start with broader scope
/sc:analyze src/component.js                  # Instead of very specific file
/sc:troubleshoot "build failing"              # Instead of specific error

# 2. Use safe flags
/sc:improve --safe --preview                  # Check before applying
/sc:cleanup --safe                            # Conservative cleanup only

# 3. Validate systematically
/sc:reflect --type task "what I'm trying to do"  # Check approach
/sc:test --coverage                            # Ensure nothing broke
```

### Performance Optimization

**For large projects:**
```bash
# Use focused analysis instead of analyzing everything
/sc:analyze src/components --focus quality     # Not entire project
/sc:analyze api/ --focus performance           # Specific performance focus

# Use depth control
/sc:analyze --depth quick                      # Fast overview
/sc:analyze critical-files/ --depth deep       # Deep dive where needed
```

**For resource constraints:**
```bash
# Use efficient command combinations
/sc:select-tool "complex operation" --efficiency  # Get optimal approach
/sc:spawn complex-task --parallel               # Parallel processing
/sc:save --checkpoint                           # Frequent saves to preserve work
```

---

## Troubleshooting Command Issues 🔧

### Common Command Problems and Solutions

**"Command not working as expected":**
```bash
# Try these diagnostic approaches
/sc:index --search "keyword"                   # Find relevant commands
/sc:select-tool "what you're trying to do"     # Get tool recommendations
/sc:reflect --type task "your goal"            # Validate approach
```

**"Analysis taking too long":**
```bash
# Use scope and depth control
/sc:analyze src/specific-folder --depth quick  # Narrow scope
/sc:analyze --focus specific-area              # Focus analysis
/sc:analyze file.js                           # Single file analysis
```

**"Build commands failing":**
```bash
# Systematic build troubleshooting
/sc:troubleshoot "build issue description" --type build
/sc:analyze package.json --focus dependencies
/sc:build --clean --verbose                   # Clean build with details
```

**"Not sure which command to use":**
```bash
# Command discovery
/sc:index                                     # Browse all commands
/sc:index --category analysis                 # Commands by category
/sc:index --search "performance"              # Search by keyword
```

### When to Use Which Approach

**Quick tasks (< 5 minutes):**
- Use direct commands: `/sc:analyze`, `/sc:build`, `/sc:improve`
- Skip session management for one-off tasks
- Use `--quick` depth for fast results

**Medium tasks (30 minutes - 2 hours):**
- Initialize with `/sc:load`
- Use checkpoints: `/sc:save --checkpoint`
- Use `--preview` before making changes
- Validate with `/sc:reflect`

**Long-term projects (days/weeks):**
- Always use session lifecycle: `/sc:load` → work → `/sc:save`
- Use `/sc:brainstorm` for requirements discovery
- Plan with `/sc:workflow` for complex features
- Regular reflection and validation

**Emergency fixes:**
- Start with `/sc:troubleshoot` for diagnosis
- Use `--safe` flags for all changes
- Test immediately: `/sc:test`
- Document fixes: `/sc:document --type fix`

---

## Quick Reference Cheat Sheet 📝

### Most Useful Commands
```bash
/sc:load                    # Start session
/sc:analyze .               # Understand project  
/sc:implement feature-name  # Build features
/sc:improve messy-code     # Clean up code
/sc:troubleshoot "issue"   # Debug problems
/sc:build                  # Build project
/sc:test --coverage        # Test everything
/sc:save                   # Save session
```

### Best Flag Combinations
```bash
--safe                     # Conservative changes only
--preview                  # Show changes before applying
--depth deep               # Thorough analysis
--focus security|performance|quality  # Domain-specific focus
--with-tests              # Include testing
--interactive             # Guided assistance
--format report           # Generate detailed reports
```

### Emergency Commands
```bash
/sc:troubleshoot "critical issue" --fix    # Emergency fixes
/sc:analyze --focus security --depth deep  # Security emergencies
/sc:build --clean --verbose               # Build emergencies
/sc:reflect --type completion             # Validate fixes work
```

### Session Management
```bash
/sc:load                              # Start/resume session
/sc:save --checkpoint "description"   # Save progress
/sc:reflect --type completion         # Validate completion
/sc:save "final description"          # End session
```

---

## Remember: Learning Through Doing 🎯

**The SuperClaude Philosophy:**
- **Start simple** - Try `/sc:analyze` or `/sc:implement` first
- **Let auto-activation work** - SuperClaude picks experts for you
- **Experiment freely** - Use `--preview` to see what would happen
- **Progressive enhancement** - Start basic, add complexity as needed

**Most important patterns:**
1. Initialize sessions: `/sc:load`
2. Save progress: `/sc:save --checkpoint`
3. Validate completion: `/sc:reflect`
4. Preview before applying: `--preview` flag
5. Use safe modes: `--safe` flag

**Remember:** You don't need to memorize everything in this cookbook. SuperClaude is designed to be discoverable through use. Start with the Quick Examples section and experiment from there!

---

## Related Guides

**🚀 Foundation Knowledge (Start Here)**
- [Installation Guide](installation-guide.md) - Get SuperClaude set up first
- [SuperClaude User Guide](superclaude-user-guide.md) - Understand the framework philosophy

**📚 Deep Understanding (After Trying Examples)**
- [Commands Guide](commands-guide.md) - Complete reference for all 21 commands
- [Session Management Guide](session-management.md) - Master /sc:load and /sc:save workflows
- [Agents Guide](agents-guide.md) - Understanding the 13 specialists behind the scenes

**⚙️ Advanced Usage (When You Want Control)**
- [Flags Guide](flags-guide.md) - Manual control and optimization flags
- [Behavioral Modes Guide](behavioral-modes-guide.md) - How SuperClaude adapts automatically
- [Best Practices Guide](best-practices.md) - Proven patterns for effective usage

**🔧 When Examples Don't Work**
- [Troubleshooting Guide](troubleshooting-guide.md) - Solutions for common command issues

**🏗️ Technical Understanding (Optional)**
- [Technical Architecture Guide](technical-architecture.md) - How the system works internally

**📖 Learning Path Using This Cookbook:**
1. Try [Quick Examples](#quick-examples---just-try-these-) for immediate results
2. Follow [Development Scenarios](#development-scenarios-) for complete workflows
3. Use [Command Combinations](#command-combinations-that-work-well-) for your specific needs
4. Reference [Best Practices](#best-practices-in-action-) for optimization

---

*Ready to start? Try `/sc:load` to initialize your session and pick any example that matches your current need! 🚀*