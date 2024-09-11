# example_usage_llama3.py

from kate.interface import AIInterface

# Initialize the interface
ai_interface = AIInterface()

# Send a prompt to LLaMA 3
# Example using the Phi 3 model
#response = ai_interface.send_prompt(prompt="What is the capital of France?", model_name="phi3")

# Example using the Gemma 2 model
response = ai_interface.send_prompt(prompt="Tell me a story.", model_name="gemma2")
print(response)
