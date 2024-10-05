# kate/get_env.py

import os

def clear_env_vars(*args):
    """
    Clears specified environment variables to reset the environment state.

    Args:
        *args: Environment variable names to clear.
    """
    for var in args:
        os.environ.pop(var, None)

# Step 1: Clear any previously set environment variables (optional)
#clear_env_vars("ORGANIZATION_ID", "OPENAI_PROJECT_ID", "OPENAI_API_KEY")

# Step 2: Directly fetch credentials from the environment without loading .env
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
OPENAI_PROJECT_ID = os.getenv("OPENAI_PROJECT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Step 3: Debugging to ensure variables are loaded correctly
print(f"Kate: Loaded ORGANIZATION_ID: {ORGANIZATION_ID}")
print(f"Kate: Loaded OPENAI_PROJECT_ID: {OPENAI_PROJECT_ID}")
print(f"Kate: Loaded OPENAI_API_KEY: {OPENAI_API_KEY}")

# Step 4: Validate environment variables to ensure they're set
if not ORGANIZATION_ID or not OPENAI_PROJECT_ID or not OPENAI_API_KEY:
    raise EnvironmentError(
        "Please ensure ORGANIZATION_ID, OPENAI_PROJECT_ID, and OPENAI_API_KEY are set in your environment."
    )
