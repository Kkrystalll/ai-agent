from config import OPEN_API_KEY
from openai import OpenAI
client = OpenAI(api_key=OPEN_API_KEY)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "早安"},
    ]
)

print(response.choices[0].message)