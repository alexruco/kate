# get_env.py

import os
from dotenv import load_dotenv

# Optionally clear existing environment variables
def clear_env_vars(*args):
    for var in args:
        os.environ.pop(var, None)

# Clear specified environment variables before loading new values
clear_env_vars("ORGANIZATION_ID", "OPENAI_PROJECT_ID", "OPENAI_API_KEY")

# Load environment variables from a .env file (optional)
load_dotenv()

# Fetch the credentials and IMAP server from environment variables
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
OPENAI_PROJECT_ID = os.getenv("OPENAI_PROJECT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# You can include defaults or raise errors if any variable is missing
if not ORGANIZATION_ID or not OPENAI_PROJECT_ID or not OPENAI_API_KEY:
    raise EnvironmentError("Please ensure ORGANIZATION_ID, OPENAI_PROJECT_ID, and OPENAI_API_KEY are set in your environment.")