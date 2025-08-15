# Sequential MCP Server

## Purpose
Multi-step problem solving, architectural analysis, systematic debugging

## Activation Patterns

**Automatic Activation**:
- Complex debugging scenarios requiring systematic investigation
- System design questions needing structured analysis
- Complex analysis requirements and systematic thinking needs
- Multi-step problems requiring decomposition and analysis

**Manual Activation**:
- Flag: `--seq`, `--sequential`

**Smart Detection**:
- Multi-step reasoning patterns detected in user queries
- Complex architectural or system-level questions
- Problems requiring hypothesis testing and validation
- Iterative refinement or improvement workflows

## Flags

**`--seq` / `--sequential`**
- Enable Sequential for complex multi-step analysis
- Auto-activates: Complex debugging, system design, multi-step analysis
- Detection: debug/trace/analyze keywords, nested conditionals, async chains

**`--no-seq` / `--no-sequential`**
- Disable Sequential server
- Fallback: Native Gemini CLI analysis
- Performance: 10-30% faster for simple tasks

## Workflow Process

1. **Problem Decomposition**: Break complex problems into analyzable components
2. **Server Coordination**: Coordinate with Context7 for documentation, Magic for UI insights, Playwright for testing
3. **Systematic Analysis**: Apply structured thinking to each component
4. **Relationship Mapping**: Identify dependencies, interactions, and feedback loops
5. **Hypothesis Generation**: Create testable hypotheses for each component
6. **Evidence Gathering**: Collect supporting evidence through tool usage
7. **Multi-Server Synthesis**: Combine findings from multiple servers
8. **Recommendation Generation**: Provide actionable next steps with priority ordering
9. **Validation**: Check reasoning for logical consistency

## Integration Points

**Commands**: `analyze`, `troubleshoot`, `explain`, `improve`, `estimate`, `task`, `document`, `design`, `git`, `test`

**Thinking Modes**: 
- `--seq`: Enable Sequential analysis for complex multi-step problems and systematic analysis with structured approach
- `--seq`: Sequential analysis for complex multi-step problems

**Other MCP Servers**: 
- Context7: Documentation lookup and pattern verification
- Magic: UI component analysis and insights
- Playwright: Testing validation and performance analysis

## Strategic Orchestration

### When to Use Sequential
- **Complex Debugging**: Multi-layer issues requiring systematic investigation
- **Architecture Planning**: System design requiring structured analysis
- **Performance Optimization**: Bottleneck identification needing methodical approach
- **Risk Assessment**: Security or compliance analysis requiring comprehensive coverage
- **Cross-Domain Problems**: Issues spanning multiple technical domains

### Multi-Server Orchestration Patterns
- **Analysis Coordination**: Sequential coordinates analysis across Context7, Magic, Playwright
- **Evidence Synthesis**: Combines findings from multiple servers into cohesive insights
- **Progressive Enhancement**: Iterative improvement cycles with quality validation
- **Hypothesis Testing**: Structured validation of assumptions across server capabilities

### Advanced Reasoning Strategies
- **Parallel Analysis Streams**: Multiple reasoning chains explored simultaneously
- **Cross-Domain Validation**: Findings validated across different technical domains
- **Dependency Chain Mapping**: Complex system relationships analyzed systematically
- **Risk-Weighted Decision Making**: Solutions prioritized by impact and implementation complexity
- **Continuous Learning Integration**: Patterns and outcomes fed back into analysis models

## Use Cases

- **Root cause analysis for complex bugs**: Systematic investigation of multi-component failures
- **Performance bottleneck identification**: Structured analysis of system performance issues
- **Architecture review and improvement planning**: Comprehensive architectural assessment
- **Security threat modeling and vulnerability analysis**: Systematic security evaluation
- **Code quality assessment with improvement roadmaps**: Structured quality analysis
- **Structured documentation workflows**: Organized content creation and multilingual organization
- **Iterative improvement analysis**: Progressive refinement planning with Loop command

## Error Recovery

- **Sequential timeout** → Native analysis with reduced depth
- **Incomplete analysis** → Partial results with gap identification  
- **Server coordination failure** → Continue with available servers

## Quality Gates Integration

- **Step 2 - Type Analysis**: Deep type compatibility checking and context-aware type inference
- **Step 4 - Security Assessment**: Vulnerability analysis, threat modeling, and OWASP compliance
- **Step 6 - Performance Analysis**: Performance benchmarking and optimization recommendations