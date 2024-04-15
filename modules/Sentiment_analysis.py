import deep_translator
from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline

def translate_to_en(text=""):
    translated_text = deep_translator.GoogleTranslator(source='fr', target='en').translate(text)
    return translated_text

tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

emotion_analysis= pipeline('sentiment-analysis', 
                    model='arpanghoshal/EmoRoBERTa')

def translate_and_analyse(text):
    return emotion_analysis(translate_to_en(text))


emotion_labels = translate_and_analyse("Je te déteste.")
print(emotion_labels)
