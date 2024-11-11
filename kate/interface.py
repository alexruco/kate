# interface.py
from kate.get_env import ORGANIZATION_ID, OPENAI_PROJECT_ID, OPENAI_API_KEY
from kate.models import openai_model, ollama_model

class AIInterface:
    def __init__(self):
        # Directly use environment variables loaded from get_env.py
        self.organization_id = ORGANIZATION_ID
        self.openai_project_id = OPENAI_PROJECT_ID
        self.openai_api_key = OPENAI_API_KEY

    def send_prompt(self, prompt, model_name, model=None, config=None):
        """Send the prompt to the indicated model and return the response."""
        
        if model_name == 'openai':
            # Check if OpenAI-specific environment variables are set
            if not (self.organization_id and self.openai_project_id and self.openai_api_key):
                raise EnvironmentError(
                    "Missing necessary environment variables for OpenAI: ORGANIZATION_ID, OPENAI_PROJECT_ID, or OPENAI_API_KEY."
                )
            if model is None:
                raise ValueError("Model must be specified for OpenAI.")
            
            return openai_model(prompt, self.organization_id, self.openai_api_key, model, config)
        
        elif model_name in ['llama3', 'phi3', 'gemma2', 'gemma2:2b', 'smollm2:135m', 'qwen2.5:latest', 'mistral-nemo:latest']:
            # Ollama models do not require OpenAI environment variables
            return ollama_model(prompt, model_name=model_name, config=config)  # Pass the full model name

        else:
            raise ValueError(f"Model {model_name} is not supported.")