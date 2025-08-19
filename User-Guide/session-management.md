# SuperGemini Session Management Guide 🧠

## Introduction

SuperGemini transforms Gemini CLI from a stateless assistant into a **persistent development partner** through intelligent session management. Sessions preserve project context, accumulated insights, and development progress across interruptions, creating continuity that builds expertise over time.

**Persistent Intelligence**: Load project context with `/sg:load`, work naturally with accumulated understanding, save progress with `/sg:save`, and resume exactly where you left off. SuperGemini remembers your codebase structure, decisions made, patterns discovered, and project goals.

**Cross-Session Learning**: Each session builds on previous understanding, creating a development partner that becomes more effective with your specific project over time.

## Session Fundamentals

**What is a SuperGemini Session?**
A session is a persistent development context that includes:
- **Project Understanding**: Codebase structure, architecture patterns, dependencies
- **Development History**: Decisions made, problems solved, patterns applied
- **Current State**: Active tasks, progress tracking, next steps
- **Learned Insights**: Code conventions, team preferences, domain knowledge

**Session Intelligence vs Standard Gemini:**
- **Standard Gemini**: Each conversation starts fresh, no project memory
- **SuperGemini Sessions**: Cumulative understanding that builds over time

**Session Types:**

**Project Sessions**: Long-term development context for specific codebases
- Persistent across weeks/months of development
- Accumulates architectural understanding
- Remembers team conventions and decisions

**Task Sessions**: Focused context for specific features or problems  
- Short to medium-term (hours to days)
- Maintains task-specific context and progress
- Integrates with project sessions for broader context

**Learning Sessions**: Educational context for understanding complex systems
- Preserves learning progress and insights
- Builds conceptual understanding over time
- Connects theoretical knowledge with practical application

**Session Persistence Powered by Serena MCP:**
- Semantic code understanding with symbol-level navigation
- Project memory that survives Gemini CLI restarts
- Intelligent context loading based on current work
- Cross-session insight accumulation and pattern recognition

## Session Commands

### /sg:load - Session Initialization

**Purpose**: Load project context and initialize persistent development session

**Usage Patterns:**
```bash
# Load existing project context
/sg:load src/

# Load with specific focus
/sg:load --focus architecture existing-project/

# Load previous session by name
/sg:load "payment-integration-session"

# Load with fresh analysis
/sg:load --refresh large-codebase/
```

**What Happens During Load:**
1. **Project Structure Analysis**: Serena MCP scans codebase organization
2. **Context Restoration**: Previous session memory and insights loaded
3. **Pattern Recognition**: Code conventions and architecture patterns identified
4. **Dependency Mapping**: Component relationships and data flow understood
5. **Session Initialization**: Persistent context established for continued work

**Load Modes:**

**Smart Load (Default):**
```bash
/sg:load project-directory/
```
- Automatically detects project type and structure
- Loads relevant previous session context
- Optimizes analysis based on project size and complexity

**Focused Load:**
```bash
/sg:load --focus security payment-system/
/sg:load --focus performance api-endpoints/
/sg:load --focus architecture microservices/
```
- Specialized analysis for specific concerns
- Activates domain experts and relevant tools
- Loads context specific to focus area

**Fresh Load:**
```bash
/sg:load --refresh --comprehensive legacy-system/
```
- Re-analyzes project from scratch
- Updates understanding with latest changes
- Comprehensive re-indexing of codebase

**Example Load Experience:**
```bash
/sg:load e-commerce-platform/

→ 🔍 Analyzing project structure...
→ 📂 Detected: React frontend + Node.js API + PostgreSQL
→ 🧠 Loading previous session: "checkout-optimization-work"
→ 📝 Restored context: 847 files analyzed, 23 patterns identified
→ ✅ Session ready: Continue checkout flow optimization
→ 💡 Next: Complete payment validation implementation
```

### /sg:save - Session Persistence

**Purpose**: Preserve session context and development progress for future continuation

**Usage Patterns:**
```bash
# Save current session with automatic naming
/sg:save

# Save with descriptive name
/sg:save "authentication-module-complete"

# Save checkpoint during long work
/sg:save --checkpoint "api-endpoints-analysis-done"

# Save with summary
/sg:save --description "Completed user registration flow, ready for testing"
```

**What Gets Saved:**
- **Project Understanding**: Current codebase analysis and insights
- **Work Progress**: Completed tasks, current focus, next steps
- **Decision History**: Architectural choices, patterns applied, trade-offs made
- **Code Context**: Modified files, dependencies, integration points
- **Learning Insights**: Discovered patterns, conventions, best practices

