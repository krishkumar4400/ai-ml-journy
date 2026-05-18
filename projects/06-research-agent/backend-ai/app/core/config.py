import os

from dotenv import load_dotenv

# -----------------------------------
# Load ENV
# -----------------------------------

load_dotenv()

# -----------------------------------
# Environment Variables
# -----------------------------------

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
