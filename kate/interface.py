# kate/interface.py
from config import Config
from models import openai_model, ollama_model

class AIInterface:
    def __init__(self, config_path=None):
        self.config = Config(config_path)

    def add_model(self, model_name, project_id=None, api_key=None, config=None):
        """Add a new model with its Project ID, API key, and optional config."""
        if project_id:
            self.config.add_project_id(model_name, project_id)
        if api_key:
            self.config.add_api_key(model_name, api_key)
        if config:
            self.config.add_config(model_name, config)

    def send_prompt(self, prompt, model_name, model=None, config=None):
        """Send the prompt to the indicated model and return the response."""
        if model_name == 'openai':
            organization_id = self.config.get_organization_id()
            api_key = self.config.get_api_key(model_name)
            config = config or self.config.get_config(model_name)
            if model is None:
                raise ValueError("Model must be specified for OpenAI.")
            return openai_model(prompt, organization_id, api_key, model, config)
        
        # Add support for gemma2:2b and other Ollama models
        elif model_name in ['llama3', 'phi3', 'gemma2', 'gemma2:2b']:
            return ollama_model(prompt, model_name=model_name, config=config)  # Pass the full model name
        
        else:
            raise ValueError(f"Model {model_name} is not supported.")
