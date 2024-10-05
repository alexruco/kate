# get_env.py
import os
from dotenv import load_dotenv

def clear_env_vars(*args):
    for var in args:
        os.environ.pop(var, None)

clear_env_vars("ORGANIZATION_ID", "OPENAI_PROJECT_ID", "OPENAI_API_KEY")

# Explicitly specify the path to the `.env` file if necessary
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(env_path)  # Use the env_path to ensure it loads from the root directory

# Fetch credentials from environment variables
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
OPENAI_PROJECT_ID = os.getenv("OPENAI_PROJECT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Debugging to ensure variables are loaded correctly
print("Loaded ORGANIZATION_ID:", ORGANIZATION_ID)
print("Loaded OPENAI_PROJECT_ID:", OPENAI_PROJECT_ID)
print("Loaded OPENAI_API_KEY:", OPENAI_API_KEY)

if not ORGANIZATION_ID or not OPENAI_PROJECT_ID or not OPENAI_API_KEY:
    raise EnvironmentError("Please ensure ORGANIZATION_ID, OPENAI_PROJECT_ID, and OPENAI_API_KEY are set in your environment.")
