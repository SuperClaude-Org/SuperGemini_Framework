# Testing & Debugging SuperGemini Framework

This guide provides comprehensive testing and debugging strategies for SuperGemini Framework development. Whether you're contributing components, fixing bugs, or optimizing performance, these techniques will help you build robust, reliable code.

**Developer-Focused Approach**: Testing and debugging strategies specifically designed for the meta-framework architecture, component system, and intelligent orchestration patterns unique to SuperGemini.

## Table of Contents

**For Screen Readers**: This document contains 10 main sections covering comprehensive testing and debugging procedures. Use heading navigation to jump between sections. Code examples include detailed comments and error handling.

1. [Quick Start Testing Tutorial](#quick-start-testing-tutorial) - Get started with basic testing
2. [Testing Environment Setup](#testing-environment-setup) - Comprehensive test configuration
3. [Testing Framework](#testing-framework) - Development testing procedures and standards
4. [Debugging SuperGemini Components](#debugging-superclaude-components) - Component-specific debugging
5. [Performance Testing & Optimization](#performance-testing--optimization) - Benchmarking and profiling
6. [Security Testing](#security-testing) - Security validation and vulnerability testing
7. [Integration Testing](#integration-testing) - End-to-end workflow validation
8. [Quality Validation](#quality-validation) - Quality gates and validation frameworks
9. [Troubleshooting Guide](#troubleshooting-guide) - Common issues and solutions
10. [Testing Glossary](#testing-glossary) - Testing terminology and concepts

**Cross-Reference Links**:
- [Contributing Code Guide](contributing-code.md) - Development workflows and standards
- [Technical Architecture Guide](technical-architecture.md) - System architecture and component specifications

**Key Testing Concepts**:
- **Component Testing**: Individual component validation and functionality testing
- **Agent System Testing**: Agent activation, coordination, and behavioral validation
- **MCP Integration Testing**: External tool coordination and protocol validation
- **Performance Profiling**: Memory usage, execution speed, and resource optimization

## Quick Start Testing Tutorial

### 1. Set Up Your Testing Environment

First, create a proper testing environment with all necessary dependencies:

```bash
# Create and activate virtual environment
python -m venv superclaude-testing
source superclaude-testing/bin/activate  # Linux/Mac
# or
superclaude-testing\Scripts\activate     # Windows

# Install testing dependencies
pip install pytest pytest-cov pytest-mock pytest-benchmark
pip install memory-profiler coverage[toml] psutil
```

### 2. Create Your First Test

```python
# tests/test_basic.py
import pytest
import tempfile
import shutil
import json
import os
from pathlib import Path
from unittest.mock import Mock, patch

# Import SuperGemini components
from setup.components.base import BaseComponent
from setup.core.registry import ComponentRegistry
from setup.services.session_manager import SessionManager

class TestBasicSetup:
    """Basic SuperGemini component testing example"""
    
    def setup_method(self):
        """Set up test environment before each test"""
        self.test_dir = Path(tempfile.mkdtemp(prefix="superclaude_test_"))
        self.registry = ComponentRegistry()
        
    def teardown_method(self):
        """Clean up after each test"""
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
            
    def test_component_installation(self):
        """Test basic component installation process"""
        # Test setup
        from setup.components.core import CoreComponent
        component = CoreComponent()
        
        # Execute test
        result = component.install(self.test_dir)
        
        # Assertions with clear validation
        assert result.success, f"Installation failed: {result.error}"
        assert (self.test_dir / 'GEMINI.md').exists(), "GEMINI.md not created"
        
        # Verify content structure
        gemini_content = (self.test_dir / 'GEMINI.md').read_text()
        assert '@FLAGS.md' in gemini_content, "FLAGS.md not referenced"
        assert '@RULES.md' in gemini_content, "RULES.md not referenced"
```

### 3. Run Your Tests

```bash
# Run basic test
python -m pytest tests/test_basic.py -v

# Run with coverage
python -m pytest tests/test_basic.py --cov=setup --cov-report=html

# Generate coverage report
open htmlcov/index.html  # View coverage in browser
```

## Testing Environment Setup

### Complete Development Environment Configuration

**Required Dependencies:**
```bash
# Core testing framework
pip install pytest>=7.0.0
pip install pytest-cov>=4.0.0
pip install pytest-mock>=3.10.0
pip install pytest-benchmark>=4.0.0

# Performance monitoring
pip install memory-profiler>=0.60.0
pip install psutil>=5.9.0
pip install py-spy>=0.3.14

# Code quality tools
pip install coverage[toml]>=7.0.0
pip install pytest-html>=3.1.0

# Mocking and fixtures
pip install responses>=0.23.0
pip install freezegun>=1.2.0
```

**Environment Variables:**
```bash
# Create test configuration file
cat > .env.testing << EOF
# Testing configuration
SUPERCLAUDE_TEST_MODE=true
SUPERCLAUDE_DEBUG=true
SUPERCLAUDE_LOG_LEVEL=debug

# Test directories
SUPERCLAUDE_TEST_DIR=/tmp/superclaude_test
SUPERCLAUDE_CONFIG_DIR=/tmp/superclaude_test_config

# MCP server testing
SUPERCLAUDE_MCP_TIMEOUT=30
SUPERCLAUDE_MCP_RETRY_COUNT=3

# Performance testing
SUPERCLAUDE_BENCHMARK_ITERATIONS=10
SUPERCLAUDE_MEMORY_LIMIT_MB=512
EOF

# Load testing environment
export $(cat .env.testing | xargs)
```

**Test Configuration Setup:**
```python
# conftest.py - Pytest configuration
import pytest
import tempfile
import shutil
import os
import sys
from pathlib import Path
from unittest.mock import Mock, patch

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

@pytest.fixture(scope="session")
def test_environment():
    """Set up isolated test environment"""
    test_dir = Path(tempfile.mkdtemp(prefix="superclaude_test_"))
    config_dir = test_dir / "config"
    config_dir.mkdir(parents=True)
    
    # Set environment variables
    original_env = os.environ.copy()
    os.environ.update({
        'SUPERCLAUDE_TEST_MODE': 'true',
        'SUPERCLAUDE_CONFIG_DIR': str(config_dir),
        'SUPERCLAUDE_TEST_DIR': str(test_dir),
        'SUPERCLAUDE_DEBUG': 'true'
    })
    
    yield {
        'test_dir': test_dir,
        'config_dir': config_dir
    }
    
    # Cleanup
    if test_dir.exists():
        shutil.rmtree(test_dir)
    os.environ.clear()
    os.environ.update(original_env)

@pytest.fixture
def mock_registry():
    """Provide mock component registry"""
    from setup.core.registry import ComponentRegistry
    with patch('setup.core.registry.ComponentRegistry') as mock:
        instance = Mock(spec=ComponentRegistry)
        instance.components = {}
        instance.list_installed.return_value = []
        mock.return_value = instance
        yield instance

@pytest.fixture
def mock_mcp_servers():
    """Mock MCP servers for testing"""
    servers = {
        'context7': Mock(),
        'sequential': Mock(),
        'magic': Mock(),
        'morphllm': Mock(),
        'serena': Mock(),
        'playwright': Mock()
    }
    
    # Configure standard responses
    for server in servers.values():
        server.connect.return_value = True
        server.ping.return_value = {'status': 'ok'}
        server.disconnect.return_value = True
    
    # Specific server behaviors
    servers['context7'].query.return_value = {'docs': 'sample documentation'}
    servers['sequential'].analyze.return_value = {'steps': ['step1', 'step2']}
    servers['magic'].generate.return_value = {'ui': '<div>component</div>'}
    
    yield servers

@pytest.fixture
def sample_task_context():
    """Provide sample task context for testing"""
    from setup.core.task_context import TaskContext
    return TaskContext(
        input_text="implement authentication system",
        file_count=5,
        complexity_score=0.7,
        domain='security',
        session_id='test-session'
    )
```

### Test Data Management

**Test Data Structure:**
```
tests/
├── fixtures/
│   ├── components/          # Sample component configurations
│   │   ├── agent_samples.json
│   │   ├── mode_samples.json
│   │   └── mcp_configs.json
│   ├── sessions/           # Sample session data
│   │   ├── basic_session.json
│   │   └── complex_session.json
│   ├── files/              # Sample project structures
│   │   ├── minimal_project/
│   │   └── complex_project/
│   └── responses/          # Mock API responses
│       ├── mcp_responses.json
│       └── agent_responses.json
```

**Test Data Factory:**
```python
# tests/factories.py
import json
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Any

@dataclass
class TestDataFactory:
    """Factory for creating test data"""
    
    @staticmethod
    def create_test_component(component_type: str = "agent") -> Dict[str, Any]:
        """Create test component configuration"""
        if component_type == "agent":
            return {
                "name": "test-agent",
                "type": "agent",
                "triggers": ["test", "example"],
                "description": "Test agent for development",
                "dependencies": ["core"],
                "config": {
                    "activation_threshold": 0.7,
                    "coordination_level": "moderate"
                }
            }
        elif component_type == "mode":
            return {
                "name": "test-mode",
                "type": "mode",
                "activation_conditions": {
                    "complexity_threshold": 0.5,
                    "keywords": ["test", "debug"]
                },
                "behavior_modifications": {
                    "verbosity": "high",
                    "error_tolerance": "low"
                }
            }
        else:
            raise ValueError(f"Unknown component type: {component_type}")
    
    @staticmethod
    def create_test_session(session_type: str = "basic") -> Dict[str, Any]:
        """Create test session data"""
        base_session = {
            "id": "test-session-123",
            "created_at": "2024-01-01T00:00:00Z",
            "last_active": "2024-01-01T01:00:00Z",
            "context_size": 1024,
            "active_components": ["core"]
        }
        
        if session_type == "complex":
            base_session.update({
                "active_components": ["core", "agents", "modes", "mcp"],
                "context_size": 4096,
                "memory_items": [
                    {"key": "project_type", "value": "web_application"},
                    {"key": "tech_stack", "value": ["python", "react", "postgresql"]}
                ]
            })
        
        return base_session
    
    @staticmethod
    def create_test_project(project_type: str = "minimal") -> Dict[str, List[str]]:
        """Create test project structure"""
        if project_type == "minimal":
            return {
                "files": [
                    "main.py",
                    "requirements.txt",
                    "README.md"
                ],
                "directories": [
                    "src/",
                    "tests/"
                ]
            }
        elif project_type == "complex":
            return {
                "files": [
                    "main.py", "config.py", "models.py", "views.py",
                    "requirements.txt", "setup.py", "README.md",
                    "tests/test_main.py", "tests/test_models.py",
                    "src/auth/login.py", "src/api/endpoints.py"
                ],
                "directories": [
                    "src/", "src/auth/", "src/api/", "src/utils/",
                    "tests/", "tests/unit/", "tests/integration/",
                    "docs/", "config/"
                ]
            }
        else:
            raise ValueError(f"Unknown project type: {project_type}")

    @staticmethod
    def load_fixture(fixture_name: str) -> Any:
        """Load test fixture from JSON file"""
        fixture_path = Path(__file__).parent / "fixtures" / f"{fixture_name}.json"
        if not fixture_path.exists():
            raise FileNotFoundError(f"Fixture not found: {fixture_path}")
        
        with open(fixture_path, 'r') as f:
            return json.load(f)
    
    @staticmethod
    def create_temp_project(test_dir: Path, project_type: str = "minimal") -> Path:
        """Create temporary project structure for testing"""
        project_structure = TestDataFactory.create_test_project(project_type)
        project_dir = test_dir / "test_project"
        project_dir.mkdir(parents=True)
        
        # Create directories
        for directory in project_structure["directories"]:
            (project_dir / directory).mkdir(parents=True, exist_ok=True)
        
        # Create files
        for file_path in project_structure["files"]:
            file_full_path = project_dir / file_path
            file_full_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Add sample content based on file type
            if file_path.endswith('.py'):
                content = f'# {file_path}\n"""Sample Python file for testing"""\n\ndef main():\n    pass\n'
            elif file_path.endswith('.md'):
                content = f'# {file_path}\n\nSample documentation for testing.\n'
            elif file_path.endswith('.txt'):
                content = 'pytest>=7.0.0\ncoverage>=7.0.0\n'
            else:
                content = f'# {file_path} - Sample content\n'
                
            file_full_path.write_text(content)
        
        return project_dir
```

## Testing Framework

### Development Testing Procedures

**Test Structure:**
```
tests/
├── unit/                    # Component unit tests
│   ├── test_components.py   # Component system tests
│   ├── test_agents.py       # Agent system tests
│   └── test_mcp.py          # MCP integration tests
├── integration/             # Integration tests
│   ├── test_installation.py # Installation process tests
│   ├── test_workflows.py    # End-to-end workflow tests
│   └── test_coordination.py # Multi-component coordination
├── performance/             # Performance benchmarks
│   ├── test_memory.py       # Memory usage tests
│   └── test_speed.py        # Execution speed tests
└── fixtures/                # Test data and configurations
```

**Running Tests:**
```bash
# Run all tests
python -m pytest tests/

# Run specific test categories
python -m pytest tests/unit/
python -m pytest tests/integration/
python -m pytest tests/performance/

# Run with coverage
python -m pytest --cov=setup --cov-report=html tests/

# Run with verbose output
python -m pytest -v tests/

# Run specific test file
python -m pytest tests/unit/test_components.py -v
```

**Test Coverage Requirements:**
- **Unit Tests**: >90% coverage for core components
- **Integration Tests**: All major workflows covered
- **Performance Tests**: Memory and speed benchmarks
- **Installation Tests**: All component installation scenarios

**Testing Standards:**
```python
# Example test structure with complete imports
import pytest
import tempfile
import shutil
import os
from pathlib import Path
from unittest.mock import Mock, patch

# SuperGemini imports
from setup.components.base import BaseComponent
from setup.components.core import CoreComponent
from setup.core.registry import ComponentRegistry
from setup.core.installation import InstallationOrchestrator, InstallOptions

class TestComponentSystem:
    def setup_method(self):
        """Set up test environment before each test"""
        self.test_dir = Path(tempfile.mkdtemp(prefix='superclaude_test_'))
        self.registry = ComponentRegistry()
        
        # Ensure clean state
        if hasattr(self.registry, 'clear'):
            self.registry.clear()
        
    def teardown_method(self):
        """Clean up after each test"""
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
            
        # Reset registry state
        if hasattr(self.registry, 'reset'):
            self.registry.reset()
            
    def test_component_installation(self):
        """Test component installation process"""
        # Test setup
        component = CoreComponent()
        install_options = InstallOptions(
            install_dir=self.test_dir,
            force=False,
            dry_run=False
        )
        
        # Execute test
        result = component.install(install_options)
        
        # Comprehensive assertions
        assert result.success, f"Installation failed: {getattr(result, 'error', 'Unknown error')}"
        assert (self.test_dir / 'GEMINI.md').exists(), "GEMINI.md not created"
        
        # Verify registry state
        installed_components = self.registry.list_installed()
        assert 'core' in installed_components, f"Core not in registry: {installed_components}"
        
        # Verify file contents
        gemini_content = (self.test_dir / 'GEMINI.md').read_text()
        assert '@FLAGS.md' in gemini_content, "FLAGS.md reference missing"
        assert '@RULES.md' in gemini_content, "RULES.md reference missing"
        
    def test_component_validation(self):
        """Test component validation before installation"""
        component = CoreComponent()
        
        # Validate component structure
        validation_result = component.validate()
        assert validation_result.is_valid, f"Component validation failed: {validation_result.errors}"
        
        # Check required attributes
        assert hasattr(component, 'name'), "Component missing name attribute"
        assert hasattr(component, 'dependencies'), "Component missing dependencies"
        assert hasattr(component, 'install'), "Component missing install method"
```

## Debugging SuperGemini Components

> **🏗️ Architecture Context**: Understanding component architecture is essential for effective debugging. Review [Technical Architecture Guide](technical-architecture.md) for system architecture details.

### Agent System Debugging

**Agent Activation Debugging:**
```python
# Debug agent selection and activation with complete imports
import re
import logging
from typing import List, Dict, Any
from setup.agents.base import BaseAgent
from setup.agents.manager import AgentManager
from setup.core.task_context import TaskContext
from setup.core.coordination import CoordinationPattern

class AgentDebugger:
    def __init__(self):
        self.agent_manager = AgentManager()
        self.logger = logging.getLogger(__name__)
        
    def debug_agent_selection(self, task_context: TaskContext) -> tuple:
        """Debug agent selection process with detailed output"""
        print("🔍 Agent Selection Debug:")
        print(f"  Input text: '{task_context.input_text}'")
        print(f"  File count: {task_context.file_count}")
        print(f"  Complexity: {task_context.complexity_score}")
        
        # Show detected triggers
        triggers = self._extract_triggers(task_context)
        print(f"  Detected triggers: {triggers}")
        
        # Show available agents
        available_agents = self.agent_manager.get_available_agents()
        print(f"  Available agents: {[agent.name for agent in available_agents]}")
        
        # Show selected agents with scoring
        selected_agents = self._select_agents_with_scores(task_context, triggers)
        print(f"  Selected agents: {selected_agents}")
        
        # Show coordination pattern
        pattern = self._determine_coordination(selected_agents, task_context)
        print(f"  Coordination pattern: {pattern}")
        
        return [agent['name'] for agent in selected_agents], pattern
        
    def _extract_triggers(self, task_context: TaskContext) -> List[str]:
        """Extract trigger keywords from task context"""
        text = task_context.input_text.lower()
        
        # Define trigger patterns
        trigger_patterns = {
            'security': ['security', 'auth', 'login', 'vulnerability', 'encrypt'],
            'frontend': ['ui', 'react', 'vue', 'angular', 'component'],
            'backend': ['api', 'server', 'database', 'endpoint'],
            'devops': ['deploy', 'docker', 'kubernetes', 'ci/cd'],
            'data': ['dataset', 'analytics', 'machine learning', 'pandas']
        }
        
        detected_triggers = []
        for category, keywords in trigger_patterns.items():
            for keyword in keywords:
                if keyword in text:
                    detected_triggers.append(f"{category}:{keyword}")
                    
        return detected_triggers
        
    def _select_agents_with_scores(self, task_context: TaskContext, triggers: List[str]) -> List[Dict[str, Any]]:
        """Select agents with confidence scores"""
        agent_scores = []
        
        for agent in self.agent_manager.get_available_agents():
            score = self._calculate_agent_score(agent, task_context, triggers)
            if score > 0.3:  # Threshold for activation
                agent_scores.append({
                    'name': agent.name,
                    'score': score,
                    'reason': self._get_activation_reason(agent, triggers)
                })
                
        # Sort by score descending
        return sorted(agent_scores, key=lambda x: x['score'], reverse=True)
        
    def _calculate_agent_score(self, agent: BaseAgent, task_context: TaskContext, triggers: List[str]) -> float:
        """Calculate agent activation score"""
        score = 0.0
        
        # Check trigger keywords
        for trigger in triggers:
            if any(keyword in trigger for keyword in agent.trigger_keywords):
                score += 0.3
                
        # Check complexity requirements
        if hasattr(agent, 'min_complexity') and task_context.complexity_score >= agent.min_complexity:
            score += 0.2
            
        # Check file type preferences
        if hasattr(task_context, 'file_types') and hasattr(agent, 'preferred_file_types'):
            if any(ft in agent.preferred_file_types for ft in task_context.file_types):
                score += 0.1
                
        return min(score, 1.0)  # Cap at 1.0
        
    def _get_activation_reason(self, agent: BaseAgent, triggers: List[str]) -> str:
        """Get human-readable reason for agent activation"""
        matching_triggers = [t for t in triggers if any(kw in t for kw in agent.trigger_keywords)]
        if matching_triggers:
            return f"Matched triggers: {matching_triggers}"
        return "General activation"
        
    def _determine_coordination(self, selected_agents: List[Dict[str, Any]], task_context: TaskContext) -> str:
        """Determine coordination pattern based on selected agents"""
        agent_count = len(selected_agents)
        complexity = task_context.complexity_score
        
        if agent_count == 1:
            return "single_agent"
        elif agent_count == 2 and complexity < 0.7:
            return "collaborative"
        elif agent_count > 2 or complexity >= 0.7:
            return "hierarchical"
        else:
            return "parallel"

# Usage in development
def debug_agent_activation_example():
    """Example usage of agent debugging"""
    # Create test context
    task_context = TaskContext(
        input_text="implement secure authentication with React components",
        file_count=8,
        complexity_score=0.8,
        domain="fullstack"
    )
    
    # Debug agent selection
    debugger = AgentDebugger()
    selected_agents, coordination_pattern = debugger.debug_agent_selection(task_context)
    
    print(f"\nResult: {len(selected_agents)} agents selected")
    print(f"Coordination: {coordination_pattern}")
    
    return selected_agents, coordination_pattern

# Run example
if __name__ == "__main__":
    debug_agent_activation_example()
```

**Agent Coordination Debugging:**
```bash
# Enable comprehensive agent debugging
export SUPERCLAUDE_DEBUG_AGENTS=true
export SUPERCLAUDE_DEBUG_COORDINATION=true
export SUPERCLAUDE_LOG_LEVEL=debug

# Create log directory if it doesn't exist
mkdir -p ~/.gemini/logs

# Run with agent tracing (corrected command)
python -m setup.main install --debug-agents --dry-run --verbose

# Alternative: Use SuperGemini CLI if installed
SuperGemini install core --debug --trace-agents --dry-run

# Monitor agent activation in real-time
tail -f ~/.gemini/logs/superclaude-debug.log | grep -E "(AGENT|COORDINATION)"

# Check specific agent logs
ls ~/.gemini/logs/agent-*.log
tail -f ~/.gemini/logs/agent-activation.log

# Debug agent selection with Python
python -c "
import os
os.environ['SUPERCLAUDE_DEBUG_AGENTS'] = 'true'

from setup.agents.manager import AgentManager
from setup.core.task_context import TaskContext

manager = AgentManager()
context = TaskContext(input_text='implement secure login system')
agents = manager.select_agents(context)
print(f'Selected agents: {[a.name for a in agents]}')
"
```

**Common Agent Issues:**
- **Agent Not Activating**: Check trigger patterns and keyword matching
- **Wrong Agent Selected**: Verify trigger priority and specificity
- **Coordination Conflicts**: Debug agent hierarchy and decision authority

### Mode System Debugging

**Mode Activation Debugging:**
```python
# Mode debugging with complete imports
from typing import Dict, List, Any
from setup.modes.base import BaseMode
from setup.modes.manager import ModeManager
from setup.core.task_context import TaskContext
from setup.core.analysis import TaskAnalysis

class ModeDebugger:
    def __init__(self):
        self.mode_manager = ModeManager()
        self.available_modes = {
            'brainstorming': {
                'triggers': ['explore', 'discuss', 'think about', 'maybe'],
                'complexity_threshold': 0.1,
                'keywords': ['brainstorm', 'idea', 'concept']
            },
            'task_management': {
                'triggers': ['implement', 'build', 'create', 'develop'],
                'complexity_threshold': 0.6,
                'file_threshold': 3
            },
            'orchestration': {
                'triggers': ['coordinate', 'manage', 'optimize'],
                'complexity_threshold': 0.8,
                'parallel_ops': True
            },
            'introspection': {
                'triggers': ['analyze', 'debug', 'understand', 'why'],
                'complexity_threshold': 0.5,
                'error_context': True
            }
        }
        
    def debug_mode_selection(self, task_context: TaskContext) -> Dict[str, Any]:
        """Debug mode selection process with detailed analysis"""
        print("🧠 Mode Selection Debug:")
        print(f"  Input: '{task_context.input_text}'")
        
        # Complexity analysis
        complexity = self._calculate_complexity(task_context)
        print(f"  Complexity score: {complexity:.2f}")
        
        # Trigger analysis
        mode_triggers = self._analyze_mode_triggers(task_context)
        print("  Mode trigger analysis:")
        for mode, trigger_data in mode_triggers.items():
            print(f"    {mode}: {trigger_data}")
            
        # Context factors
        context_factors = self._analyze_context_factors(task_context)
        print(f"  Context factors: {context_factors}")
            
        # Final mode selection
        selected_modes = self._select_modes(task_context, complexity, mode_triggers)
        print(f"  Selected modes: {selected_modes}")
        
        return {
            'selected_modes': selected_modes,
            'complexity': complexity,
            'triggers': mode_triggers,
            'context_factors': context_factors
        }
        
    def _calculate_complexity(self, task_context: TaskContext) -> float:
        """Calculate task complexity score"""
        complexity = 0.0
        
        # File count factor
        if hasattr(task_context, 'file_count'):
            complexity += min(task_context.file_count / 10, 0.3)
        
        # Text complexity
        text = task_context.input_text.lower()
        complexity_keywords = ['complex', 'advanced', 'integrate', 'coordinate']
        for keyword in complexity_keywords:
            if keyword in text:
                complexity += 0.1
                
        # Multiple requirements
        requirement_markers = ['and', 'also', 'plus', 'additionally']
        for marker in requirement_markers:
            if marker in text:
                complexity += 0.05
                
        return min(complexity, 1.0)
        
    def _analyze_mode_triggers(self, task_context: TaskContext) -> Dict[str, Dict[str, Any]]:
        """Analyze which mode triggers are activated"""
        text = task_context.input_text.lower()
        mode_analysis = {}
        
        for mode_name, mode_config in self.available_modes.items():
            triggered_keywords = []
            trigger_score = 0.0
            
            # Check keyword triggers
            for trigger in mode_config['triggers']:
                if trigger in text:
                    triggered_keywords.append(trigger)
                    trigger_score += 0.2
                    
            # Check additional keywords if defined
            if 'keywords' in mode_config:
                for keyword in mode_config['keywords']:
                    if keyword in text:
                        triggered_keywords.append(keyword)
                        trigger_score += 0.1
                        
            mode_analysis[mode_name] = {
                'triggered_keywords': triggered_keywords,
                'trigger_score': trigger_score,
                'meets_threshold': trigger_score >= 0.1
            }
            
        return mode_analysis
        
    def _analyze_context_factors(self, task_context: TaskContext) -> Dict[str, Any]:
        """Analyze contextual factors affecting mode selection"""
        factors = {}
        
        # File count
        if hasattr(task_context, 'file_count'):
            factors['file_count'] = task_context.file_count
            factors['multi_file'] = task_context.file_count > 3
            
        # Domain specificity
        if hasattr(task_context, 'domain'):
            factors['domain'] = task_context.domain
            
        # Error presence
        error_indicators = ['error', 'bug', 'issue', 'problem', 'broken']
        factors['has_error'] = any(indicator in task_context.input_text.lower() 
                                 for indicator in error_indicators)
                                 
        # Uncertainty indicators
        uncertainty_words = ['maybe', 'perhaps', 'not sure', 'thinking']
        factors['has_uncertainty'] = any(word in task_context.input_text.lower() 
                                       for word in uncertainty_words)
        
        return factors
        
    def _select_modes(self, task_context: TaskContext, complexity: float, 
                      mode_triggers: Dict[str, Dict[str, Any]]) -> List[str]:
        """Select appropriate modes based on analysis"""
        selected = []
        
        # Priority-based selection
        if mode_triggers['brainstorming']['meets_threshold']:
            selected.append('brainstorming')
        elif complexity >= 0.8:
            selected.append('orchestration')
        elif complexity >= 0.6:
            selected.append('task_management')
            
        # Add introspection if error context
        context_factors = self._analyze_context_factors(task_context)
        if context_factors.get('has_error', False):
            selected.append('introspection')
            
        # Default to brainstorming if no clear mode
        if not selected:
            selected.append('brainstorming')
            
        return selected

# Usage example
def debug_mode_selection_example():
    """Example usage of mode debugging"""
    # Test cases
    test_cases = [
        "I'm thinking about building a web application",
        "Implement authentication system with React and Node.js",
        "Debug this complex microservices architecture issue",
        "Coordinate deployment across multiple environments"
    ]
    
    debugger = ModeDebugger()
    
    for test_input in test_cases:
        print(f"\n{'='*50}")
        print(f"Testing: '{test_input}'")
        print('='*50)
        
        task_context = TaskContext(
            input_text=test_input,
            file_count=5,
            domain='general'
        )
        
        result = debugger.debug_mode_selection(task_context)
        print(f"Final result: {result['selected_modes']}")

if __name__ == "__main__":
    debug_mode_selection_example()
```

**Mode State Inspection:**
```bash
# Enable comprehensive mode debugging
export SUPERCLAUDE_DEBUG_MODES=true
export SUPERCLAUDE_DEBUG_MODE_TRANSITIONS=true
export SUPERCLAUDE_LOG_LEVEL=debug

# Create debugging environment
mkdir -p ~/.gemini/logs
mkdir -p ~/.gemini/debug

# Inspect current mode state
python -c "
import os
import json
from setup.modes.manager import ModeManager
from setup.core.task_context import TaskContext

# Enable debug logging
os.environ['SUPERCLAUDE_DEBUG_MODES'] = 'true'

# Initialize mode manager
manager = ModeManager()

# Check active modes
active_modes = manager.get_active_modes()
print(f'Active modes: {active_modes}')

# Check mode history
mode_history = manager.get_mode_history()
print(f'Mode history: {mode_history}')

# Test mode transitions
test_context = TaskContext(
    input_text='debug complex authentication error',
    complexity_score=0.8
)

# Trigger mode selection
selected_modes = manager.select_modes(test_context)
print(f'Selected modes for test: {selected_modes}')

# Save debug state
debug_state = {
    'active_modes': active_modes,
    'history': mode_history,
    'test_selection': selected_modes
}

with open(os.path.expanduser('~/.gemini/debug/mode_state.json'), 'w') as f:
    json.dump(debug_state, f, indent=2)
    
print('Debug state saved to ~/.gemini/debug/mode_state.json')
"

# Monitor mode transitions in real-time
tail -f ~/.gemini/logs/superclaude-debug.log | grep -E "(MODE|TRANSITION)"

# Check mode-specific logs
ls ~/.gemini/logs/mode-*.log

# Debug mode configuration
python -c "
from setup.modes.manager import ModeManager
manager = ModeManager()
print('Available modes:')
for mode_name in manager.get_available_modes():
    mode = manager.get_mode(mode_name)
    print(f'  {mode_name}: {mode.get_config()}')
"
```

### MCP Server Debugging

**MCP Connection Debugging:**
```python
# MCP server debugging with complete imports
import json
import time
import subprocess
import socket
from typing import Dict, Any, Optional
from pathlib import Path
from setup.mcp.manager import MCPManager
from setup.mcp.connection import MCPConnection
from setup.core.config import ConfigManager

class MCPDebugger:
    def __init__(self):
        self.mcp_manager = MCPManager()
        self.config_manager = ConfigManager()
        self.server_configs = {
            'context7': {
                'command': 'npx',
                'args': ['@context7/mcp-server'],
                'port': 3001,
                'timeout': 30
            },
            'sequential': {
                'command': 'npx',
                'args': ['@sequential-thinking/mcp-server'],
                'port': 3002,
                'timeout': 30
            },
            'magic': {
                'command': 'npx',
                'args': ['@magic-ui/mcp-server'],
                'port': 3003,
                'timeout': 30
            },
            'morphllm': {
                'command': 'python',
                'args': ['-m', 'morphllm.mcp_server'],
                'port': 3004,
                'timeout': 30
            },
            'serena': {
                'command': 'python',
                'args': ['-m', 'serena.mcp_server'],
                'port': 3005,
                'timeout': 30
            },
            'playwright': {
                'command': 'npx',
                'args': ['@playwright/mcp-server'],
                'port': 3006,
                'timeout': 30
            }
        }
        
    def debug_server_connection(self, server_name: str) -> Dict[str, Any]:
        """Comprehensive MCP server debugging"""
        print(f"🔌 MCP Server Debug: {server_name}")
        
        debug_results = {
            'server_name': server_name,
            'timestamp': time.time(),
            'checks': {}
        }
        
        # Check server configuration
        config = self._get_server_config(server_name)
        print(f"  Configuration: {config}")
        debug_results['checks']['configuration'] = config
        
        # Check prerequisites
        prereq_check = self._check_prerequisites(server_name)
        print(f"  Prerequisites: {prereq_check}")
        debug_results['checks']['prerequisites'] = prereq_check
        
        # Test connection
        try:
            connection_result = self._test_connection(server_name)
            print(f"  Connection: ✅ Success")
            debug_results['checks']['connection'] = connection_result
            
            # Test basic functionality
            if connection_result.get('connected', False):
                ping_result = self._test_ping(server_name)
                print(f"  Ping response: {ping_result}")
                debug_results['checks']['ping'] = ping_result
                
        except Exception as e:
            print(f"  Connection: ❌ Failed - {e}")
            debug_results['checks']['connection'] = {
                'connected': False,
                'error': str(e),
                'error_type': type(e).__name__
            }
            
        # Check server health
        health = self._check_server_health(server_name)
        print(f"  Health status: {health}")
        debug_results['checks']['health'] = health
        
        # Check port availability
        port_status = self._check_port_availability(server_name)
        print(f"  Port status: {port_status}")
        debug_results['checks']['port'] = port_status
        
        return debug_results
        
    def _get_server_config(self, server_name: str) -> Dict[str, Any]:
        """Get server configuration from multiple sources"""
        # Check default configs
        default_config = self.server_configs.get(server_name, {})
        
        # Check user configuration
        claude_config_path = Path.home() / '.gemini.json'
        user_config = {}
        
        if claude_config_path.exists():
            try:
                with open(claude_config_path, 'r') as f:
                    full_config = json.load(f)
                    mcp_servers = full_config.get('mcpServers', {})
                    user_config = mcp_servers.get(server_name, {})
            except Exception as e:
                user_config = {'config_error': str(e)}
                
        return {
            'default': default_config,
            'user': user_config,
            'merged': {**default_config, **user_config}
        }
        
    def _check_prerequisites(self, server_name: str) -> Dict[str, Any]:
        """Check if server prerequisites are met"""
        config = self.server_configs.get(server_name, {})
        command = config.get('command', '')
        
        prereq_results = {
            'command_available': False,
            'node_version': None,
            'python_version': None,
            'package_installed': False
        }
        
        # Check command availability
        try:
            result = subprocess.run(['which', command], 
                                  capture_output=True, text=True, timeout=5)
            prereq_results['command_available'] = result.returncode == 0
        except Exception:
            prereq_results['command_available'] = False
            
        # Check Node.js version for npm packages
        if command in ['npx', 'npm', 'node']:
            try:
                result = subprocess.run(['node', '--version'], 
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    prereq_results['node_version'] = result.stdout.strip()
            except Exception:
                pass
                
        # Check Python version for Python packages
        if command == 'python':
            try:
                result = subprocess.run(['python', '--version'], 
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    prereq_results['python_version'] = result.stdout.strip()
            except Exception:
                pass
                
        return prereq_results
        
    def _test_connection(self, server_name: str) -> Dict[str, Any]:
        """Test actual connection to MCP server"""
        try:
            # Try to connect through MCP manager
            connection = self.mcp_manager.connect_server(server_name)
            
            if connection and hasattr(connection, 'is_connected'):
                return {
                    'connected': connection.is_connected(),
                    'connection_time': time.time(),
                    'server_info': getattr(connection, 'server_info', None)
                }
            else:
                return {
                    'connected': False,
                    'error': 'Failed to create connection object'
                }
                
        except Exception as e:
            return {
                'connected': False,
                'error': str(e),
                'error_type': type(e).__name__
            }
            
    def _test_ping(self, server_name: str) -> Dict[str, Any]:
        """Test server responsiveness with ping"""
        try:
            connection = self.mcp_manager.get_connection(server_name)
            if connection:
                start_time = time.time()
                response = connection.ping()
                end_time = time.time()
                
                return {
                    'success': True,
                    'response_time': end_time - start_time,
                    'response': response
                }
            else:
                return {
                    'success': False,
                    'error': 'No active connection'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'error_type': type(e).__name__
            }
            
    def _check_server_health(self, server_name: str) -> Dict[str, Any]:
        """Check overall server health"""
        health_status = {
            'overall': 'unknown',
            'issues': [],
            'recommendations': []
        }
        
        # Check if server is in active connections
        active_servers = self.mcp_manager.get_active_servers()
        if server_name in active_servers:
            health_status['overall'] = 'healthy'
        else:
            health_status['overall'] = 'inactive'
            health_status['issues'].append('Server not in active connections')
            health_status['recommendations'].append(f'Try: SuperGemini install {server_name}')
            
        return health_status
        
    def _check_port_availability(self, server_name: str) -> Dict[str, Any]:
        """Check if server port is available or in use"""
        config = self.server_configs.get(server_name, {})
        port = config.get('port')
        
        if not port:
            return {'available': None, 'message': 'No port configured'}
            
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('localhost', port))
            sock.close()
            
            if result == 0:
                return {
                    'available': False,
                    'port': port,
                    'message': f'Port {port} is in use (server may be running)'
                }
            else:
                return {
                    'available': True,
                    'port': port,
                    'message': f'Port {port} is available'
                }
                
        except Exception as e:
            return {
                'available': None,
                'port': port,
                'error': str(e)
            }

# Usage examples
def debug_all_mcp_servers():
    """Debug all configured MCP servers"""
    debugger = MCPDebugger()
    
    for server_name in debugger.server_configs.keys():
        print(f"\n{'='*60}")
        result = debugger.debug_server_connection(server_name)
        
        # Save debug results
        debug_file = Path.home() / '.gemini' / 'debug' / f'mcp_{server_name}_debug.json'
        debug_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(debug_file, 'w') as f:
            json.dump(result, f, indent=2, default=str)
            
        print(f"Debug results saved to: {debug_file}")

# Usage
if __name__ == "__main__":
    debugger = MCPDebugger()
    
    # Debug specific server
    result = debugger.debug_server_connection('context7')
    
    # Or debug all servers
    # debug_all_mcp_servers()
```

**MCP Communication Tracing:**
```bash
# Enable comprehensive MCP communication logging
export SUPERCLAUDE_DEBUG_MCP=true
export SUPERCLAUDE_TRACE_MCP=true
export SUPERCLAUDE_MCP_LOG_LEVEL=debug

# Create MCP log directory
mkdir -p ~/.gemini/logs/mcp

# Trace MCP requests and responses (fixed commands)
python -m setup.main debug --mcp-trace --verbose

# Alternative: Use direct debugging
python -c "
import os
import logging
os.environ['SUPERCLAUDE_DEBUG_MCP'] = 'true'

from setup.mcp.manager import MCPManager

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

manager = MCPManager()
print('Available servers:', manager.get_available_servers())
print('Active servers:', manager.get_active_servers())

# Test connection to specific server
try:
    connection = manager.connect_server('context7')
    print(f'Context7 connection: {connection}')
except Exception as e:
    print(f'Connection failed: {e}')
"

# Monitor MCP communication in real-time
tail -f ~/.gemini/logs/superclaude-debug.log | grep -E "(MCP|REQUEST|RESPONSE)"

# Check individual MCP server logs
ls ~/.gemini/logs/mcp-*.log
tail -f ~/.gemini/logs/mcp-context7.log

# Debug specific MCP server issues
python -c "
from setup.mcp.debugging import MCPDebugger
debugger = MCPDebugger()
debugger.debug_all_mcp_servers()
"
```

## Common Issues Troubleshooting

### Installation and Setup Issues

**Issue: Component Installation Fails**
```bash
# Problem: Permission denied or file conflicts
ERROR: Permission denied: '/home/user/.gemini/GEMINI.md'

# Diagnosis
ls -la ~/.gemini/
whoami
groups

# Solution
sudo chown -R $USER:$USER ~/.gemini
chmod 755 ~/.gemini
chmod 644 ~/.gemini/*.md

# Verification
python -c "
from setup.components.core import CoreComponent
from setup.core.installation import InstallOptions
from pathlib import Path

component = CoreComponent()
install_dir = Path.home() / '.gemini'
options = InstallOptions(install_dir=install_dir, force=True)
result = component.install(options)
print(f'Installation result: {result.success}')
if not result.success:
    print(f'Error: {result.error}')
"
```

**Issue: MCP Server Connection Failures**
```bash
# Problem: Context7 server fails to start
ERROR: MCP server 'context7' failed to connect

# Comprehensive diagnosis
python -c "
from setup.mcp.debugging import MCPDebugger
debugger = MCPDebugger()
result = debugger.debug_server_connection('context7')
print('Debug complete. Check ~/.gemini/debug/mcp_context7_debug.json')
"

# Common fixes
# 1. Check Node.js version
node --version  # Should be 16+
npm --version

# 2. Reinstall MCP packages
npm install -g @context7/mcp-server
npm install -g @sequential-thinking/mcp-server
npm install -g @magic-ui/mcp-server

# 3. Verify PATH
echo $PATH | grep npm
which npx

# 4. Check port conflicts
netstat -tlnp | grep :300[1-6]

# 5. Reset MCP configuration
SuperGemini install mcp --force --reset
```

**Issue: Agent System Not Activating**
```bash
# Problem: Expected agents not selected for tasks
# Diagnosis script
python -c "
from setup.agents.debugging import AgentDebugger
from setup.core.task_context import TaskContext

debugger = AgentDebugger()
context = TaskContext(
    input_text='implement secure authentication system',
    file_count=5,
    complexity_score=0.7
)

agents, pattern = debugger.debug_agent_selection(context)
print(f'Expected: security-engineer')
print(f'Actually selected: {agents}')
print(f'Coordination: {pattern}')
"

# Common solutions
# 1. Check trigger keywords
cat ~/.gemini/AGENT_SecurityEngineer.md | grep -i "trigger"

# 2. Update agent triggers
# Edit ~/.gemini/AGENT_SecurityEngineer.md
# Add keywords: auth, authentication, secure, login

# 3. Clear agent cache
rm -f ~/.gemini/cache/agent_*.cache

# 4. Verify agent installation
python -c "
from setup.agents.manager import AgentManager
manager = AgentManager()
agents = manager.get_available_agents()
print([agent.name for agent in agents])
"
```

### Development and Testing Issues

**Issue: Tests Failing Due to Environment**
```bash
# Problem: Tests fail with import errors or missing dependencies
# Solution: Set up proper test environment

# 1. Create isolated test environment
python -m venv test_env
source test_env/bin/activate

# 2. Install all dependencies
pip install -e .[dev,test]
pip install pytest pytest-cov pytest-mock

# 3. Set test environment variables
export SUPERCLAUDE_TEST_MODE=true
export SUPERCLAUDE_CONFIG_DIR=/tmp/superclaude_test
export PYTHONPATH=$PWD:$PYTHONPATH

# 4. Verify test setup
python -c "
import sys
print('Python path:', sys.path)

try:
    from setup.components.base import BaseComponent
    print('✅ Components import successful')
except ImportError as e:
    print('❌ Components import failed:', e)

try:
    from setup.core.registry import ComponentRegistry
    print('✅ Registry import successful')
except ImportError as e:
    print('❌ Registry import failed:', e)
"

# 5. Run basic connectivity test
pytest tests/test_basic.py -v --tb=short
```

**Issue: Session Management Problems**
```bash
# Problem: Sessions not loading or saving properly
# Diagnosis
python -c "
from setup.services.session_manager import SessionManager
import json

manager = SessionManager()

# Check session directory
session_dir = manager.get_session_directory()
print(f'Session directory: {session_dir}')
print(f'Directory exists: {session_dir.exists()}')

if session_dir.exists():
    sessions = list(session_dir.glob('*.json'))
    print(f'Existing sessions: {len(sessions)}')
    for session in sessions:
        print(f'  {session.name}')

# Test session creation
try:
    test_session = manager.create_session('test-debug')
    print(f'✅ Session creation successful: {test_session.id}')
    
    # Test session save/load
    manager.save_session(test_session.id)
    loaded = manager.load_session(test_session.id)
    print(f'✅ Session save/load successful')
    
except Exception as e:
    print(f'❌ Session operation failed: {e}')
"

# Common fixes
# 1. Check permissions
chmod 755 ~/.gemini/sessions/
chmod 644 ~/.gemini/sessions/*.json

# 2. Clear corrupted sessions
rm ~/.gemini/sessions/corrupted_session_*.json

# 3. Reset session storage
mv ~/.gemini/sessions ~/.gemini/sessions_backup
mkdir -p ~/.gemini/sessions
```

### Performance and Memory Issues

**Issue: High Memory Usage**
```python
# Diagnosis script
import psutil
import gc
from setup.services.session_manager import SessionManager
from setup.core.registry import ComponentRegistry

def diagnose_memory_issues():
    """Comprehensive memory diagnosis"""
    print("🧠 Memory Diagnosis Report")
    print("=" * 40)
    
    # System memory
    memory = psutil.virtual_memory()
    print(f"System Memory: {memory.percent}% used ({memory.used // 1024**2} MB)")
    
    # Process memory
    process = psutil.Process()
    process_memory = process.memory_info()
    print(f"Process Memory: {process_memory.rss // 1024**2} MB")
    
    # Python object counts
    gc.collect()
    object_counts = {}
    for obj in gc.get_objects():
        obj_type = type(obj).__name__
        object_counts[obj_type] = object_counts.get(obj_type, 0) + 1
    
    # Show top memory consumers
    top_objects = sorted(object_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    print("\nTop Object Types:")
    for obj_type, count in top_objects:
        print(f"  {obj_type}: {count}")
    
    # Check SuperGemini specific memory usage
    try:
        session_manager = SessionManager()
        active_sessions = session_manager.get_active_sessions()
        print(f"\nActive Sessions: {len(active_sessions)}")
        
        registry = ComponentRegistry()
        loaded_components = registry.get_loaded_components()
        print(f"Loaded Components: {len(loaded_components)}")
        
    except Exception as e:
        print(f"SuperGemini memory check failed: {e}")
    
    # Memory leak detection
    gc.set_debug(gc.DEBUG_LEAK)
    gc.collect()
    leaked_objects = gc.garbage
    if leaked_objects:
        print(f"\n⚠️  Potential memory leaks: {len(leaked_objects)} objects")
    else:
        print("\n✅ No obvious memory leaks detected")

if __name__ == "__main__":
    diagnose_memory_issues()
```

### Debugging Workflow Integration

**Debugging Workflow for Complex Issues:**
```python
# Complete debugging workflow script
import json
import time
from pathlib import Path
from setup.agents.debugging import AgentDebugger
from setup.modes.debugging import ModeDebugger
from setup.mcp.debugging import MCPDebugger

class ComprehensiveDebugger:
    def __init__(self):
        self.debug_dir = Path.home() / '.gemini' / 'debug'
        self.debug_dir.mkdir(parents=True, exist_ok=True)
        
        self.agent_debugger = AgentDebugger()
        self.mode_debugger = ModeDebugger()
        self.mcp_debugger = MCPDebugger()
        
    def run_full_diagnosis(self, issue_description: str) -> Dict[str, Any]:
        """Run comprehensive diagnosis for any issue"""
        print(f"🔍 Starting comprehensive diagnosis for: {issue_description}")
        
        diagnosis_results = {
            'issue_description': issue_description,
            'timestamp': time.time(),
            'components': {}
        }
        
        # Test agent system
        print("\n1. Testing Agent System...")
        agent_results = self._test_agent_system()
        diagnosis_results['components']['agents'] = agent_results
        
        # Test mode system
        print("\n2. Testing Mode System...")
        mode_results = self._test_mode_system()
        diagnosis_results['components']['modes'] = mode_results
        
        # Test MCP servers
        print("\n3. Testing MCP Servers...")
        mcp_results = self._test_mcp_system()
        diagnosis_results['components']['mcp'] = mcp_results
        
        # Generate recommendations
        print("\n4. Generating Recommendations...")
        recommendations = self._generate_recommendations(diagnosis_results)
        diagnosis_results['recommendations'] = recommendations
        
        # Save results
        results_file = self.debug_dir / f'diagnosis_{int(time.time())}.json'
        with open(results_file, 'w') as f:
            json.dump(diagnosis_results, f, indent=2, default=str)
            
        print(f"\n📊 Diagnosis complete. Results saved to: {results_file}")
        return diagnosis_results
        
    def _test_agent_system(self) -> Dict[str, Any]:
        """Test agent system functionality"""
        from setup.core.task_context import TaskContext
        
        test_contexts = [
            TaskContext(input_text="implement authentication", complexity_score=0.5),
            TaskContext(input_text="debug security issue", complexity_score=0.8),
            TaskContext(input_text="create UI components", complexity_score=0.6)
        ]
        
        results = {'tests': [], 'overall_health': 'unknown'}
        
        for i, context in enumerate(test_contexts):
            try:
                agents, pattern = self.agent_debugger.debug_agent_selection(context)
                results['tests'].append({
                    'test_id': i,
                    'input': context.input_text,
                    'selected_agents': agents,
                    'coordination_pattern': pattern,
                    'success': True
                })
            except Exception as e:
                results['tests'].append({
                    'test_id': i,
                    'input': context.input_text,
                    'error': str(e),
                    'success': False
                })
                
        # Determine overall health
        successful_tests = sum(1 for test in results['tests'] if test.get('success', False))
        if successful_tests == len(test_contexts):
            results['overall_health'] = 'healthy'
        elif successful_tests > 0:
            results['overall_health'] = 'partial'
        else:
            results['overall_health'] = 'failed'
            
        return results
        
    def _test_mode_system(self) -> Dict[str, Any]:
        """Test mode system functionality"""
        # Similar implementation for mode testing
        return {'overall_health': 'healthy', 'tests': []}
        
    def _test_mcp_system(self) -> Dict[str, Any]:
        """Test MCP server system"""
        mcp_servers = ['context7', 'sequential', 'magic']
        results = {'servers': {}, 'overall_health': 'unknown'}
        
        healthy_servers = 0
        for server in mcp_servers:
            try:
                server_result = self.mcp_debugger.debug_server_connection(server)
                results['servers'][server] = server_result
                
                if server_result['checks'].get('connection', {}).get('connected', False):
                    healthy_servers += 1
                    
            except Exception as e:
                results['servers'][server] = {'error': str(e), 'healthy': False}
                
        # Determine overall health
        if healthy_servers == len(mcp_servers):
            results['overall_health'] = 'healthy'
        elif healthy_servers > 0:
            results['overall_health'] = 'partial'
        else:
            results['overall_health'] = 'failed'
            
        return results
        
    def _generate_recommendations(self, diagnosis_results: Dict[str, Any]) -> List[str]:
        """Generate specific recommendations based on diagnosis"""
        recommendations = []
        
        # Agent system recommendations
        agent_health = diagnosis_results['components']['agents']['overall_health']
        if agent_health != 'healthy':
            recommendations.append("Reinstall agent components: SuperGemini install agents --force")
            recommendations.append("Check agent trigger keywords in ~/.gemini/AGENT_*.md files")
            
        # MCP system recommendations
        mcp_health = diagnosis_results['components']['mcp']['overall_health']
        if mcp_health != 'healthy':
            recommendations.append("Check Node.js version: node --version (requires 16+)")
            recommendations.append("Reinstall MCP servers: SuperGemini install mcp --force")
            recommendations.append("Check MCP server logs: ~/.gemini/logs/mcp-*.log")
            
        # General recommendations
        if not recommendations:
            recommendations.append("✅ All systems appear healthy")
        else:
            recommendations.insert(0, "🔧 Recommended fixes:")
            
        return recommendations

# Usage
if __name__ == "__main__":
    debugger = ComprehensiveDebugger()
    
    # Example usage
    issue = "Agents not activating for security tasks"
    results = debugger.run_full_diagnosis(issue)
    
    print("\n📋 Summary:")
    for rec in results['recommendations']:
        print(f"  {rec}")
```

### Session Management Debugging

**Session Context Inspection:**
```python
# Session debugging with complete imports
import json
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
from setup.services.session_manager import SessionManager
from setup.core.session import Session
from setup.core.memory import MemoryManager

class SessionDebugger:
    def __init__(self):
        self.session_manager = SessionManager()
        self.memory_manager = MemoryManager()
        
    def debug_session_state(self, session_id: str) -> Dict[str, Any]:
        """Comprehensive session state debugging"""
        print(f"💾 Session Debug: {session_id}")
        
        debug_results = {
            'session_id': session_id,
            'timestamp': time.time(),
            'checks': {}
        }
        
        try:
            # Load session context
            session = self._load_session_context(session_id)
            if session:
                context_info = self._analyze_session_context(session)
                print(f"  Context size: {context_info['size']} items")
                debug_results['checks']['context'] = context_info
                
                # Analyze memory usage
                memory_usage = self._analyze_memory_usage(session)
                print(f"  Memory usage: {memory_usage['total_mb']} MB")
                debug_results['checks']['memory'] = memory_usage
                
                # Check context health
                health = self._check_context_health(session)
                print(f"  Context health: {health['status']}")
                debug_results['checks']['health'] = health
                
                # Show recent activities
                activities = self._get_recent_activities(session, limit=10)
                print(f"  Recent activities: {len(activities)} items")
                debug_results['checks']['activities'] = activities
                
                for activity in activities[:5]:  # Show first 5
                    print(f"    {activity['timestamp']}: {activity['action']}")
                    
            else:
                error_msg = f"Session {session_id} not found or failed to load"
                print(f"  Error: {error_msg}")
                debug_results['checks']['error'] = error_msg
                
        except Exception as e:
            error_msg = f"Session debugging failed: {str(e)}"
            print(f"  Error: {error_msg}")
            debug_results['checks']['error'] = error_msg
            
        return debug_results
        
    def _load_session_context(self, session_id: str) -> Optional[Session]:
        """Load session with error handling"""
        try:
            return self.session_manager.load_session(session_id)
        except Exception as e:
            print(f"Failed to load session {session_id}: {e}")
            return None
            
    def _analyze_session_context(self, session: Session) -> Dict[str, Any]:
        """Analyze session context structure and content"""
        context_info = {
            'size': 0,
            'components': [],
            'memory_items': 0,
            'last_activity': None
        }
        
        try:
            # Get context size
            if hasattr(session, 'context'):
                context_info['size'] = len(session.context)
                
            # Get active components
            if hasattr(session, 'active_components'):
                context_info['components'] = session.active_components
                
            # Get memory items count
            if hasattr(session, 'memory_items'):
                context_info['memory_items'] = len(session.memory_items)
                
            # Get last activity
            if hasattr(session, 'last_activity'):
                context_info['last_activity'] = session.last_activity
                
        except Exception as e:
            context_info['error'] = str(e)
            
        return context_info
        
    def _analyze_memory_usage(self, session: Session) -> Dict[str, Any]:
        """Analyze session memory usage"""
        memory_info = {
            'total_mb': 0,
            'context_mb': 0,
            'memory_items_mb': 0,
            'breakdown': {}
        }
        
        try:
            import sys
            
            # Calculate context memory
            if hasattr(session, 'context'):
                context_size = sys.getsizeof(session.context)
                memory_info['context_mb'] = context_size / (1024 * 1024)
                
            # Calculate memory items size
            if hasattr(session, 'memory_items'):
                memory_items_size = sys.getsizeof(session.memory_items)
                memory_info['memory_items_mb'] = memory_items_size / (1024 * 1024)
                
            # Total memory
            memory_info['total_mb'] = memory_info['context_mb'] + memory_info['memory_items_mb']
            
            # Memory breakdown by type
            if hasattr(session, 'memory_items'):
                type_counts = {}
                for item in session.memory_items:
                    item_type = type(item).__name__
                    type_counts[item_type] = type_counts.get(item_type, 0) + 1
                memory_info['breakdown'] = type_counts
                
        except Exception as e:
            memory_info['error'] = str(e)
            
        return memory_info
        
    def _check_context_health(self, session: Session) -> Dict[str, Any]:
        """Check session context health and consistency"""
        health_info = {
            'status': 'unknown',
            'issues': [],
            'warnings': []
        }
        
        try:
            # Check if session is valid
            if not hasattr(session, 'id'):
                health_info['issues'].append('Session missing ID')
                
            # Check context consistency
            if hasattr(session, 'context') and session.context is None:
                health_info['warnings'].append('Context is None')
                
            # Check memory item validity
            if hasattr(session, 'memory_items'):
                invalid_items = 0
                for item in session.memory_items:
                    if not hasattr(item, 'key') or not hasattr(item, 'value'):
                        invalid_items += 1
                if invalid_items > 0:
                    health_info['warnings'].append(f'{invalid_items} invalid memory items')
                    
            # Determine overall status
            if health_info['issues']:
                health_info['status'] = 'unhealthy'
            elif health_info['warnings']:
                health_info['status'] = 'warning'
            else:
                health_info['status'] = 'healthy'
                
        except Exception as e:
            health_info['status'] = 'error'
            health_info['issues'].append(f'Health check failed: {str(e)}')
            
        return health_info
        
    def _get_recent_activities(self, session: Session, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent session activities"""
        activities = []
        
        try:
            if hasattr(session, 'activity_log'):
                # Get from activity log
                for activity in session.activity_log[-limit:]:
                    activities.append({
                        'timestamp': activity.get('timestamp', 'unknown'),
                        'action': activity.get('action', 'unknown'),
                        'details': activity.get('details', {})
                    })
            else:
                # Generate synthetic activity info
                activities.append({
                    'timestamp': datetime.now().isoformat(),
                    'action': 'session_loaded',
                    'details': {'session_id': session.id}
                })
                
        except Exception as e:
            activities.append({
                'timestamp': datetime.now().isoformat(),
                'action': 'error',
                'details': {'error': str(e)}
            })
            
        return activities
        
    def debug_all_sessions(self) -> Dict[str, Any]:
        """Debug all available sessions"""
        print("🔍 Debugging All Sessions")
        print("=" * 40)
        
        all_results = {
            'session_count': 0,
            'healthy_sessions': 0,
            'sessions': {}
        }
        
        try:
            available_sessions = self.session_manager.list_sessions()
            all_results['session_count'] = len(available_sessions)
            
            for session_id in available_sessions:
                print(f"\nDebugging session: {session_id}")
                session_result = self.debug_session_state(session_id)
                all_results['sessions'][session_id] = session_result
                
                # Count healthy sessions
                if session_result['checks'].get('health', {}).get('status') == 'healthy':
                    all_results['healthy_sessions'] += 1
                    
        except Exception as e:
            all_results['error'] = str(e)
            
        print(f"\n📊 Summary: {all_results['healthy_sessions']}/{all_results['session_count']} sessions healthy")
        return all_results

# Usage examples
def debug_session_example():
    """Example session debugging usage"""
    debugger = SessionDebugger()
    
    # Debug specific session
    result = debugger.debug_session_state('current-session')
    
    # Save debug results
    debug_file = Path.home() / '.gemini' / 'debug' / 'session_debug.json'
    debug_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(debug_file, 'w') as f:
        json.dump(result, f, indent=2, default=str)
        
    print(f"Debug results saved to: {debug_file}")
    return result

# Usage
if __name__ == "__main__":
    debug_session_example()
```

**Session Lifecycle Tracing:**
```bash
# Enable comprehensive session debugging
export SUPERCLAUDE_DEBUG_SESSIONS=true
export SUPERCLAUDE_DEBUG_SESSION_LIFECYCLE=true
export SUPERCLAUDE_LOG_LEVEL=debug

# Create session debug environment
mkdir -p ~/.gemini/debug/sessions
mkdir -p ~/.gemini/logs

# Trace session operations with enhanced debugging
python -c "
import os
import json
from pathlib import Path
from setup.services.session_manager import SessionManager
from setup.core.session import Session

# Enable debug mode
os.environ['SUPERCLAUDE_DEBUG_SESSIONS'] = 'true'

# Initialize session manager with debugging
manager = SessionManager()

# Enable debug mode if available
if hasattr(manager, 'enable_debug_mode'):
    manager.enable_debug_mode()
    print('✅ Debug mode enabled')

# Check existing sessions
print('\\n📁 Existing Sessions:')
try:
    sessions = manager.list_sessions()
    print(f'Found {len(sessions)} sessions:')
    for session_id in sessions:
        print(f'  - {session_id}')
except Exception as e:
    print(f'Failed to list sessions: {e}')

# Create test session with tracing
print('\\n🔄 Creating Test Session:')
try:
    test_session = manager.create_session('debug-test-session')
    print(f'✅ Created session: {test_session.id}')
    
    # Add some test data
    test_session.add_memory('test_key', 'test_value')
    test_session.add_context('test_context', {'type': 'debug'})
    
    # Save session
    manager.save_session(test_session.id)
    print('✅ Session saved')
    
    # Load session with tracing
    print('\\n📥 Loading Session:')
    loaded_session = manager.load_session(test_session.id)
    
    if loaded_session:
        print(f'✅ Session loaded: {loaded_session.id}')
        
        # Debug info
        if hasattr(loaded_session, 'debug_info'):
            debug_info = loaded_session.debug_info()
            print(f'Debug info: {debug_info}')
        else:
            print('Session structure:')
            print(f'  ID: {getattr(loaded_session, \"id\", \"N/A\")}')
            print(f'  Memory items: {len(getattr(loaded_session, \"memory_items\", []))}')
            print(f'  Context size: {len(getattr(loaded_session, \"context\", {}))}')
    else:
        print('❌ Failed to load session')
        
except Exception as e:
    print(f'❌ Session operation failed: {e}')
    import traceback
    traceback.print_exc()
"

# Check session storage and metadata
echo -e "\n📂 Session Storage Analysis:"
ls -la ~/.gemini/sessions/ 2>/dev/null || echo "Session directory not found"

# Check for session metadata
if [ -f ~/.gemini/sessions/session-metadata.json ]; then
    echo -e "\n📄 Session Metadata:"
    cat ~/.gemini/sessions/session-metadata.json | python -m json.tool
else
    echo "No session metadata file found"
fi

# Check session logs
echo -e "\n📋 Session Logs:"
ls -la ~/.gemini/logs/*session*.log 2>/dev/null || echo "No session logs found"

# Monitor session activity in real-time
echo -e "\n🔍 Monitoring Session Activity:"
echo "Run this in a separate terminal:"
echo "tail -f ~/.gemini/logs/superclaude-debug.log | grep -E '(SESSION|MEMORY|CONTEXT)'"
```

**Memory Debugging:**
```python
# Memory debugging with complete imports
import gc
import sys
import time
import psutil
import tracemalloc
from typing import Dict, List, Any, Optional
from setup.services.session_manager import SessionManager
from setup.core.registry import ComponentRegistry
from setup.mcp.manager import MCPManager

class MemoryDebugger:
    def __init__(self):
        self.session_manager = SessionManager()
        self.component_registry = ComponentRegistry()
        self.mcp_manager = MCPManager()
        
    def debug_memory_usage(self) -> Dict[str, Any]:
        """Comprehensive memory usage debugging"""
        print("🧠 Memory Usage Debug:")
        
        memory_report = {
            'timestamp': time.time(),
            'system': {},
            'process': {},
            'superclaude': {},
            'sessions': {},
            'components': {},
            'leaks': []
        }
        
        # System memory
        system_memory = self._debug_system_memory()
        print(f"  System memory: {system_memory['percent']}% used ({system_memory['used_gb']:.1f} GB)")
        memory_report['system'] = system_memory
        
        # Process memory
        process_memory = self._debug_process_memory()
        print(f"  Process memory: {process_memory['rss_mb']:.1f} MB RSS, {process_memory['vms_mb']:.1f} MB VMS")
        memory_report['process'] = process_memory
        
        # SuperGemini specific memory
        sc_memory = self._get_superclaude_memory()
        print(f"  SuperGemini components: {sc_memory['total_mb']:.1f} MB")
        memory_report['superclaude'] = sc_memory
        
        # Session memory breakdown
        session_memory = self._debug_session_memory()
        print(f"  Active sessions: {len(session_memory)} sessions, {session_memory.get('total_mb', 0):.1f} MB")
        memory_report['sessions'] = session_memory
        
        # Component memory
        component_memory = self._debug_component_memory()
        print(f"  Loaded components: {len(component_memory)} components")
        memory_report['components'] = component_memory
        
        # Memory leak detection
        leaks = self._detect_memory_leaks()
        if leaks:
            print(f"  🚨 Potential leaks: {len(leaks)} objects")
            memory_report['leaks'] = leaks
        else:
            print("  ✅ No obvious memory leaks detected")
            
        return memory_report
        
    def _debug_system_memory(self) -> Dict[str, Any]:
        """Debug system-wide memory usage"""
        try:
            memory = psutil.virtual_memory()
            return {
                'total_gb': memory.total / (1024**3),
                'used_gb': memory.used / (1024**3),
                'available_gb': memory.available / (1024**3),
                'percent': memory.percent
            }
        except Exception as e:
            return {'error': str(e)}
            
    def _debug_process_memory(self) -> Dict[str, Any]:
        """Debug current process memory usage"""
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            memory_percent = process.memory_percent()
            
            return {
                'rss_mb': memory_info.rss / (1024**2),
                'vms_mb': memory_info.vms / (1024**2),
                'percent': memory_percent,
                'num_threads': process.num_threads()
            }
        except Exception as e:
            return {'error': str(e)}
            
    def _get_superclaude_memory(self) -> Dict[str, Any]:
        """Get SuperGemini specific memory usage"""
        try:
            total_size = 0
            component_sizes = {}
            
            # Measure component registry
            if hasattr(self.component_registry, 'components'):
                registry_size = sys.getsizeof(self.component_registry.components)
                component_sizes['registry'] = registry_size / (1024**2)
                total_size += registry_size
                
            # Measure MCP manager
            if hasattr(self.mcp_manager, 'connections'):
                mcp_size = sys.getsizeof(self.mcp_manager.connections)
                component_sizes['mcp_manager'] = mcp_size / (1024**2)
                total_size += mcp_size
                
            # Measure session manager
            if hasattr(self.session_manager, 'sessions'):
                session_mgr_size = sys.getsizeof(self.session_manager.sessions)
                component_sizes['session_manager'] = session_mgr_size / (1024**2)
                total_size += session_mgr_size
                
            return {
                'total_mb': total_size / (1024**2),
                'breakdown': component_sizes
            }
        except Exception as e:
            return {'error': str(e)}
            
    def _debug_session_memory(self) -> Dict[str, Any]:
        """Debug session memory usage"""
        try:
            sessions = self._get_active_sessions()
            session_memory = {}
            total_memory = 0
            
            for session_id, session in sessions.items():
                size = self._get_session_memory_size(session)
                session_memory[session_id] = size
                total_memory += size
                
            return {
                'sessions': session_memory,
                'total_mb': total_memory / (1024**2),
                'count': len(sessions)
            }
        except Exception as e:
            return {'error': str(e)}
            
    def _debug_component_memory(self) -> Dict[str, Any]:
        """Debug component memory usage"""
        try:
            components = {}
            
            # Get loaded components
            if hasattr(self.component_registry, 'get_loaded_components'):
                loaded = self.component_registry.get_loaded_components()
                for component_name, component in loaded.items():
                    size = sys.getsizeof(component) / (1024**2)
                    components[component_name] = {
                        'size_mb': size,
                        'type': type(component).__name__
                    }
                    
            return components
        except Exception as e:
            return {'error': str(e)}
            
    def _get_active_sessions(self) -> Dict[str, Any]:
        """Get active sessions safely"""
        try:
            if hasattr(self.session_manager, 'get_active_sessions'):
                return self.session_manager.get_active_sessions()
            elif hasattr(self.session_manager, 'sessions'):
                return self.session_manager.sessions
            else:
                return {}
        except Exception:
            return {}
            
    def _get_session_memory_size(self, session) -> int:
        """Get memory size of a session object"""
        try:
            if hasattr(session, 'get_memory_size'):
                return session.get_memory_size()
            else:
                # Calculate manually
                size = sys.getsizeof(session)
                if hasattr(session, 'context'):
                    size += sys.getsizeof(session.context)
                if hasattr(session, 'memory_items'):
                    size += sys.getsizeof(session.memory_items)
                return size
        except Exception:
            return 0
            
    def _detect_memory_leaks(self) -> List[Dict[str, Any]]:
        """Detect potential memory leaks"""
        try:
            # Force garbage collection
            gc.collect()
            
            # Check for unreachable objects
            unreachable = gc.garbage
            leaks = []
            
            for obj in unreachable[:10]:  # Limit to first 10
                leaks.append({
                    'type': type(obj).__name__,
                    'size': sys.getsizeof(obj),
                    'id': id(obj)
                })
                
            # Check for circular references
            referrers = {}
            for obj in gc.get_objects():
                obj_type = type(obj).__name__
                referrers[obj_type] = referrers.get(obj_type, 0) + 1
                
            # Look for suspicious patterns
            suspicious_types = ['function', 'method', 'traceback']
            for obj_type in suspicious_types:
                if referrers.get(obj_type, 0) > 1000:
                    leaks.append({
                        'type': f'excessive_{obj_type}',
                        'count': referrers[obj_type],
                        'warning': f'High number of {obj_type} objects'
                    })
                    
            return leaks
        except Exception as e:
            return [{'error': str(e)}]
            
    def start_memory_monitoring(self, output_file: Optional[str] = None):
        """Start continuous memory monitoring"""
        try:
            # Start tracemalloc for detailed tracking
            tracemalloc.start()
            
            print("🔍 Memory monitoring started")
            print("Call stop_memory_monitoring() to get detailed report")
            
            if output_file:
                print(f"Results will be saved to: {output_file}")
                
        except Exception as e:
            print(f"Failed to start memory monitoring: {e}")
            
    def stop_memory_monitoring(self, output_file: Optional[str] = None) -> Dict[str, Any]:
        """Stop memory monitoring and generate report"""
        try:
            if not tracemalloc.is_tracing():
                print("Memory monitoring not active")
                return {}
                
            # Get current trace
            current, peak = tracemalloc.get_traced_memory()
            
            # Get top stats
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')
            
            # Stop tracing
            tracemalloc.stop()
            
            report = {
                'current_mb': current / (1024**2),
                'peak_mb': peak / (1024**2),
                'top_memory_locations': []
            }
            
            # Add top memory consuming locations
            for index, stat in enumerate(top_stats[:10]):
                report['top_memory_locations'].append({
                    'rank': index + 1,
                    'size_mb': stat.size / (1024**2),
                    'count': stat.count,
                    'filename': stat.traceback.format()[0] if stat.traceback else 'unknown'
                })
                
            print(f"📊 Memory Monitoring Report:")
            print(f"  Current usage: {report['current_mb']:.1f} MB")
            print(f"  Peak usage: {report['peak_mb']:.1f} MB")
            
            if output_file:
                import json
                with open(output_file, 'w') as f:
                    json.dump(report, f, indent=2, default=str)
                print(f"  Report saved to: {output_file}")
                
            return report
            
        except Exception as e:
            print(f"Failed to stop memory monitoring: {e}")
            return {'error': str(e)}

# Usage examples
def memory_debugging_example():
    """Example memory debugging workflow"""
    debugger = MemoryDebugger()
    
    # Basic memory check
    print("=== Basic Memory Analysis ===")
    memory_report = debugger.debug_memory_usage()
    
    # Start detailed monitoring
    print("\n=== Starting Detailed Monitoring ===")
    debugger.start_memory_monitoring()
    
    # Simulate some work
    try:
        from setup.core.task_context import TaskContext
        contexts = []
        for i in range(100):
            context = TaskContext(
                input_text=f"test task {i}",
                complexity_score=0.5
            )
            contexts.append(context)
            
        print(f"Created {len(contexts)} task contexts")
        
    except Exception as e:
        print(f"Test work failed: {e}")
    
    # Stop monitoring and get report
    print("\n=== Monitoring Report ===")
    monitoring_report = debugger.stop_memory_monitoring('/tmp/memory_report.json')
    
    return memory_report, monitoring_report

if __name__ == "__main__":
    memory_debugging_example()
```

## Development Testing Patterns

### Unit Testing Patterns

**Component Testing Pattern:**
```python
class TestComponentBase:
    """Base class for component testing"""
    
    @pytest.fixture
    def temp_install_dir(self):
        """Provide temporary installation directory"""
        temp_dir = Path(tempfile.mkdtemp())
        yield temp_dir
        shutil.rmtree(temp_dir)
        
    @pytest.fixture  
    def mock_registry(self):
        """Provide mock component registry"""
        registry = ComponentRegistry()
        registry.components = {}  # Clean state
        return registry

class TestAgentComponent(TestComponentBase):
    def test_agent_installation(self, temp_install_dir, mock_registry):
        """Test agent component installation"""
        # Setup
        agent_component = AgentComponent()
        
        # Execute
        result = agent_component.install(temp_install_dir)
        
        # Verify
        assert result.success
        assert (temp_install_dir / 'AGENT_SecurityEngineer.md').exists()
        
        # Verify content
        content = (temp_install_dir / 'AGENT_SecurityEngineer.md').read_text()
        assert 'security' in content
        assert 'vulnerability' in content
```

**Integration Testing Pattern:**
```python
class TestComponentIntegration:
    def test_full_installation_workflow(self):
        """Test complete installation workflow"""
        # Setup clean environment
        test_config = self._create_test_config()
        
        # Install core components
        installer = InstallationOrchestrator()
        result = installer.install_components(['core'], test_config)
        
        assert result.success
        assert test_config.install_dir.exists()
        
        # Verify core functionality
        gemini_md = test_config.install_dir / 'GEMINI.md'
        assert gemini_md.exists()
        
        content = gemini_md.read_text()
        assert '@FLAGS.md' in content
        assert '@RULES.md' in content
        
    def test_mcp_integration(self):
        """Test MCP server integration"""
        # Install MCP component
        mcp_component = MCPComponent()
        result = mcp_component.install(self.test_dir)
        
        # Verify MCP configuration
        mcp_config = self.test_dir / '.gemini.json'
        assert mcp_config.exists()
        
        config_data = json.loads(mcp_config.read_text())
        assert 'mcpServers' in config_data
        assert 'context7' in config_data['mcpServers']
```

**Test-Driven Development Pattern:**
```python
# 1. Write test first (Red)
def test_new_agent_activation():
    """Test new data science agent activation"""
    agent_system = AgentSystem()
    
    # Should activate on data science keywords
    task_context = TaskContext(
        input_text="analyze this dataset with pandas",
        file_types=['.csv', '.ipynb']
    )
    
    selected_agents = agent_system.select_agents(task_context)
    assert 'data-scientist' in selected_agents

# 2. Implement minimal code (Green)
class AgentSystem:
    def select_agents(self, task_context):
        if 'dataset' in task_context.input_text:
            return ['data-scientist']
        return []

# 3. Refactor (Refactor)
class AgentSystem:
    def select_agents(self, task_context):
        selected = []
        
        # Data science triggers
        data_triggers = ['dataset', 'pandas', 'numpy', 'analytics']
        if any(trigger in task_context.input_text for trigger in data_triggers):
            selected.append('data-scientist')
            
        return selected
```

## Chaos Engineering & Fault Injection ⏱️ **45-60 minutes setup**

**🎯 Skill Level: Advanced**

Systematic chaos engineering framework for testing SuperGemini Framework resilience and fault tolerance:

### Chaos Engineering Framework

**Chaos Testing Philosophy:**
SuperGemini Framework operates in complex environments with multiple failure modes. Chaos engineering proactively tests system resilience by intentionally introducing controlled failures.

```python
# chaos/framework/chaos_engine.py
import random
import time
import threading
import subprocess
from typing import List, Dict, Any, Callable
from dataclasses import dataclass
from enum import Enum

class FailureType(Enum):
    """Types of failures that can be injected"""
    NETWORK_LATENCY = "network_latency"
    NETWORK_PARTITION = "network_partition"
    MEMORY_PRESSURE = "memory_pressure"
    CPU_SPIKE = "cpu_spike"
    DISK_IO_FAILURE = "disk_io_failure"
    PROCESS_KILL = "process_kill"
    MCP_SERVER_CRASH = "mcp_server_crash"
    AGENT_COORDINATION_FAILURE = "agent_coordination_failure"
    CONFIG_CORRUPTION = "config_corruption"

@dataclass
class ChaosExperiment:
    """Definition of a chaos engineering experiment"""
    name: str
    description: str
    failure_type: FailureType
    target_components: List[str]
    duration_seconds: int
    intensity: float  # 0.0 to 1.0
    recovery_time: int
    success_criteria: Dict[str, Any]
    rollback_strategy: str

class ChaosEngine:
    """Core chaos engineering orchestration engine"""
    
    def __init__(self):
        self.active_experiments = {}
        self.failure_injectors = {
            FailureType.NETWORK_LATENCY: NetworkLatencyInjector(),
            FailureType.MEMORY_PRESSURE: MemoryPressureInjector(), 
            FailureType.PROCESS_KILL: ProcessKillInjector(),
            FailureType.MCP_SERVER_CRASH: MCPServerCrashInjector(),
            FailureType.AGENT_COORDINATION_FAILURE: AgentFailureInjector(),
            FailureType.CONFIG_CORRUPTION: ConfigCorruptionInjector()
        }
        
    def execute_experiment(self, experiment: ChaosExperiment) -> Dict[str, Any]:
        """Execute a chaos engineering experiment with monitoring"""
        
        experiment_id = f"{experiment.name}_{int(time.time())}"
        print(f"🔥 Starting chaos experiment: {experiment.name}")
        
        # Pre-experiment baseline measurement
        baseline_metrics = self._measure_baseline_performance()
        
        # Start monitoring
        monitor = self._start_experiment_monitoring(experiment_id)
        
        try:
            # Inject failure
            injector = self.failure_injectors[experiment.failure_type]
            failure_context = injector.inject_failure(experiment)
            
            print(f"💥 Failure injected: {experiment.failure_type.value}")
            self.active_experiments[experiment_id] = {
                'experiment': experiment,
                'failure_context': failure_context,
                'start_time': time.time()
            }
            
            # Monitor system behavior during failure
            failure_metrics = self._monitor_during_failure(
                experiment, 
                experiment.duration_seconds
            )
            
            # Stop failure injection
            injector.stop_failure(failure_context)
            print(f"🛑 Failure injection stopped")
            
            # Monitor recovery
            recovery_metrics = self._monitor_recovery(
                experiment,
                experiment.recovery_time
            )
            
            # Analyze results
            results = self._analyze_experiment_results(
                experiment,
                baseline_metrics,
                failure_metrics,
                recovery_metrics
            )
            
            return results
            
        except Exception as e:
            print(f"❌ Chaos experiment failed: {e}")
            # Emergency cleanup
            self._emergency_cleanup(experiment_id)
            raise
            
        finally:
            # Stop monitoring
            monitor.stop()
            # Clean up experiment tracking
            if experiment_id in self.active_experiments:
                del self.active_experiments[experiment_id]
```

**Fault Injection Framework:**
```python
# chaos/fault_injection/targeted_faults.py
import pytest
import asyncio
from chaos.framework.chaos_engine import ChaosEngine, ChaosExperiment, FailureType

class TestFaultInjection:
    """Targeted fault injection tests for specific components"""
    
    @pytest.fixture
    def chaos_engine(self):
        return ChaosEngine()
    
    def test_mcp_server_connection_failure(self, chaos_engine):
        """Test MCP server connection failure handling"""
        
        experiment = ChaosExperiment(
            name="MCP Connection Failure Test",
            description="Test framework behavior when MCP servers become unavailable",
            failure_type=FailureType.MCP_SERVER_CRASH,
            target_components=["context7"],
            duration_seconds=30,
            intensity=1.0,  # Complete failure
            recovery_time=15,
            success_criteria={
                "fallback_activated": True,
                "error_handling": True,
                "recovery_time": 20
            },
            rollback_strategy="automatic"
        )
        
        # Execute fault injection
        results = chaos_engine.execute_experiment(experiment)
        
        # Verify graceful degradation
        assert results['fallback_activated'], "Fallback mechanisms should activate"
        assert results['error_handling'], "Errors should be handled gracefully"
        assert results['recovery_time'] <= 20, "Recovery should complete within 20 seconds"
    
    def test_concurrent_failure_scenarios(self, chaos_engine):
        """Test system behavior under multiple concurrent failures"""
        
        # Test concurrent network and memory failures
        network_experiment = ChaosExperiment(
            name="Network Latency",
            failure_type=FailureType.NETWORK_LATENCY,
            target_components=["context7", "sequential"],
            duration_seconds=45,
            intensity=0.6,
            recovery_time=20,
            success_criteria={"max_latency": 2.0},
            rollback_strategy="automatic"
        )
        
        memory_experiment = ChaosExperiment(
            name="Memory Pressure",
            failure_type=FailureType.MEMORY_PRESSURE,
            target_components=["framework"],
            duration_seconds=45,
            intensity=0.5,
            recovery_time=20,
            success_criteria={"memory_leak_check": True},
            rollback_strategy="automatic"
        )
        
        # Execute both experiments and verify system stability
        network_result = chaos_engine.execute_experiment(network_experiment)
        memory_result = chaos_engine.execute_experiment(memory_experiment)
        
        assert network_result['system_stability'], "Network failure should not break system"
        assert memory_result['system_stability'], "Memory pressure should be handled gracefully"
```

### Property-Based Testing with Hypothesis

**Property-Based Testing Framework:**
```python
# tests/property_based/test_framework_properties.py
from hypothesis import given, strategies as st, settings, example
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant
import pytest

class SuperGeminiPropertyTests:
    """Property-based tests for SuperGemini Framework invariants"""
    
    @given(component_ids=st.lists(
        st.sampled_from(['core', 'mcp', 'agents', 'modes']),
        min_size=1,
        max_size=4,
        unique=True
    ))
    @settings(max_examples=50)
    def test_component_installation_idempotency(self, component_ids):
        """Property: Installing the same component multiple times should be idempotent"""
        from setup.core.component_manager import ComponentManager
        from setup.core.installation import InstallOptions
        from pathlib import Path
        import tempfile
        
        # Create temporary installation directory
        with tempfile.TemporaryDirectory() as temp_dir:
            install_dir = Path(temp_dir)
            manager = ComponentManager()
            options = InstallOptions(install_dir=install_dir, backup_existing=True)
            
            # Install components first time
            results1 = []
            for component_id in component_ids:
                result = manager.install_component(component_id, options)
                results1.append(result)
            
            # Get state after first installation
            state1 = self._get_installation_state(install_dir)
            
            # Install same components again
            results2 = []
            for component_id in component_ids:
                result = manager.install_component(component_id, options)
                results2.append(result)
            
            # Get state after second installation
            state2 = self._get_installation_state(install_dir)
            
            # Property: Second installation should be idempotent
            assert state1 == state2, "Repeated installation should be idempotent"
            
            # Property: All installations should succeed
            for result in results1 + results2:
                assert result.success, f"Installation should succeed: {result.error}"
    
    @given(agent_combinations=st.lists(
        st.sampled_from([
            'system-architect', 'security-engineer', 'backend-architect',
            'frontend-architect', 'performance-engineer'
        ]),
        min_size=1,
        max_size=3,
        unique=True
    ))
    def test_agent_coordination_consistency(self, agent_combinations):
        """Property: Agent coordination should be consistent regardless of activation order"""
        from setup.services.agent_manager import AgentManager
        from setup.services.task_context import TaskContext
        
        manager = AgentManager()
        
        # Create consistent task context
        context = TaskContext(
            description="Test task for property testing",
            complexity=0.5,
            domains=['testing'],
            requirements={}
        )
        
        # Test different activation orders
        import itertools
        for permutation in itertools.permutations(agent_combinations):
            result = manager.activate_agents(list(permutation), context)
            
            # Property: Activation should always succeed with valid agents
            assert result.success, f"Agent activation should succeed: {result.error}"
            
            # Property: Same agents should be activated regardless of order
            activated_agents = set(result.activated_agents)
            expected_agents = set(agent_combinations)
            assert activated_agents == expected_agents, "Same agents should be activated"

class MCPServerStateMachine(RuleBasedStateMachine):
    """Stateful property testing for MCP server lifecycle"""
    
    def __init__(self):
        super().__init__()
        self.server_states = {}
        self.connection_pool = {}
        
    @rule(server_name=st.sampled_from(['context7', 'sequential', 'magic', 'morphllm']))
    def connect_server(self, server_name):
        """Rule: Connect to an MCP server"""
        from setup.services.mcp_manager import MCPManager
        
        manager = MCPManager()
        
        try:
            connection = manager.connect_server(server_name)
            self.server_states[server_name] = 'connected'
            self.connection_pool[server_name] = connection
        except Exception as e:
            self.server_states[server_name] = 'error'
    
    @rule(server_name=st.sampled_from(['context7', 'sequential', 'magic', 'morphllm']))
    def disconnect_server(self, server_name):
        """Rule: Disconnect from an MCP server"""
        if server_name in self.connection_pool:
            connection = self.connection_pool[server_name]
            connection.disconnect()
            self.server_states[server_name] = 'disconnected'
            del self.connection_pool[server_name]
    
    @invariant()
    def connected_servers_have_connections(self):
        """Invariant: All servers marked as connected should have active connections"""
        for server_name, state in self.server_states.items():
            if state == 'connected':
                assert server_name in self.connection_pool, f"Connected server {server_name} should have connection object"

# Run property-based tests
class TestMCPServerProperties(MCPServerStateMachine.TestCase):
    """Property-based test runner for MCP server state machine"""
    pass
```

### Test Data Management and Fixtures

**Comprehensive Test Data Framework:**
```python
# tests/fixtures/test_data_manager.py
import json
import yaml
import pytest
from pathlib import Path
from typing import Dict, Any, List
from dataclasses import dataclass, asdict

@dataclass
class TestScenario:
    """Structured test scenario definition"""
    name: str
    description: str
    input_data: Dict[str, Any]
    expected_output: Dict[str, Any]
    test_configuration: Dict[str, Any]
    tags: List[str]

class TestDataManager:
    """Centralized test data management system"""
    
    def __init__(self, data_directory: Path = None):
        self.data_dir = data_directory or Path(__file__).parent / "data"
        self.data_dir.mkdir(exist_ok=True)
        self.scenarios_cache = {}
        
    def create_agent_test_scenario(self, agent_name: str, complexity: float = 0.5) -> TestScenario:
        """Create standardized test scenario for agent testing"""
        
        scenario = TestScenario(
            name=f"agent_{agent_name}_test",
            description=f"Standard test scenario for {agent_name} agent",
            input_data={
                "task_description": f"Test task for {agent_name}",
                "complexity": complexity,
                "domains": [agent_name.replace('-', '_')],
                "requirements": self._get_agent_requirements(agent_name)
            },
            expected_output={
                "success": True,
                "agent_activated": agent_name,
                "response_time": {"max": 5.0, "typical": 2.0},
                "quality_score": {"min": 0.8}
            },
            test_configuration={
                "timeout": 30,
                "retry_count": 3,
                "mock_external_services": True
            },
            tags=["agent_test", agent_name, f"complexity_{complexity}"]
        )
        
        return scenario
    
    def create_mcp_integration_scenario(self, server_name: str, operation: str) -> TestScenario:
        """Create test scenario for MCP server integration"""
        
        scenario = TestScenario(
            name=f"mcp_{server_name}_{operation}",
            description=f"Integration test for {server_name} MCP server {operation} operation",
            input_data={
                "server_name": server_name,
                "operation": operation,
                "parameters": self._get_operation_parameters(server_name, operation),
                "connection_config": {
                    "timeout": 30,
                    "max_retries": 3
                }
            },
            expected_output={
                "connection_success": True,
                "operation_success": True,
                "response_format": "valid",
                "performance": {
                    "response_time": {"max": 10.0},
                    "memory_usage": {"max": "100MB"}
                }
            },
            test_configuration={
                "mock_server": False,
                "health_check": True,
                "cleanup_after": True
            },
            tags=["mcp_test", server_name, operation]
        )
        
        return scenario
    
    def save_scenario(self, scenario: TestScenario):
        """Save test scenario to persistent storage"""
        
        scenario_file = self.data_dir / f"{scenario.name}.json"
        
        with open(scenario_file, 'w') as f:
            json.dump(asdict(scenario), f, indent=2)
        
        # Update cache
        self.scenarios_cache[scenario.name] = scenario
    
    def load_scenario(self, scenario_name: str) -> TestScenario:
        """Load test scenario from storage"""
        
        # Check cache first
        if scenario_name in self.scenarios_cache:
            return self.scenarios_cache[scenario_name]
        
        scenario_file = self.data_dir / f"{scenario_name}.json"
        
        if not scenario_file.exists():
            raise FileNotFoundError(f"Test scenario not found: {scenario_name}")
        
        with open(scenario_file, 'r') as f:
            scenario_data = json.load(f)
        
        scenario = TestScenario(**scenario_data)
        self.scenarios_cache[scenario_name] = scenario
        
        return scenario
    
    def get_scenarios_by_tag(self, tag: str) -> List[TestScenario]:
        """Get all scenarios with specific tag"""
        
        matching_scenarios = []
        
        # Load all scenario files
        for scenario_file in self.data_dir.glob("*.json"):
            try:
                scenario = self.load_scenario(scenario_file.stem)
                if tag in scenario.tags:
                    matching_scenarios.append(scenario)
            except Exception as e:
                print(f"Error loading scenario {scenario_file}: {e}")
        
        return matching_scenarios

# Pytest fixtures for test data management
@pytest.fixture
def test_data_manager():
    """Fixture providing test data manager"""
    return TestDataManager()

@pytest.fixture
def agent_test_scenarios(test_data_manager):
    """Fixture providing agent test scenarios"""
    agents = ['system-architect', 'security-engineer', 'backend-architect']
    scenarios = {}
    
    for agent in agents:
        scenarios[agent] = test_data_manager.create_agent_test_scenario(agent)
        test_data_manager.save_scenario(scenarios[agent])
    
    return scenarios

@pytest.fixture
def mcp_test_scenarios(test_data_manager):
    """Fixture providing MCP server test scenarios"""
    mcp_servers = [
        ('context7', 'documentation_lookup'),
        ('sequential', 'multi_step_analysis'),
        ('magic', 'ui_generation'),
        ('morphllm', 'code_transformation')
    ]
    
    scenarios = {}
    
    for server, operation in mcp_servers:
        scenario = test_data_manager.create_mcp_integration_scenario(server, operation)
        scenarios[f"{server}_{operation}"] = scenario
        test_data_manager.save_scenario(scenario)
    
    return scenarios

# Usage in tests
def test_agent_coordination_with_scenarios(agent_test_scenarios):
    """Test agent coordination using pre-defined scenarios"""
    
    for agent_name, scenario in agent_test_scenarios.items():
        print(f"Testing agent: {agent_name}")
        
        # Use scenario data for test execution
        input_data = scenario.input_data
        expected_output = scenario.expected_output
        
        # Execute test using scenario parameters
        from setup.services.agent_manager import AgentManager
        
        manager = AgentManager()
        result = manager.activate_agents([agent_name], input_data)
        
        # Validate against expected output
        assert result.success == expected_output['success']
        assert result.response_time <= expected_output['response_time']['max']

def test_mcp_integration_with_scenarios(mcp_test_scenarios):
    """Test MCP server integration using pre-defined scenarios"""
    
    for scenario_name, scenario in mcp_test_scenarios.items():
        print(f"Testing MCP scenario: {scenario_name}")
        
        input_data = scenario.input_data
        expected_output = scenario.expected_output
        
        # Execute MCP test using scenario
        from setup.services.mcp_manager import MCPManager
        
        manager = MCPManager()
        connection = manager.connect_server(input_data['server_name'])
        
        assert connection.is_connected() == expected_output['connection_success']
        
        # Test operation
        response = connection.execute_operation(input_data['operation'], input_data['parameters'])
        assert response.success == expected_output['operation_success']
```

## Performance Testing

### Performance Testing Methodologies

**Memory Performance Testing:**
```python
class MemoryPerformanceTest:
    def test_memory_usage_limits(self):
        """Test memory usage stays within limits"""
        import psutil
        import gc
        
        # Baseline memory
        gc.collect()
        baseline = psutil.Process().memory_info().rss
        
        # Load large session
        session_manager = SessionManager()
        large_session = session_manager.create_large_test_session()
        
        # Measure memory increase
        current = psutil.Process().memory_info().rss
        memory_increase = current - baseline
        
        # Assert reasonable memory usage (< 500MB increase)
        assert memory_increase < 500 * 1024 * 1024
        
    def test_session_loading_speed(self):
        """Test session loading performance"""
        import time
        
        session_manager = SessionManager()
        
        # Create test session with known size
        test_session = session_manager.create_test_session(size='large')
        
        # Measure loading time
        start_time = time.time()
        loaded_session = session_manager.load_session(test_session.id)
        load_time = time.time() - start_time
        
        # Assert reasonable load time (< 5 seconds)
        assert load_time < 5.0
        assert loaded_session.is_valid()
```

**Component Performance Benchmarks:**
```python
class ComponentPerformanceBenchmark:
    def benchmark_component_installation(self):
        """Benchmark component installation speed"""
        import timeit
        
        def install_core():
            installer = InstallationOrchestrator()
            temp_dir = Path(tempfile.mkdtemp())
            installer.install_components(['core'], InstallOptions(install_dir=temp_dir))
            shutil.rmtree(temp_dir)
        
        # Run benchmark
        execution_time = timeit.timeit(install_core, number=10)
        avg_time = execution_time / 10
        
        # Assert reasonable installation time (< 2 seconds average)
        assert avg_time < 2.0
        
    def benchmark_agent_selection(self):
        """Benchmark agent selection performance"""
        agent_system = AgentSystem()
        
        # Create complex task context
        complex_context = TaskContext(
            input_text="complex microservices security performance analysis",
            file_count=100,
            complexity_score=0.9
        )
        
        # Measure selection time
        start_time = time.time()
        selected_agents = agent_system.select_agents(complex_context)
        selection_time = time.time() - start_time
        
        # Assert fast selection (< 100ms)
        assert selection_time < 0.1
        assert len(selected_agents) > 0
```

**Load Testing:**
```python
class LoadTest:
    def test_concurrent_installations(self):
        """Test concurrent component installations"""
        import threading
        import concurrent.futures
        
        def install_component(component_name):
            installer = InstallationOrchestrator()
            temp_dir = Path(tempfile.mkdtemp())
            try:
                result = installer.install_components([component_name], 
                                                    InstallOptions(install_dir=temp_dir))
                return result.success
            finally:
                shutil.rmtree(temp_dir)
        
        # Test concurrent installations
        components = ['core', 'agents', 'modes', 'mcp']
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(install_component, comp) for comp in components]
            results = [future.result() for future in futures]
        
        # All installations should succeed
        assert all(results)
```

## Integration Testing

### Component Integration Testing

**Multi-Component Workflow Testing:**
```python
class TestComponentIntegration:
    def test_full_workflow_integration(self):
        """Test complete workflow with multiple components"""
        # Install all components
        installer = InstallationOrchestrator()
        components = ['core', 'agents', 'modes', 'mcp']
        
        result = installer.install_components(components, self.test_config)
        assert result.success
        
        # Test agent-mode integration
        agent_system = AgentSystem()
        mode_system = ModeSystem()
        
        # Complex task requiring multiple agents and modes
        task_context = TaskContext(
            input_text="analyze security vulnerabilities in microservices architecture",
            complexity_score=0.8,
            file_count=50
        )
        
        # Should activate security-engineer + system-architect + introspection mode
        selected_agents = agent_system.select_agents(task_context)
        selected_modes = mode_system.select_modes(task_context)
        
        assert 'security-engineer' in selected_agents
        assert 'system-architect' in selected_agents
        assert 'introspection' in selected_modes
        
    def test_mcp_agent_coordination(self):
        """Test MCP server and agent coordination"""
        # Setup MCP servers
        mcp_manager = MCPManager()
        mcp_manager.connect_server('context7')
        mcp_manager.connect_server('sequential')
        
        # Setup agents
        agent_system = AgentSystem()
        
        # Task requiring both MCP and agents
        task_context = TaskContext(
            input_text="implement React authentication with best practices",
            domain='frontend'
        )
        
        # Should coordinate frontend-architect + security-engineer + context7 + magic
        coordination_plan = agent_system.create_coordination_plan(task_context)
        
        assert 'frontend-architect' in coordination_plan.agents
        assert 'security-engineer' in coordination_plan.agents
        assert 'context7' in coordination_plan.mcp_servers
        assert 'magic' in coordination_plan.mcp_servers
```

**End-to-End Workflow Testing:**
```python
class TestEndToEndWorkflows:
    def test_complete_development_workflow(self):
        """Test complete development workflow simulation"""
        # 1. Project initialization
        session_manager = SessionManager()
        session = session_manager.create_session('test-project')
        
        # 2. Requirements discovery (brainstorming mode)
        brainstorm_task = TaskContext(
            input_text="build e-commerce platform",
            session_id=session.id
        )
        
        result = self._execute_task(brainstorm_task)
        assert result.mode == 'brainstorming'
        assert result.agents == ['system-architect', 'requirements-analyst']
        
        # 3. Implementation planning (task management mode)
        planning_task = TaskContext(
            input_text="implement user authentication system", 
            session_id=session.id,
            complexity_score=0.7
        )
        
        result = self._execute_task(planning_task)
        assert result.mode == 'task-management'
        assert 'security-engineer' in result.agents
        
        # 4. Code implementation (orchestration mode)
        implementation_task = TaskContext(
            input_text="create React login components with JWT",
            session_id=session.id,
            file_count=15
        )
        
        result = self._execute_task(implementation_task)
        assert result.mode == 'orchestration'
        assert 'context7' in result.mcp_servers
        assert 'magic' in result.mcp_servers
        
        # 5. Session persistence
        session_manager.save_session(session.id)
        
        # 6. Session restoration
        restored_session = session_manager.load_session(session.id)
        assert restored_session.context_size > 0
        assert restored_session.has_memory('authentication-implementation')
```

**Cross-Platform Integration Testing:**
```python
class TestCrossPlatformIntegration:
    @pytest.mark.parametrize("platform", ["linux", "macos", "windows"])
    def test_installation_cross_platform(self, platform):
        """Test installation across different platforms"""
        if platform == "windows":
            expected_executable = "SuperGemini.exe"
            path_separator = "\"
        else:
            expected_executable = "SuperGemini"
            path_separator = "/"
        
        # Platform-specific installation
        installer = InstallationOrchestrator()
        config = PlatformConfig(platform=platform)
        
        result = installer.install_components(['core'], config)
        assert result.success
        
        # Verify platform-specific behavior
        install_path = config.install_dir
        assert install_path.exists()
        
        # Test executable permissions (Unix-like systems)
        if platform != "windows":
            executable_path = install_path / "bin" / expected_executable
            assert executable_path.exists()
            assert os.access(executable_path, os.X_OK)
```

## Debugging Tools & Utilities

### Built-in Debugging Tools

**SuperGemini Debug Command:**
```bash
# Comprehensive system diagnostics
SuperGemini debug --comprehensive

# Component-specific debugging
SuperGemini debug --components agents,mcp

# Performance debugging
SuperGemini debug --performance --memory

# Session debugging
SuperGemini debug --sessions --verbose

# MCP server debugging
SuperGemini debug --mcp-servers --trace
```

**Debug Environment Variables:**
```bash
# Enable debug logging
export SUPERCLAUDE_DEBUG=true
export SUPERCLAUDE_LOG_LEVEL=debug

# Component-specific debugging
export SUPERCLAUDE_DEBUG_AGENTS=true
export SUPERCLAUDE_DEBUG_MODES=true
export SUPERCLAUDE_DEBUG_MCP=true
export SUPERCLAUDE_DEBUG_SESSIONS=true

# Performance debugging
export SUPERCLAUDE_DEBUG_PERFORMANCE=true
export SUPERCLAUDE_DEBUG_MEMORY=true

# MCP communication tracing
export SUPERCLAUDE_TRACE_MCP=true
```

**Development Debugging Utilities:**
```python
# setup/utils/debug.py
class DebugUtils:
    @staticmethod
    def enable_comprehensive_debugging():
        """Enable all debugging features"""
        logging.basicConfig(level=logging.DEBUG)
        os.environ.update({
            'SUPERCLAUDE_DEBUG': 'true',
            'SUPERCLAUDE_DEBUG_AGENTS': 'true',
            'SUPERCLAUDE_DEBUG_MODES': 'true',
            'SUPERCLAUDE_DEBUG_MCP': 'true'
        })
        
    @staticmethod
    def create_debug_session():
        """Create session with debug instrumentation"""
        session = DebugSession()
        session.enable_tracing()
        session.enable_memory_monitoring()
        return session
        
    @staticmethod
    def dump_system_state():
        """Dump complete system state for analysis"""
        state = {
            'components': ComponentRegistry().get_status(),
            'agents': AgentSystem().get_status(),
            'mcp_servers': MCPManager().get_status(),
            'sessions': SessionManager().get_status(),
            'memory': MemoryManager().get_usage()
        }
        
        with open('debug-system-state.json', 'w') as f:
            json.dump(state, f, indent=2)
            
        return state

# Usage in development
if __name__ == "__main__":
    DebugUtils.enable_comprehensive_debugging()
    state = DebugUtils.dump_system_state()
    print(f"System state dumped: {len(state)} components")
```

**Custom Debugging Tools:**
```python
class ComponentDebugger:
    """Advanced component debugging and analysis"""
    
    def __init__(self):
        self.trace_buffer = []
        self.performance_metrics = {}
        
    def trace_component_lifecycle(self, component):
        """Trace complete component lifecycle"""
        tracer = ComponentTracer(component)
        
        # Hook into lifecycle events
        tracer.on_install = self._trace_install
        tracer.on_activate = self._trace_activate
        tracer.on_execute = self._trace_execute
        tracer.on_deactivate = self._trace_deactivate
        
        return tracer
        
    def analyze_performance_bottlenecks(self):
        """Analyze performance bottlenecks in traces"""
        bottlenecks = []
        
        for trace in self.trace_buffer:
            if trace.duration > 1.0:  # > 1 second
                bottlenecks.append({
                    'component': trace.component,
                    'operation': trace.operation,
                    'duration': trace.duration,
                    'stack_trace': trace.stack_trace
                })
                
        return bottlenecks
        
    def generate_debug_report(self):
        """Generate comprehensive debug report"""
        report = {
            'execution_traces': self.trace_buffer,
            'performance_metrics': self.performance_metrics,
            'bottlenecks': self.analyze_performance_bottlenecks(),
            'memory_usage': self._get_memory_analysis(),
            'recommendations': self._generate_recommendations()
        }
        
        return report

# Usage
debugger = ComponentDebugger()
tracer = debugger.trace_component_lifecycle(agent_component)

# Execute component operations
agent_component.install(test_dir)

# Generate debug report
report = debugger.generate_debug_report()
```

**Log Analysis Tools:**
```python
class LogAnalyzer:
    """Analyze SuperGemini logs for issues and patterns"""
    
    def analyze_installation_logs(self, log_file):
        """Analyze installation logs for failures"""
        issues = []
        
        with open(log_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                # Check for error patterns
                if 'ERROR' in line:
                    issues.append({
                        'line': line_num,
                        'type': 'error',
                        'message': line.strip()
                    })
                elif 'TIMEOUT' in line:
                    issues.append({
                        'line': line_num,
                        'type': 'timeout',
                        'message': line.strip()
                    })
                elif 'FAILED' in line:
                    issues.append({
                        'line': line_num,
                        'type': 'failure',
                        'message': line.strip()
                    })
                    
        return issues
        
    def extract_performance_metrics(self, log_file):
        """Extract performance metrics from logs"""
        metrics = {
            'component_install_times': {},
            'agent_activation_times': {},
            'mcp_response_times': {}
        }
        
        # Parse log patterns for timing information
        # Implementation details...
        
        return metrics

# Usage
analyzer = LogAnalyzer()
issues = analyzer.analyze_installation_logs('~/.gemini/logs/installation.log')
metrics = analyzer.extract_performance_metrics('~/.gemini/logs/performance.log')
```

## Common Development Issues

### Installation & Configuration Issues

**Component Installation Failures:**
```bash
# Issue: Component dependencies not resolved
ERROR: Component 'mcp' requires 'core' but it's not installed

# Solution: Install in dependency order
SuperGemini install --components core mcp --resolve-dependencies

# Issue: Permission denied during installation
ERROR: Permission denied: '/home/user/.gemini/GEMINI.md'

# Solution: Fix permissions
sudo chown -R $USER ~/.gemini
chmod 755 ~/.gemini
```

**MCP Server Connection Issues:**
```bash
# Issue: Context7 server fails to start
ERROR: MCP server 'context7' failed to connect

# Debug: Check Node.js and server path
node --version  # Should be 16+
which context7  # Verify installation path

# Solution: Reinstall MCP servers
SuperGemini install --components mcp --force
npm install -g @context7/mcp-server
```

**Configuration Conflicts:**
```python
# Issue: GEMINI.md import conflicts
ERROR: Circular import detected: GEMINI.md -> FLAGS.md -> GEMINI.md

# Debug: Check import structure
def debug_import_structure():
    with open('~/.gemini/GEMINI.md', 'r') as f:
        content = f.read()
        imports = re.findall(r'@(\w+\.md)', content)
        print(f"Imports detected: {imports}")
        
    # Check for circular references
    for import_file in imports:
        import_path = Path('~/.gemini') / import_file
        if import_path.exists():
            with open(import_path, 'r') as f:
                nested_imports = re.findall(r'@(\w+\.md)', f.read())
                if 'GEMINI.md' in nested_imports:
                    print(f"Warning: Circular import: {import_file} -> GEMINI.md")

# Solution: Remove circular imports
# Edit problematic files to remove @GEMINI.md references
```

### Component Development Issues

**Agent System Issues:**
```python
# Issue: Agent not activating for expected keywords
class AgentActivationDebugger:
    def debug_activation_failure(self, input_text, expected_agent):
        print(f"Debugging agent activation failure:")
        print(f"  Input: '{input_text}'")
        print(f"  Expected: {expected_agent}")
        
        # Check trigger patterns
        agent_config = self._get_agent_config(expected_agent)
        triggers = agent_config.get('triggers', [])
        print(f"  Agent triggers: {triggers}")
        
        # Check keyword matching
        matches = []
        for trigger in triggers:
            if trigger.lower() in input_text.lower():
                matches.append(trigger)
        print(f"  Matched triggers: {matches}")
        
        if not matches:
            print("  No triggers matched - consider adding new keywords")
            # Suggest new triggers
            suggestions = self._suggest_triggers(input_text)
            print(f"  Suggested triggers: {suggestions}")
        
        return matches

# Usage
debugger = AgentActivationDebugger()
debugger.debug_activation_failure("implement secure login", "security-engineer")
```

**Mode Selection Issues:**
```python
# Issue: Wrong behavioral mode activated
class ModeSelectionDebugger:
    def debug_mode_selection(self, task_context):
        print("Mode selection debug:")
        
        # Analyze complexity score
        complexity = self._calculate_complexity(task_context)
        print(f"  Complexity score: {complexity}")
        
        # Check mode thresholds
        mode_thresholds = {
            'brainstorming': 0.2,
            'task_management': 0.6,
            'orchestration': 0.8,
            'introspection': 0.5  # Special conditions
        }
        
        for mode, threshold in mode_thresholds.items():
            if complexity >= threshold:
                print(f"  {mode}: {complexity} >= {threshold}")
            else:
                print(f"  {mode}: {complexity} < {threshold}")
        
        # Check special conditions
        special_triggers = self._check_special_triggers(task_context)
        print(f"  Special triggers: {special_triggers}")
        
        return self._select_final_mode(complexity, special_triggers)

# Usage
context = TaskContext(
    input_text="fix authentication bug",
    file_count=5,
    error_present=True
)
debugger = ModeSelectionDebugger()
selected_mode = debugger.debug_mode_selection(context)
```

### Issue Escalation & Resolution Process

**Development Issue Classification:**
```python
class IssueClassifier:
    SEVERITY_LEVELS = {
        'critical': {
            'description': 'System unusable, data loss risk',
            'examples': ['Installation completely fails', 'Session data corruption'],
            'response_time': '2 hours',
            'escalation': 'immediate'
        },
        'high': {
            'description': 'Major functionality broken',
            'examples': ['MCP servers not connecting', 'Agent system not activating'],
            'response_time': '24 hours',
            'escalation': 'next business day'
        },
        'medium': {
            'description': 'Feature partially working',
            'examples': ['Some agents not activating', 'Performance degradation'],
            'response_time': '1 week',
            'escalation': 'weekly review'
        },
        'low': {
            'description': 'Minor issues or enhancements',
            'examples': ['Documentation improvements', 'Edge case handling'],
            'response_time': '1 month',
            'escalation': 'monthly review'
        }
    }
    
    def classify_issue(self, issue_description):
        """Classify issue severity based on description"""
        description_lower = issue_description.lower()
        
        # Critical indicators
        critical_keywords = ['data loss', 'corruption', 'completely broken', 'system unusable']
        if any(keyword in description_lower for keyword in critical_keywords):
            return 'critical'
            
        # High severity indicators
        high_keywords = ['not working', 'major failure', 'broken functionality']
        if any(keyword in description_lower for keyword in high_keywords):
            return 'high'
            
        # Medium severity indicators
        medium_keywords = ['performance', 'slow', 'partially working']
        if any(keyword in description_lower for keyword in medium_keywords):
            return 'medium'
            
        return 'low'

# Usage
classifier = IssueClassifier()
severity = classifier.classify_issue("MCP servers not connecting after installation")
print(f"Issue severity: {severity}")
print(f"Response expectation: {classifier.SEVERITY_LEVELS[severity]['response_time']}")
```

**Development Support Workflow:**
```bash
# Step 1: Self-diagnosis
SuperGemini debug --comprehensive > debug-report.txt

# Step 2: Check common issues
python -c "
from setup.utils.troubleshooter import AutoTroubleshooter
troubleshooter = AutoTroubleshooter()
solutions = troubleshooter.suggest_solutions('mcp server connection failed')
for solution in solutions:
    print(f'Solution: {solution}')
"

# Step 3: Community support
# Search existing issues: https://github.com/SuperGemini-Org/SuperGemini_Framework/issues
# Join discussions: https://github.com/SuperGemini-Org/SuperGemini_Framework/discussions

# Step 4: Create detailed issue report
# Include:
# - SuperGemini version: SuperGemini --version
# - System info: uname -a
# - Python version: python --version  
# - Debug report: debug-report.txt
# - Steps to reproduce
# - Expected vs actual behavior
```

## Performance Testing & Optimization

> **⚡ Performance Context**: Performance optimization strategies are detailed in [Technical Architecture Guide](technical-architecture.md#performance-system).

### Performance Benchmarking

**Memory Performance Testing:**
```python
import psutil
import memory_profiler
from pytest import benchmark

class TestPerformance:
    """Performance testing suite for SuperGemini components"""
    
    @memory_profiler.profile
    def test_memory_usage_component_installation(self):
        """Profile memory usage during component installation"""
        initial_memory = psutil.Process().memory_info().rss
        
        # Install large component set
        installer = InstallationOrchestrator()
        installer.install_components(['core', 'agents', 'modes', 'mcp'])
        
        final_memory = psutil.Process().memory_info().rss
        memory_increase = final_memory - initial_memory
        
        # Assert memory usage is within acceptable limits
        assert memory_increase < 100 * 1024 * 1024, f"Memory usage too high: {memory_increase} bytes"
    
    def test_agent_activation_speed(self, benchmark):
        """Benchmark agent activation performance"""
        agent_manager = AgentManager()
        task_context = TaskContext(
            input_text="implement secure authentication system",
            complexity_score=0.8
        )
        
        # Benchmark agent selection and activation
        result = benchmark(agent_manager.activate_agents, task_context)
        
        # Performance targets
        assert benchmark.stats['mean'] < 0.5, "Agent activation too slow"
        assert len(result) > 0, "No agents activated"
```

**Load Testing:**
```python
def test_concurrent_installations():
    """Test system under concurrent installation load"""
    import concurrent.futures
    import threading
    
    def install_component(component_id):
        installer = InstallationOrchestrator()
        return installer.install_component(component_id)
    
    # Test concurrent installations
    components = ['agent1', 'agent2', 'mode1', 'mode2']
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(install_component, comp) for comp in components]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    
    # Verify all installations succeeded
    assert all(result.success for result in results)
```

## Security Testing

> **🔒 Security Integration**: Security testing is integrated with development workflows outlined in [Contributing Code Guide](contributing-code.md#security-guidelines).

### Security Testing Framework

**Security Test Categories:**
```python
class SecurityTestSuite:
    """Comprehensive security testing for SuperGemini components"""
    
    def test_input_validation(self):
        """Test input sanitization and validation"""
        malicious_inputs = [
            "../../../etc/passwd",  # Path traversal
            "<script>alert('xss')</script>",  # XSS
            "'; DROP TABLE users; --",  # SQL injection
            "$(rm -rf /)",  # Command injection
        ]
        
        for malicious_input in malicious_inputs:
            with pytest.raises(ValidationError):
                self.component.process_input(malicious_input)
    
    def test_file_path_validation(self):
        """Test safe file path handling"""
        from setup.core.security import PathValidator
        
        validator = PathValidator(base_dir="/safe/base/dir")
        
        # Test safe paths
        assert validator.is_safe("subdir/file.txt")
        assert validator.is_safe("./relative/path.py")
        
        # Test dangerous paths
        assert not validator.is_safe("../../../etc/passwd")
        assert not validator.is_safe("/absolute/path/outside")
```

### Vulnerability Testing

**Security Validation Tools:**
```bash
# Install security testing tools
pip install bandit safety pip-audit

# Run security scans
python -m bandit -r setup/ SuperGemini/
python -m safety check
python -m pip-audit

# Test for hardcoded secrets
grep -r "password\|api_key\|secret" --exclude-dir=tests setup/
```

## Integration Testing

> **🔗 Integration Context**: Integration patterns are detailed in [Technical Architecture Guide](technical-architecture.md#integration-patterns).

### End-to-End Integration Testing

**Full System Integration Tests:**
```python
class TestSystemIntegration:
    """End-to-end system integration testing"""
    
    def test_complete_development_workflow(self):
        """Test complete development workflow end-to-end"""
        # 1. Initialize system
        system = SuperGeminiFramework()
        system.initialize()
        
        # 2. Install components
        installer = system.get_installer()
        result = installer.install(['core', 'agents', 'mcp'])
        assert result.success
        
        # 3. Activate agents for task
        task_context = TaskContext(
            input_text="build secure web application with React",
            file_count=15,
            complexity_score=0.9
        )
        
        agents = system.activate_agents(task_context)
        assert 'security-engineer' in [a.name for a in agents]
        assert 'frontend-architect' in [a.name for a in agents]
        
        # 4. Coordinate agent collaboration
        coordinator = system.get_coordinator()
        plan = coordinator.create_collaboration_plan(agents, task_context)
        assert plan.coordination_pattern in ['hierarchical', 'collaborative']
        
        # 5. Execute with MCP integration
        mcp_manager = system.get_mcp_manager()
        mcp_servers = mcp_manager.activate_servers(['context7', 'magic', 'sequential'])
        assert all(server.is_connected() for server in mcp_servers)
        
        # 6. Validate final output
        execution_result = system.execute_task(task_context, agents, mcp_servers)
        assert execution_result.success
        assert execution_result.quality_score >= 0.8
```

## Quality Validation

> **📊 Metrics Integration**: Quality metrics are integrated with development processes in [Contributing Code Guide](contributing-code.md#code-review).

### Quality Validation Framework

**Multi-Dimensional Quality Assessment:**
```python
class QualityValidator:
    """Comprehensive quality validation system"""
    
    def __init__(self):
        self.quality_gates = [
            CodeQualityGate(),
            SecurityQualityGate(),
            PerformanceQualityGate(),
            DocumentationQualityGate()
        ]
    
    def validate_component(self, component):
        """Run complete quality validation"""
        results = {}
        overall_score = 0.0
        
        for gate in self.quality_gates:
            result = gate.validate(component)
            results[gate.name] = result
            overall_score += result.score * gate.weight
        
        return QualityReport(
            overall_score=overall_score,
            gate_results=results,
            passed=overall_score >= 0.8
        )
```

### Automated Quality Checks

**Quality Pipeline:**
```bash
# Quality validation pipeline
python -m pytest tests/ --cov=setup --cov-fail-under=90
python -m pylint setup/ --fail-under=8.0
python -m mypy setup/ --strict
python -m black --check setup/
python -m isort --check-only setup/

# Performance benchmarks
python -m pytest tests/performance/ --benchmark-only
python -m memory_profiler tests/test_memory_usage.py

# Security validation
python -m bandit -r setup/ --severity-level medium
python -m safety check --json
```

## Troubleshooting Guide

> **🔧 Development Support**: For development-specific troubleshooting, see [Contributing Code Guide](contributing-code.md#error-handling-and-troubleshooting).

### Common Testing Issues

**Test Environment Issues:**
```bash
# Issue: Tests failing with import errors
# Solution: Ensure proper PYTHONPATH and virtual environment
export PYTHONPATH=$PWD:$PYTHONPATH
source venv/bin/activate
python -m pytest tests/ -v

# Issue: Mock objects not working correctly
# Solution: Use proper mock configuration
python -c "
from unittest.mock import Mock, patch
with patch('setup.core.registry.ComponentRegistry') as mock_registry:
    mock_registry.return_value.list_installed.return_value = ['core']
    # Run test code here
"

# Issue: Test data cleanup failing
# Solution: Ensure proper teardown methods
python -c "
import tempfile
import shutil
from pathlib import Path

test_dir = Path(tempfile.mkdtemp())
try:
    # Test code here
    pass
finally:
    if test_dir.exists():
        shutil.rmtree(test_dir)
"
```

## Quality Assurance

### Quality Assurance Processes

**Pre-Development Quality Gates:**
```python
class PreDevelopmentQA:
    def validate_requirements(self, requirements):
        """Validate requirements before development starts"""
        validations = {
            'completeness': self._check_completeness(requirements),
            'testability': self._check_testability(requirements),
            'consistency': self._check_consistency(requirements),
            'feasibility': self._check_feasibility(requirements)
        }
        
        return all(validations.values()), validations
        
    def _check_completeness(self, requirements):
        """Check if requirements are complete"""
        required_sections = ['purpose', 'acceptance_criteria', 'dependencies']
        return all(section in requirements for section in required_sections)
        
    def _check_testability(self, requirements):
        """Check if requirements are testable"""
        # Requirements should have measurable outcomes
        return 'acceptance_criteria' in requirements and len(requirements['acceptance_criteria']) > 0

# Usage
qa = PreDevelopmentQA()
requirements = {
    'purpose': 'Add new security agent',
    'acceptance_criteria': ['Agent activates on security keywords', 'Integrates with MCP servers'],
    'dependencies': ['core', 'agents']
}
is_valid, details = qa.validate_requirements(requirements)
```

**Development Quality Gates:**
```python
class DevelopmentQA:
    def validate_component(self, component_path):
        """Comprehensive component validation"""
        validations = {
            'code_quality': self._check_code_quality(component_path),
            'test_coverage': self._check_test_coverage(component_path),
            'documentation': self._check_documentation(component_path),
            'integration': self._check_integration(component_path),
            'performance': self._check_performance(component_path)
        }
        
        score = sum(validations.values()) / len(validations)
        return score >= 0.8, validations, score
        
    def _check_code_quality(self, component_path):
        """Check code quality metrics"""
        # Run linting and complexity analysis
        lint_score = self._run_linter(component_path)
        complexity_score = self._check_complexity(component_path)
        
        return (lint_score + complexity_score) / 2
        
    def _check_test_coverage(self, component_path):
        """Check test coverage percentage"""
        coverage_report = self._run_coverage_analysis(component_path)
        return coverage_report.percentage / 100
        
    def _check_documentation(self, component_path):
        """Check documentation completeness"""
        # Verify docstrings, README, examples
        has_docstrings = self._check_docstrings(component_path)
        has_readme = self._check_readme(component_path)
        has_examples = self._check_examples(component_path)
        
        return (has_docstrings + has_readme + has_examples) / 3

# Usage
qa = DevelopmentQA()
passes_qa, details, score = qa.validate_component('setup/components/new_agent.py')
print(f"QA Score: {score:.2f}")
```

**Integration Quality Gates:**
```python
class IntegrationQA:
    def validate_integration(self, component_name):
        """Validate component integration with framework"""
        integration_tests = {
            'installation': self._test_installation(component_name),
            'activation': self._test_activation(component_name),
            'coordination': self._test_coordination(component_name),
            'compatibility': self._test_compatibility(component_name),
            'rollback': self._test_rollback(component_name)
        }
        
        passing_tests = sum(integration_tests.values())
        total_tests = len(integration_tests)
        
        return passing_tests == total_tests, integration_tests
        
    def _test_installation(self, component_name):
        """Test component installs correctly"""
        try:
            installer = TestInstaller()
            result = installer.install_component(component_name, dry_run=True)
            return result.success
        except Exception:
            return False
            
    def _test_activation(self, component_name):
        """Test component activates correctly"""
        try:
            registry = ComponentRegistry()
            component = registry.get_component(component_name)
            return component.can_activate()
        except Exception:
            return False

# Usage
qa = IntegrationQA()
passes_integration, test_results = qa.validate_integration('security_agent')
```

### Code Review Criteria

**Automated Code Review Checklist:**
```python
class CodeReviewBot:
    def __init__(self):
        self.review_criteria = {
            'style': {
                'weight': 0.2,
                'checks': ['pep8_compliance', 'naming_conventions', 'imports_organized']
            },
            'functionality': {
                'weight': 0.3,
                'checks': ['methods_work', 'error_handling', 'edge_cases']
            },
            'testing': {
                'weight': 0.25,
                'checks': ['unit_tests', 'integration_tests', 'coverage_80_plus']
            },
            'documentation': {
                'weight': 0.15,
                'checks': ['docstrings', 'type_hints', 'examples']
            },
            'integration': {
                'weight': 0.1,
                'checks': ['framework_compatibility', 'backwards_compatible']
            }
        }
        
    def review_pull_request(self, pr_path):
        """Automated pull request review"""
        results = {}
        total_score = 0
        
        for category, config in self.review_criteria.items():
            category_score = 0
            category_results = {}
            
            for check in config['checks']:
                check_result = self._run_check(check, pr_path)
                category_results[check] = check_result
                category_score += check_result
                
            category_score = category_score / len(config['checks'])
            results[category] = {
                'score': category_score,
                'details': category_results
            }
            
            total_score += category_score * config['weight']
            
        return total_score, results
        
    def _run_check(self, check_name, pr_path):
        """Run individual code review check"""
        check_methods = {
            'pep8_compliance': self._check_pep8,
            'naming_conventions': self._check_naming,
            'unit_tests': self._check_unit_tests,
            'coverage_80_plus': self._check_coverage,
            'docstrings': self._check_docstrings,
            'framework_compatibility': self._check_framework_compat
        }
        
        check_method = check_methods.get(check_name, lambda x: 0.5)
        return check_method(pr_path)

# Usage
reviewer = CodeReviewBot()
score, details = reviewer.review_pull_request('pull_requests/add-data-scientist-agent')
print(f"Review Score: {score:.2f}")

if score >= 0.8:
    print("✅ Pull request meets quality standards")
else:
    print("❌ Pull request needs improvement")
    for category, result in details.items():
        if result['score'] < 0.7:
            print(f"  Improve {category}: {result['score']:.2f}")
```

**Human Code Review Guidelines:**
```python
class HumanReviewGuidelines:
    REVIEW_CHECKLIST = {
        'architecture': [
            'Does the component follow SuperGemini patterns?',
            'Is the component properly integrated with the registry?',
            'Are dependencies clearly defined and minimal?',
            'Does it follow the single responsibility principle?'
        ],
        'security': [
            'Are user inputs validated and sanitized?',
            'Is sensitive information properly handled?',
            'Are file operations secure (no path traversal)?',
            'Are external commands properly escaped?'
        ],
        'performance': [
            'Are there any obvious performance bottlenecks?',
            'Is memory usage reasonable?',
            'Are there unnecessary loops or operations?',
            'Is caching used appropriately?'
        ],
        'maintainability': [
            'Is the code readable and well-organized?',
            'Are complex operations properly documented?',
            'Are magic numbers and strings avoided?',
            'Is error handling comprehensive?'
        ],
        'testing': [
            'Are all public methods tested?',
            'Are edge cases covered?',
            'Are integration points tested?',
            'Is test data realistic and comprehensive?'
        ]
    }
    
    def generate_review_template(self, component_type):
        """Generate review template based on component type"""
        base_template = "## Code Review Checklist

"
        
        for category, questions in self.REVIEW_CHECKLIST.items():
            base_template += f"### {category.title()}
"
            for question in questions:
                base_template += f"- [ ] {question}
"
            base_template += "
"
            
        # Add component-specific considerations
        if component_type == 'agent':
            base_template += "### Agent-Specific
"
            base_template += "- [ ] Trigger patterns are comprehensive
"
            base_template += "- [ ] Agent coordination is properly implemented
"
            base_template += "- [ ] MCP server integration works correctly

"
            
        elif component_type == 'mode':
            base_template += "### Mode-Specific
"
            base_template += "- [ ] Activation conditions are clear and correct
"
            base_template += "- [ ] Mode behavior is well-defined
"
            base_template += "- [ ] Interaction with other modes is handled

"
            
        base_template += "## Overall Assessment
"
        base_template += "- [ ] Ready to merge
"
        base_template += "- [ ] Needs minor changes
"
        base_template += "- [ ] Needs major changes
"
        base_template += "- [ ] Needs redesign
"
        
        return base_template

# Usage
guidelines = HumanReviewGuidelines()
review_template = guidelines.generate_review_template('agent')
print(review_template)
```

### Quality Standards & Metrics

**Quality Metrics Dashboard:**
```python
class QualityMetrics:
    def __init__(self):
        self.metrics = {
            'code_coverage': {'target': 90, 'current': 0},
            'complexity_score': {'target': 7, 'current': 0},  # Cyclomatic complexity
            'documentation_coverage': {'target': 95, 'current': 0},
            'integration_test_pass': {'target': 100, 'current': 0},
            'performance_benchmark': {'target': 100, 'current': 0}  # % of baseline
        }
        
    def collect_metrics(self, component_path):
        """Collect all quality metrics for a component"""
        self.metrics['code_coverage']['current'] = self._measure_coverage(component_path)
        self.metrics['complexity_score']['current'] = self._measure_complexity(component_path)
        self.metrics['documentation_coverage']['current'] = self._measure_docs(component_path)
        self.metrics['integration_test_pass']['current'] = self._measure_integration(component_path)
        self.metrics['performance_benchmark']['current'] = self._measure_performance(component_path)
        
        return self.metrics
        
    def generate_quality_report(self):
        """Generate comprehensive quality report"""
        report = "# Quality Metrics Report

"
        
        overall_score = 0
        total_weight = 0
        
        for metric_name, metric_data in self.metrics.items():
            target = metric_data['target']
            current = metric_data['current']
            
            # Calculate score (0-100)
            if metric_name == 'complexity_score':
                # Lower is better for complexity
                score = max(0, 100 - (current - target) * 10) if current > target else 100
            else:
                # Higher is better for other metrics
                score = min(100, (current / target) * 100)
                
            status = "✅" if score >= 80 else "⚠️" if score >= 60 else "❌"
            
            report += f"## {metric_name.replace('_', ' ').title()}
"
            report += f"{status} **Score: {score:.1f}/100**
"
            report += f"- Target: {target}
"
            report += f"- Current: {current}

"
            
            overall_score += score
            total_weight += 1
            
        overall_score = overall_score / total_weight
        overall_status = "✅" if overall_score >= 80 else "⚠️" if overall_score >= 60 else "❌"
        
        report += f"## Overall Quality Score
"
        report += f"{overall_status} **{overall_score:.1f}/100**
"
        
        return report, overall_score

# Usage
metrics = QualityMetrics()
component_metrics = metrics.collect_metrics('setup/components/agents.py')
report, score = metrics.generate_quality_report()
print(report)
```

**Continuous Quality Monitoring:**
```python
class QualityMonitor:
    def __init__(self):
        self.quality_history = []
        self.alerts = []
        
    def monitor_quality_trends(self, component_path):
        """Monitor quality trends over time"""
        current_metrics = QualityMetrics().collect_metrics(component_path)
        
        # Add timestamp
        current_metrics['timestamp'] = datetime.now()
        self.quality_history.append(current_metrics)
        
        # Check for quality degradation
        if len(self.quality_history) >= 2:
            self._check_degradation_alerts()
            
        return current_metrics
        
    def _check_degradation_alerts(self):
        """Check for quality degradation and generate alerts"""
        current = self.quality_history[-1]
        previous = self.quality_history[-2]
        
        for metric_name in current.keys():
            if metric_name == 'timestamp':
                continue
                
            current_value = current[metric_name]['current']
            previous_value = previous[metric_name]['current']
            
            # Check for significant degradation (>10% drop)
            if current_value < previous_value * 0.9:
                alert = {
                    'type': 'quality_degradation',
                    'metric': metric_name,
                    'previous': previous_value,
                    'current': current_value,
                    'degradation': ((previous_value - current_value) / previous_value) * 100,
                    'timestamp': current['timestamp']
                }
                self.alerts.append(alert)
                
    def generate_quality_dashboard(self):
        """Generate quality dashboard HTML"""
        # Implementation would generate interactive dashboard
        # showing quality trends, alerts, and recommendations
        pass

# Usage
monitor = QualityMonitor()
current_quality = monitor.monitor_quality_trends('setup/components/core.py')

if monitor.alerts:
    print("🚨 Quality Alerts:")
    for alert in monitor.alerts:
        print(f"  {alert['metric']}: {alert['degradation']:.1f}% degradation")
```

---

## Related Resources

### Essential Development Resources

**Core Documentation:**
- [Technical Architecture](technical-architecture.md) - Framework design and patterns
- [Contributing Code](contributing-code.md) - Development setup and guidelines
- [Best Practices](../Reference/quick-start-practices.md) - Optimization and quality standards

**Testing Resources:**
- [Examples Cookbook](../Reference/examples-cookbook.md) - Practical testing examples
- [Troubleshooting Guide](../Reference/troubleshooting.md) - Common issues and solutions

**Component Development:**
- [Agents Guide](../User-Guide/agents.md) - Agent system development
- [Modes Guide](../User-Guide/modes.md) - Behavioral mode development
- [MCP Servers](../User-Guide/mcp-servers.md) - MCP integration development

### External Testing Tools

**Python Testing Ecosystem:**
```bash
# Core testing tools
pip install pytest pytest-cov pytest-mock pytest-benchmark

# Performance testing
pip install memory-profiler py-spy

# Code quality
pip install flake8 black isort mypy

# Coverage visualization
pip install coverage[toml] pytest-html
```

**Testing Frameworks Integration:**
```python
# pytest configuration (conftest.py)
import pytest
import tempfile
import shutil
from pathlib import Path

@pytest.fixture(scope="session")
def test_environment():
    """Set up test environment for SuperGemini testing"""
    test_dir = Path(tempfile.mkdtemp(prefix="superclaude_test_"))
    
    # Setup test configuration
    os.environ['SUPERCLAUDE_TEST_MODE'] = 'true'
    os.environ['SUPERCLAUDE_CONFIG_DIR'] = str(test_dir)
    
    yield test_dir
    
    # Cleanup
    shutil.rmtree(test_dir)
    os.environ.pop('SUPERCLAUDE_TEST_MODE', None)
    os.environ.pop('SUPERCLAUDE_CONFIG_DIR', None)

@pytest.fixture
def mock_mcp_servers():
    """Mock MCP servers for testing"""
    from unittest.mock import Mock
    
    mock_servers = {
        'context7': Mock(),
        'sequential': Mock(),
        'magic': Mock()
    }
    
    # Configure mock responses
    mock_servers['context7'].query.return_value = {'status': 'success'}
    mock_servers['sequential'].analyze.return_value = {'complexity': 0.7}
    
    return mock_servers
```

**CI/CD Integration:**
```yaml
# .github/workflows/test.yml
name: SuperGemini Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: [3.8, 3.9, 3.10, 3.11]
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[dev]"
        
    - name: Run tests
      run: |
        pytest tests/ --cov=setup --cov-report=xml
        
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

### Community Resources

**Development Community:**
- [GitHub Discussions](https://github.com/SuperGemini-Org/SuperGemini_Framework/discussions) - Technical discussions
- [GitHub Issues](https://github.com/SuperGemini-Org/SuperGemini_Framework/issues) - Bug reports and feature requests
- [Contributing Guidelines](../CONTRIBUTING.md) - Contribution process

**Learning Resources:**
- [Quick Start Guide](../Getting-Started/quick-start.md) - Framework overview
- [Installation Guide](../Getting-Started/installation.md) - Setup instructions
- [Commands Reference](../User-Guide/commands.md) - Usage examples

**Advanced Topics:**
- [Session Management](../User-Guide/session-management.md) - Persistent workflows
- [Flags Guide](../User-Guide/flags.md) - Behavioral control
- [Technical Roadmap](https://github.com/SuperGemini-Org/SuperGemini_Framework/projects) - Future development

---

**Development Support:**
For testing and debugging assistance, join our community discussions or create an issue with detailed reproduction steps and system information.

---

## Testing Glossary

**For Screen Readers**: This glossary contains alphabetically ordered testing and debugging terms specific to SuperGemini Framework development. Each term includes practical definitions and framework-specific context.

### A

**Agent Testing**: Specialized testing procedures for validating AI agent behavior, activation triggers, coordination patterns, and collaborative synthesis within the SuperGemini orchestration system.

**Automated Quality Gates**: Continuous validation checkpoints that automatically verify code quality, security compliance, performance standards, and architectural consistency throughout development workflows.

**Accessibility Testing**: Validation procedures that ensure documentation and interfaces are usable by developers with disabilities, including screen reader compatibility and inclusive design patterns.

### B

**Behavioral Testing**: Testing methodology for validating AI behavioral modifications through configuration files, including mode activation, instruction injection, and dynamic behavior changes.

**Benchmark Testing**: Performance measurement procedures that establish baseline metrics for component installation, agent coordination, MCP server startup, and system resource utilization.

### C

**Component Integration Testing**: Testing methodology that validates the interaction between SuperGemini components including agents, MCP servers, behavioral modes, and core framework elements.

**Configuration Testing**: Validation procedures for testing configuration file loading, instruction injection, and behavioral programming patterns unique to SuperGemini's meta-framework approach.

**Coverage Analysis**: Measurement of test completeness including code coverage, feature coverage, and integration scenario coverage for comprehensive quality validation.

### D

**Debug Profiling**: Systematic debugging approach using memory profilers, performance monitors, and execution tracers to identify bottlenecks and optimization opportunities in framework components.

**Development Testing**: Testing procedures specifically designed for framework contributors, including component validation, installation testing, and development environment verification.

### E

**End-to-End Testing**: Comprehensive testing that validates complete user workflows from input through detection, routing, orchestration, and execution within SuperGemini Framework.

**Error Recovery Testing**: Validation procedures for testing fault tolerance, graceful degradation, and recovery mechanisms when components fail or connections are lost.

### F

**Framework Testing**: Specialized testing methodologies for meta-framework components including instruction injection, behavioral programming, and configuration-driven behavior modification.

**Functional Testing**: Testing approach that validates component functionality, feature implementation, and user workflow completion within the SuperGemini ecosystem.

### I

**Integration Testing**: Testing methodology that validates the interaction between SuperGemini components and external systems including Gemini Code, MCP servers, and development tools.

**Installation Testing**: Verification procedures for testing component installation, dependency resolution, configuration setup, and environment validation across different platforms.

### M

**MCP Server Testing**: Specialized testing procedures for validating Model Context Protocol server integration, communication protocols, health monitoring, and error recovery mechanisms.

**Memory Profiling**: Performance testing methodology that monitors memory usage, leak detection, and resource optimization for framework components and agent coordination.

### P

**Performance Testing**: Comprehensive testing approach that measures execution speed, resource utilization, memory efficiency, and scalability for framework components and orchestration patterns.

**Plugin Testing**: Testing methodology for validating custom extensions, agent development, MCP server integration, and behavioral mode creation within the plugin architecture.

### Q

**Quality Validation**: Multi-dimensional testing approach that evaluates functionality, security, performance, maintainability, and architectural consistency throughout development workflows.

### R

**Regression Testing**: Testing methodology that ensures new changes don't break existing functionality, particularly important for configuration-driven behavioral programming systems.

**Resource Testing**: Performance validation that monitors system resource usage including memory, CPU, disk space, and network utilization during framework operations.

### S

**Security Testing**: Comprehensive security validation including vulnerability testing, sandboxing verification, input validation testing, and threat modeling for framework components.

**System Testing**: End-to-end validation of complete SuperGemini Framework functionality including detection engines, orchestration layers, and execution frameworks.

### U

**Unit Testing**: Testing methodology that validates individual components, functions, and modules in isolation, essential for framework component development and maintenance.

**User Workflow Testing**: Testing approach that validates complete user scenarios from task input through framework orchestration to result delivery and quality validation.

### V

**Validation Framework**: Comprehensive system for ensuring framework reliability through automated testing, continuous integration, performance monitoring, and quality assurance.

**Vulnerability Testing**: Security testing methodology that identifies and validates protection against potential security threats, input injection, and system exploitation attempts.

### Testing Skill Level Guidance

**Beginner Testing Path**:
1. **Start Here**: [Quick Start Testing Tutorial](#quick-start-testing-tutorial) for basic testing concepts
2. **Environment Setup**: [Testing Environment Setup](#testing-environment-setup) for proper configuration
3. **Basic Testing**: Simple unit tests and component validation
4. **Practice**: Work through provided code examples and test cases

**Intermediate Testing Skills**:
1. **Component Testing**: [Debugging SuperGemini Components](#debugging-superclaude-components) for component-specific testing
2. **Integration Testing**: [Integration Testing](#integration-testing) for workflow validation
3. **Quality Gates**: [Quality Validation](#quality-validation) for comprehensive testing frameworks
4. **Performance**: Basic [Performance Testing & Optimization](#performance-testing--optimization)

**Advanced Testing Expertise**:
1. **Security Testing**: [Security Testing](#security-testing) for vulnerability assessment
2. **Performance Optimization**: Advanced performance profiling and optimization
3. **Custom Testing**: Framework extension testing and custom agent validation
4. **Test Framework Development**: Contributing to testing infrastructure

**Testing Support Resources**:
- **Documentation**: Cross-references to [Contributing Code Guide](contributing-code.md) and [Technical Architecture Guide](technical-architecture.md)
- **Community**: GitHub Discussions for testing questions and best practices
- **Examples**: Comprehensive code examples with detailed comments throughout this guide
- **Troubleshooting**: [Troubleshooting Guide](#troubleshooting-guide) for common testing issues

**Quality Assurance Standards**:
- **Test Coverage**: Minimum 95% code coverage for framework components
- **Performance Benchmarks**: Specific metrics for memory usage, execution time, and resource efficiency
- **Security Validation**: Comprehensive security testing for all framework components
- **Cross-Platform Testing**: Validation across Linux, macOS, and Windows development environments