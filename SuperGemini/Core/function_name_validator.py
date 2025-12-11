#!/usr/bin/env python3
"""
Function Name Validator for Gemini API
Validates and corrects function names to meet Gemini API requirements.

Requirements:
- Must start with a letter (a-z, A-Z) or underscore (_)
- Can only contain: letters, digits, underscores, dots (.), or dashes (-)
- Maximum length: 64 characters
"""

import re
from typing import Tuple


class FunctionNameValidator:
    """Validator for Gemini API function names."""
    
    # Gemini API function name constraints
    MAX_LENGTH = 64
    VALID_CHARS_PATTERN = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_.\-]*$')
    VALID_START_PATTERN = re.compile(r'^[a-zA-Z_]')
    VALID_BODY_PATTERN = re.compile(r'^[a-zA-Z0-9_.\-]+$')
    
    @classmethod
    def validate(cls, name: str) -> Tuple[bool, str]:
        """
        Validate if a function name meets Gemini API requirements.
        
        Args:
            name: The function name to validate
            
        Returns:
            Tuple of (is_valid, error_message)
            - is_valid: True if the name is valid, False otherwise
            - error_message: Empty string if valid, otherwise describes the issue
        """
        if not name:
            return False, "Function name cannot be empty"
        
        if len(name) > cls.MAX_LENGTH:
            return False, f"Function name exceeds maximum length of {cls.MAX_LENGTH} characters (current: {len(name)})"
        
        if not cls.VALID_START_PATTERN.match(name[0]):
            return False, f"Function name must start with a letter or underscore, found: '{name[0]}'"
        
        if not cls.VALID_CHARS_PATTERN.match(name):
            invalid_chars = set()
            for char in name:
                if not re.match(r'[a-zA-Z0-9_.\-]', char):
                    invalid_chars.add(char)
            return False, f"Function name contains invalid characters: {', '.join(repr(c) for c in sorted(invalid_chars))}"
        
        return True, ""
    
    @classmethod
    def correct(cls, name: str, fallback_prefix: str = "func") -> str:
        """
        Correct a function name to meet Gemini API requirements.
        
        Args:
            name: The function name to correct
            fallback_prefix: Prefix to use if the name is empty or starts with invalid character
            
        Returns:
            A corrected function name that meets all requirements
        """
        if not name:
            return fallback_prefix
        
        # Replace invalid characters with underscores
        corrected = re.sub(r'[^a-zA-Z0-9_.\-]', '_', name)
        
        # Ensure it starts with a letter or underscore
        if not cls.VALID_START_PATTERN.match(corrected[0]):
            # If starts with a digit, dot, or dash, prepend the fallback prefix
            corrected = f"{fallback_prefix}_{corrected}"
        
        # Truncate to maximum length
        if len(corrected) > cls.MAX_LENGTH:
            corrected = corrected[:cls.MAX_LENGTH]
            # Ensure we didn't cut off in the middle leaving a trailing invalid char
            # (though underscores, dots, and dashes are valid at the end)
        
        # Final validation - this should always pass now
        is_valid, _ = cls.validate(corrected)
        if not is_valid:
            # Fallback to a safe default if somehow still invalid
            return fallback_prefix
        
        return corrected
    
    @classmethod
    def validate_and_correct(cls, name: str, fallback_prefix: str = "func") -> Tuple[bool, str, str]:
        """
        Validate a function name and provide a corrected version if invalid.
        
        Args:
            name: The function name to validate
            fallback_prefix: Prefix to use for correction if needed
            
        Returns:
            Tuple of (is_valid, corrected_name, message)
            - is_valid: True if the original name was valid
            - corrected_name: The original name if valid, otherwise a corrected version
            - message: Empty if valid, otherwise describes what was corrected
        """
        is_valid, error_msg = cls.validate(name)
        
        if is_valid:
            return True, name, ""
        
        corrected = cls.correct(name, fallback_prefix)
        message = f"Original name '{name}' was invalid: {error_msg}. Corrected to: '{corrected}'"
        
        return False, corrected, message


# Convenience functions for direct use
def validate_function_name(name: str) -> Tuple[bool, str]:
    """
    Validate if a function name meets Gemini API requirements.
    
    Args:
        name: The function name to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    return FunctionNameValidator.validate(name)


def correct_function_name(name: str, fallback_prefix: str = "func") -> str:
    """
    Correct a function name to meet Gemini API requirements.
    
    Args:
        name: The function name to correct
        fallback_prefix: Prefix to use if the name is empty or starts with invalid character
        
    Returns:
        A corrected function name that meets all requirements
    """
    return FunctionNameValidator.correct(name, fallback_prefix)


def validate_and_correct_function_name(name: str, fallback_prefix: str = "func") -> Tuple[bool, str, str]:
    """
    Validate a function name and provide a corrected version if invalid.
    
    Args:
        name: The function name to validate
        fallback_prefix: Prefix to use for correction if needed
        
    Returns:
        Tuple of (is_valid, corrected_name, message)
    """
    return FunctionNameValidator.validate_and_correct(name, fallback_prefix)


if __name__ == "__main__":
    # Example usage and testing
    test_cases = [
        "valid_function_name",
        "ValidFunctionName",
        "_private_function",
        "function.with.dots",
        "function-with-dashes",
        "123_starts_with_number",
        "has spaces in it",
        "has@special#chars",
        "a" * 70,  # Too long
        "",  # Empty
        "café",  # Unicode
        ".starts.with.dot",
        "-starts-with-dash",
    ]
    
    print("Function Name Validation Tests")
    print("=" * 80)
    
    for test_name in test_cases:
        is_valid, corrected, message = validate_and_correct_function_name(test_name)
        
        print(f"\nOriginal: {repr(test_name)}")
        print(f"Valid: {is_valid}")
        if not is_valid:
            print(f"Corrected: {repr(corrected)}")
            print(f"Message: {message}")
        else:
            print(f"✓ Name is valid")
