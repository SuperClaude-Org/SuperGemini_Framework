# SuperGemini MCP Servers Guide 🔌

## 🎯 The Simple Truth About MCP Servers

MCP (Model Context Protocol) servers are specialized tools that extend Claude Code's capabilities beyond native functionality. SuperGemini integrates 6 carefully selected MCP servers that automatically activate based on your tasks, providing enhanced documentation access, advanced reasoning, UI generation, browser automation, code transformation, and project memory.

**Seamless Integration**: Type `/sg:implement "React dashboard"` → Magic MCP activates for UI generation. Type `/sg:analyze --think-hard` → Sequential MCP enables structured reasoning. The system intelligently selects the right tools for your context.

## Overview

**What MCP Servers Do:**
- **Context7**: Official library documentation and framework patterns
- **Sequential**: Multi-step reasoning and hypothesis testing
- **Magic**: Modern UI component generation from 21st.dev patterns
- **Playwright**: Real browser automation and E2E testing
- **Morphllm**: Efficient pattern-based code transformations
- **Serena**: Semantic code understanding with project memory

**How They Enhance SuperGemini:**
- **Automatic Activation**: Intelligent context-based server selection
- **Parallel Coordination**: Multiple servers working together on complex tasks
- **Quality Enhancement**: Specialized tools for specific domains
- **Efficiency Gains**: 30-50% improvement in complex workflows
- **Session Persistence**: Maintain context across development sessions

## Available MCP Servers

### Context7 Server 📚

**Purpose**: Official library documentation and framework pattern access

**Capabilities:**
- Curated documentation lookup for popular libraries
- Version-specific API references and examples
- Framework best practices and implementation patterns
- Up-to-date code examples from official sources

**Auto-Activation Triggers:**
- Library imports: `import`, `require`, `from`, `use`
- Framework keywords: React, Vue, Angular, Next.js, Express
- Documentation requests: "official docs", "API reference"
- Pattern queries: "best practices", "recommended approach"

**Usage Examples:**
```bash
# Automatic activation
/sg:implement "React useEffect for data fetching"
# → Context7 provides official React hooks documentation

# Manual activation
/sg:analyze auth-system/ --c7
# → Access authentication pattern libraries
```

**Best For:**
- Following official framework patterns
- Ensuring API compliance and best practices
- Learning new libraries with authoritative sources
- Version-specific implementation requirements

---

### Sequential Server 🧠

**Purpose**: Structured multi-step reasoning and systematic analysis

**Capabilities:**
- Hypothesis generation and testing workflows
- Complex problem decomposition
- Evidence-based reasoning chains
- Systematic debugging methodologies

**Auto-Activation Triggers:**
- Complex debugging scenarios with multiple layers
- Architectural analysis and system design
- `--think`, `--think-hard`, `--ultrathink` flags
- Multi-component failure investigation

**Usage Examples:**
```bash
# Automatic activation
/sg:troubleshoot "API performance degrading under load"
# → Sequential enables systematic root cause analysis

# Manual activation  
/sg:analyze --think-hard microservices-architecture/
# → Deep architectural analysis with structured reasoning
```

**Best For:**
- Root cause analysis of complex issues
- System architecture design and evaluation
- Performance bottleneck identification
- Security vulnerability assessment

---

### Magic Server ✨

**Purpose**: Modern UI component generation from 21st.dev design patterns

**Capabilities:**
- Production-ready React, Vue, Angular components
- Accessibility-compliant UI elements
- Design system integration
- Responsive and interactive components

**Auto-Activation Triggers:**
- UI component requests: button, form, modal, table
- `/ui` or `/21` commands
- Frontend development keywords: responsive, accessible, component
- Design system implementation needs

**Usage Examples:**
```bash
# Automatic activation
/sg:implement "responsive dashboard with data visualization" 
# → Magic generates modern UI components with accessibility

# Manual activation
/sg:design "e-commerce checkout flow" --magic
# → UI-focused design with component generation
```

**Best For:**
- Creating production-ready UI components
- Implementing accessible design systems
- Rapid frontend prototyping
- Modern framework component architecture

---

### Playwright Server 🎭

**Purpose**: Real browser automation and comprehensive E2E testing

**Capabilities:**
- Cross-browser testing automation
- Visual regression testing
- Accessibility compliance validation
- User interaction simulation

**Auto-Activation Triggers:**
- Browser testing and E2E scenarios
- Visual testing and screenshot requests
- Accessibility testing requirements
- User workflow validation needs

**Usage Examples:**
```bash
# Automatic activation
/sg:test --type e2e "user registration flow"
# → Playwright automates browser testing

# Manual activation
/sg:validate "form accessibility compliance" --play
# → Browser-based accessibility testing
```

