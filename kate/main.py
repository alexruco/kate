# kate/main.py
from interface import AIInterface

def get_response(prompt, ai):
    model = ''
    model_version = None  # Set model_version to None by default for simplification
    
    # Treating each AI model as distinct, including 'gemma2:2b'
    if ai in ['llama3', 'phi3', 'gemma2', 'gemma2:2b']:  
        model = ai  # Use the full model name as provided
    
    elif ai == 'gpt3':
        model = 'openai'
        model_version = 'gpt-3.5-turbo'
    
    elif ai == 'gpt4o-mini':
        model = 'openai'
        model_version = 'gpt-4o-mini'

    elif ai == 'gpt4o':
        model = 'openai'
        model_version = 'gpt-4o'
    
    elif ai == 'gpt4-turbo':
        model = 'openai'
        model_version = 'gpt-4-turbo'
    
    else:
        raise ValueError(f"AI model '{ai}' is not supported.")
            
    ai_interface = AIInterface()
    response = ai_interface.send_prompt(prompt, model, model_version)

    return response

# Example usage

prompt = "What is the capital of France?"
ai = "gemma2:2b"  # Treat 'gemma2:2b' as a distinct model
response = get_response(prompt, ai)
print(response)
