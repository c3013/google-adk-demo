#!/usr/bin/env python3
"""
Test script to validate the demo.py structure without external dependencies
"""

import sys
import ast

def test_demo_syntax():
    """Test that demo.py has valid Python syntax"""
    try:
        with open('demo.py', 'r') as f:
            code = f.read()
        ast.parse(code)
        print("✓ demo.py syntax is valid")
        return True
    except SyntaxError as e:
        print(f"✗ Syntax error in demo.py: {e}")
        return False

def test_simple_example_syntax():
    """Test that simple_example.py has valid Python syntax"""
    try:
        with open('simple_example.py', 'r') as f:
            code = f.read()
        ast.parse(code)
        print("✓ simple_example.py syntax is valid")
        return True
    except SyntaxError as e:
        print(f"✗ Syntax error in simple_example.py: {e}")
        return False

def test_required_functions():
    """Test that demo.py contains required functions"""
    try:
        with open('demo.py', 'r') as f:
            code = f.read()
        
        required_items = [
            'class OpenSourceModelDemo',
            'def initialize_client',
            'def generate_text',
            'def chat_session',
            'def load_config_from_env',
            'def load_config_from_args',
            'def print_usage',
            'def run_examples',
            'def main',
        ]
        
        all_found = True
        for item in required_items:
            if item in code:
                print(f"✓ Found: {item}")
            else:
                print(f"✗ Missing: {item}")
                all_found = False
        
        return all_found
    except Exception as e:
        print(f"✗ Error checking functions: {e}")
        return False

def test_configuration_support():
    """Test that configuration parameters are properly handled"""
    try:
        with open('demo.py', 'r') as f:
            code = f.read()
        
        required_params = ['api_key', 'base_url', 'model']
        all_found = True
        
        for param in required_params:
            if param in code:
                print(f"✓ Configuration parameter supported: {param}")
            else:
                print(f"✗ Missing configuration parameter: {param}")
                all_found = False
        
        return all_found
    except Exception as e:
        print(f"✗ Error checking configuration: {e}")
        return False

def main():
    """Run all tests"""
    print("="*60)
    print("Testing Google ADK Demo Implementation")
    print("="*60)
    print()
    
    tests = [
        ("Syntax validation - demo.py", test_demo_syntax),
        ("Syntax validation - simple_example.py", test_simple_example_syntax),
        ("Required functions check", test_required_functions),
        ("Configuration support check", test_configuration_support),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-"*60)
        result = test_func()
        results.append(result)
    
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
