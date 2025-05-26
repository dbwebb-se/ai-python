import os
from dotenv import load_dotenv
load_dotenv()

from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint=os.getenv("OPENAI_API_ENDPOINT"),
  api_key=os.getenv("OPENAI_API_KEY"),
  api_version="2025-01-01-preview"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Do elephants eat bananas?"},
    ]
)

print(response.choices[0].message.content)

print(response.usage)
