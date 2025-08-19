# SemanticPrompt MCP Server

**Purpose**: Core thinking engine for SuperGemini Framework with 4-step systematic reasoning and agent persona orchestration

**Tool Name**: `chain_of_thought`

**Activation**: Available through `/sg:cot` command in SuperGemini Framework

## Triggers
- Complex multi-step problems requiring structured reasoning
- Tasks needing systematic sg command selection and agent coordination  
- SuperGemini Framework workflows with TOML-based guidance
- Problems requiring agent persona extraction and embodiment
- Document tracking and meta-cognitive attention requirements
- Single agent architecture needing multi-perspective problem solving

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

### Step 2: sg Command Selection (MANDATORY - 90% Preference)
- Strong preference for sg commands over direct responses
- Automatic TOML document reading and guidance extraction
- Document caching: never read same TOML twice (system-reminder reference)
- Skip only when ALL conditions met: ≤2 lines response, no files, no analysis, pure recall
- Available commands: analyze, build, cleanup, design, document, estimate, explain, git, implement, improve, index, load, reflect, save, select-tool, test, troubleshoot

### Step 3: Agent Persona Extraction & Reading
- Extract agents array from selected TOML command files
- Read individual agent definitions from ~/.gemini/agents/{agents}.md  
- Reference AGENTS.md (system-reminder) for additional context
- Prevent duplicate agent reads using system-reminder optimization
- Handle SuperGemini single agent constraint through sequential persona embodiment

### Step 4: Agent Embodiment & Execution
- Embody extracted agent personas with specialized knowledge
- Multi-agent coordination for complex problems
- Execute solutions using agent methodologies and SuperGemini principles
- Apply framework-guided problem-solving approaches

## Configuration Profiles

### SuperGemini Mode (`supergemini.json`) - Production Default
- 4-step structured thinking with automatic sg command integration
- 90% command preference with intelligent skip conditions
- Agent persona system with TOML extraction and embodiment
- Document tracking and system-reminder optimization
- Meta-cognitive attention mechanisms for framework compliance
- Compatible with SuperGemini single agent architecture

### Other Profiles Available
- `supergemini.json` - SuperGemini Framework (3-step process)
- `default.json` - Basic mode (general problem solving)

### Advanced Features
- **Thought Revision**: Modify and branch previous reasoning steps
- **Document Tracking**: Prevents duplicate reads, maintains session context, caches TOML and agent files
- **Branch Reasoning**: Alternative reasoning paths with unique identifiers
- **Error Recovery**: Detailed error messages with context and suggestions
- **Environment Configuration**: Full customization via environment variables

## Examples
```
"analyze this authentication system" → SemanticPrompt (4-step: Intent → sg:analyze → security-engineer → execution)
"implement user registration" → SemanticPrompt (4-step: Intent → sg:implement → [backend-architect, security-engineer] → execution)
"debug performance issues" → SemanticPrompt (4-step: Intent → sg:troubleshoot → [performance-engineer, root-cause-analyst] → execution)
"design API architecture" → SemanticPrompt (4-step: Intent → sg:design → [system-architect, backend-architect] → execution)
"what time is it?" → Native response (skip: simple recall, ≤2 lines, no analysis)
"hello" → Native response (skip: greeting, no files, pure interaction)
```

## Integration Benefits
- **Framework Compliance**: Ensures SuperGemini methodology adherence
- **Agent Orchestration**: Coordinates specialized AI personas for optimal results
- **Document Intelligence**: Leverages TOML command documentation automatically
- **Meta-Cognitive Enhancement**: Enforces systematic thinking and attention protocols
- **Session Optimization**: Tracks and prevents duplicate operations for efficiency