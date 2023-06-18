import os
import openai
from openai.embeddings_utils import get_embedding,cosine_similarity
import click
import pandas as pd
import numpy as np

# Simple semantic search
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


df = pd.read_csv('words.csv') # This line creates a pandas dataframe from the csv file

# print(df.tail(5)) # This line prints the last 5 rows of the dataframe

# print(get_embedding("Hello", engine="text-embedding-ada-002"))

# get embedding for each word in the dataframe
df['embedding'] = df['Text'].apply(lambda x: get_embedding(x, engine="text-embedding-ada-002"))

df.to_csv('embeddings.csv')

# Convert the values in 'embedding' column to string representations
df['embedding'] = df['embedding'].astype(str)

# convert last column to numpy array
df['embedding'] = df['embedding'].apply(eval).apply(np.array)

# get the search term from the user
user_search = input("Enter a search term: ")

# get the embedding for the search term
search_term_embedding = get_embedding(user_search, engine="text-embedding-ada-002")

#print(search_term_embedding)

# calculate the similarity between the search term and each word in the dataframe
df["similarity"] = df["embedding"].apply(lambda x: cosine_similarity(x, search_term_embedding))

# sort the dataframe by the similarity score
df = df.sort_values(by="similarity", ascending=False)

# print the top 5 results
print(df.head(5))

print(df)



