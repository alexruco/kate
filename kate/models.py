# kate/models.py

from openai import OpenAI
import subprocess
import logging
import json


logging.basicConfig(level=logging.INFO)


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


def llama3_model(prompt, config=None):
    """Interact with the LLaMA 3 model running locally via Ollama."""
    
    # Construct the command to run the LLaMA 3 model using Ollama
    command = ["ollama", "run", "llama3", prompt]

    # If there are configuration options, pass them as JSON
    if config:
        command.append(json.dumps(config))

    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise Exception(f"LLaMA 3 model request failed: {result.stderr}")
    
    return result.stdout.strip()


def ollama_model(prompt, model_name="llama3", config=None):
    """
    Interact with an Ollama model (LLaMA 3, Phi 3, mistral-nemo, or Gemma 2) running locally.
    
    Parameters:
    - prompt: The input prompt for the model.
    - model_name: The name of the model to run (default is "llama3").
    - config: Optional configuration parameters to pass to the model.
    
    Returns:
    - The model's response.
    """
    # Construct the command to run the specified model using Ollama
    command = ["ollama", "run", model_name, prompt]

    # If there are configuration options, pass them as JSON
    if config:
        command.append(json.dumps(config))

    logging.info(f"Running Ollama model: {model_name}")

    # Run the command and capture the output
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=120)
        result.check_returncode()  # Raises an error if the command fails
    except subprocess.TimeoutExpired:
        logging.error(f"Timeout: Ollama model {model_name} took too long to respond.")
        raise
    except subprocess.CalledProcessError as e:
        logging.error(f"Ollama model {model_name} request failed: {e.stderr}")
        raise Exception(f"Ollama model {model_name} request failed: {e.stderr}")

    return result.stdout.strip()
