import deep_translator  # Importation de la bibliothèque pour la traduction
from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline  # Importation des composants de Hugging Face Transformers

# Initialisation du tokenizer pour RoBERTa
tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")

# Initialisation du modèle RoBERTa pour la classification de séquences
model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

# Initialisation du pipeline pour l'analyse de sentiment avec le modèle RoBERTa
emotion_analysis = pipeline('sentiment-analysis', 
                    model='arpanghoshal/EmoRoBERTa')

# Fonction pour traduire un texte en anglais
def translate_to_en(text=""):
    """
    Cette fonction prend en entrée un texte en français et le traduit en anglais.

    Args:
        text (str): Le texte à traduire en anglais. Par défaut, c'est une chaîne vide.

    Returns:
        str: Le texte traduit en anglais.
    """
    translated_text = deep_translator.GoogleTranslator(source='fr', target='en').translate(text)
    return translated_text

# Fonction pour traduire un texte en anglais et l'analyser pour l'émotion
def translate_and_analyse(text):
    """
    Cette fonction traduit un texte en anglais et l'analyse pour déterminer l'émotion dominante.

    Args:
        text (str): Le texte à analyser.

    Returns:
        dict: Un dictionnaire contenant le label d'émotion et sa probabilité associée.
        Voici la liste des emotions possible:
        admiration,amusement,anger,annoyance,approval,caring,confusion,curiosity,desire,disappointment,disapproval,disgust,embarrassment,excitement,fear,gratitude,grief,oy,love,nervousness,optimism,pride,realization,relief,remorse,sadness,surprise,neutral
    """
    return emotion_analysis(translate_to_en(text))[0]

def sentiment_to_emoticon(sentiment):
    """
    Cette fonction prend un sentiment en entrée et renvoie une émoticône équivalente.

    Args:
        sentiment (str): Le sentiment à traduire en émoticône.

    Returns:
        str: L'émoticône équivalente au sentiment. Si aucun sentiment correspondant n'est trouvé, la fonction renvoie None.
    """
    emoticon_dict = {
        "admiration": "😍",
        "amusement": "😄",
        "anger": "😠",
        "annoyance": "😒",
        "approval": "👍",
        "caring": "❤️",
        "confusion": "😕",
        "curiosity": "🤔",
        "desire": "😏",
        "disappointment": "😞",
        "disapproval": "👎",
        "disgust": "🤢",
        "embarrassment": "😳",
        "excitement": "😃",
        "fear": "😨",
        "gratitude": "🙏",
        "grief": "😢",
        "joy": "😊",
        "love": "😍",
        "nervousness": "😬",
        "optimism": "😊",
        "pride": "😊",
        "realization": "😲",
        "relief": "😌",
        "remorse": "😔",
        "sadness": "😔",
        "surprise": "😮",
        "neutral": "😐"
    }

    return emoticon_dict.get(sentiment.lower(), None)



if __name__ == "__main__":
    # Exemple d'utilisation de la fonction translate_and_analyse avec le texte "Je t'aime."
    emotion_labels = translate_and_analyse("c'est incroyable.")
    print(emotion_labels)
    emoticon_emoticon = sentiment_to_emoticon(emotion_labels['label'])
    print(emoticon_emoticon)
