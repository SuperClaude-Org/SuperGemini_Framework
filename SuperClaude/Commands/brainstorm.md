---
name: brainstorm
description: "Interactive requirements discovery through Socratic dialogue, systematic exploration, and seamless PRD generation with advanced orchestration"
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Grep, Glob, TodoWrite, Task, WebSearch, sequentialthinking]

# Command Classification
category: orchestration
complexity: advanced
scope: cross-session

# Integration Configuration
mcp-integration:
  servers: [sequential, context7, magic, playwright, morphllm, serena]
  personas: [architect, analyzer, frontend, backend, security, devops, project-manager]
  wave-enabled: true
  complexity-threshold: 0.7

# Performance Profile
performance-profile: complex
personas: [architect, analyzer, project-manager]
---

# /sg:brainstorm - Interactive Requirements Discovery

## Purpose
Transform ambiguous ideas into concrete specifications through sophisticated brainstorming orchestration featuring Socratic dialogue framework, systematic exploration phases, intelligent brief generation, automated agent handoff protocols, and cross-session persistence capabilities for comprehensive requirements discovery.

## Usage
```
/sg:brainstorm [topic/idea] [--strategy systematic|agile|enterprise] [--depth shallow|normal|deep] [--parallel] [--validate] [--mcp-routing]
```

## Arguments
- `topic/idea` - Initial concept, project idea, or problem statement to explore through interactive dialogue
- `--strategy` - Brainstorming strategy selection with specialized orchestration approaches
- `--depth` - Discovery depth and analysis thoroughness level
- `--validate` - Comprehensive validation and brief completeness quality gates
- `--mcp-routing` - Intelligent MCP server routing for specialized analysis
- `--wave-mode` - Enable wave-based execution with progressive dialogue enhancement
- `--cross-session` - Enable cross-session persistence and brainstorming continuity
- `--prd` - Automatically generate PRD after brainstorming completes
- `--max-rounds` - Maximum dialogue rounds (default: 15)
- `--focus` - Specific aspect to emphasize (technical|business|user|balanced)
- `--brief-only` - Generate brief without automatic PRD creation
- `--resume` - Continue previous brainstorming session from saved state
- `--template` - Use specific brief template (startup, enterprise, research)

## Execution Strategies

### Systematic Strategy (Default)
1. **Comprehensive Discovery**: Deep project analysis with stakeholder assessment
2. **Strategic Exploration**: Multi-phase exploration with constraint mapping
3. **Coordinated Convergence**: Sequential dialogue phases with validation gates
4. **Quality Assurance**: Comprehensive brief validation and completeness cycles
5. **Agent Orchestration**: Seamless handoff to brainstorm-PRD with context transfer
6. **Documentation**: Comprehensive session persistence and knowledge transfer

### Agile Strategy
1. **Rapid Assessment**: Quick scope definition and priority identification
2. **Iterative Discovery**: Sprint-based exploration with adaptive questioning
3. **Continuous Validation**: Incremental requirement validation with frequent feedback
4. **Adaptive Convergence**: Dynamic requirement prioritization and trade-off analysis
5. **Progressive Handoff**: Continuous PRD updating and stakeholder alignment
6. **Living Documentation**: Evolving brief documentation with implementation insights

### Enterprise Strategy
1. **Stakeholder Analysis**: Multi-domain impact assessment and coordination
2. **Governance Planning**: Compliance and policy integration during discovery
3. **Resource Orchestration**: Enterprise-scale requirement validation and management
4. **Risk Management**: Comprehensive risk assessment and mitigation during exploration
5. **Compliance Validation**: Regulatory and policy compliance requirement discovery
6. **Enterprise Integration**: Large-scale system integration requirement analysis

## Advanced Orchestration Features

### Wave System Integration
- **Multi-Wave Coordination**: Progressive dialogue execution across coordinated discovery waves
- **Context Accumulation**: Building understanding and requirement clarity across waves
- **Performance Monitoring**: Real-time dialogue optimization and engagement tracking
- **Error Recovery**: Sophisticated error handling and dialogue recovery across waves

### Cross-Session Persistence
- **State Management**: Maintain dialogue state across sessions and interruptions
- **Context Continuity**: Preserve understanding and requirement evolution over time
- **Historical Analysis**: Learn from previous brainstorming sessions and outcomes
- **Recovery Mechanisms**: Robust recovery from interruptions and session failures