**Save Types:**

**Milestone Save:**
```bash
/sg:save "payment-integration-complete"
```
- Major feature completion or phase end
- Comprehensive context preservation
- Clear handoff point for future sessions

**Checkpoint Save:**
```bash
/sg:save --checkpoint "database-schema-analysis"
```
- Periodic progress preservation
- Intermediate work state capture
- Recovery point for complex work

**Automatic Save:**
```bash
# Triggered automatically during:
- Long-running tasks (every 30 minutes)
- Before risky operations
- Session interruption detection
- Context limit approaching
```

**Save Output Example:**
```bash
/sg:save "user-dashboard-feature-complete"

→ 💾 Saving session context...
→ 📊 Progress summary:
  ✅ 3 components implemented
  ✅ 12 tests passing
  ✅ API integration complete
  📝 Documentation updated
→ 🧠 Context preserved:
  - 247 files in working memory
  - 15 architectural patterns identified
  - 8 integration points mapped
→ ✅ Session saved: "user-dashboard-feature-complete"
→ 🔄 Ready for future continuation
```

### /sg:reflect - Session Validation

**Purpose**: Analyze session progress, validate task completion, and assess development quality

**Usage Patterns:**
```bash
# General session reflection
/sg:reflect

# Specific task validation
/sg:reflect "payment-processing-implementation"

# Quality assessment
/sg:reflect --type quality-review

# Completion verification
/sg:reflect --type completion-check
```

**Reflection Types:**

**Progress Analysis:**
```bash
/sg:reflect --type progress
```
- Current task status and completion percentage
- Blockers and dependencies identified
- Next steps and priority recommendations
- Timeline and effort assessment

**Quality Review:**
```bash
/sg:reflect --type quality
```
- Code quality assessment and improvements needed
- Test coverage and validation gaps
- Security and performance considerations
- Documentation and maintainability review

**Completion Verification:**
```bash
/sg:reflect --type completion
```
- Task completion criteria assessment
- Integration and testing verification
- Deployment readiness evaluation
- Handoff preparation and next steps

**Learning Assessment:**
```bash
/sg:reflect --type learning
```
- Insights gained and patterns discovered
- Decision rationale and trade-offs made
- Knowledge gaps and learning opportunities
- Best practices and conventions established

**Example Reflection Output:**
```bash
/sg:reflect --type completion "user-authentication-system"

→ 🎯 Task Completion Analysis:
  ✅ JWT authentication implemented
  ✅ Password hashing and validation  
  ✅ Session management
  ⚠️  Email verification pending
  ❌ OAuth integration incomplete

→ 📊 Quality Assessment:
  ✅ Security best practices followed
  ✅ 89% test coverage achieved
  ⚠️  Performance testing needed
  ✅ Documentation complete

→ 🔄 Next Steps:
  1. Complete email verification flow
  2. Implement OAuth providers
  3. Performance optimization
  4. Production deployment preparation

→ 💡 Session Status: 75% complete, 2-3 days remaining
```

## Session Lifecycle Management

**Complete Session Workflow:**

### Phase 1: Session Initialization
```bash
# 1. Project Discovery and Loading
/sg:load new-project/
→ Project analysis and context establishment

# 2. Goal Setting and Planning  
/sg:brainstorm "improve user onboarding experience"
→ Requirements discovery and strategic planning

# 3. Initial Analysis
/sg:analyze --focus user-experience --seq
→ Comprehensive system understanding
```

### Phase 2: Active Development
```bash
# 4. Implementation Planning
/sg:workflow "streamlined-onboarding-flow"
→ Systematic implementation strategy

# 5. Feature Development (Iterative)
/sg:implement "progressive-user-registration"
→ Coordinated development with automatic progress tracking

# 6. Regular Checkpoints
/sg:save --checkpoint "registration-flow-complete"
→ Periodic progress preservation
```

### Phase 3: Validation and Quality
```bash
# 7. Progress Review
/sg:reflect --type progress
→ Status assessment and next steps

# 8. Quality Assurance
/sg:test --comprehensive user-onboarding/
→ Testing and validation workflows

# 9. Quality Review
/sg:reflect --type quality
→ Code review and improvement identification
```

### Phase 4: Completion and Handoff
```bash
# 10. Completion Verification
/sg:reflect --type completion
→ Task completion criteria validation

# 11. Final Documentation
/sg:document --type user-guide onboarding-system/
→ Documentation and knowledge transfer

# 12. Session Archive
/sg:save "onboarding-improvement-complete"
→ Final context preservation and handoff preparation
```

**Session State Transitions:**

