# import the necessary packages
import torch
import clip
import PIL


# chech if cuda is available
device = "cuda" if torch .cuda.is_available() else "cpu"

# load the model

model, preprocess = clip.load('ViT-B/32', device=device)

# load the image and encode it using CLIP

# load image

image = PIL.Image.open('/resources/ASTRONAUTS.jpg')

# preprocess image
image_input = preprocess(image).unsqueeze(0).to(device)

# encode image using the CLIP model
with torch.no_grad():
    image_features = model.encode_image(image_input)


# Define a list of text prompts
prompts = [
"A large galaxy in the center of a cluster of galaxies located in the constellation Bostes",
"MTA Long Island Bus has just left the Hempstead Bus Terminal on the N6",
"STS-86 mission specialists Vladimir Titov and Jean-Loup Chretien pose for photos in the Base Block","A view of the International Space Station (ISS) from the Soyuz TMA-19 spacecraft, as it approaches the station for docking",
"A domesticated tiger in a cage with a tiger trainer in the background",
"A mechanical engineer working on a car engine",
]


# Encode the text prompts using the CLIP model
with torch.no_grad():
    text_features = model.encode_text(clip.tokenize(prompts).to(device))

# Calculate the cosine similarity between the image and text features
similarity_scores = (100.0 * image_features @ text_features.T).softmax(dim=-1)


# Print the prompt with the highest similarity score
most_similar_prompt_index = similarity_scores.argmax().item()
most_similar_prompt = prompts[most_similar_prompt_index]
print(f"The image is most similar to the prompt: {most_similar_prompt}")


