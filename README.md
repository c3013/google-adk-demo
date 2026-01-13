# Google ADK Python Demo - Open Source Models

This project demonstrates how to use Google's ADK (Application Development Kit) with Python to call open-source models with configurable parameters.

## Features

- ✅ Support for custom model configuration
- ✅ Configurable API key and base URL
- ✅ Multiple ways to provide configuration (environment variables, command line, config file)
- ✅ Interactive chat session
- ✅ Example demonstrations (text generation, code generation, Q&A)
- ✅ Compatible with OpenAI-compatible APIs and open-source models
- ✅ Dual mode: Google SDK for Google models, HTTP mode for custom endpoints

## How It Works

The demo intelligently selects the best method to communicate with your chosen model:

- **Google SDK Mode**: When connecting to Google's Generative AI API, it uses the official Google SDK
- **HTTP Mode**: For custom endpoints (OpenAI, Ollama, LM Studio, etc.), it uses direct HTTP calls compatible with the OpenAI API format

This hybrid approach ensures maximum compatibility with any API endpoint!

## Installation

1. Clone this repository:
```bash
git clone https://github.com/c3013/google-adk-demo.git
cd google-adk-demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

You can configure the demo in three ways:

### Method 1: Environment Variables (.env file)

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
API_KEY=your_api_key_here
BASE_URL=https://api.example.com/v1
MODEL=gpt-3.5-turbo
```

### Method 2: Command Line Arguments

```bash
python demo.py <api_key> <base_url> <model>
```

Example:
```bash
python demo.py sk-xxx https://api.openai.com/v1 gpt-3.5-turbo
```

### Method 3: Configuration File

Edit `config.yaml` with your settings (for future enhancement).

## Usage

### Run the Demo

Using environment variables:
```bash
python demo.py
```

Using command line arguments:
```bash
python demo.py your_api_key https://api.example.com/v1 gpt-3.5-turbo
```

### Example Output

The demo will:
1. Initialize the Google ADK client with your configuration
2. Run example demonstrations:
   - Simple text generation
   - Code generation
   - Question answering
3. Optionally start an interactive chat session

## Supported Models

This demo works with any OpenAI-compatible API, including:

- **OpenAI**: gpt-3.5-turbo, gpt-4, etc.
- **Open Source Models via compatible APIs**:
  - Llama 2
  - Mistral
  - Mixtral
  - CodeLlama
  - Vicuna
  - And more...

- **Local LLM Servers**:
  - Ollama
  - LM Studio
  - LocalAI
  - Text Generation WebUI

## Example Configurations

### OpenAI
```env
API_KEY=sk-xxxxxxxxxxxxxxxx
BASE_URL=https://api.openai.com/v1
MODEL=gpt-3.5-turbo
```

### Local Ollama
```env
API_KEY=dummy_key
BASE_URL=http://localhost:11434/v1
MODEL=llama2
```

### Hugging Face Inference API
```env
API_KEY=hf_xxxxxxxxxxxxxxxx
BASE_URL=https://api-inference.huggingface.co/models
MODEL=mistralai/Mistral-7B-Instruct-v0.1
```

## Project Structure

```
google-adk-demo/
├── demo.py              # Main demo script
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment configuration
├── config.yaml          # Example YAML configuration
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Code Structure

The `demo.py` script contains:

- `OpenSourceModelDemo` class: Main demo class with methods for:
  - `initialize_client()`: Initialize Google ADK client
  - `generate_text()`: Generate text using the model
  - `chat_session()`: Interactive chat session
- Configuration loading from multiple sources
- Example demonstrations
- Interactive mode

## Features in Detail

### Text Generation
```python
demo.generate_text("What is artificial intelligence?", max_tokens=150)
```

### Interactive Chat
The demo includes an interactive chat session where you can have a conversation with the model:
```
You: Hello!
Assistant: Hi there! How can I help you today?
```

Type `quit` or `exit` to end the chat session.

## Requirements

- Python 3.8+
- google-genai >= 0.2.0
- python-dotenv >= 1.0.0
- pyyaml >= 6.0

## Error Handling

The demo includes comprehensive error handling for:
- Missing configuration
- Client initialization failures
- API call errors
- Network issues

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

## Acknowledgments

- Google ADK team for the SDK
- Open source LLM community
