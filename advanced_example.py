#!/usr/bin/env python3
"""
Advanced example demonstrating various features of the Google ADK demo
This shows how to use the OpenSourceModelDemo class programmatically
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import demo module
sys.path.insert(0, str(Path(__file__).parent))

# Note: This is an example of how to use the demo programmatically
# To run this, you'll need to install the dependencies first:
# pip install -r requirements.txt

def example_basic_usage():
    """Example 1: Basic usage with direct configuration"""
    print("\n" + "="*60)
    print("Example 1: Basic Usage")
    print("="*60)
    
    # Import after path is set
    from demo import OpenSourceModelDemo
    
    # Configure the demo
    api_key = "your_api_key_here"
    base_url = "https://api.openai.com/v1"
    model = "gpt-3.5-turbo"
    
    # Create demo instance
    demo = OpenSourceModelDemo(api_key, base_url, model)
    
    # Initialize and use
    if demo.initialize_client():
        demo.generate_text("What is machine learning?", max_tokens=100)

def example_with_environment():
    """Example 2: Using environment variables"""
    print("\n" + "="*60)
    print("Example 2: Using Environment Variables")
    print("="*60)
    
    from demo import OpenSourceModelDemo
    
    # Set environment variables (in practice, use .env file)
    os.environ['API_KEY'] = 'your_api_key'
    os.environ['BASE_URL'] = 'https://api.openai.com/v1'
    os.environ['MODEL'] = 'gpt-3.5-turbo'
    
    # Load from environment
    api_key = os.getenv('API_KEY')
    base_url = os.getenv('BASE_URL')
    model = os.getenv('MODEL')
    
    # Create and use
    demo = OpenSourceModelDemo(api_key, base_url, model)
    if demo.initialize_client():
        result = demo.generate_text("Explain Python decorators", max_tokens=150)
        if result:
            print(f"Generated {len(result.split())} words")

def example_multiple_prompts():
    """Example 3: Processing multiple prompts"""
    print("\n" + "="*60)
    print("Example 3: Multiple Prompts")
    print("="*60)
    
    from demo import OpenSourceModelDemo
    
    # Configuration
    demo = OpenSourceModelDemo(
        api_key="your_api_key",
        base_url="https://api.openai.com/v1",
        model="gpt-3.5-turbo"
    )
    
    if not demo.initialize_client():
        return
    
    # List of prompts to process
    prompts = [
        "What is AI?",
        "What is ML?",
        "What is DL?",
    ]
    
    results = []
    for i, prompt in enumerate(prompts, 1):
        print(f"\nProcessing prompt {i}/{len(prompts)}...")
        result = demo.generate_text(prompt, max_tokens=50)
        if result:
            results.append(result)
    
    print(f"\nProcessed {len(results)} prompts successfully")

def example_error_handling():
    """Example 4: Error handling"""
    print("\n" + "="*60)
    print("Example 4: Error Handling")
    print("="*60)
    
    from demo import OpenSourceModelDemo
    
    # Try with invalid configuration
    demo = OpenSourceModelDemo(
        api_key="invalid_key",
        base_url="https://invalid.url",
        model="invalid_model"
    )
    
    # This should handle the error gracefully
    if not demo.initialize_client():
        print("✓ Error was handled properly")
    else:
        # Try to use it anyway (will likely fail)
        result = demo.generate_text("Test prompt", max_tokens=10)
        if result is None:
            print("✓ Generation error was handled properly")

def example_configuration_variations():
    """Example 5: Different configuration variations"""
    print("\n" + "="*60)
    print("Example 5: Configuration Variations")
    print("="*60)
    
    # Example configurations for different providers
    configurations = [
        {
            "name": "OpenAI",
            "api_key": "sk-...",
            "base_url": "https://api.openai.com/v1",
            "model": "gpt-3.5-turbo",
        },
        {
            "name": "Local Ollama",
            "api_key": "dummy_key",
            "base_url": "http://localhost:11434/v1",
            "model": "llama2",
        },
        {
            "name": "Google Gemini",
            "api_key": "AIza...",
            "base_url": "https://generativelanguage.googleapis.com/v1beta",
            "model": "gemini-2.0-flash-exp",
        },
    ]
    
    print("\nSupported configurations:")
    for i, config in enumerate(configurations, 1):
        print(f"\n{i}. {config['name']}")
        print(f"   Base URL: {config['base_url']}")
        print(f"   Model: {config['model']}")
        print(f"   API Key: {config['api_key'][:10]}...")

def print_usage_info():
    """Print usage information"""
    print("\n" + "="*60)
    print("Advanced Usage Examples")
    print("="*60)
    print("""
This file demonstrates various ways to use the Google ADK demo:

1. Basic usage with direct configuration
2. Using environment variables
3. Processing multiple prompts
4. Error handling
5. Configuration variations for different providers

To run these examples:
1. Install dependencies: pip install -r requirements.txt
2. Update the API keys in the examples above
3. Run: python advanced_example.py

Or modify this file to create your own custom usage!
""")

def main():
    """Main function"""
    print_usage_info()
    
    print("\n" + "="*60)
    print("Note: Examples are shown for demonstration only")
    print("Update API keys and uncomment function calls to run")
    print("="*60)
    
    # Uncomment to run examples (after adding valid API keys):
    # example_basic_usage()
    # example_with_environment()
    # example_multiple_prompts()
    # example_error_handling()
    example_configuration_variations()

if __name__ == "__main__":
    main()
