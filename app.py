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

next = openai.Completion.create(
    model="text-davinci-003",
    prompt="Once upon a time",
    max_tokens=15,
    temperature=2,
)

print(next)

''' Tokens, by definition, are common sequences of characters in the output text. A good way
to remember is that one token usually means about 4 letters of text for normal English words. This
means that 100 tokens are about the same as 75 words. Grasping this will aid you in comprehending
the pricing. Later in this book, we will delve deeper into pricing details'''

# maximum logprobs is 5
# maximum temperature is 2