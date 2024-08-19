# tests/test_models.py

from unittest.mock import patch, MagicMock
from kate.models import openai_model

def test_openai_model():
    """Test the openai_model function."""

    # Mock the response from OpenAI's API
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "choices": [{"message": {"content": "Mocked response from OpenAI"}}]
    }

    # Patch the `httpx.Client.request` method used internally by OpenAI's API client
    with patch("httpx.Client.request", return_value=mock_response) as mock_request:
        # Call the openai_model function with mock data
        prompt = "Hello, world!"
        organization_id = "fake-org-id"
        api_key = "fake-api-key"
        model = "gpt-3.5-turbo"
        response = openai_model(prompt, organization_id, api_key, model)
        
        # Check that the response is as expected
        assert response == "Mocked response from OpenAI"

        # Ensure the API call was made
        mock_request.assert_called_once()
