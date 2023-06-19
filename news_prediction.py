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