**Active Session States:**
- **Discovery**: Requirements exploration and goal setting
- **Analysis**: System understanding and strategy development  
- **Implementation**: Active development and feature creation
- **Validation**: Testing, review, and quality assurance
- **Completion**: Final verification and handoff preparation

**Session Continuity Patterns:**
- **Daily Sessions**: Load → Work → Checkpoint → Save
- **Weekly Sprints**: Load → Sprint planning → Daily work → Sprint review → Save
- **Feature Cycles**: Load → Analysis → Implementation → Testing → Completion → Save

## Memory and Context

**Serena MCP-Powered Memory System:**

**Project Memory Components:**
- **Structural Memory**: Codebase organization, file relationships, dependencies
- **Semantic Memory**: Code meaning, business logic, domain concepts
- **Historical Memory**: Development decisions, evolution patterns, change history
- **Contextual Memory**: Working sessions, current focus, progress state

**Memory Operations:**

**Memory Accumulation:**
```bash
# As you work, memory automatically builds:
/sg:analyze user-service/
→ Records: Service patterns, data flows, API contracts

/sg:implement "user-preferences"  
→ Records: Implementation patterns, coding conventions, integration points

/sg:troubleshoot "performance-issue"
→ Records: Problem patterns, solution strategies, optimization techniques
```

**Memory Recall:**
```bash
# Previous insights automatically inform current work:
/sg:implement "user-notifications"
→ Recalls: User service patterns, preference storage, communication flows
→ Applies: Established conventions, tested patterns, integration strategies
```

**Memory Types:**

**Architectural Memory:**
```json
{
  "patterns": ["MVC", "Repository Pattern", "Dependency Injection"],
  "conventions": ["camelCase variables", "async/await preferred"],
  "decisions": ["PostgreSQL for persistence", "JWT for authentication"],
  "integrations": ["Stripe API", "SendGrid", "Redis cache"]
}
```

**Development Memory:**
```json
{
  "workflows": ["TDD approach", "Feature branch strategy"],
  "quality_gates": ["ESLint rules", "Test coverage >80%"],
  "preferences": ["Functional components", "Hooks over classes"],
  "tooling": ["Jest testing", "Prettier formatting"]
}
```

**Context Preservation:**
```json
{
  "current_task": "implement-user-dashboard",
  "progress": "components-complete-api-pending",
  "next_steps": ["API integration", "state management", "testing"],
  "blockers": ["API rate limiting", "design system tokens"]
}
```

**Memory Intelligence:**

**Smart Context Loading:**
- Loads relevant memory based on current work
- Prioritizes recent and frequently accessed patterns
- Connects related concepts and components

**Pattern Recognition:**
- Identifies recurring code patterns and conventions
- Suggests consistent approaches based on project history
- Detects deviations from established patterns

**Predictive Context:**
- Anticipates needed information based on current task
- Pre-loads related components and dependencies
- Suggests next steps based on similar previous work

## Session Workflows

**Common Session Patterns:**

### Daily Development Session
```bash
# Morning: Resume previous work
/sg:load project/
→ Context restoration and progress review

# Planning: Review and plan day's work
/sg:reflect --type progress
→ Status assessment and priority setting

# Work: Active development with periodic saves
/sg:implement "current-feature"
/sg:save --checkpoint "feature-milestone"

# Evening: End-of-day preservation
/sg:reflect --type completion
/sg:save "end-of-day-progress"
```

### Feature Development Cycle
```bash
# Discovery Phase
/sg:load project/
/sg:brainstorm "new-feature-requirements"
/sg:save --checkpoint "requirements-complete"

# Planning Phase  
/sg:workflow "feature-implementation-plan"
/sg:design "feature-architecture"
/sg:save --checkpoint "planning-complete"

# Implementation Phase
/sg:implement "feature-core-functionality"
/sg:save --checkpoint "core-complete"

/sg:implement "feature-integration"
/sg:save --checkpoint "integration-complete"

# Validation Phase
/sg:test --comprehensive feature/
/sg:reflect --type quality
/sg:save "feature-complete"
```

### Bug Investigation Session
```bash
# Load with focus on problem area
/sg:load --focus debugging problematic-module/

# Systematic investigation
/sg:troubleshoot "specific-bug-description"
/sg:analyze --focus root-cause affected-components/

# Solution implementation
/sg:implement "bug-fix-solution"
/sg:test --focus regression bug-area/

# Validation and documentation
/sg:reflect --type completion
/sg:document --type bug-report "issue-resolution"
/sg:save "bug-fix-complete"
```

