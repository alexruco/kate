# kate/__init__.py

"""
Kate AI Interface
==================
This package provides an interface to interact with various AI models, including OpenAI and LLaMA 3 via Ollama.

Modules:
---------
- config: Handles loading and managing API keys, project IDs, and other configurations.
- interface: Provides a high-level interface for sending prompts to different AI models.
- models: Contains functions to interact with specific AI models (e.g., OpenAI, LLaMA 3).
"""
import sys
from os import path

# Ensure that the parent directory is in the system path
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '..')))

from kate.interface import AIInterface
from kate.models import openai_model, llama3_model
from kate.main import get_response

__all__ = [
    "AIInterface",
    "openai_model",
    "llama3_model",
    "get_response"
]
