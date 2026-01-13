#!/usr/bin/env python3
"""
Google ADK Python Demo - Open Source Models
This demo shows how to call open-source models with configurable
model, api_key, and base_url parameters.

This implementation supports two modes:
1. Direct HTTP API calls for maximum compatibility
2. Google genai SDK for Google models

For open-source models via custom endpoints (Ollama, LM Studio, etc.),
it uses direct HTTP requests which work with any OpenAI-compatible API.
"""

import os
import sys
import json
import requests
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Try to import Google SDK (optional)
HAS_GOOGLE_SDK = False
try:
    from google import genai
    from google.genai import types
    HAS_GOOGLE_SDK = True
except ImportError:
    pass  # Will use HTTP mode for all requests


class OpenSourceModelDemo:
    """Demo class for calling open-source models with custom endpoints"""
    
    def __init__(self, api_key: str, base_url: str, model: str):
        """
        Initialize the demo with configuration
        
        Args:
            api_key: API key for authentication
            base_url: Base URL for the API endpoint (e.g., https://api.openai.com/v1)
            model: Model name to use (e.g., gpt-3.5-turbo, llama2, etc.)
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')  # Remove trailing slash
        self.model = model
        self.client = None
        self.use_google_sdk = False
        
    def initialize_client(self):
        """Initialize the client based on the base URL"""
        try:
            # Check if using Google's API
            if 'generativelanguage.googleapis.com' in self.base_url and HAS_GOOGLE_SDK:
                self.use_google_sdk = True
                self.client = genai.Client(api_key=self.api_key)
                print(f"✓ Client initialized successfully (Google SDK mode)")
            else:
                # Use HTTP mode for open-source models and custom endpoints
                self.use_google_sdk = False
                print(f"✓ Client initialized successfully (HTTP mode)")
            
            print(f"  Model: {self.model}")
            print(f"  Base URL: {self.base_url}")
            print(f"  API Key: {self.api_key[:10]}..." if len(self.api_key) > 10 else "  API Key: ***")
            return True
        except Exception as e:
            print(f"✗ Failed to initialize client: {e}")
            print(f"\nNote: Make sure your base_url is correct and accessible")
            print(f"Current base_url: {self.base_url}")
            return False
    
    def _generate_with_http(self, prompt: str, max_tokens: int) -> Optional[str]:
        """Generate text using direct HTTP API calls (OpenAI-compatible)"""
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(url, headers=headers, json=data, timeout=60)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"HTTP request failed to {url}: {str(e)}")
        
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        else:
            raise ValueError(f"Unexpected API response format. Expected 'choices' field but got: {list(result.keys())}")
    
    def _generate_with_google_sdk(self, prompt: str, max_tokens: int) -> Optional[str]:
        """Generate text using Google SDK"""
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=max_tokens,
                temperature=0.7,
            )
        )
        return response.text
    
    def generate_text(self, prompt: str, max_tokens: int = 100) -> Optional[str]:
        """
        Generate text using the configured model
        
        Args:
            prompt: The input prompt
            max_tokens: Maximum tokens to generate
            
        Returns:
            Generated text or None if failed
        """
        try:
            print(f"\n{'='*60}")
            print(f"Prompt: {prompt}")
            print(f"{'='*60}")
            
            # Generate content using the appropriate method
            if self.use_google_sdk and self.client:
                result = self._generate_with_google_sdk(prompt, max_tokens)
            else:
                result = self._generate_with_http(prompt, max_tokens)
            
            print(f"\nResponse:\n{result}")
            print(f"{'='*60}\n")
            
            return result
        except Exception as e:
            print(f"✗ Error generating text: {e}")
            print(f"\nTroubleshooting:")
            print(f"  1. Check if the API endpoint is accessible")
            print(f"  2. Verify your API key is correct")
            print(f"  3. Ensure the model name is valid for your endpoint")
            return None
    
    def chat_session(self):
        """Start an interactive chat session"""
        print("\n" + "="*60)
        print("Interactive Chat Session")
        print("Type 'quit' or 'exit' to end the session")
        print("="*60 + "\n")
        
        history = []
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['quit', 'exit']:
                    print("Ending chat session...")
                    break
                
                if not user_input:
                    continue
                
                # Generate response using the appropriate method
                if self.use_google_sdk and self.client:
                    response = self.client.models.generate_content(
                        model=self.model,
                        contents=user_input,
                        config=types.GenerateContentConfig(
                            max_output_tokens=200,
                            temperature=0.7,
                        )
                    )
                    assistant_response = response.text
                else:
                    # Use HTTP mode
                    assistant_response = self._generate_with_http(user_input, 200)
                
                if assistant_response:
                    print(f"Assistant: {assistant_response}\n")
                    history.append({"role": "user", "content": user_input})
                    history.append({"role": "assistant", "content": assistant_response})
                else:
                    print("✗ Failed to get response\n")
                
            except KeyboardInterrupt:
                print("\n\nChat session interrupted.")
                break
            except Exception as e:
                print(f"✗ Error in chat: {e}\n")


def load_config_from_env():
    """Load configuration from environment variables"""
    load_dotenv()
    
    api_key = os.getenv('API_KEY')
    base_url = os.getenv('BASE_URL')
    model = os.getenv('MODEL')
    
    return api_key, base_url, model


def load_config_from_args():
    """Load configuration from command line arguments"""
    if len(sys.argv) < 4:
        return None, None, None
    
    return sys.argv[1], sys.argv[2], sys.argv[3]


def print_usage():
    """Print usage information"""
    print("""
