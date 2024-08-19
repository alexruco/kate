# tests/test_ai_interface.py

import pytest
from unittest.mock import patch, MagicMock
from kate.interface import AIInterface
from kate.main import get_response

class TestAIInterface:
    @patch('kate.interface.Config')  # Ensure correct path to Config class
    def test_initialization(self, mock_config):
        # Test AIInterface initialization
        ai_interface = AIInterface()
        mock_config.assert_called_once_with(None)  # Ensure Config was initialized correctly

   # tests/test_ai_interface.py

    @patch('kate.interface.openai_model')  # Correct the path to the function being mocked
    @patch('kate.interface.Config')
    def test_send_prompt_openai(self, mock_config, mock_openai_model):
        # Test sending prompt to OpenAI model
        mock_config.return_value.get_organization_id.return_value = 'test_org_id'
        mock_config.return_value.get_api_key.return_value = 'test_api_key'
        mock_config.return_value.get_config.return_value = None  # Ensure config is None

        ai_interface = AIInterface()
        ai_interface.send_prompt('Hello, world!', 'openai', 'gpt-3.5-turbo')

        mock_openai_model.assert_called_once_with('Hello, world!', 'test_org_id', 'test_api_key', 'gpt-3.5-turbo', None)

    @patch('kate.interface.llama3_model')  # Correct the path to the function being mocked
    def test_send_prompt_llama3(self, mock_llama3_model):
        # Test sending prompt to LLaMA 3 model
        ai_interface = AIInterface()
        ai_interface.send_prompt('Hello, world!', 'llama3')
    
        mock_llama3_model.assert_called_once_with('Hello, world!', None)

    def test_send_prompt_invalid_model(self):
        # Test sending prompt to an unsupported model
        ai_interface = AIInterface()
        with pytest.raises(ValueError) as exc_info:
            ai_interface.send_prompt('Hello, world!', 'invalid_model')
        
        assert str(exc_info.value) == "Model invalid_model is not supported."