### Learning and Exploration Session
```bash
# Focused learning context
/sg:load --focus architecture new-codebase/

# Systematic exploration
/sg:analyze --introspect --seq codebase-structure/
/sg:explain "complex-architectural-patterns"

# Knowledge consolidation
/sg:reflect --type learning
/sg:document --type architecture-notes findings/
/sg:save "architecture-understanding-session"
```

### Code Review Session
```bash
# Load changes context
/sg:load --focus quality pending-changes/

# Comprehensive review
/sg:analyze --focus quality --seq changes/
/sg:test --focus regression change-areas/

# Quality assessment
/sg:reflect --type quality
/sg:document --type review-notes quality-assessment/
/sg:save "code-review-complete"
```

**Session Optimization Patterns:**

**Short Sessions (1-2 hours):**
- Quick load with specific focus
- Targeted work on single component
- Checkpoint saves for continuity

**Medium Sessions (Half-day):**
- Comprehensive load and planning
- Multi-component development
- Regular checkpoints and quality reviews

**Long Sessions (Full-day):**
- Full context loading and analysis
- Complex feature development cycles
- Multiple validation and reflection points

## Multi-Session Projects

**Long-Term Project Management:**

### Project Session Architecture
```bash
# Master Project Session
/sg:load enterprise-platform/
→ Maintains overall project context and architecture understanding

# Feature Branch Sessions  
/sg:load --branch feature/user-management user-service/
/sg:load --branch feature/payment-integration payment-service/
→ Focused context for specific feature development

# Integration Sessions
/sg:load --integration-focus platform-services/
→ Cross-service integration and system-level concerns
```

### Session Hierarchy Management

**Project Level (Months):**
- Overall architecture and system understanding
- Cross-cutting concerns and integration patterns
- Long-term technical decisions and evolution

**Epic Level (Weeks):**
- Feature set implementation and integration
- Domain-specific patterns and conventions
- Epic-level progress and quality tracking

**Story Level (Days):**
- Individual feature implementation
- Component-level development and testing
- Story completion and handoff

**Session Coordination Patterns:**

**Team Coordination:**
```bash
# Shared Project Context
/sg:load --shared team-project/
→ Common understanding accessible to all team members

# Individual Developer Sessions
/sg:load --developer alice team-project/user-auth/
/sg:load --developer bob team-project/payment-system/
→ Personal development context within shared project

# Integration Sessions
/sg:load --integration team-project/
→ Cross-developer integration and system-level work
```

**Cross-Session Continuity:**

**Session Handoff:**
```bash
# End of developer session
/sg:save --handoff "alice-user-auth-complete" --next-developer bob

# New developer pickup
/sg:load --handoff "alice-user-auth-complete"
→ Complete context transfer with work continuation
```

**Progress Synchronization:**
```bash
# Daily standup preparation
/sg:reflect --type team-progress
→ Team-level progress summary and coordination

# Sprint planning context
/sg:load --sprint-context team-project/
→ Sprint-level understanding and planning context
```

**Long-Term Memory Evolution:**

**Memory Consolidation:**
- Weekly: Consolidate daily insights into persistent patterns
- Monthly: Archive completed features, preserve key learnings  
- Quarterly: Architectural review and pattern evolution

**Memory Inheritance:**
- New features inherit patterns from completed work
- Team members inherit shared conventions and decisions
- Project evolution builds on accumulated architectural understanding

## Session Troubleshooting

**Common Session Issues:**

### Session Context Lost
**Problem**: `/sg:load` doesn't restore expected context
```bash
# Symptoms
/sg:load project/
→ "No previous session found" or minimal context restored
```

**Solutions:**
```bash
# 1. Check available sessions
/sg:load --list-sessions

# 2. Load by specific session name
/sg:load "session-name"

# 3. Fresh analysis if needed
/sg:load --refresh --comprehensive project/

# 4. Check Serena MCP status
SuperGemini status --mcp serena
```

### Memory Fragmentation
**Problem**: Session memory becomes inconsistent or incomplete
```bash
# Symptoms
- Conflicting pattern suggestions
- Missing context for recent work
- Inconsistent architectural understanding
```

**Solutions:**
```bash
# 1. Memory consolidation
/sg:reflect --type memory-health
/sg:save --consolidate "clean-session-state"

# 2. Selective memory refresh
/sg:load --refresh-memory specific-area/

# 3. Clean session restart
/sg:save --archive "old-session"
/sg:load --fresh project/
```

### Session Performance Issues
**Problem**: Slow session loading or excessive memory usage
```bash
# Symptoms
- Long load times (>30 seconds)
- Memory warnings during operation
- Reduced response quality
```

