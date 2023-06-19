import os
import openai
import pandas as pd
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity


# Predicting News Category Using Embedding


def init_api():
    ''' Load API key from .env file'''
    with open(".env") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value

    openai.api_key = os.environ["API_KEY"]
    openai.organization = os.environ["ORG_ID"]


init_api()

categories = [
'U.S. NEWS',
'COMEDY',
'PARENTING',
'WORLD NEWS',
'CULTURE & ARTS',
'TECH',
'SPORTS'
]


# Define a function to classify sentence
def classify_sentence(sentence):
    # Get the embedding for the sentence
    sentence_embedding = get_embedding(sentence, model="text-embedding-ada-002")
    
    # Caculate the similarity score between the sentence and each category
    similarity_scores = {}
    for category in categories:
        category_embeddings = get_embedding(category, model="text-embedding-ada-002")
        similarity_scores[category] = cosine_similarity(sentence_embedding, category_embeddings)
        
    # Return the category with the highest similarity score
    return max(similarity_scores, key=similarity_scores.get)

