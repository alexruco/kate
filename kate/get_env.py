import os

# Attempt to load environment variables, with defaulting to None if not set
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
OPENAI_PROJECT_ID = os.getenv("OPENAI_PROJECT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Optional warning only when one of the variables is missing (adjust based on specific requirements)
if not (ORGANIZATION_ID and OPENAI_PROJECT_ID and OPENAI_API_KEY):
    missing_vars = []
    if not ORGANIZATION_ID:
        missing_vars.append("ORGANIZATION_ID")
    if not OPENAI_PROJECT_ID:
        missing_vars.append("OPENAI_PROJECT_ID")
    if not OPENAI_API_KEY:
        missing_vars.append("OPENAI_API_KEY")
    
    if missing_vars:
        print(f"Warning: Missing environment variables: {', '.join(missing_vars)}. Some functionality may be limited.")