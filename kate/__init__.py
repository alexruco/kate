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

from .config import Config
from .interface import AIInterface
from .models import openai_model, llama3_model

__all__ = [
    "Config",
    "AIInterface",
    "openai_model",
    "llama3_model"
]
