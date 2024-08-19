from kate.interface import AIInterface

def get_response(prompt, ai):
    model = ''
    model_version = ''
    
    if ai == 'llama3':  # Corrected 'llamma3' to 'llama3'
        model = 'llama3'
        model_version = None 
    
    elif ai == 'gpt3':    
        model = 'openai'
        model_version = 'gpt-3.5-turbo'   
     
    elif ai == 'gpt4o-mini':  # Corrected 'llamma3' to 'llama3'
        model = 'openai'
        model_version = 'gpt-4o-mini'

    elif ai == 'gpt4o':  # Corrected 'llamma3' to 'llama3'
        model = 'openai'
        model_version = 'gpt-4o'
    
    elif ai == 'gpt4-turbo':  # Corrected 'llamma3' to 'llama3'
        model = 'openai'
        model_version = 'gpt-4-turbo'
      
            
    ai_interface = AIInterface()
    response = ai_interface.send_prompt(prompt, model, model_version)

    return response

#example usage

prompt = "What is the capital of France?"
ai = "llama3"
response = get_response(prompt, ai)
print(response)