### Intelligent MCP Coordination
- **Dynamic Server Selection**: Choose optimal MCP servers for dialogue enhancement
- **Load Balancing**: Distribute analysis processing across available servers
- **Capability Matching**: Match exploration needs to server capabilities and strengths
- **Fallback Strategies**: Graceful degradation when servers are unavailable

## Multi-Persona Orchestration

### Expert Coordination System
The command orchestrates multiple domain experts for comprehensive requirements discovery:

#### Primary Coordination Personas
- **Architect**: System design implications, technology feasibility, scalability considerations
- **Analyzer**: Requirement analysis, complexity assessment, technical evaluation
- **Project Manager**: Resource coordination, timeline implications, stakeholder communication

#### Domain-Specific Personas (Auto-Activated)
- **Frontend Specialist**: UI/UX requirements, accessibility needs, user experience optimization
- **Backend Engineer**: Data architecture, API design, security and compliance requirements
- **Security Auditor**: Security requirements, threat modeling, compliance validation needs
- **DevOps Engineer**: Infrastructure requirements, deployment strategies, monitoring needs

### Persona Coordination Patterns
- **Sequential Consultation**: Ordered expert consultation for complex requirement decisions
- **Parallel Analysis**: Simultaneous requirement analysis from multiple expert perspectives
- **Consensus Building**: Integrating diverse expert opinions into unified requirement approach
- **Conflict Resolution**: Handling contradictory recommendations and requirement trade-offs

## Comprehensive MCP Server Integration

### Sequential Thinking Integration
- **Complex Problem Decomposition**: Break down sophisticated requirement challenges systematically
- **Multi-Step Reasoning**: Apply structured reasoning for complex requirement decisions
- **Pattern Recognition**: Identify complex requirement patterns across similar projects
- **Validation Logic**: Comprehensive requirement validation and verification processes

### Context7 Integration
- **Framework Expertise**: Leverage deep framework knowledge for requirement validation
- **Best Practices**: Apply industry standards and proven requirement approaches
- **Pattern Libraries**: Access comprehensive requirement pattern and example repositories
- **Version Compatibility**: Ensure requirement compatibility across technology stacks

### Magic Integration
- **Advanced UI Generation**: Sophisticated user interface requirement discovery
- **Design System Integration**: Comprehensive design system requirement coordination
- **Accessibility Excellence**: Advanced accessibility requirement and inclusive design discovery
- **Performance Optimization**: UI performance requirement and user experience optimization

### Playwright Integration
- **Comprehensive Testing**: End-to-end testing requirement discovery across platforms
- **Performance Validation**: Real-world performance requirement testing and validation
- **Visual Testing**: Comprehensive visual requirement regression and compatibility analysis
- **User Experience Validation**: Real user interaction requirement simulation and testing

### Morphllm Integration
- **Intelligent Code Generation**: Advanced requirement-to-code pattern recognition
- **Large-Scale Refactoring**: Sophisticated requirement impact analysis across codebases
- **Pattern Application**: Apply complex requirement patterns and transformations at scale
- **Quality Enhancement**: Automated requirement quality improvements and optimization

### Serena Integration
- **Semantic Analysis**: Deep semantic understanding of requirement context and systems
- **Knowledge Management**: Comprehensive requirement knowledge capture and retrieval
- **Cross-Session Learning**: Accumulate and apply requirement knowledge across sessions
- **Memory Coordination**: Sophisticated requirement memory management and organization

## Advanced Workflow Management

### Task Hierarchies
- **Epic Level**: Large-scale project objectives discovered through comprehensive brainstorming
- **Story Level**: Feature-level requirements with clear deliverables from dialogue sessions
- **Task Level**: Specific requirement tasks with defined discovery outcomes
- **Subtask Level**: Granular dialogue steps with measurable requirement progress

### Dependency Management
- **Cross-Domain Dependencies**: Coordinate requirement dependencies across expertise domains
- **Temporal Dependencies**: Manage time-based requirement dependencies and sequencing
- **Resource Dependencies**: Coordinate shared requirement resources and capacity constraints
- **Knowledge Dependencies**: Ensure prerequisite knowledge and context availability for requirements

