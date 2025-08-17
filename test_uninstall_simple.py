#!/usr/bin/env python3
"""
Simple test script to isolate the uninstall recursion issue
"""

import sys
import threading
from pathlib import Path

def test_basic_uninstall():
    """Test basic uninstall without the complex registry"""
    print("Testing basic uninstall functionality...")
    
    # Add recursion detection
    thread_local = threading.local()
    if hasattr(thread_local, 'uninstall_in_progress'):
        print("[✗] Recursion detected in uninstall operation")
        return False
    thread_local.uninstall_in_progress = True
    
    try:
        # Simulate the parts that were causing recursion
        install_dir = Path.home() / ".gemini"
        print(f"Testing with install directory: {install_dir}")
        
        if not install_dir.exists():
            print("No installation found")
            return True
        
        # Test settings service directly
        sys.path.insert(0, str(Path(__file__).parent))
        from setup.services.settings import SettingsService
        
        print("Creating SettingsService...")
        settings_manager = SettingsService(install_dir)
        
        print("Getting installed components...")
        components = settings_manager.get_installed_components()
        print(f"Found components: {components}")
        
        print("Testing metadata loading...")
        metadata = settings_manager.load_metadata()
        print(f"Metadata: {metadata}")
        
        return True
        
    except RecursionError as e:
        print(f"[✗] Recursion error: {e}")
        return False
    except Exception as e:
        print(f"[✗] Error: {e}")
        return False
    finally:
        if hasattr(thread_local, 'uninstall_in_progress'):
            delattr(thread_local, 'uninstall_in_progress')

def test_registry():
    """Test component registry"""
    print("\nTesting component registry...")
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from setup.core.registry import ComponentRegistry
        
        components_dir = Path(__file__).parent / "setup" / "components"
        print(f"Components directory: {components_dir}")
        
        registry = ComponentRegistry(components_dir)
        print("Discovering components...")
        registry.discover_components()
        
        print("Listing components...")
        component_list = registry.list_components()
        print(f"Found components: {component_list}")
        
        return True
        
    except RecursionError as e:
        print(f"[✗] Recursion error in registry: {e}")
        return False
    except Exception as e:
        print(f"[✗] Error in registry: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("SuperGemini Uninstall Recursion Test")
    print("=" * 60)
    
    test1 = test_basic_uninstall()
    test2 = test_registry()
    
    print("\n" + "=" * 60)
    print("Test Results:")
    print(f"Basic uninstall: {'PASS' if test1 else 'FAIL'}")
    print(f"Registry test: {'PASS' if test2 else 'FAIL'}")
    print("=" * 60)
    
    if not test1 or not test2:
        sys.exit(1)