# tests/test_ai_interface.py

import pytest
from kate.interface import AIInterface

@pytest.fixture
def ai_interface():
    """Fixture to initialize the AIInterface."""
    return AIInterface()

def test_send_prompt_openai(monkeypatch, ai_interface):
    """Test sending a prompt using the OpenAI model."""

    # Mock the openai_model function to avoid real API calls
    def mock_openai_model(prompt, org_id, api_key, model, config):
        return "OpenAI response"

    # Correctly mock the openai_model function
    monkeypatch.setattr('kate.interface.openai_model', mock_openai_model)

    model_name = "gpt-3.5-turbo"
    prompt = "Hello, OpenAI!"

    # Call the send_prompt method
    response = ai_interface.send_prompt(prompt, 'openai', model_name)

    # Check that the response matches the mocked return value
    assert response == "OpenAI response"

def test_send_prompt_llamma3(monkeypatch, ai_interface):
    """Test sending a prompt using the LLaMA 3 model."""

    # Mock the llamma3_model function to avoid real command execution
    def mock_llamma3_model(prompt, config):
        return "LLaMA 3 response"

    # Correctly mock the llamma3_model function
    monkeypatch.setattr('kate.interface.llamma3_model', mock_llamma3_model)

    prompt = "Hello, LLaMA 3!"

    # Call the send_prompt method
    response = ai_interface.send_prompt(prompt, 'llamma3')

    # Check that the response matches the mocked return value
    assert response == "LLaMA 3 response"
