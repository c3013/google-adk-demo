#!/usr/bin/env python3
"""
Example: Using Google ADK with local Ollama models

This example demonstrates how to use the Google ADK demo with
Ollama, a tool for running large language models locally.

Prerequisites:
1. Install Ollama: https://ollama.ai
2. Pull a model: ollama pull llama2
3. Start Ollama server: ollama serve (usually auto-starts)

Usage:
    python examples/ollama_example.py
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from demo import OpenSourceModelDemo


def main():
    """Main function for Ollama example"""
    
    print("="*60)
    print("Google ADK Demo - Ollama Local Model Example")
    print("="*60)
    
    # Configuration for local Ollama
    # Ollama typically runs on http://localhost:11434
    # The API_KEY can be any dummy value for local usage
    api_key = "ollama"  # Dummy key for local usage
    base_url = "http://localhost:11434/v1"
    model = "llama2"  # or llama2:7b, mistral, codellama, etc.
    
    print(f"\nConfiguration:")
    print(f"  API Key: {api_key} (dummy for local)")
    print(f"  Base URL: {base_url}")
    print(f"  Model: {model}")
    print(f"\nNote: Make sure Ollama is running!")
    print(f"  - Install: https://ollama.ai")
    print(f"  - Pull model: ollama pull {model}")
    print(f"  - Check status: ollama list")
    
    # Create demo instance
    demo = OpenSourceModelDemo(api_key, base_url, model)
    
    # Initialize client
    print("\nInitializing client...")
    if not demo.initialize_client():
        print("\n✗ Failed to initialize client.")
        print("\nTroubleshooting:")
        print("  1. Check if Ollama is running: curl http://localhost:11434/api/tags")
        print("  2. Verify the model is installed: ollama list")
        print("  3. Try pulling the model: ollama pull llama2")
        sys.exit(1)
    
    # Example 1: Simple question
    print("\n" + "="*60)
    print("Example 1: Simple Question")
    print("="*60)
    demo.generate_text(
        "What are the benefits of running LLMs locally?",
        max_tokens=200
    )
    
    # Example 2: Code generation
    print("\n" + "="*60)
    print("Example 2: Code Generation")
    print("="*60)
    demo.generate_text(
        "Write a Python function to read a JSON file and return a dictionary",
        max_tokens=150
    )
    
    # Example 3: Explain a concept
    print("\n" + "="*60)
    print("Example 3: Concept Explanation")
    print("="*60)
    demo.generate_text(
        "Explain what Ollama is and why it's useful for developers",
        max_tokens=200
    )
    
    # Offer interactive mode
    print("\n" + "="*60)
    response = input("Would you like to start an interactive chat? (y/n): ").strip().lower()
    if response == 'y':
        demo.chat_session()
    
    print("\n" + "="*60)
    print("Example completed!")
    print("="*60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExample interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
