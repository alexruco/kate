# kate/config.py

import json


class Config:
    def __init__(self, config_path=None):
        self.api_keys = {}
        self.project_ids = {}
        self.configs = {}
        self.organization_id = None
        # Prioritize the provided config path; fall back to the default path if not provided
        if config_path:
            self.load_config(config_path)
        else:
            #linux example
            #self.load_config("/home/ruco/projects/seomaggie/config.json")
            #max example
            self.load_config("/Users/aimaggie.com/projects/aimaggie.com/config.json")

    def load_config(self, config_path):
        """Load API keys, project IDs, organization ID, and configurations from a JSON file."""
        with open(config_path, 'r') as f:
            config_data = json.load(f)
            self.organization_id = config_data.get("organization_id")
            self.api_keys = config_data.get("api_keys", {})
            self.project_ids = config_data.get("project_ids", {})
            self.configs = config_data.get("configs", {})

    def get_organization_id(self):
        """Retrieve the organization ID."""
        return self.organization_id

    def add_api_key(self, model_name, api_key):
        """Add an API key for a specific model."""
        self.api_keys[model_name] = api_key

    def get_api_key(self, model_name):
        """Retrieve the API key for a specific model."""
        return self.api_keys.get(model_name)

    def add_project_id(self, model_name, project_id):
        """Add a Project ID for a specific model."""
        self.project_ids[model_name] = project_id

    def get_project_id(self, model_name):
        """Retrieve the Project ID for a specific model."""
        return self.project_ids.get(model_name)

    def add_config(self, model_name, config):
        """Add configuration for a specific model."""
        self.configs[model_name] = config

    def get_config(self, model_name):
        """Retrieve the configuration for a specific model."""
        return self.configs.get(model_name)
