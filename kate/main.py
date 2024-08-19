from interface import AIInterface

def get_response(prompt, ai):
    model = ''
    model_version = ''
    
    if ai == 'gpt3':
        model = 'openai'
        model_version = 'gpt-3.5-turbo'
    elif ai == 'llama3':  # Corrected 'llamma3' to 'llama3'
        model = 'llama3'
        model_version = None
            
    ai_interface = AIInterface()
    response = ai_interface.send_prompt(prompt, model, model_version)

    return response

print(get_response('Hello, world!', 'llama3'))  # Corrected 'llamma3' to 'llama3'
print(get_response('Hello, world!', 'gpt3'))
