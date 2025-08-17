# SemanticPrompt MCP Server

**Purpose**: 4-step SuperGemini Framework thinking engine with automatic sg command integration and agent persona orchestration

**Tool Name**: `chain_of_thought`

**Activation**: Available through `/sg:cot` command in SuperGemini Framework

## Triggers
- Complex multi-step problems requiring structured reasoning
- Tasks needing systematic command selection and agent coordination
- SuperGemini Framework workflows with TOML-based guidance
- Chain-of-thought reasoning for Gemini CLI operations
- Agent persona extraction and embodiment scenarios
- Document tracking and meta-cognitive attention requirements

## Choose When
- **Over simple responses**: When tasks require 3+ reasoning steps
- **For framework integration**: SuperGemini workflows needing TOML command guidance
- **For agent coordination**: Multi-agent problem solving with specialized perspectives
- **For systematic execution**: 90% command preference with intelligent skip detection
- **Not for trivial tasks**: Simple explanations, basic information recall, greeting responses

## Works Best With
- **Context7**: SemanticPrompt coordinates reasoning → Context7 provides framework patterns
- **Sequential**: SemanticPrompt structures thinking → Sequential executes deep analysis
- **Magic**: SemanticPrompt selects approach → Magic implements UI components
- **All MCP Servers**: Central orchestration engine for multi-server coordination

## 4-Step Framework Process

### Step 1: Intent Analysis
- Analyze user intent, files involved, expected outcome
- Identify complexity level and reasoning requirements
- Determine if systematic execution is needed

### Step 2: Command Selection (MANDATORY - 90% Preference)
- Strong preference for sg commands over direct responses
- Automatic TOML document reading and guidance extraction
- Skip only when ALL conditions met: ≤2 lines response, no files, no analysis, pure recall
- Available commands: analyze, build, cleanup, design, document, estimate, explain, git, implement, improve, index, load, reflect, save, select-tool, test, troubleshoot

### Step 3: Agent Persona Extraction
- Extract agents array from selected TOML command files
- Read individual agent definitions from ~/.gemini/agents/{agents}.md
- Reference AGENTS.md for additional context and coordination
- Prevent duplicate agent reads using system-reminder optimization

### Step 4: Agent Embodiment & Execution
- Embody extracted agent personas with specialized knowledge
- Multi-agent coordination for complex problems
- Execute solutions using agent methodologies and SuperGemini principles
- Apply framework-guided problem-solving approaches

## Configuration Profiles

### SuperGemini Mode (`supergemini.json`)
- 4-step structured thinking with automatic sg command integration
- 90% command preference with intelligent skip conditions
- Agent persona system with TOML extraction and embodiment
- Document tracking and system-reminder optimization
- Meta-cognitive attention mechanisms for framework compliance

### Advanced Features
- **Thought Revision**: Modify and branch previous reasoning steps
- **Document Tracking**: Prevents duplicate reads, maintains session context
- **Branch Reasoning**: Alternative reasoning paths with unique identifiers
- **Error Recovery**: Detailed error messages with context and suggestions
- **Environment Configuration**: Full customization via environment variables

## Examples
```
"analyze this authentication system" → SemanticPrompt (4-step analysis with agent coordination)
"implement user registration" → SemanticPrompt (TOML-guided implementation with personas)
"debug performance issues" → SemanticPrompt (systematic debugging with specialized agents)
"design API architecture" → SemanticPrompt (multi-agent design coordination)
"what time is it?" → Native response (simple recall, skip conditions met)
"hello" → Native response (greeting, no reasoning needed)
```

## Integration Benefits
- **Framework Compliance**: Ensures SuperGemini methodology adherence
- **Agent Orchestration**: Coordinates specialized AI personas for optimal results
- **Document Intelligence**: Leverages TOML command documentation automatically
- **Meta-Cognitive Enhancement**: Enforces systematic thinking and attention protocols
- **Session Optimization**: Tracks and prevents duplicate operations for efficiency