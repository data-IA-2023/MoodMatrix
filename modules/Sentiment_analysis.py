# Ce module est compatible avec python 3.10, 3.11 et 3.12.
import deep_translator  # Importation de la bibliothèque pour la traduction
from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline  # Importation des composants de Hugging Face Transformers
from langdetect import detect  # Importation de la fonction detect de la bibliothèque langdetect

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
    Cette fonction prend en entrée un texte et le traduit en anglais.
    Elle détecte d'abord la langue du texte, puis le traduit en anglais.

    Args:
        text (str): Le texte à traduire. Par défaut, c'est une chaîne vide.

    Returns:
        dict: Un dictionnaire contenant la langue détectée et le texte traduit en anglais.
    """
    langue=detect(text)
    translated_text = deep_translator.GoogleTranslator(source=langue, target='en').translate(text)
    return {'langue': langue, 'textTraduie':translated_text}

# Fonction pour traduire un texte en anglais et l'analyser pour l'émotion
def translate_and_analyse(text):
    """
    Cette fonction prend un texte en entrée, le traduit en anglais, puis analyse son émotion dominante.

    Args:
        text (str): Le texte à analyser.

    Returns:
        dict: Un dictionnaire contenant le texte d'origine, sa traduction en anglais, l'émotion détectée, 
              la langue d'origine et une émoticône correspondant à l'émotion détectée.un exemple:
              {'text': "c'est incroiyable.", 'traduction': "it's incredible.", 'emotion': 'admiration', 'langue': 'fr', 'emoticon': '😍'}
              
    """
    trad=translate_to_en(text)
    emo=emotion_analysis(trad['textTraduie'])[0]['label']
    #print(type(emo),emo)
    
    return {'text':text,'traduction':trad['textTraduie'], "emotion" : emo, "langue" : trad["langue"], 'emoticon':sentiment_to_emoticon(emo)}

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