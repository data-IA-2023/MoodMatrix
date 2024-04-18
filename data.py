import csv

def convert_csv_to_qa_pairs(csv_file, txt_file):
    with open(csv_file, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header
        with open(txt_file, "w", encoding="utf-8") as txt_file:
            for row in reader:
                question, answer = row
                txt_file.write(f"thème: {question}\n")
                txt_file.write(f"prompt: {answer}\n\n")

# Appel de la fonction pour convertir le fichier CSV en fichier texte
#convert_csv_to_qa_pairs("chatgpt-prompts-French.csv", "data.txt")


import json

def convert_json_to_qa_pairs(json_file, txt_file):
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        with open(txt_file, "w", encoding="utf-8") as txt_file:
            for item in data:
                instruction = item["instruction"]
                response = item["output"]
                txt_file.write(f"question: {instruction}\n")
                txt_file.write(f"réponse: {response}\n\n")

# Appel de la fonction pour convertir le fichier JSON en paires de questions-réponses
#convert_json_to_qa_pairs("Acquiesce_data_110k_instructions.json", "data.txt")


import subprocess

# Exécuter la commande nvidia-smi
result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)

# Vérifier si la commande s'est exécutée avec succès
if result.returncode == 0:
    # Afficher la sortie de la commande
    print(result.stdout)
else:
    # Afficher le message d'erreur en cas d'échec
    print("Erreur lors de l'exécution de la commande nvidia-smi:", result.stderr)