import openai

openai.api_key = "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"


def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    return response['data'][0]['url']


if __name__ == "__main__":
    print("Bot: Say your wish")
    user_input = input("You: ")

    if user_input.lower() not in ["quit", "exit"]:
        response = generate_image(user_input)

        print("Bot: ", response)
