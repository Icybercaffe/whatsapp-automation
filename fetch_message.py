import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_love_message():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": (
                    "Write a single, short and warm message to my  mother, "
                    "showing love, gratitude, or appreciation. Maximum 12 words. "
                    "in English. No extra text, no lists, no explanations."
                )
            }
        ],
        max_tokens=50,
        temperature=0.8
    )
    message = response.choices[0].message.content.strip()
    return message

if __name__ == "__main__":
    print(get_love_message())

