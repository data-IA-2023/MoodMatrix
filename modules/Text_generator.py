"""
=========================================
classe :
    Text_generator
methode :
    reponce_generator ( dict_analyse ) => return : assistant_response
=========================================
"""

# =========================================
# importation :
# =========================================

import requests

# =========================================
# classe et méthode :
# =========================================   

"""
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
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
        break  # Sortie de la boucle si une erreur se produit ou si aucune réponse n'est générée
"""

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

def reponce_generator ( dict_analyse ) :
    """
    arg :
        dict_analyse : dict retourné par l'analyse de sentiment
    return :
        str : assistant_response
    """
    conversation_history = ""

    while True:
        # user_input = input("Vous: ")
        emo_input = dict_analyse
        print(emo_input)
        if emo_input['emotion'] == 'neutre':
            final_input = emo_input['text']
        else: 
            final_input = emo_input['text'] + '\n' + f'je me sens {emo_input['emotion']}'
        conversation_history += f"\nUtilisateur: {final_input}\nAssistant: "
        response = query({
            "inputs": conversation_history,
            "options": {
                "use_cache": False,
                "max_length": None,  # Définir une longueur maximale élevée pour les réponses
                "temperature" : 0.2,
                "top_k" : 100,
                "no_repeat_ngram_size" : 3,
                "num_beams" : 2,
                "safe_prompt" : False,
                "tool_choice" : None    
            }
        })
        if response and len(response) > 0 and response[0].get("generated_text"):
            assistant_response = response[0]["generated_text"].split("Assistant: ")[-1].strip()
            print("########################################")
            print("Assistant:", assistant_response)
            conversation_history += assistant_response
            return assistant_response
        # else:
        #     error_messege = "Désolé, une erreur s'est produite ou aucune réponse n'a été générée."
        #     print(error_messege)
        #     return error_messege
        #     break  # Sortie de la boucle si une erreur se produit ou si aucune réponse n'est générée