**Best For:**
- End-to-end user workflow testing
- Cross-browser compatibility validation
- Visual regression testing
- Accessibility compliance verification

---

### Morphllm Server 🔄

**Purpose**: Efficient pattern-based code transformations and bulk editing

**Capabilities:**
- Multi-file pattern transformations
- Style guide enforcement across codebases
- Framework migration assistance
- Bulk code modernization

**Auto-Activation Triggers:**
- Multi-file edit operations
- Framework updates and migrations
- Code cleanup and standardization
- Pattern-based refactoring tasks

**Usage Examples:**
```bash
# Automatic activation
/sg:improve legacy-codebase/ --focus maintainability
# → Morphllm applies consistent patterns across files

# Manual activation
/sg:cleanup src/ --morph
# → Pattern-based code organization
```

**Best For:**
- Large-scale refactoring projects
- Code style standardization
- Framework migration projects
- Bulk code transformations

---

### Serena Server 🧭

**Purpose**: Semantic code understanding with persistent project memory

**Capabilities:**
- Symbol-level code navigation and analysis
- Cross-session project memory
- Semantic code transformations
- Large codebase architecture understanding

**Auto-Activation Triggers:**
- Symbol operations: rename, extract, move functions
- Project-wide code navigation
- Session management: `/sg:load`, `/sg:save`
- Large codebase analysis requirements

**Usage Examples:**
```bash
# Automatic activation  
/sg:load existing-project/
# → Serena builds project understanding and memory

# Manual activation
/sg:refactor "extract UserService class" --serena
# → Semantic-aware code restructuring
```

**Best For:**
- Long-term project development
- Complex codebase navigation
- Semantic code refactoring
- Cross-session context preservation

## Installation & Configuration

### Automatic Installation (Recommended)

**During SuperGemini Setup:**
```bash
SuperGemini install
# → Interactive installer offers MCP server selection
# → Automatically configures selected servers
# → Creates .claude.json with server configurations
```

**Installation Options:**
- **All Servers**: Complete MCP capability (recommended for full features)
- **Essential Only**: Context7 + Sequential (minimal but powerful)
- **Custom Selection**: Choose specific servers for your workflow
- **Skip MCP**: Native-only installation for resource constraints

### Manual Configuration

**Server-Specific Installation:**
```bash
# Install specific MCP components
SuperGemini install --components mcp

# Individual server configuration
SuperGemini install --components mcp_context7 mcp_sequential

# Force reinstall with updated configurations
SuperGemini install --components mcp --force
```

**Configuration File (`.claude.json`):**
```json
{
  "mcpServers": {
    "context7": {
      "command": "node",
      "args": ["/path/to/context7-server"],
      "env": {"NODE_ENV": "production"}
    },
    "sequential": {
      "command": "node", 
      "args": ["/path/to/sequential-server"]
    }
  }
}
```

### Prerequisites by Server

**Node.js Required (Most Servers):**
- Context7, Magic, Sequential, Playwright require Node.js 16+
- Install: `brew install node` (macOS) or visit https://nodejs.org

**Python Required:**
- Morphllm, Serena work with Python environment
- Already satisfied by SuperGemini installation

**System Resources:**
- **Minimal**: 2GB RAM for basic MCP functionality
- **Recommended**: 4GB RAM for full MCP suite
- **Storage**: 200MB additional for MCP server installations

## Usage Patterns

### Automatic Server Selection

**Context-Based Activation:**
SuperGemini analyzes your request and automatically selects optimal MCP servers:

```bash
# Frontend development → Magic + Context7
/sg:implement "responsive navigation component"

# Performance investigation → Sequential + Playwright  
/sg:troubleshoot "page load time >3 seconds"

# Large refactoring → Serena + Morphllm + Sequential
/sg:improve legacy-authentication-system/

# Documentation lookup → Context7
/sg:explain "React useCallback best practices"

# Browser testing → Playwright + Sequential
/sg:test --type e2e user-checkout-flow/
```

**Intelligence Behind Selection:**
- **Keywords**: "component", "UI" → Magic activation
- **File types**: `.jsx`, `.vue` → Magic + Context7
- **Complexity**: Multi-file operations → Serena + Morphllm
- **Analysis depth**: `--think-hard` → Sequential + Context7
- **Testing scope**: E2E workflows → Playwright + Sequential

### Manual Server Control

**Force Specific Servers:**
```bash
# Enable specific servers
/sg:analyze codebase/ --c7 --seq --serena

# Disable all MCP servers
/sg:implement "simple function" --no-mcp

# Enable all servers for maximum capability
/sg:design "complex system architecture" --all-mcp

# Lightweight execution
/sg:explain "function purpose" --no-mcp
```

