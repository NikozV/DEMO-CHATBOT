import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY", None)
