import os
from urllib import response
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


# configure the model ID.
model = "curie:ft-personal-2023-06-21-19-07-39"

# Let's use a drug from each class
drugs = [
    "A CN Gel(Topical) 20gmA CN Soap 75gm' used for?",  # Class 0
    "Addnok Tablet 20'S' used for?",  # Class 1
    "ABICET M Tablet 10's' used for?",  # Class
]

class_map = {
    0: "Acne",
    1: "Adhd",
    2: "Allergies"
    # ...
}

# Returns a drug class for each drug
for drug_name in drugs:
    prompt = "Drug: {}\nMalady:".format(drug_name)

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=1,
        max_tokens=1,
    )

    # Print the generated text
    response = response.choices[0].text

    # The result should be 0, 1, and 2
    #print(drug_class)

    try:
        print(drug_name + " is used for " + class_map[int(response)] )
    except:
        print("I don't know what " + drug_name + " is used for")
    print()