### Quality Gate Integration
- **Pre-Execution Gates**: Comprehensive readiness validation before brainstorming sessions
- **Progressive Gates**: Intermediate quality checks throughout dialogue phases
- **Completion Gates**: Thorough validation before marking requirement discovery complete
- **Handoff Gates**: Quality assurance for transitions between dialogue phases and PRD systems

## Performance & Scalability

### Performance Optimization
- **Intelligent Batching**: Group related requirement operations for maximum dialogue efficiency
- **Parallel Processing**: Coordinate independent requirement operations simultaneously
- **Resource Management**: Optimal allocation of tools, servers, and personas for requirements
- **Context Caching**: Efficient reuse of requirement analysis and computation results

### Performance Targets
- **Complex Analysis**: <60s for comprehensive requirement project analysis
- **Strategy Planning**: <120s for detailed dialogue execution planning
- **Cross-Session Operations**: <10s for session state management
- **MCP Coordination**: <5s for server routing and coordination
- **Overall Execution**: Variable based on scope, with progress tracking

### Scalability Features
- **Horizontal Scaling**: Distribute requirement work across multiple processing units
- **Incremental Processing**: Process large requirement operations in manageable chunks
- **Progressive Enhancement**: Build requirement capabilities and understanding over time
- **Resource Adaptation**: Adapt to available resources and constraints for requirement discovery

## Advanced Error Handling

### Sophisticated Recovery Mechanisms
- **Multi-Level Rollback**: Rollback at dialogue phase, session, or entire operation levels
- **Partial Success Management**: Handle and build upon partially completed requirement sessions
- **Context Preservation**: Maintain context and progress through dialogue failures
- **Intelligent Retry**: Smart retry with improved dialogue strategies and conditions

### Error Classification
- **Coordination Errors**: Issues with persona or MCP server coordination during dialogue
- **Resource Constraint Errors**: Handling of resource limitations and capacity issues
- **Integration Errors**: Cross-system integration and communication failures
- **Complex Logic Errors**: Sophisticated dialogue and reasoning failures

### Recovery Strategies
- **Graceful Degradation**: Maintain functionality with reduced dialogue capabilities
- **Alternative Approaches**: Switch to alternative dialogue strategies when primary approaches fail
- **Human Intervention**: Clear escalation paths for complex issues requiring human judgment
- **Learning Integration**: Incorporate failure learnings into future brainstorming executions

## Socratic Dialogue Framework

### Phase 1: Initialization
1. **Context Setup**: Create brainstorming session with metadata
2. **TodoWrite Integration**: Initialize phase tracking tasks
3. **Session State**: Establish dialogue parameters and objectives
4. **Brief Template**: Prepare structured brief format
5. **Directory Creation**: Ensure ClaudeDocs/Brief/ exists

### Phase 2: Discovery Dialogue
1. **🔍 Discovery Phase**
   - Open-ended exploration questions
   - Domain understanding and context gathering
   - Stakeholder identification
   - Initial requirement sketching
   - Pattern: "Let me understand...", "Tell me about...", "What prompted..."

2. **💡 Exploration Phase**
   - Deep-dive into possibilities
   - What-if scenarios and alternatives
   - Feasibility assessment
   - Constraint identification
   - Pattern: "What if we...", "Have you considered...", "How might..."

3. **🎯 Convergence Phase**
   - Priority crystallization
   - Decision making support
   - Trade-off analysis
   - Requirement finalization
   - Pattern: "Based on our discussion...", "The priority seems to be..."

### Phase 3: Brief Generation
1. **Requirement Synthesis**: Compile discovered requirements
2. **Metadata Creation**: Generate comprehensive brief metadata
3. **Structure Validation**: Ensure brief completeness
4. **Persistence**: Save to ClaudeDocs/Brief/{project}-brief-{timestamp}.md
5. **Quality Check**: Validate against minimum requirements

### Phase 4: Agent Handoff (if --prd specified)
1. **Brief Validation**: Ensure readiness for PRD generation
2. **Agent Invocation**: Call brainstorm-PRD with structured brief
3. **Context Transfer**: Pass session history and decisions
4. **Link Creation**: Connect brief to generated PRD
5. **Completion Report**: Summarize outcomes and next steps