**Server Combination Strategies:**

**Documentation + Analysis:**
```bash
/sg:analyze security-patterns/ --c7 --seq
# → Context7 provides security patterns + Sequential analyzes implementation
```

**UI Development:**
```bash
/sg:implement "dashboard interface" --magic --c7 --play
# → Magic generates components + Context7 patterns + Playwright testing
```

**Code Transformation:**
```bash
/sg:improve legacy-code/ --serena --morph --seq
# → Serena analyzes structure + Morphllm transforms + Sequential validates
```

### Multi-Server Coordination

**Complex Workflow Example:**
```bash
/sg:implement "e-commerce checkout system"
```

**Automatic Coordination:**
1. **Sequential**: Breaks down checkout workflow systematically
2. **Context7**: Provides payment integration patterns
3. **Magic**: Generates checkout UI components
4. **Serena**: Manages code organization and dependencies
5. **Playwright**: Creates E2E testing for checkout flow

**Efficiency Gains:**
- **30-50% faster development** through specialized tools
- **Higher quality output** through domain expertise
- **Reduced context switching** with intelligent automation
- **Comprehensive coverage** across all development aspects

## Advanced Features

### Multi-Server Orchestration

**Intelligent Workflow Coordination:**
SuperGemini orchestrates multiple MCP servers for complex tasks:

**Full-Stack Development Workflow:**
```bash
/sg:implement "real-time chat application"
```
1. **Sequential**: Analyzes requirements and architecture
2. **Context7**: Provides WebSocket and React patterns  
3. **Magic**: Generates chat UI components
4. **Serena**: Manages project structure and dependencies
5. **Playwright**: Creates E2E tests for messaging flow
6. **Morphllm**: Applies consistent code patterns

**Performance Optimization Workflow:**
```bash
/sg:analyze --focus performance --ultrathink
```
1. **Sequential**: Systematic performance analysis methodology
2. **Serena**: Code structure and bottleneck identification
3. **Context7**: Framework-specific optimization patterns
4. **Playwright**: Real browser performance testing
5. **Morphllm**: Code optimization pattern application

### Resource Management

**Performance Optimization:**

**Smart Resource Allocation:**
- **Green Zone** (0-75% usage): All servers available
- **Yellow Zone** (75-85%): Priority servers only
- **Red Zone** (85%+): Essential servers, compressed output

**Server Priority Matrix:**
| Priority | Servers | Use Case |
|----------|---------|----------|
| **Essential** | Context7, Sequential | Core functionality |
| **High** | Magic, Serena | Development workflows |
| **Standard** | Playwright, Morphllm | Testing and optimization |

**Concurrency Control:**
```bash
# Limit concurrent server operations
/sg:implement "complex feature" --concurrency 2

# Maximum performance mode
/sg:analyze large-codebase/ --all-mcp --concurrency 6

# Resource-constrained mode  
/sg:troubleshoot issue/ --c7 --seq --concurrency 1
```

### Advanced Configuration

**Custom Server Configurations:**
```json
{
  "mcpServers": {
    "context7": {
      "command": "node",
      "args": ["/custom/context7-server"],
      "env": {
        "CONTEXT7_CACHE_SIZE": "1000",
        "CONTEXT7_TIMEOUT": "30000"
      }
    },
    "sequential": {
      "command": "node",
      "args": ["/custom/sequential-server"],
      "env": {
        "MAX_THINKING_DEPTH": "10",
        "REASONING_TIMEOUT": "60000"
      }
    }
  }
}
```

**Performance Tuning:**
- **Context7**: Cache size, request timeout, documentation sources
- **Sequential**: Thinking depth, reasoning timeout, branch limits
- **Magic**: Component complexity, accessibility level, framework targets
- **Playwright**: Browser pool size, timeout values, screenshot quality
- **Morphllm**: Pattern matching precision, transformation scope
- **Serena**: Memory retention, project indexing depth, symbol resolution

### Integration Patterns

**Mode Integration:**
- **Brainstorming Mode**: Sequential for structured discovery
- **Task Management Mode**: Serena for session persistence
- **Orchestration Mode**: All servers for optimal tool selection
- **Token Efficiency Mode**: Selective activation for resource optimization

**Command Integration:**
- **Analysis Commands**: Sequential + Serena for deep understanding
- **Implementation Commands**: Magic + Context7 for development
- **Testing Commands**: Playwright + Sequential for comprehensive validation
- **Documentation Commands**: Context7 + Magic for pattern-rich docs

## Troubleshooting

