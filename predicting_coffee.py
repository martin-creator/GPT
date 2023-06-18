# When a user enters the name of a coffee, we will use the OpenAI Embeddings API to get the
# embedding for the review text of that coffee. Then, we will calculate the cosine similarity between
# the input coffee review and all other reviews in the dataset. The reviews with the highest cosine
# similarity scores will be the most similar to the input coffee’s review. We will then print the names
# of the most similar coffees to the user.

import os
import openai
import pandas as pd
import numpy as np
import nltk
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity

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


# download the dataset

def download_nltk_data():
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")

    try:
        nltk.data.find("tokenizers/stopwords")
    except LookupError:
        nltk.download("stopwords")
