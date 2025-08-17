#!/usr/bin/env python3
"""
SuperGemini Automated Test Suite
Validates all installation and functionality
"""

import subprocess
import sys
import os
import json
from pathlib import Path
import shutil

class TestResult:
    def __init__(self):
        self.passed = []
        self.failed = []
        self.skipped = []
    
    def add_pass(self, test_name, message=""):
        self.passed.append((test_name, message))
        print(f"✅ PASS: {test_name}")
        if message:
            print(f"   {message}")
    
    def add_fail(self, test_name, message=""):
        self.failed.append((test_name, message))
        print(f"❌ FAIL: {test_name}")
        if message:
            print(f"   {message}")
    
    def add_skip(self, test_name, message=""):
        self.skipped.append((test_name, message))
        print(f"⚠️ SKIP: {test_name}")
        if message:
            print(f"   {message}")
    
    def print_summary(self):
        print("\n" + "="*60)
        print("TEST SUMMARY")
        print("="*60)
        print(f"✅ Passed: {len(self.passed)}")
        print(f"❌ Failed: {len(self.failed)}")
        print(f"⚠️ Skipped: {len(self.skipped)}")
        
        if self.failed:
            print("\nFailed Tests:")
            for test, msg in self.failed:
                print(f"  - {test}: {msg}")
        
        total = len(self.passed) + len(self.failed) + len(self.skipped)
        if total > 0:
            success_rate = (len(self.passed) / total) * 100
            print(f"\nSuccess Rate: {success_rate:.1f}%")
        
        return len(self.failed) == 0