### Common Issues & Solutions

**MCP Server Not Starting:**
```bash
# Check server configuration
ls ~/.claude/.claude.json

# Verify server installation
SuperGemini install --list-components

# Reinstall MCP configuration
SuperGemini install --components mcp --force

# Test specific server
SuperGemini test-mcp context7
```

**Node.js Dependency Issues:**
```bash
# Verify Node.js version (16+ required)
node --version

# Install missing dependencies
npm install -g @anthropic/context7-server
npm install -g @anthropic/sequential-server

# Clear Node.js cache
npm cache clean --force
```

**Performance Issues:**
```bash
# Reduce server load
/sg:command --concurrency 1

# Use selective servers
/sg:command --c7 --seq  # Instead of --all-mcp

# Check system resources
top | grep node
ps aux | grep mcp
```

**Server Connection Timeouts:**
```bash
# Increase timeout in .claude.json
{
  "mcpServers": {
    "context7": {
      "timeout": 60000  // Increase from default 30000
    }
  }
}

# Restart Claude Code session
# MCP connections refresh on restart
```

### Diagnostics

**MCP Server Status Check:**
```bash
# Check all server health
SuperGemini status --mcp

# Test individual servers
SuperGemini test-mcp --server context7
SuperGemini test-mcp --server sequential

# Detailed diagnostics
SuperGemini diagnose --verbose
```

**Log Analysis:**
```bash
# View MCP server logs
tail -f ~/.claude/logs/mcp-context7.log
tail -f ~/.claude/logs/mcp-sequential.log

# SuperGemini operation logs  
tail -f ~/.claude/logs/superclaude.log

# Claude Code MCP logs
tail -f ~/.claude/logs/claude-mcp.log
```

**Manual Testing:**
```bash
# Test Context7 documentation lookup
echo "Test React hooks documentation" | claude --mcp context7

# Test Sequential reasoning
echo "Analyze this complex problem" | claude --mcp sequential

# Test server combination
echo "Complex analysis task" | claude --mcp context7,sequential
```

### Resolution Steps

**Step 1: Basic Verification**
1. Check SuperGemini installation: `SuperGemini --version`
2. Verify MCP component: `SuperGemini install --list-components`
3. Check Node.js: `node --version` (should be 16+)
4. Restart Claude Code session

**Step 2: Configuration Check**
1. Verify `.claude.json` exists: `ls ~/.claude/.claude.json`
2. Check server paths and permissions
3. Test configuration syntax: `SuperGemini validate-config`

**Step 3: Server Specific**
1. **Context7**: Check documentation server connection
2. **Sequential**: Verify reasoning engine startup
3. **Magic**: Test UI component generation endpoint
4. **Playwright**: Check browser automation setup
5. **Morphllm**: Verify code transformation pipeline
6. **Serena**: Test project memory and indexing

**Step 4: Full Reset (Last Resort)**
```bash
# Backup existing configuration
cp ~/.claude/.claude.json ~/.claude/.claude.json.backup

# Remove and reinstall MCP
SuperGemini uninstall --components mcp
SuperGemini install --components mcp

# Restore custom settings if needed
```

## Developer Integration

### MCP Server Development

**Creating Custom MCP Servers:**

**Server Structure:**
```javascript
// custom-mcp-server.js
import { Server } from '@modelcontextprotocol/sdk/server/index.js';

const server = new Server(
  {
    name: "custom-server",
    version: "1.0.0"
  },
  {
    capabilities: {
      resources: {},
      tools: {},
      prompts: {}
    }
  }
);

// Tool implementation
server.setRequestHandler(
  'tools/call',
  async (request) => {
    // Custom tool logic
    return { content: [{ type: "text", text: result }] };
  }
);
```

**SuperGemini Integration:**
```python
# setup/components/custom_mcp.py
from setup.components.base import BaseComponent

class CustomMCPComponent(BaseComponent):
    def get_metadata(self):
        return {
            "name": "custom_mcp",
            "description": "Custom MCP server integration",
            "dependencies": ["core"]
        }
    
    def install(self, install_dir):
        # Install custom server configuration
        self._install_mcp_config(install_dir)
```

### Communication Protocols

**MCP Protocol Flow:**
1. **Initialization**: Claude Code connects to MCP server via JSON-RPC
2. **Capability Exchange**: Server announces available tools and resources
3. **Request/Response**: Claude sends requests, server processes and responds
4. **Session Management**: Maintain context across multiple interactions

**Message Structure:**
```json
{
  "jsonrpc": "2.0",
  "id": "request-id",
  "method": "tools/call",
  "params": {
    "name": "analyze-code",
    "arguments": {
      "code": "function example() { return 'hello'; }",
      "language": "javascript"
    }
  }
}
```

