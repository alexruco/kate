# example_usage.py

from kate.interface import AIInterface

# Initialize the interface; it automatically loads the organization ID, API keys, and project IDs from config.json
ai_interface = AIInterface()

# Define the OpenAI model you want to use
model_name_version = "gpt-3.5-turbo"

# Send a prompt to OpenAI
response = ai_interface.send_prompt('Hello, world!', 'openai', model_name_version)
print(response)
