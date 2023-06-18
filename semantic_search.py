import os
import openai
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