**SuperGemini MCP Interface:**
```python
class MCPCoordinator:
    def select_servers(self, task_context):
        """Intelligent server selection based on task analysis"""
        servers = []
        
        if self._needs_documentation(task_context):
            servers.append("context7")
        
        if self._needs_reasoning(task_context):
            servers.append("sequential")
            
        if self._needs_ui_generation(task_context):
            servers.append("magic")
            
        return servers
    
    def coordinate_request(self, servers, request):
        """Orchestrate multi-server workflows"""
        results = []
        for server in servers:
            result = await self._send_request(server, request)
            results.append(result)
        
        return self._synthesize_results(results)
```

### Integration APIs

**Configuration API:**
```python
# Register custom MCP server
from setup.services.config_service import ConfigService

config_service = ConfigService()
config_service.add_mcp_server({
    "name": "custom-server",
    "command": "node",
    "args": ["/path/to/custom-server.js"],
    "env": {"CUSTOM_CONFIG": "value"}
})
```

**Tool Registration:**
```python
# Register server capabilities with SuperGemini
from setup.core.mcp_registry import MCPRegistry

registry = MCPRegistry()
registry.register_server("custom-server", {
    "capabilities": ["code-analysis", "documentation"],
    "triggers": ["custom", "analyze", "special-keyword"],
    "priority": "standard"
})
```

**Integration Testing:**
```python
# Test custom MCP server integration
from setup.testing.mcp_test import MCPTestSuite

test_suite = MCPTestSuite()
test_suite.test_server_connection("custom-server")
test_suite.test_tool_functionality("custom-server", "analyze-code")
test_suite.test_integration_workflow(["custom-server", "sequential"])
```

---

## MCP Server Quick Reference 📋

| Server | Purpose | Auto-Triggers | Manual Flags | Best For |
|--------|---------|---------------|--------------|----------|
| **Context7** | Documentation | Library imports, API questions | `--c7`, `--context7` | Official patterns, framework docs |
| **Sequential** | Reasoning | Complex debugging, analysis | `--seq`, `--sequential` | Systematic thinking, root cause |
| **Magic** | UI Generation | Component requests, frontend | `--magic` | Modern UI, accessibility |
| **Playwright** | Browser Testing | E2E testing, visual validation | `--play`, `--playwright` | User workflows, cross-browser |
| **Morphllm** | Code Transform | Multi-file edits, refactoring | `--morph`, `--morphllm` | Pattern application, bulk changes |
| **Serena** | Project Memory | Symbol operations, large codebases | `--serena` | Session persistence, navigation |

**Server Combinations:**
- **Full-Stack Development**: Magic + Context7 + Serena
- **Quality Analysis**: Sequential + Playwright + Serena  
- **Large Refactoring**: Serena + Morphllm + Sequential
- **Learning/Documentation**: Context7 + Sequential + Magic

**Performance Control:**
- `--all-mcp`: Enable all servers (max capability)
- `--no-mcp`: Disable all servers (lightweight)
- `--concurrency N`: Control parallel operations
- Resource awareness: Auto-scaling based on system load

---

## Related Guides

**Learning Progression:**

**🌱 Essential (Week 1)**
- [Quick Start Guide](../Getting-Started/quick-start.md) - Experience MCP servers naturally
- [Installation Guide](../Getting-Started/installation.md) - MCP server setup
- [Commands Reference](commands.md) - Commands that activate MCP servers

**🌿 Intermediate (Week 2-3)**
- [Behavioral Modes](modes.md) - How modes coordinate MCP servers
- [Agents Guide](agents.md) - Agent-MCP server integration
- [Examples Cookbook](../Reference/examples-cookbook.md) - MCP workflow patterns

**🌲 Advanced (Month 2+)**
- [Session Management](session-management.md) - Serena MCP workflows
- [Best Practices](../Reference/best-practices.md) - MCP optimization strategies
- [Flags Guide](flags.md) - Advanced MCP control

**🔧 Expert**
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - MCP integration details
- [Contributing Code](../Developer-Guide/contributing-code.md) - Custom MCP development
- [Testing & Debugging](../Developer-Guide/testing-debugging.md) - MCP troubleshooting

**MCP-Specific Resources:**
- **Official MCP Documentation**: https://modelcontextprotocol.io/
- **Context7 Server**: Enhanced documentation lookup capabilities
- **Sequential Thinking**: Advanced reasoning and analysis
- **Magic UI**: Modern component generation from 21st.dev
- **Community MCP Servers**: https://github.com/modelcontextprotocol/servers