Google ADK Python Demo - Open Source Models

Usage:
  1. Using environment variables (.env file):
     python demo.py
     
  2. Using command line arguments:
     python demo.py <api_key> <base_url> <model>

Example:
  python demo.py sk-xxx https://api.openai.com/v1 gpt-3.5-turbo

Configuration via .env file:
  Create a .env file with the following content:
    API_KEY=your_api_key_here
    BASE_URL=https://api.example.com/v1
    MODEL=gpt-3.5-turbo

Supported open-source models (depends on your API endpoint):
  - gpt-3.5-turbo
  - gpt-4
  - llama-2-7b
  - mistral-7b
  - Any model supported by your API endpoint
""")


def run_examples(demo: OpenSourceModelDemo):
    """Run example demonstrations"""
    print("\n" + "="*60)
    print("Running Example Demonstrations")
    print("="*60)
    
    # Example 1: Simple text generation
    print("\n1. Simple Text Generation")
    demo.generate_text("What is artificial intelligence?", max_tokens=150)
    
    # Example 2: Code generation
    print("\n2. Code Generation")
    demo.generate_text("Write a Python function to calculate fibonacci numbers", max_tokens=200)
    
    # Example 3: Question answering
    print("\n3. Question Answering")
    demo.generate_text("Explain the difference between machine learning and deep learning", max_tokens=150)


def main():
    """Main function"""
    print("="*60)
    print("Google ADK Python Demo - Open Source Models")
    print("="*60)
    
    # Try loading from command line arguments first
    api_key, base_url, model = load_config_from_args()
    
    # If not provided via args, try environment variables
    if not all([api_key, base_url, model]):
        api_key, base_url, model = load_config_from_env()
    
    # Validate configuration
    if not all([api_key, base_url, model]):
        print("\n✗ Missing configuration!")
        print("  Please provide API_KEY, BASE_URL, and MODEL")
        print_usage()
        sys.exit(1)
    
    # Create demo instance
    demo = OpenSourceModelDemo(api_key, base_url, model)
    
    # Initialize client
    if not demo.initialize_client():
        sys.exit(1)
    
    # Run examples
    try:
        run_examples(demo)
        
        # Ask if user wants to start interactive chat
        print("\n" + "="*60)
        response = input("Would you like to start an interactive chat session? (y/n): ").strip().lower()
        if response == 'y':
            demo.chat_session()
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\n✗ Error running demo: {e}")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("Demo completed successfully!")
    print("="*60)


if __name__ == "__main__":
    main()
