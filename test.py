from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
import os
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="hi",
    model="openai/gpt-oss-20b",
)
print(response.output_text)