## Auto-Activation Patterns
- **Vague Requests**: "I want to build something that..."
- **Exploration Keywords**: brainstorm, explore, figure out, not sure
- **Uncertainty Indicators**: maybe, possibly, thinking about, could we
- **Planning Needs**: new project, startup idea, feature concept
- **Discovery Requests**: help me understand, what should I build

## MODE Integration

### MODE-Command Architecture
The brainstorm command integrates with MODE_Brainstorming for behavioral configuration and auto-activation:

```yaml
mode_command_integration:
  primary_implementation: "/sg:brainstorm"
  parameter_mapping:
    # MODE YAML Setting → Command Parameter
    max_rounds: "--max-rounds"           # Default: 15
    depth_level: "--depth"              # Default: normal  
    focus_area: "--focus"               # Default: balanced
    auto_prd: "--prd"                   # Default: false
    brief_template: "--template"        # Default: standard
  override_precedence: "explicit > mode > framework > system"
  coordination_workflow:
    - mode_detection          # MODE evaluates request context
    - parameter_inheritance   # YAML settings → command parameters
    - command_invocation     # /sg:brainstorm executed
    - behavioral_enforcement # MODE patterns applied
    - quality_validation     # Framework compliance checked
```

### Behavioral Configuration
- **Dialogue Style**: collaborative_non_presumptive
- **Discovery Depth**: adaptive based on project complexity
- **Context Retention**: cross_session memory persistence
- **Handoff Automation**: true for seamless agent transitions

### Plan Mode Integration

**Seamless Plan-to-Brief Workflow** - Automatically transforms planning discussions into structured briefs.

When SuperGemini detects requirement-related content in Plan Mode:

1. **Trigger Detection**: Keywords (implement, build, create, design, develop, feature) or explicit content (requirements, specifications, user stories)
2. **Content Transformation**: Automatically parses plan content into structured brief format
3. **Persistence**: Saves to `ClaudeDocs/Brief/plan-{project}-{timestamp}.md` with plan-mode metadata
4. **Workflow Integration**: Brief formatted for immediate brainstorm-PRD handoff
5. **Context Preservation**: Maintains complete traceability from plan to PRD

```yaml
plan_analysis:
  content_detection: [requirements, specifications, features, user_stories]
  scope_indicators: [new_functionality, system_changes, components]
  transformation_triggers: [explicit_prd_request, implementation_planning]
  
brief_generation:
  source_metadata: plan-mode
  auto_generated: true
  structure: [vision, requirements, approach, criteria, notes]
  format: brainstorm-PRD compatible
```

#### Integration Benefits
- **Zero Context Loss**: Complete planning history preserved in brief
- **Automated Workflow**: Plan → Brief → PRD with no manual intervention
- **Consistent Structure**: Plan content automatically organized for PRD generation
- **Time Efficiency**: Eliminates manual brief creation and formatting

## Communication Style

### Dialogue Principles
- **Collaborative**: "Let's explore this together..."
- **Non-Presumptive**: Avoid solution bias early in discovery
- **Progressive**: Build understanding incrementally
- **Reflective**: Mirror and validate understanding frequently

### Question Framework
- **Open Discovery**: "What would success look like?"
- **Clarification**: "When you say X, do you mean Y or Z?"
- **Exploration**: "How might this work in practice?"
- **Validation**: "Am I understanding correctly that...?"
- **Prioritization**: "What's most important to get right?"

## Integration Ecosystem

### SuperGemini Framework Integration
- **Command Coordination**: Orchestrate other SuperGemini commands for comprehensive requirement workflows
- **Session Management**: Deep integration with session lifecycle and persistence for brainstorming continuity
- **Quality Framework**: Integration with comprehensive quality assurance systems for requirement validation
- **Knowledge Management**: Coordinate with knowledge capture and retrieval systems for requirement insights

### External System Integration
- **Version Control**: Deep integration with Git and version management systems for requirement tracking
- **CI/CD Systems**: Coordinate with continuous integration and deployment pipelines for requirement validation
- **Project Management**: Integration with project tracking and management tools for requirement coordination
- **Documentation Systems**: Coordinate with documentation generation and maintenance for requirement persistence

