import openai
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")


def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit"]:
            break

        response = chat(user_input)

        print("Bot: ", response)
