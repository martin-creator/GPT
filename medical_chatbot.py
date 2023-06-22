# Advanced Fine Tuning by creating a medical chatbot

import openai

def regular_discussion(prompt):
    """
    params: prompt - a string
    Returns a response from the API using Davinci.
    If the user asks about a drug, the function will call get_malady_name().
    """
    prompt = """
    The following is a conversation with an AI assistant. The assistant is helpful, \
    creative, clever, very friendly and careful with Human's health topics
    The AI assistant is not a doctor and does not diagnose or treat medical conditio\
    ns to Human
    The AI assistant is not a pharmacist and does not dispense or recommend medicati\
    ons to Human
    The AI assistant does not provide medical advice to Human
    The AI assistant does not provide medical and health diagnosis to Human
    The AI assistant does not provide medical treatment to Human
    The AI assistant does not provide medical prescriptions to Human
    If Human writes the name of a drug the assistant will reply with "######".

    Human: Hi
    AI: Hello Human. How are you? I'll be glad to help. Give me the name of a drug a\
    nd I'll tell you what it's used for.
    Human: Vitibex
    AI: ######
    Human: I'm fine. How are you?
    AI: I am fine. Thank you for asking. I'll be glad to help. Give me the name of a\
    drug and I'll tell you what it's used for.
    Human: What is Chaos Engineering?
    AI: I'm sorry, I am not qualified to do that. I'm only programmed to answer ques\
    tions about drugs. Give me the name of a drug and I'll tell you what it's used for.
    Human: Where is Carthage?
    AI: I'm sorry, I am not qualified to do that. I'm only programmed to answer ques\
    tions about drugs. Give me the name of a drug and I'll tell you what it's used for.
    Human: What is Maxcet 5mg Tablet 10'S?
    AI: ######
    Human: What is Axepta?
    AI: ######
    Human: {}
    AI:""".format(prompt)

    # Get the response from the API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        stop=["\n", " Human:", " AI:"],
    )


def get_malady_name(drug_name):
    """
    params: drug_name - a string
    Returns a malady name that corresponds to a drug name from the fine-tuned model.
    The function will call get_malady_description() to get a description of the mala\
    dy.
    """
    # Configure the model ID. Change this to your model ID.
    model = "ada:ft-learninggpt:drug-malady-data-2023-02-21-20-36-07"
    class_map = {
    0: "Acne",
    1: "Adhd",
    2: "Allergies",
    # ...
    }

    # Returns a drug class for each drug
    prompt = "Drug: {}\nMalady:".format(drug_name)

    response = openai.Completion.create(
    model=model,
    prompt= prompt,
    temperature=1,
    max_tokens=1,
    )

    response = response.choices[0].text.strip()

    try:
        malady = class_map[int(response)]
        print("AI: This drug used for {}.".format(malady))
        print(get_malady_description(malady))
    except:
        print("AI: I dont know what '" + drug_name + "' is used for.")


def get_malady_description(malady):
    """
    params: malady - a string
    Get a description of a malady from the API using Davinci.
    """

    prompt = """
    The following is a conversation with an AI assistant. The assistant is helpful, \
    creative, clever, and very friendly.
    The assistant does not provide medical advice. It only defines a malady, a disea\
    se, or a condition.
    If the assistant does not know the answer to a question, it will ask to rephrase\
    it.

    Q: What is {}?
    A:""".format(malady)

    # Get the response from the API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        stop=["\n", " Q", " A:"],
    )

    return response.choices[0].text.strip()


    if __name__ == "__main__":
        while True:
            regular_discussion(input("Human: "))
