import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

api_key = os.getenv("OPENAI_API_KEY")  # Get the API key from environment variable

client = openai.OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
