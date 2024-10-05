# interface.py
from kate.get_env import ORGANIZATION_ID, OPENAI_PROJECT_ID, OPENAI_API_KEY
from kate.models import openai_model, ollama_model

class AIInterface:
    def __init__(self):
        # Directly use environment variables loaded from get_env.py
        self.organization_id = ORGANIZATION_ID
        self.openai_project_id = OPENAI_PROJECT_ID
        self.openai_api_key = OPENAI_API_KEY

        # Ensure required environment variables are available
        if not self.organization_id or not self.openai_project_id or not self.openai_api_key:
            raise EnvironmentError("Missing necessary environment variables: ORGANIZATION_ID, OPENAI_PROJECT_ID, or OPENAI_API_KEY.")

    def send_prompt(self, prompt, model_name, model=None, config=None):
        """Send the prompt to the indicated model and return the response."""
        if model_name == 'openai':
            # Use organization ID and API key from environment
            if model is None:
                raise ValueError("Model must be specified for OpenAI.")
            return openai_model(prompt, self.organization_id, self.openai_api_key, model, config)
        
        # Add support for gemma2:2b and other Ollama models
        elif model_name in ['llama3', 'phi3', 'gemma2', 'gemma2:2b']:
            return ollama_model(prompt, model_name=model_name, config=config)  # Pass the full model name
        
        else:
            raise ValueError(f"Model {model_name} is not supported.")
