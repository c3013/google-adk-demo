#!/usr/bin/env python3
"""
Simple example of using Google ADK with open-source models
This is a minimal example to get started quickly

Note: This example uses the google-genai SDK. For custom endpoints
(open-source models, Ollama, etc.), use the full demo.py script.
"""

import os

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Error: google-genai not installed")
    print("Install it with: pip install google-genai")
    exit(1)

def simple_example():
    """
    Simple example showing basic usage
    """
    # Configuration
    api_key = "your_api_key_here"  # Replace with your actual API key
    model = "gemini-2.0-flash-exp"  # Replace with your model name
    
    # You can also get from environment variables
    # api_key = os.getenv('API_KEY')
    # model = os.getenv('MODEL', 'gemini-2.0-flash-exp')
    
    # Initialize client
    client = genai.Client(api_key=api_key)
    
    # Generate content
    prompt = "Write a haiku about coding"
    
    print(f"Prompt: {prompt}\n")
    
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=100,
            temperature=0.7,
        )
    )
    
    print(f"Response:\n{response.text}")

if __name__ == "__main__":
    simple_example()
