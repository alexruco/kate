import os

# Attempt to load environment variables, defaulting to None if not set
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
OPENAI_PROJECT_ID = os.getenv("OPENAI_PROJECT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Print a warning if any of the required OpenAI environment variables are missing
# No error is raised here; they are simply left as None if not provided
missing_vars = []
if not ORGANIZATION_ID:
    missing_vars.append("ORGANIZATION_ID")
if not OPENAI_PROJECT_ID:
    missing_vars.append("OPENAI_PROJECT_ID")
if not OPENAI_API_KEY:
    missing_vars.append("OPENAI_API_KEY")

if missing_vars:
    print(f"Warning: Missing environment variables: {', '.join(missing_vars)}. OpenAI functionality may be limited.")