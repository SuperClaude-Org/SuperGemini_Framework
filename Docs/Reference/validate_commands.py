#!/usr/bin/env python3
"""
SuperGemini Framework Command Validation Script

This script validates all documented SuperGemini commands and flags to ensure
documentation accuracy and system reliability.

Usage:
    python3 validate_commands.py [--quick] [--verbose] [--export-report]
    
Requirements:
    - SuperGemini Framework installed
    - Gemini CLI installed (npm install -g @google/gemini-cli)
    - MCP servers configured (for full validation)
"""

import sys
import os
import subprocess
import time
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass, asdict
from enum import Enum
import argparse

class ValidationResult(Enum):
    PASS = "✅"
    FAIL = "❌"  
    WARNING = "⚠️"
    SKIP = "⏭️"
    UNKNOWN = "❓"

@dataclass
class TestResult:
    name: str
    category: str
    command: str
    expected_behavior: str
    result: ValidationResult
    message: str
    execution_time: float = 0.0
    details: Optional[Dict] = None

class SuperGeminiValidator:
    """Comprehensive validation system for SuperGemini commands and flags."""
    
    def __init__(self, verbose: bool = False, quick_mode: bool = False):
        self.verbose = verbose
        self.quick_mode = quick_mode
        self.results: List[TestResult] = []
        self.start_time = datetime.now()
        
        # Documented commands from commands.md
        # Note: brainstorm has been integrated as a behavioral mode
        self.essential_commands = [
            "implement", "analyze", "troubleshoot", 
            "test", "improve", "document", "workflow"
        ]
        
        self.development_commands = ["build", "design"]
        self.analysis_commands = ["explain"]
        self.quality_commands = ["cleanup"]
        self.project_mgmt_commands = ["estimate", "task", "spawn"]
        self.utility_commands = ["git", "index"]
        self.session_commands = ["load", "save", "reflect", "select-tool"]
        
        # All commands combined
        self.all_commands = (
            self.essential_commands + self.development_commands + 
            self.analysis_commands + self.quality_commands +
            self.project_mgmt_commands + self.utility_commands + 
            self.session_commands
        )
        
        # Documented flags from flags.md
        self.analysis_flags = ["--think", "--think-hard", "--ultrathink"]
        self.mode_flags = ["--introspect", "--task-manage"]
        self.efficiency_flags = ["--uc", "--token-efficient", "--orchestrate"]
        self.mcp_flags = [
            "--c7", "--context7", "--seq", "--sequential", "--magic",
            "--morph", "--morphllm", "--serena", "--play", "--playwright",
            "--all-mcp", "--no-mcp"
        ]
        self.focus_flags = [
            "--focus security", "--focus performance", "--focus quality",
            "--focus architecture", "--focus accessibility", "--focus testing"
        ]
        self.safety_flags = ["--safe-mode", "--validate", "--dry-run", "--backup"]
        self.execution_flags = [
            "--parallel", "--sequential", "--concurrency 2", "--scope file",
            "--scope module", "--scope project", "--scope system"
        ]
        
        # All flags combined
        self.all_flags = (
            self.analysis_flags + self.mode_flags + self.efficiency_flags +
            self.mcp_flags + self.focus_flags + self.safety_flags + 
            self.execution_flags
        )

    def log(self, message: str, level: str = "INFO"):
        """Log message with timestamp and level."""
        if self.verbose or level in ["ERROR", "WARNING"]:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] {level}: {message}")

    def run_command_test(self, command: str, timeout: int = 30) -> Tuple[bool, str, float]:
        """
        Attempt to run a SuperGemini command in a controlled way.
        
        Note: This simulates command execution since actual SuperGemini commands
        require Gemini CLI to be installed and properly configured.
        """
        start_time = time.time()
        
        try:
            # For validation purposes, we'll check command syntax and structure
            # In a real deployment, this would interface with the installed Gemini CLI
            
            if not command.startswith("/sg:"):
                return False, "Invalid command format - must start with /sg:", time.time() - start_time
            
            cmd_name = command.split()[0][4:]  # Remove /sg: prefix
            
            if cmd_name not in self.all_commands:
                return False, f"Unknown command: {cmd_name}", time.time() - start_time
            
            # Simulate basic validation checks
            time.sleep(0.1)  # Simulate processing time
            
            # Check for obvious syntax errors
            if "--" in command:
                flags = [part for part in command.split() if part.startswith("--")]
                for flag in flags:
                    if not self._is_valid_flag_syntax(flag):
                        return False, f"Invalid flag syntax: {flag}", time.time() - start_time
                
                # Check for contradictory flag combinations
                conflict_result = self._check_flag_conflicts(flags)
                if conflict_result:
                    return False, conflict_result, time.time() - start_time
            
            execution_time = time.time() - start_time
            return True, f"Command syntax valid: {command}", execution_time
            
        except Exception as e:
            execution_time = time.time() - start_time
            return False, f"Command test failed: {str(e)}", execution_time

    def _is_valid_flag_syntax(self, flag: str) -> bool:
        """Validate flag syntax against documented patterns."""
        # Remove values for validation (e.g., "--concurrency 2" -> "--concurrency")
        base_flag = flag.split()[0] if " " in flag else flag
        
        valid_flag_patterns = [
            # Analysis flags
            "--think", "--think-hard", "--ultrathink",
            # Mode flags  
            "--introspect", "--task-manage", "--delegate",
            # Efficiency flags
            "--uc", "--ultracompressed", "--token-efficient", "--orchestrate",
            # MCP flags
            "--c7", "--context7", "--seq", "--sequential", "--magic",
            "--morph", "--morphllm", "--serena", "--play", "--playwright", 
            "--all-mcp", "--no-mcp",
            # Focus flags (special case with values)
            "--focus",
            # Safety flags
            "--safe-mode", "--validate", "--dry-run", "--backup",
            # Execution flags
            "--parallel", "--sequential", "--concurrency", "--scope",
            # Build and optimization flags
            "--optimize", "--target", "--fix-errors", "--deps-install",
            # Test flags
            "--coverage", "--fix", "--watch", "--smoke", "--related-tests",
            "--browsers", "--type", "--report",
            # Documentation flags
            "--type", "--format", "--inline", "--audience",
            # Improvement flags
            "--fix", "--preview", "--safe-mode", "--measure-impact",
            # Task management flags
            "--breakdown", "--priority", "--detailed", "--estimates",
            # Additional common flags
            "--verbose", "--quiet", "--help", "--format", "--export",
            "--depth", "--strategy", "--level", "--confirm-before-delete"
        ]
        
        return base_flag in valid_flag_patterns

    def _check_flag_conflicts(self, flags: List[str]) -> Optional[str]:
        """Check for contradictory flag combinations."""
        base_flags = [flag.split()[0] for flag in flags]
        
        # Define contradictory flag pairs
        conflicts = [
            ("--all-mcp", "--no-mcp", "Cannot use all MCP servers and no MCP servers simultaneously"),
            ("--parallel", "--sequential", "Cannot use parallel and sequential execution simultaneously"),
            ("--verbose", "--quiet", "Cannot use verbose and quiet modes simultaneously"),
            ("--think", "--no-mcp", "Deep thinking modes require MCP servers (--think conflicts with --no-mcp)"),
            ("--think-hard", "--no-mcp", "Deep thinking modes require MCP servers (--think-hard conflicts with --no-mcp)"),
            ("--ultrathink", "--no-mcp", "Deep thinking modes require MCP servers (--ultrathink conflicts with --no-mcp)"),
        ]
        
        for flag1, flag2, message in conflicts:
            if flag1 in base_flags and flag2 in base_flags:
                return f"Flag conflict: {message}"
        
        # Check for invalid focus domain values
        focus_flags = [flag for flag in flags if flag.startswith("--focus")]
        for focus_flag in focus_flags:
            if " " in focus_flag:
                domain = focus_flag.split(" ", 1)[1]
                valid_domains = ["security", "performance", "quality", "architecture", "accessibility", "testing"]
                if domain not in valid_domains:
                    return f"Invalid focus domain: {domain}. Valid domains: {', '.join(valid_domains)}"
        
        return None

    def validate_command_syntax(self) -> None:
        """Test basic command syntax validation."""
        self.log("Starting command syntax validation...")
        
        for cmd in self.all_commands:
            test_command = f"/sg:{cmd}"
            success, message, exec_time = self.run_command_test(test_command)
            
            result = TestResult(
                name=f"Syntax: {cmd}",
                category="Command Syntax",
                command=test_command,
                expected_behavior="Valid command syntax recognized",
                result=ValidationResult.PASS if success else ValidationResult.FAIL,
                message=message,
                execution_time=exec_time
            )
            self.results.append(result)

    def validate_flag_combinations(self) -> None:
        """Test documented flag combinations."""
        self.log("Starting flag combination validation...")
        
        # Test common flag combinations from documentation
        test_combinations = [
            # Analysis combinations
            ("/sg:analyze src/ --think", "Standard analysis with structured thinking"),
            ("/sg:analyze --focus security --think-hard", "Deep security analysis"),
            ("/sg:troubleshoot 'issue' --ultrathink --seq", "Maximum troubleshooting"),
            
            # Development combinations
            ("/sg:implement 'feature' --magic --c7", "UI feature with patterns"),
            ("/sg:improve code/ --morph --serena", "Code improvement with context"),
            ("/sg:build --optimize --validate", "Safe production build"),
            
            # Workflow combinations
            ("/sg:brainstorm 'idea' --think --c7", "Structured brainstorming"),
            ("/sg:task 'complex' --task-manage --delegate", "Complex task coordination"),
            ("/sg:test --coverage --play", "Comprehensive testing"),
            
            # Safety combinations
            ("/sg:improve production/ --safe-mode --backup", "Safe production changes"),
            ("/sg:cleanup legacy/ --dry-run --validate", "Preview cleanup"),
            
            # Efficiency combinations
            ("/sg:analyze large/ --uc --scope module", "Efficient scoped analysis"),
            ("/sg:implement 'simple' --no-mcp", "Lightweight implementation"),
        ]
        
        for command, description in test_combinations:
            success, message, exec_time = self.run_command_test(command)
            
            result = TestResult(
                name=f"Combo: {description}",
                category="Flag Combinations", 
                command=command,
                expected_behavior=description,
                result=ValidationResult.PASS if success else ValidationResult.FAIL,
                message=message,
                execution_time=exec_time
            )
            self.results.append(result)

    def validate_mcp_server_flags(self) -> None:
        """Test MCP server activation flags."""
        self.log("Starting MCP server flag validation...")
        
        mcp_tests = [
            ("--c7", "Context7 server for documentation"),
            ("--seq", "Sequential server for reasoning"),
            ("--magic", "Magic server for UI components"),
            ("--morph", "Morphllm server for transformations"),
            ("--serena", "Serena server for project memory"),
            ("--play", "Playwright server for browser testing"),
            ("--all-mcp", "All MCP servers activated"),
            ("--no-mcp", "No MCP servers, native only"),
        ]
        
        for flag, description in mcp_tests:
            command = f"/sg:analyze test/ {flag}"
            success, message, exec_time = self.run_command_test(command)
            
            result = TestResult(
                name=f"MCP: {flag}",
                category="MCP Server Flags",
                command=command, 
                expected_behavior=description,
                result=ValidationResult.PASS if success else ValidationResult.FAIL,
                message=message,
                execution_time=exec_time
            )
            self.results.append(result)

    def validate_focus_flags(self) -> None:
        """Test domain focus flags."""
        self.log("Starting focus flag validation...")
        
        focus_domains = [
            "security", "performance", "quality", 
            "architecture", "accessibility", "testing"
        ]
        
        for domain in focus_domains:
            command = f"/sg:analyze code/ --focus {domain}"
            success, message, exec_time = self.run_command_test(command)
            
            result = TestResult(
                name=f"Focus: {domain}",
                category="Focus Flags",
                command=command,
                expected_behavior=f"Analysis focused on {domain} domain",
                result=ValidationResult.PASS if success else ValidationResult.FAIL,
                message=message,
                execution_time=exec_time
            )
            self.results.append(result)

    def validate_workflow_examples(self) -> None:
        """Test documented workflow examples."""
        self.log("Starting workflow example validation...")
        
        workflows = [
            # New Project Setup workflow
            [
                "/sg:brainstorm 'project concept'",
                "/sg:design 'system architecture'", 
                "/sg:workflow 'implementation plan'",
                "/sg:save 'project-plan'"
            ],
            
            # Feature Development workflow  
            [
                "/sg:load 'project-context'",
                "/sg:implement 'feature name'",
                "/sg:test --coverage",
                "/sg:document --type api"
            ],
            
            # Bug Investigation workflow
            [
                "/sg:troubleshoot 'issue description'",
                "/sg:analyze --focus problem-area",
                "/sg:improve --fix --safe-mode",
                "/sg:test --related-tests"
            ]
        ]
        
        for i, workflow in enumerate(workflows):
            workflow_name = f"Workflow {i+1}"
            all_valid = True
            messages = []
            total_time = 0
            
            for step, command in enumerate(workflow):
                success, message, exec_time = self.run_command_test(command)
                total_time += exec_time
                
                if not success:
                    all_valid = False
                    messages.append(f"Step {step+1} failed: {message}")
                else:
                    messages.append(f"Step {step+1} passed")
            
            result = TestResult(
                name=workflow_name,
                category="Workflow Examples",
                command=" → ".join(workflow),
                expected_behavior="Complete workflow execution",
                result=ValidationResult.PASS if all_valid else ValidationResult.FAIL,
                message="; ".join(messages),
                execution_time=total_time
            )
            self.results.append(result)

    def validate_error_conditions(self) -> None:
        """Test error handling for invalid inputs."""
        self.log("Starting error condition validation...")
        
        error_tests = [
            # Invalid commands
            ("/sg:invalid-command", "Should reject unknown commands"),
            ("/invalid:format", "Should reject invalid command format"),
            ("sc:missing-slash", "Should reject missing slash prefix"),
            
            # Invalid flag combinations
            ("/sg:analyze --all-mcp --no-mcp", "Should handle contradictory flags"),
            ("/sg:implement --invalid-flag", "Should reject unknown flags"),
            ("/sg:test --focus invalid-domain", "Should reject invalid focus domains"),
            
            # Malformed syntax
            ("/sg:analyze --", "Should handle incomplete flags"),
            ("/sg:implement ''", "Should handle empty arguments"),
        ]
        
        for command, expected_behavior in error_tests:
            success, message, exec_time = self.run_command_test(command)
            
            # For error tests, we expect failure (proper error handling)
            expected_to_fail = True
            actual_result = ValidationResult.PASS if not success else ValidationResult.FAIL
            
            result = TestResult(
                name=f"Error: {command.split()[0] if command.split() else 'malformed'}",
                category="Error Handling",
                command=command,
                expected_behavior=expected_behavior,
                result=actual_result,
                message=message,
                execution_time=exec_time
            )
            self.results.append(result)

    def check_system_requirements(self) -> None:
        """Validate system setup and requirements."""
        self.log("Checking system requirements...")
        
        # Check Python version
        python_version = sys.version_info
        python_ok = python_version >= (3, 8)
        
        result = TestResult(
            name="Python Version",
            category="System Requirements",
            command="python --version",
            expected_behavior="Python 3.8+",
            result=ValidationResult.PASS if python_ok else ValidationResult.FAIL,
            message=f"Python {python_version.major}.{python_version.minor}.{python_version.micro}",
            execution_time=0.0
        )
        self.results.append(result)
        
        # Check if we're in SuperGemini project directory
        current_dir = Path.cwd()
        is_superclaude_project = (
            (current_dir / "SuperGemini").exists() or
            (current_dir / "pyproject.toml").exists() and "SuperGemini" in (current_dir / "pyproject.toml").read_text()
        )
        
        result = TestResult(
            name="Project Directory",
            category="System Requirements", 
            command="pwd",
            expected_behavior="In SuperGemini project directory",
            result=ValidationResult.PASS if is_superclaude_project else ValidationResult.WARNING,
            message=f"Current directory: {current_dir}",
            execution_time=0.0
        )
        self.results.append(result)

    def run_integration_tests(self) -> None:
        """Run integration tests simulating real usage."""
        self.log("Starting integration tests...")
        
        # Test session lifecycle
        session_commands = [
            "/sg:load test-project/",
            "/sg:analyze src/ --think",
            "/sg:implement 'test feature' --magic",
            "/sg:save 'test-session'"
        ]
        
        session_valid = True
        session_messages = []
        session_time = 0
        
        for command in session_commands:
            success, message, exec_time = self.run_command_test(command)
            session_time += exec_time
            
            if success:
                session_messages.append(f"✓ {command}")
            else:
                session_valid = False
                session_messages.append(f"✗ {command}: {message}")
        
        result = TestResult(
            name="Session Lifecycle",
            category="Integration Tests",
            command=" → ".join(session_commands),
            expected_behavior="Complete session management workflow",
            result=ValidationResult.PASS if session_valid else ValidationResult.FAIL,
            message="; ".join(session_messages),
            execution_time=session_time
        )
        self.results.append(result)

    def generate_report(self) -> Dict:
        """Generate comprehensive validation report."""
        total_tests = len(self.results)
        passed_tests = len([r for r in self.results if r.result == ValidationResult.PASS])
        failed_tests = len([r for r in self.results if r.result == ValidationResult.FAIL])
        warning_tests = len([r for r in self.results if r.result == ValidationResult.WARNING])
        
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        execution_time = (datetime.now() - self.start_time).total_seconds()
        
        # Group results by category
        categories = {}
        for result in self.results:
            if result.category not in categories:
                categories[result.category] = []
            categories[result.category].append(result)
        
        report = {
            "timestamp": self.start_time.isoformat(),
            "execution_time_seconds": execution_time,
            "summary": {
                "total_tests": total_tests,
                "passed": passed_tests,
                "failed": failed_tests,
                "warnings": warning_tests,
                "success_rate_percent": round(success_rate, 2)
            },
            "categories": {}
        }
        
        for category, tests in categories.items():
            category_passed = len([t for t in tests if t.result == ValidationResult.PASS])
            category_total = len(tests)
            category_rate = (category_passed / category_total * 100) if category_total > 0 else 0
            
            report["categories"][category] = {
                "success_rate": round(category_rate, 2),
                "total": category_total,
                "passed": category_passed,
                "failed": len([t for t in tests if t.result == ValidationResult.FAIL]),
                "tests": [asdict(test) for test in tests]
            }
        
        return report

    def print_summary(self) -> None:
        """Print validation summary to console."""
        report = self.generate_report()
        summary = report["summary"]
        
        print("\n" + "="*60)
        print("🧪 SUPERCLAUDE COMMAND VALIDATION SUMMARY")
        print("="*60)
        print(f"⏱️  Execution Time: {report['execution_time_seconds']:.2f} seconds")
        print(f"📊 Success Rate: {summary['success_rate_percent']}%")
        print(f"✅ Passed: {summary['passed']}")
        print(f"❌ Failed: {summary['failed']}")
        print(f"⚠️  Warnings: {summary['warnings']}")
        print(f"📈 Total Tests: {summary['total_tests']}")
        
        # Category breakdown
        print("\n📂 CATEGORY BREAKDOWN:")
        for category, data in report["categories"].items():
            status_icon = "✅" if data["success_rate"] >= 90 else "⚠️" if data["success_rate"] >= 70 else "❌"
            print(f"{status_icon} {category}: {data['success_rate']:.1f}% ({data['passed']}/{data['total']})")
        
        # Failed tests detail
        failed_results = [r for r in self.results if r.result == ValidationResult.FAIL]
        if failed_results:
            print(f"\n❌ FAILED TESTS ({len(failed_results)}):")
            for result in failed_results:
                print(f"   • {result.category}: {result.name}")
                print(f"     Command: {result.command}")
                print(f"     Error: {result.message}")
        
        # Warnings detail
        warning_results = [r for r in self.results if r.result == ValidationResult.WARNING]
        if warning_results:
            print(f"\n⚠️  WARNINGS ({len(warning_results)}):")
            for result in warning_results:
                print(f"   • {result.category}: {result.name}")
                print(f"     Message: {result.message}")
        
        print("\n" + "="*60)

    def export_report(self, filename: str = None) -> str:
        """Export detailed report to JSON file."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"superclaude_validation_report_{timestamp}.json"
        
        report = self.generate_report()
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        self.log(f"Report exported to: {filename}")
        return filename

    def run_all_validations(self) -> None:
        """Execute complete validation suite."""
        print("🚀 Starting SuperGemini Framework validation...")
        print(f"📅 Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🏃 Mode: {'Quick' if self.quick_mode else 'Comprehensive'}")
        print()
        
        # System requirements check
        self.check_system_requirements()
        
        # Core validations
        self.validate_command_syntax()
        
        if not self.quick_mode:
            self.validate_flag_combinations()
            self.validate_mcp_server_flags() 
            self.validate_focus_flags()
            self.validate_workflow_examples()
            self.validate_error_conditions()
            self.run_integration_tests()
        
        self.log("Validation suite completed")

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Validate SuperGemini Framework commands and flags",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python3 validate_commands.py                    # Full validation
    python3 validate_commands.py --quick            # Quick syntax check only
    python3 validate_commands.py --verbose          # Detailed logging
    python3 validate_commands.py --export-report    # Export JSON report
        """
    )
    
    parser.add_argument(
        "--quick", 
        action="store_true", 
        help="Run quick validation (syntax only)"
    )
    parser.add_argument(
        "--verbose", 
        action="store_true", 
        help="Enable verbose logging"
    )
    parser.add_argument(
        "--export-report", 
        action="store_true", 
        help="Export detailed JSON report"
    )
    parser.add_argument(
        "--report-file", 
        type=str, 
        help="Custom report filename"
    )
    
    args = parser.parse_args()
    
    # Initialize validator
    validator = SuperGeminiValidator(
        verbose=args.verbose,
        quick_mode=args.quick
    )
    
    try:
        # Run validation suite
        validator.run_all_validations()
        
        # Print summary
        validator.print_summary()
        
        # Export report if requested
        if args.export_report:
            report_file = validator.export_report(args.report_file)
            print(f"\n📄 Detailed report saved: {report_file}")
        
        # Exit code based on results
        failed_count = len([r for r in validator.results if r.result == ValidationResult.FAIL])
        exit_code = 1 if failed_count > 0 else 0
        
        if exit_code == 0:
            print("🎉 All validations passed!")
        else:
            print(f"⚠️  {failed_count} validation(s) failed. See details above.")
        
        sys.exit(exit_code)
        
    except KeyboardInterrupt:
        print("\n🛑 Validation interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n💥 Validation failed with error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()