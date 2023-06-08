import openai

# Set the OpenAI API key
openai.api_key = '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'

# The chat models are currently "gpt-3.5-turbo" or "text-davinci-002"
model = "gpt-3.5-turbo"


def chat_with_gpt3(message):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message['content']


while True:
    user_message = input("You: ")
    print("AI: ", chat_with_gpt3(user_message))
