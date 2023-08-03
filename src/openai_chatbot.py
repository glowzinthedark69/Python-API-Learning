import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="In pycharm how do I mark a file so that it is not included in GIT after it has already been added?",
    max_tokens=150,
)

print(response.choices[0].text.strip())