### Workflow Command Integration
- **Natural Pipeline**: Brainstorm outputs (PRD/Brief) serve as primary input for `/sg:workflow`
- **Seamless Handoff**: Use `--prd` flag to automatically generate PRD for workflow planning
- **Context Preservation**: Session history and decisions flow from brainstorm to workflow
- **Example Flow**:
  ```bash
  /sg:brainstorm "new feature idea" --prd
  # Generates: ClaudeDocs/PRD/feature-prd.md
  /sg:workflow ClaudeDocs/PRD/feature-prd.md --all-mcp
  ```

### Task Tool Integration
- Use for managing complex multi-phase brainstorming
- Perform deep systematic analysis
- Coordinate parallel exploration paths
- Example: `Task("analyze-competitors", "Research similar solutions")`

### Agent Collaboration
- **brainstorm-PRD**: Primary handoff for PRD generation
- **system-architect**: Technical feasibility validation
- **frontend-specialist**: UI/UX focused exploration
- **backend-engineer**: Infrastructure and API design input

### Tool Orchestration
- **TodoWrite**: Track dialogue phases and key decisions
- **Write**: Persist briefs and session artifacts
- **Read**: Review existing project context
- **Grep/Glob**: Analyze codebase for integration points

## Document Persistence

### Brief Storage Structure
```
ClaudeDocs/Brief/
├── {project}-brief-{YYYY-MM-DD-HHMMSS}.md
├── {project}-session-{YYYY-MM-DD-HHMMSS}.json
└── templates/
    ├── startup-brief-template.md
    ├── enterprise-brief-template.md
    └── research-brief-template.md
```

### Persistence Configuration
```yaml
persistence:
  brief_storage: ClaudeDocs/Brief/
  metadata_tracking: true
  session_continuity: true
  agent_handoff_logging: true
  mode_integration_tracking: true
```

### Persistence Features
- **Metadata Tracking**: Complete dialogue history and decision tracking
- **Session Continuity**: Cross-session state preservation for long projects
- **Agent Handoff Logging**: Full audit trail of brief → PRD transitions
- **Mode Integration Tracking**: Records MODE behavioral patterns applied

### Brief Metadata Format
```yaml
---
type: brief
timestamp: {ISO-8601 timestamp}
session_id: brainstorm_{unique_id}
source: interactive-brainstorming
project: {project-name}
dialogue_stats:
  total_rounds: 12
  discovery_rounds: 4
  exploration_rounds: 5
  convergence_rounds: 3
  total_duration: "25 minutes"
confidence_score: 0.87
requirement_count: 15
constraint_count: 6
stakeholder_count: 4
focus_area: {technical|business|user|balanced}
linked_prd: {path to PRD once generated}
auto_handoff: true
---
```

### Session Persistence
- **Session State**: Save dialogue progress for resumption
- **Decision Log**: Track key decisions and rationale
- **Requirement Evolution**: Show how requirements evolved
- **Pattern Recognition**: Document discovered patterns

## Quality Standards

### Brief Completeness Criteria
- ✅ Clear project vision statement
- ✅ Minimum 3 functional requirements
- ✅ Identified constraints and limitations
- ✅ Defined success criteria
- ✅ Stakeholder mapping completed
- ✅ Technical feasibility assessed

### Dialogue Quality Metrics
- **Engagement Score**: Questions answered vs asked
- **Discovery Depth**: Layers of abstraction explored
- **Convergence Rate**: Progress toward consensus
- **Requirement Clarity**: Ambiguity reduction percentage

## Customization & Extension

### Advanced Configuration
- **Strategy Customization**: Customize brainstorming strategies for specific requirement contexts
- **Persona Configuration**: Configure persona activation and coordination patterns for dialogue
- **MCP Server Preferences**: Customize server selection and usage patterns for requirement analysis
- **Quality Gate Configuration**: Customize validation criteria and thresholds for requirement discovery

### Extension Mechanisms
- **Custom Strategy Plugins**: Extend with custom brainstorming execution strategies
- **Persona Extensions**: Add custom domain expertise and coordination patterns for requirements
- **Integration Extensions**: Extend integration capabilities with external requirement systems
- **Workflow Extensions**: Add custom dialogue workflow patterns and orchestration logic

