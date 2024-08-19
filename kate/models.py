# kate/models.py

from openai import OpenAI
import subprocess
import json

def openai_model(prompt, organization_id, api_key, model, config=None):
    """Interact with OpenAI's API using the updated Python client."""
    
    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Send the request to the OpenAI API
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        **(config or {})
    )

    # Extract and return the message content from the response
    return response.choices[0].message.content


def llamma3_model(prompt, config=None):
    """Interact with the LLaMA 3 model running locally via Ollama."""
    
    # Construct the command to run the LLaMA 3 model using Ollama
    command = ["ollama", "run", "llama3", prompt]

    # If there are configuration options, pass them as JSON, including max_tokens if provided
    if config:
        command += ["--config", json.dumps(config)]

    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise Exception(f"LLaMA 3 model request failed: {result.stderr}")
    
    # Return the model's response
    return result.stdout.strip()
