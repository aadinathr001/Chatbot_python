# Groq Chatbot

A simple Python project that connects to Groq's API using the OpenAI-compatible client and sends a basic prompt to an LLM.

## Overview

This project is a minimal example of how to:

- load a Groq API key from environment variables
- create a client using Groq's OpenAI-compatible endpoint
- send a prompt to a Groq-hosted model
- print the generated response

## Project Files

- `test.py` - the main script that calls the Groq API
- `groq_api_models.json` - a JSON list of available Groq models
- `.env` - environment file for your API key (not committed to Git in most cases)

## Requirements

Install the required Python packages:

```bash
pip install python-dotenv openai
```

## Setup

1. Create a `.env` file in the project root.
2. Add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

3. Run the script:

```bash
python test.py
```

## Example Output

The script sends:

```text
hi
```

and prints the model response text.

## Notes

- This project is a starter example, not a full chatbot interface.
- It uses the Groq endpoint under the OpenAI-compatible API format.
- You can replace the model name with another available Groq model from `groq_api_models.json`.

## License

This project is for learning and experimentation.
