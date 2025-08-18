#!/usr/bin/env python3
"""Debug script to find recursion issue in SuperGemini"""

import sys
import traceback
from pathlib import Path

# Add setup directory to path
setup_dir = Path(__file__).parent / "setup"
sys.path.insert(0, str(setup_dir.parent))

# Enable verbose logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Track recursion
import functools

def track_calls(func):
    """Decorator to track function calls"""
    func._call_count = 0
    func._call_stack = []
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func._call_count += 1
        func._call_stack.append((args[:2] if args else [], kwargs))
        
        if func._call_count > 10:
            print(f"\n!!! RECURSION DETECTED in {func.__name__}!!!")
            print(f"Call count: {func._call_count}")
            print("Call stack (last 5):")
            for i, (a, k) in enumerate(func._call_stack[-5:]):
                print(f"  {i}: args={a}, kwargs={k}")
            traceback.print_stack()
            raise RecursionError(f"Too many calls to {func.__name__}")
        
        try:
            result = func(*args, **kwargs)
            func._call_count -= 1
            func._call_stack.pop()
            return result
        except Exception as e:
            func._call_count -= 1
            if func._call_stack:
                func._call_stack.pop()
            raise
    
    return wrapper

# Patch the Component class
try:
    from setup.core.base import Component
    original_init = Component.__init__
    Component.__init__ = track_calls(original_init)
    
    from setup.core.registry import ComponentRegistry
    original_discover = ComponentRegistry.discover_components
    ComponentRegistry.discover_components = track_calls(original_discover)
    
    original_load = ComponentRegistry._load_component_module
    ComponentRegistry._load_component_module = track_calls(original_load)
    
except Exception as e:
    print(f"Failed to patch: {e}")
    traceback.print_exc()

# Now try to run the problematic code
try:
    print("\n=== Starting test ===")
    from setup.utils.paths import get_safe_components_directory
    from setup.core.registry import ComponentRegistry
    
    components_dir = get_safe_components_directory()
    print(f"Components dir: {components_dir}")
    
    registry = ComponentRegistry(components_dir)
    print("Created registry")
    
    registry.discover_components()
    print("Discovered components")
    
    # Try to get core component
    core_class = registry.get_component_class("core")
    print(f"Got core class: {core_class}")
    
    # Try to create instance
    if core_class:
        instance = core_class()
        print(f"Created instance: {instance}")
        
        # Try to get metadata
        metadata = instance.get_metadata()
        print(f"Got metadata: {metadata}")
    
    print("\n=== Test completed successfully ===")
    
except RecursionError as e:
    print(f"\n!!! RECURSION ERROR: {e}")
    
except Exception as e:
    print(f"\n!!! ERROR: {e}")
    traceback.print_exc()