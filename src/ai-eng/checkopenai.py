import openai 
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPEN_AI_KEY")

if not api_key:
    raise ValueError("OPEN_AI_KEY env var is not set")

client = openai.OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user", "content":"Hello, world!"
        }
    ]
    
)

print("Response from OpenAI API:")
print(response.choices[0].message.content)