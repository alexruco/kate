# tests/test_models.py

import pytest
from kate.models import openai_model, other_model

def test_openai_model(monkeypatch):
    """Test the openai_model function."""

    # Mock the requests.post method to simulate an API response
    class MockResponse:
        def json(self):
            return {"choices": [{"message": {"content": "Mocked response from OpenAI"}}]}

    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)

    # Call the openai_model function with mock data
    api_key = "fake-api-key"
    prompt = "Hello, world!"
    response = openai_model(prompt, api_key)

    # Assert that the mocked response is returned
    assert response["choices"][0]["message"]["content"] == "Mocked response from OpenAI"

def test_other_model():
    """Test the other_model function."""

    # Call the other_model function with mock data
    api_key = "fake-api-key"
    prompt = "Hello, world!"
    response = other_model(prompt, api_key)

    # Assert that the mocked response is correct
    assert response["response"] == "This is a response from another model."
