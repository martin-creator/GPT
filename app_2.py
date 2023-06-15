# Editing Text Using GPT

import os 
import openai

def init_api():
    ''' Load API key from .env file'''
    with open(".env") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value

    openai.api_key = os.environ["API_KEY"]
    openai.organization = os.environ["ORG_ID"]

init_api()

response = openai.Edit.create(
    model="text-davinci-edit-001",
    input="Hallo Welt",
    instruction="Translate to English"
)

print(response)