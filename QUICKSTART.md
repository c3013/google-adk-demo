# Google ADK Python Demo - Quick Start Guide

## What is this demo?

This demo shows how to use Google's Generative AI SDK (ADK) to call open-source models or any OpenAI-compatible API with custom configuration.

## Quick Start (3 steps)

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure your API

Create a `.env` file with your configuration:

```bash
cp .env.example .env
```

Edit `.env`:
```env
API_KEY=your_api_key_here
BASE_URL=https://api.example.com/v1
MODEL=gpt-3.5-turbo
```

### Step 3: Run the demo

```bash
python demo.py
```

## What does the demo do?

1. **Initializes Google ADK client** with your custom configuration
2. **Runs three examples**:
   - Text generation: "What is artificial intelligence?"
   - Code generation: "Write a Python function for fibonacci"
   - Q&A: "Explain ML vs Deep Learning"
3. **Offers interactive chat** where you can ask questions

## Alternative: Use command line arguments

Skip the `.env` file and provide configuration directly:

```bash
python demo.py YOUR_API_KEY https://api.example.com/v1 gpt-3.5-turbo
```

## Simple Example

Want something even simpler? Check `simple_example.py`:

```python
from google import genai

client = genai.Client(api_key="your_key")
response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents="Write a haiku about coding"
)
print(response.text)
```

Run it:
```bash
python simple_example.py
```

## Supported APIs

This demo works with any OpenAI-compatible API endpoint:

### Cloud APIs
- OpenAI (https://api.openai.com/v1)
- Azure OpenAI
- Anthropic Claude (via compatibility layer)
- Google Gemini (via Google ADK)

### Local/Open Source
- **Ollama** (http://localhost:11434/v1)
  - Run: `ollama serve`
  - Models: llama2, mistral, codellama, etc.
  
- **LM Studio** (http://localhost:1234/v1)
  - Great GUI for running local models
  
- **LocalAI** (http://localhost:8080/v1)
  - Self-hosted OpenAI alternative
  
- **Text Generation WebUI** (http://localhost:5000/v1)
  - Feature-rich local LLM interface

## Configuration Examples

### Example 1: OpenAI
```env
API_KEY=sk-proj-xxxxxxxxxxxxx
BASE_URL=https://api.openai.com/v1
MODEL=gpt-3.5-turbo
```

### Example 2: Local Ollama (Free!)
```env
API_KEY=dummy_key
BASE_URL=http://localhost:11434/v1
MODEL=llama2
```

First, install and run Ollama:
```bash
# Install Ollama from https://ollama.ai
ollama pull llama2
ollama serve
```

### Example 3: Google Gemini
```env
API_KEY=your_google_api_key
BASE_URL=https://generativelanguage.googleapis.com/v1beta
MODEL=gemini-2.0-flash-exp
```

Get API key from: https://ai.google.dev/

## Troubleshooting

### "Missing configuration" error
- Make sure your `.env` file exists and has all three variables
- Or provide all three command line arguments

### "Client initialization failed"
- Check your API key is correct
- Verify the BASE_URL is reachable
- Test with: `curl <BASE_URL>/models`

### "Model not found"
- Ensure the model name matches what's available at your endpoint
- For Ollama: `ollama list` to see available models
- For OpenAI: Check their documentation for model names

### Import errors
- Make sure you ran: `pip install -r requirements.txt`
- Use a virtual environment if needed:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

## Next Steps

1. Try the demo with different models
2. Experiment with the interactive chat mode
3. Modify the examples in `demo.py` for your use case
4. Build your own application using this as a template

## Learn More

- Google ADK Documentation: https://ai.google.dev/
- OpenAI API Documentation: https://platform.openai.com/docs
- Ollama: https://ollama.ai
- LocalAI: https://localai.io

## Need Help?

- Check existing issues on GitHub
- Open a new issue with your question
- Include error messages and your configuration (remove API keys!)
