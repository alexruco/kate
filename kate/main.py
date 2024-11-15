# kate/main.py
from kate.interface import AIInterface

def get_response(prompt, ai):
    model = ''
    model_version = None  # Set model_version to None by default for simplification
    
    # Treating each AI model as distinct, including 'gemma2:2b'
    if ai in ['llama3', 'phi3', 'gemma2', 'gemma2:2b','gemma2:latest','smollm2:135m','qwen2.5:latest', 'mistral-nemo:latest']:  
        model = ai  # Use the full model name as providedp
    
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

#prompt = "What is the capital of France?"

# Comment/uncomment the line below to switch between AI models
#ai = "gemma2:2b"  # Option 1: Treat 'gemma2:2b' as a distinct model
#ai = "phi3"      # Option 2: Use 'phi3'
#ai = "gpt3"      # Option 3: Use GPT-3
# ai = "gpt4o"     # Option 4: Use GPT-4
# ai = "gpt4-turbo" # Option 5: Use GPT-4 Turbo

#response = get_response(prompt, ai)
#print(response)
