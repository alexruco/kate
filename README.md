# kate - AI Interface 🚀

Welcome to **kate**! This project is designed to provide a seamless interface to interact with various AI models, including OpenAI and LLaMA 3 via Ollama. It centralizes API keys, configurations, and offers a simple function to send prompts to your chosen model and return the response, all in one place.

## Features ✨

- **Multi-Model Support**: Easily switch between different AI models like OpenAI and LLaMA 3 by specifying the model name in your prompts. 🎉
- **Centralized Configuration**: Store and manage your API keys, project IDs, and other configurations in one place, reducing the need for repetitive setup in your code. 🔥
- **Simple Interface**: Send a prompt and receive a response with just one function call, making it easy to integrate AI models into your projects. 🌟

## Installation 💻

You can install the package via pip:

```bash
pip install GIT+https://github.com/alexruco/kate

```
## Configuration 🔧

By default, this package uses a centralized configuration file located at:

/Users/aimaggie.com/projects/aimaggie.com/kate/config.json

Important: This path is hardcoded in the package. If you wish to change the location of the configuration file, you must modify the Config class in kate/config.py. Alternatively, you can provide a custom configuration path when initializing the AIInterface:

```python
from kate.interface import AIInterface

# Example: Using a custom configuration file path
ai_interface = AIInterface(config_path="/path/to/your/custom/config.json")

```

Make sure your config.json file contains the necessary API keys, project IDs, and other configurations needed by the models you intend to use.

Here's an example of what your config.json file should look like:

```json
{
    "openai": {
        "api_key": "your-openai-api-key",
        "project_id": "your-openai-project-id",
        "organization_id": "your-openai-organization-id"
    }
}

```

## Usage 📚

Here's a quick example to get you started:

```python
from kate.interface import AIInterface

# Initialize the interface; it automatically loads the organization ID, API keys, and project IDs from config.json
ai_interface = AIInterface()

# Define the OpenAI model you want to use
model_name = "gpt-3.5-turbo"

# Send a prompt to OpenAI and print the response
response = ai_interface.send_prompt('Hello, world!', 'openai', model_name)
print(response)

# Or send a prompt to LLaMA 3 via Ollama
response = ai_interface.send_prompt('Hello, world!', 'llamma3')
print(response)
```

## Running Tests 🧪

To run the tests, you can use the unittest module or pytest.

```python
python -m unittest discover tests
# or
pytest
```

## Contributing 🤝

We welcome contributions from the community! Here’s how you can get involved:

    Report Bugs: If you find a bug, please open an issue here.
    Suggest Features: We’d love to hear your ideas! Suggest new features by opening an issue.
    Submit Pull Requests: Ready to contribute? Fork the repo, make your changes, and submit a pull request. Please ensure your code follows our coding standards and is well-documented.
    Improve Documentation: Help us improve our documentation. Feel free to make edits or add new content.

How to Submit a Pull Request

    Fork the repository.
    Create a new branch: git checkout -b my-feature-branch.
    Make your changes and commit them: git commit -m 'Add some feature'.
    Push to the branch: git push origin my-feature-branch.
    Open a pull request on the original repository.

## License 📄

This project is licensed under the MIT License. Feel free to use, modify, and distribute this software in accordance with the terms outlined in the LICENSE file.