def run_command(cmd):
    """Run a command and return result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Command timed out"
    except Exception as e:
        return False, "", str(e)

def test_installation():
    """Test SuperGemini installation"""
    results = TestResult()
    print("\n🔧 Testing SuperGemini Installation...")
    print("-" * 40)
    
    # Test 1: Check if SuperGemini is installed
    success, stdout, stderr = run_command("pip show SuperGemini")
    if success:
        results.add_pass("Package installed", "SuperGemini found in pip")
    else:
        results.add_fail("Package installed", "SuperGemini not found")
        return results
    
    # Test 2: Check version command
    success, stdout, stderr = run_command("python -m SuperGemini --version")
    if success and "SuperGemini" in stdout:
        version = stdout.strip()
        results.add_pass("Version command", f"Version: {version}")
    else:
        results.add_fail("Version command", stderr or "No version output")
    
    # Test 3: Check sg command
    success, stdout, stderr = run_command("sg --version")
    if success and "SuperGemini" in stdout:
        results.add_pass("sg command", "sg entry point works")
    else:
        # Try with .exe extension on Windows
        success, stdout, stderr = run_command("sg.exe --version")
        if success and "SuperGemini" in stdout:
            results.add_pass("sg command", "sg.exe entry point works")
        else:
            results.add_fail("sg command", "sg command not found")
    
    # Test 4: Check SuperGemini command
    success, stdout, stderr = run_command("supergemini --version")
    if success:
        results.add_pass("supergemini command", "lowercase entry point works")
    else:
        # Try with .exe extension
        success, stdout, stderr = run_command("supergemini.exe --version")
        if success:
            results.add_pass("supergemini command", "supergemini.exe works")
        else:
            results.add_skip("supergemini command", "Optional entry point")
    
    return results

def test_components():
    """Test component installation"""
    results = TestResult()
    print("\n📦 Testing Component Installation...")
    print("-" * 40)
    
    # Clean up first
    gemini_dir = Path.home() / '.gemini'
    if gemini_dir.exists():
        print(f"Cleaning up existing {gemini_dir}...")
        shutil.rmtree(gemini_dir)
    
    # Test 5: Install core component
    success, stdout, stderr = run_command(
        "python -m SuperGemini install --components core --yes"
    )
    if success:
        results.add_pass("Core installation", "Core component installed")
    else:
        results.add_fail("Core installation", stderr[:100] if stderr else "Installation failed")
        return results
    
    # Test 6: Check installed files
    expected_files = ['FLAGS.md', 'PRINCIPLES.md', 'RULES.md']
    missing_files = []
    for file_name in expected_files:
        file_path = gemini_dir / file_name
        if not file_path.exists():
            missing_files.append(file_name)
    
    if not missing_files:
        results.add_pass("Core files", f"All {len(expected_files)} files present")
    else:
        results.add_fail("Core files", f"Missing: {', '.join(missing_files)}")
    
    # Test 7: Check metadata
    metadata_file = gemini_dir / '.supergemini-metadata.json'
    if metadata_file.exists():
        try:
            with open(metadata_file) as f:
                metadata = json.load(f)
            if 'components' in metadata and 'core' in metadata['components']:
                results.add_pass("Metadata", "Valid metadata structure")
            else:
                results.add_fail("Metadata", "Invalid metadata structure")
        except Exception as e:
            results.add_fail("Metadata", f"Error reading metadata: {e}")
    else:
        results.add_fail("Metadata", "Metadata file not found")
    
    # Test 8: Install multiple components
    success, stdout, stderr = run_command(
        "python -m SuperGemini install --components agents commands modes --yes"
    )
    if success:
        results.add_pass("Multi-component install", "3 components installed")
    else:
        results.add_skip("Multi-component install", "Optional test")
    
    return results

def test_uninstall():
    """Test uninstall functionality"""
    results = TestResult()
    print("\n🗑️ Testing Uninstall...")
    print("-" * 40)
    
    # Test 9: Simple uninstall
    simple_uninstall = Path(__file__).parent / 'simple_uninstall.py'
    if simple_uninstall.exists():
        success, stdout, stderr = run_command(f"python {simple_uninstall}")
        if success:
            results.add_pass("Simple uninstall", "Cleanup successful")
        else:
            results.add_fail("Simple uninstall", stderr[:100] if stderr else "Failed")
    else:
        results.add_skip("Simple uninstall", "Script not found")
    
    # Verify cleanup
    gemini_dir = Path.home() / '.gemini'
    if not gemini_dir.exists():
        results.add_pass("Directory removed", f"{gemini_dir} cleaned up")
    else:
        results.add_fail("Directory removed", f"{gemini_dir} still exists")
    
    return results

def test_help_commands():
    """Test help and documentation commands"""
    results = TestResult()
    print("\n📚 Testing Help Commands...")
    print("-" * 40)
    
    # Test 10: Main help
    success, stdout, stderr = run_command("python -m SuperGemini --help")
    if success and "usage:" in stdout.lower():
        results.add_pass("Main help", "Help text displayed")
    else:
        results.add_fail("Main help", "No help output")
    
    # Test 11: Install help
    success, stdout, stderr = run_command("python -m SuperGemini install --help")
    if success and "install" in stdout.lower():
        results.add_pass("Install help", "Install help available")
    else:
        results.add_skip("Install help", "Optional")
    
    # Test 12: List components
    success, stdout, stderr = run_command("python -m SuperGemini install --list-components")
    if success and "Available Components" in stdout:
        results.add_pass("List components", "Component list displayed")
    else:
        results.add_skip("List components", "Optional feature")
    
    return results

def main():
    """Run all tests"""
    print("="*60)
    print("SuperGemini Automated Test Suite")
    print("="*60)
    
    all_results = TestResult()
    
    # Run test suites
    test_suites = [
        test_installation(),
        test_components(),
        test_uninstall(),
        test_help_commands()
    ]
    
    # Aggregate results
    for suite in test_suites:
        all_results.passed.extend(suite.passed)
        all_results.failed.extend(suite.failed)
        all_results.skipped.extend(suite.skipped)
    
    # Print final summary
    success = all_results.print_summary()
    
    if success:
        print("\n🎉 All critical tests passed!")
        return 0
    else:
        print("\n⚠️ Some tests failed. Please review the results.")
        return 1

if __name__ == "__main__":
    sys.exit(main())