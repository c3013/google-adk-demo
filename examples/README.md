# Examples Directory

This directory contains various examples demonstrating different use cases of the Google ADK demo with open-source models.

## Available Examples

1. **ollama_example.py** - Example using local Ollama models

## How to Use

Each example is self-contained and can be run independently:

```bash
# Set your configuration
export API_KEY=your_key
export BASE_URL=your_url
export MODEL=your_model

# Run an example
python examples/ollama_example.py
```

Or provide configuration directly in the script.

## Creating Your Own Example

Copy any example file and modify it for your use case:

```bash
cp examples/ollama_example.py examples/my_example.py
# Edit my_example.py with your custom logic
python examples/my_example.py
```
