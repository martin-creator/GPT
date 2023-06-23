import os
import openai
import click

# develop a command-line tool that can assist us with Linux commands through conversation.
# Click documentation: https://click.palletsprojects.com/en/8.1.x/


def init_api():
    ''' Load API key from .env file'''
    with open(".env") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value

    openai.api_key = os.environ["API_KEY"]
    openai.organization = os.environ["ORG_ID"]


init_api()

# No Context = Chaos of Randomness

initial_prompt = """You: Hi there!
    You: Hello!
    AI: How are you?
    You: {}
    AI: """

while True:
    prompt = input("You: ")

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=initial_prompt.format(prompt),
        temperature=1,
        max_tokens=100,
        stop=[" You", " AI:"]
    )

    print("AI:", response["choices"][0]["text"])