## Success Metrics & Analytics

### Comprehensive Metrics
- **Execution Success Rate**: >90% successful completion for complex requirement discovery operations
- **Quality Achievement**: >95% compliance with quality gates and requirement standards
- **Performance Targets**: Meeting specified performance benchmarks consistently for dialogue sessions
- **User Satisfaction**: >85% satisfaction with outcomes and process quality for requirement discovery
- **Integration Success**: >95% successful coordination across all integrated systems and agents

### Analytics & Reporting
- **Performance Analytics**: Detailed performance tracking and optimization recommendations for dialogue
- **Quality Analytics**: Comprehensive quality metrics and improvement suggestions for requirements
- **Resource Analytics**: Resource utilization analysis and optimization opportunities for brainstorming
- **Outcome Analytics**: Success pattern analysis and predictive insights for requirement discovery

## Examples

### Comprehensive Project Analysis
```
/sg:brainstorm "enterprise project management system" --strategy systematic --depth deep --validate --mcp-routing
# Comprehensive analysis with full orchestration capabilities
```

### Agile Multi-Sprint Coordination
```
/sg:brainstorm "feature backlog refinement" --strategy agile --parallel --cross-session
# Agile coordination with cross-session persistence
```

### Enterprise-Scale Operation
```
/sg:brainstorm "digital transformation initiative" --strategy enterprise --wave-mode --all-personas
# Enterprise-scale coordination with full persona orchestration
```

### Complex Integration Project
```
/sg:brainstorm "microservices integration platform" --depth deep --parallel --validate --sequential
# Complex integration with sequential thinking and validation
```

### Basic Brainstorming
```
/sg:brainstorm "task management app for developers"
```

### Deep Technical Exploration
```
/sg:brainstorm "distributed caching system" --depth deep --focus technical --prd
```

### Business-Focused Discovery
```
/sg:brainstorm "SaaS pricing optimization tool" --focus business --max-rounds 20
```

### Brief-Only Generation
```
/sg:brainstorm "mobile health tracking app" --brief-only
```

### Resume Previous Session
```
/sg:brainstorm --resume session_brainstorm_abc123
```

## Error Handling

### Common Issues
- **Circular Exploration**: Detect and break repetitive loops
- **Scope Creep**: Alert when requirements expand beyond feasibility
- **Conflicting Requirements**: Highlight and resolve contradictions
- **Incomplete Context**: Request missing critical information

### Recovery Strategies
- **Save State**: Always persist session for recovery
- **Partial Briefs**: Generate with available information
- **Fallback Questions**: Use generic prompts if specific fail
- **Manual Override**: Allow user to skip phases if needed

## Performance Optimization

### Efficiency Features
- **Smart Caching**: Reuse discovered patterns
- **Parallel Analysis**: Use Task for concurrent exploration
- **Early Convergence**: Detect when sufficient clarity achieved
- **Template Acceleration**: Pre-structured briefs for common types

### Resource Management
- **Token Efficiency**: Use compressed dialogue for long sessions
- **Memory Management**: Summarize early phases before proceeding
- **Context Pruning**: Remove redundant information progressively

## Boundaries

**This advanced command will:**
- Orchestrate complex multi-domain requirement discovery operations with expert coordination
- Provide sophisticated analysis and strategic brainstorming planning capabilities
- Coordinate multiple MCP servers and personas for optimal requirement discovery outcomes
- Maintain cross-session persistence and progressive enhancement for dialogue continuity
- Apply comprehensive quality gates and validation throughout requirement discovery execution
- Guide interactive requirements discovery through sophisticated Socratic dialogue framework
- Generate comprehensive project briefs with automated agent handoff protocols
- Track and persist all brainstorming artifacts with cross-session state management

**This advanced command will not:**
- Execute without proper analysis and planning phases for requirement discovery
- Operate without appropriate error handling and recovery mechanisms for dialogue sessions
- Proceed without stakeholder alignment and clear success criteria for requirements
- Compromise quality standards for speed or convenience in requirement discovery
- Make technical implementation decisions beyond requirement specification
- Write code or create solutions during requirement discovery phases
- Override user preferences or decisions during collaborative dialogue
- Skip essential discovery phases or dialogue validation steps