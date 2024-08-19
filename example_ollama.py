# example_usage_llama3.py

from kate.interface import AIInterface

# Initialize the interface
ai_interface = AIInterface()

# Send a prompt to LLaMA 3
response = ai_interface.send_prompt('Hello, world!', 'llamma3',None)
print(response)