**Solutions:**
```bash
# 1. Optimize session scope
/sg:load --scope module target-area/

# 2. Use focused loading
/sg:load --focus performance specific-concern/

# 3. Memory cleanup
/sg:save --cleanup "optimized-session"

# 4. Check system resources
SuperGemini diagnose --memory
```

### Integration Conflicts
**Problem**: Multi-session project coordination issues
```bash
# Symptoms
- Conflicting architectural decisions
- Integration pattern mismatches
- Cross-team context confusion
```

**Solutions:**
```bash
# 1. Sync with master session
/sg:load --sync-master project/

# 2. Resolve conflicts explicitly
/sg:reflect --type integration-conflicts
/sg:resolve-conflicts --strategy team-lead-wins

# 3. Re-establish shared context
/sg:load --shared-refresh team-project/
```

**Session Recovery Procedures:**

### Emergency Session Recovery
```bash
# 1. Check session backups
/sg:load --list-backups

# 2. Restore from backup
/sg:load --restore-backup "backup-timestamp"

# 3. Partial recovery if needed
/sg:load --partial-restore specific-components/

# 4. Rebuild from artifacts
/sg:load --rebuild-from git-history project/
```

### Session Health Monitoring
```bash
# Regular health checks
/sg:reflect --type session-health
→ Memory consistency, context completeness, performance metrics

# Memory optimization
/sg:save --optimize "clean-session"
→ Consolidate insights, remove redundant context

# Performance tuning
/sg:load --performance-mode project/
→ Optimized loading for resource-constrained environments
```

**Best Practices for Session Reliability:**

1. **Regular Saves**: Save at natural breakpoints and end of work
2. **Descriptive Names**: Use clear, descriptive session names
3. **Health Monitoring**: Regular reflection and health checks
4. **Backup Strategy**: Multiple checkpoint saves during long work
5. **Scope Management**: Load only necessary context for current work
6. **Memory Hygiene**: Periodic consolidation and cleanup

## Related Guides

**Learning Progression:**

**🌱 Essential (Week 1)**
- [Quick Start Guide](../Getting-Started/quick-start.md) - First session experience
- [Commands Reference](commands.md) - Session commands (/sg:load, /sg:save, /sg:reflect)
- [Installation Guide](../Getting-Started/installation.md) - Serena MCP setup for sessions

**🌿 Intermediate (Week 2-3)**
- [MCP Servers Guide](mcp-servers.md) - Serena MCP for persistent memory
- [Behavioral Modes](modes.md) - Task Management mode for session coordination
- [Agents Guide](agents.md) - Agent persistence across sessions

**🌲 Advanced (Month 2+)**
- [Best Practices](../Reference/best-practices.md) - Session optimization strategies
- [Examples Cookbook](../Reference/examples-cookbook.md) - Multi-session project patterns
- [Flags Guide](flags.md) - Session control flags and optimization

**🔧 Expert**
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - Session implementation details
- [Contributing Code](../Developer-Guide/contributing-code.md) - Extending session capabilities

**Session-Specific Learning:**

**🎯 Session Command Mastery:**
- **Load Patterns**: `/sg:load` variations for different contexts
- **Save Strategies**: Checkpoint vs milestone vs completion saves
- **Reflection Types**: Progress, quality, completion, learning assessments

**🧠 Memory Management:**
- **Context Building**: How memory accumulates and evolves
- **Pattern Recognition**: Understanding session intelligence
- **Memory Optimization**: Efficient context management

**👥 Team Coordination:**
- **Shared Sessions**: Multi-developer session coordination
- **Handoff Patterns**: Session transfer and continuity
- **Integration Sessions**: Cross-team collaboration

**🔄 Project Lifecycle:**
- **Daily Workflows**: Effective day-to-day session patterns
- **Feature Cycles**: Multi-session feature development
- **Long-term Projects**: Enterprise-scale session management

**💡 Session Mastery Tips:**
- **Start Small**: Begin with simple load-work-save patterns
- **Build Habits**: Regular reflection and checkpoint saves
- **Learn Memory**: Understand how context builds over time
- **Optimize Gradually**: Advanced patterns as projects grow
- **Monitor Health**: Regular session health and performance checks

**Common Session Workflows:**
- **New Project**: Load → Analyze → Plan → Save
- **Daily Work**: Load → Progress check → Work → Checkpoint → Save
- **Feature Development**: Load → Brainstorm → Implement → Test → Reflect → Save
- **Bug Investigation**: Load focused → Troubleshoot → Fix → Validate → Save
- **Code Review**: Load changes → Analyze quality → Review → Document → Save