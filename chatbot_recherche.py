import requests
#from sentiment_analysis import translate_and_analyse
import json
#from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer
#from transformers import BlenderbotSmallForConditionalGeneration, BlenderbotSmallTokenizer
import time


####################################################################################################
#Modèle de mistral : efficace mais schizophrène 
####################################################################################################

#API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print("Statut HTTP:", response.status_code)
    try:
        print("Réponse JSON:", response.json())
        return response.json()
    except ValueError:
        print("Réponse non-JSON:", response.text)
        return None

conversation_history = ""

while True:
    user_input = input("Vous: ")
    conversation_history += f"\nUtilisateur: {user_input}\nAssistant: "
    response = query({
        "inputs": conversation_history,
        "options": {
            "use_cache": False,
            "max_length": 4096,  # Définir une longueur maximale élevée pour les réponses
            "temperature" : 0.7,
            "top_k" : 100,
            "top_p" : 0.9,
            "no_repeat_ngram_size" : 3,
            "num_beams" : 2,    
        }
    })
    if response and response[0].get("generated_text"):
        assistant_response = response[0]["generated_text"].split("Assistant: ")[-1].strip()
        print("Assistant:", assistant_response)
        conversation_history += assistant_response
    else:
        print("Désolé, une erreur s'est produite ou aucune réponse n'a été générée.")
        break  # Sortie de la boucle si une erreur se produit ou si aucune réponse n'est générée"""

####################################################################################################
#Modèle basé sur gpt2 spécialisé sur les conversations : efficace cependant mauvais en français
####################################################################################################

"""
# Load tokenizer and explicitly set padding to the left
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
tokenizer.padding_side = 'left'  # Setting padding to the left
tokenizer.pad_token = tokenizer.eos_token  # Set pad token to EOS token, necessary for models like DialoGPT

# Load the model
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Function to generate response using DialoGPT
def generate_response(input_text):
    # Encode the input text, adding the EOS token at the end
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt", padding="longest")

    # Generate a response from the model
    chat_history_ids = model.generate(
        input_ids=input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        top_k=50
    )

    # Decode and print the response
    response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

# Example usage
while True:
    user_input = input("You: ")
    response = generate_response(user_input)
    print("Chatbot:", response)"""


####################################################################################################
#Modèle de meta : non entrainé donc inefficace 
####################################################################################################
"""
tokenizer = BlenderbotSmallTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = BlenderbotSmallForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")

def generate_response(input_text):
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_beams=5, early_stopping=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

while True:
    user_input = input("Vous: ")
    response = generate_response(user_input)
    print("Chatbot:", response)"""

########################################################################################################################################################################################################
#Modèle gpt2 : modèle non entrainé et donc inefficace 
####################################################################################################
"""# Load model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Example input
input_text = "Hello, how are you?"

# Tokenize input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate response
output_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

# Decode and print response
response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print("Response:", response)"""


####################################################################################################
#entrainement personnel d'un modèle basé sur mistral : trop long par rapport à la deadline
####################################################################################################
"""
from transformers import AutoTokenizer, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments
import torch

# Étape 1 : Téléchargement du modèle Mistral
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

# Étape 2 : Prétraitement des données
# Vous avez déjà converti le dataset PIAF en fichier texte dans l'étape précédente

# Étape 3 : Chargement du dataset
dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="data.txt",  # Chemin vers le fichier texte contenant les dialogues PIAF
    block_size=128
)

# Étape 4 : Création du data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Étape 5 : Configuration des arguments d'entraînement
training_args = TrainingArguments(
    output_dir="./models",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)

# Étape 6 : Création du Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

# Étape 7 : Entraînement du modèle
trainer.train()"""

####################################################################################################
#Modèle basé sur mistral entrainé sur un dataset français : nécessite cuda et plante si on cherche une alternative
####################################################################################################
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer

model_id = "jpacifico/French-Alpaca-7B-Instruct-beta"
model = AutoModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id, add_eos_token=True, padding_side='left')
streamer = TextStreamer(tokenizer, timeout=10.0, skip_prompt=True, skip_special_tokens=True)

# Parameters
temperature: float = 0.7
top_p: float = 1.0
top_k: float = 0
repetition_penalty: float = 1.1
max_new_tokens: int = 1024

def chat_with_frenchalpaca(query: str):
    input_ids = tokenizer.apply_chat_template([{"role": "user", "content": query}], return_tensors="pt")
    input_length = input_ids.shape[1]

    generated_outputs = model.generate(
        input_ids=input_ids,
        temperature=temperature,
        do_sample=temperature > 0.0,
        top_p=top_p,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
        max_new_tokens=max_new_tokens,
        pad_token_id=tokenizer.eos_token_id,
        streamer=streamer,
        return_dict_in_generate=True,
    )
    generated_tokens = generated_outputs.sequences[0, input_length:]
    generated_text = tokenizer.decode(generated_tokens, skip_special_tokens=True)

    return generated_text

prompt = "Donne moi une recette populaire à Aix-En-Provence"
result = chat_with_frenchalpaca(prompt)
print(result)


"""
     