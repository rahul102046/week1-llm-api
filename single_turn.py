import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

response = client.chat.completions.create(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of Australia?"
        }
    ]
)

print("\nFULL RESPONSE:\n")
print(response)

print("\nANSWER:\n")
print(response.choices[0].message.content)

print("\nUSAGE:\n")
print(response.usage)