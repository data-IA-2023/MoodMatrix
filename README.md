# MoodMatrix

Pour la documentation, allez sur le wiki : [Wiki](https://github.com/data-IA-2023/MoodMatrix/wiki/Accueil)

## Présentation

Dans le cadre de la création d’un robot capable de percevoir et de réagir aux émotions des humains, nous avons créé une IA capable d'interpréter les émotions à partir d’un texte.
Cette IA se présente sous la forme d'un chat bot émotionnel qui utilise le modèle de classification émotionnelle EmoRoBERTa et le LLM Mistral 7B.

### Schéma fonctionel de l'application :
![](https://github.com/data-IA-2023/MoodMatrix/blob/main/ressource/moodMatrix.png?raw=true)

## Démarche et choix des outils

### Comparaison des outils de chatBot :

Crisp chatbot : Cette extension inclut le live chat, les notifications en temps réel, le chatbot, les applications pour ordinateur de bureau et portable et le paramétrage des heures de disponibilité du chat. Le chatbot est payant.

Rasa : Chatbot opensource et très rapide à prendre en main. Il est entièrement personnalisable et donc très adaptable. Mais il ne fonctionne pas avec les versions python plus récentes que 3.10, et ne fonctionne pas avec docker.

mistral IA : Modèle gratuit, rapide et performant, un concurrent de GPT 3.5.

neo GPT : Basé sur chatGPT 3.5, ce chatbot n'est pas disponible gratuitement.

Choix : Mistral IA

### Comparaison des outils NLP d'analyse de sentiment/émotion :

VADER (Valence Aware Dictionary and sEntiment Reasoner) : VADER est un outil d'analyse de sentiment basé sur des règles et conçu pour analyser les sentiments exprimés dans du texte social. Il est souvent utilisé pour l'analyse de sentiment dans les médias sociaux. Python : nltk.sentiment.vader.

TextBlob : TextBlob est une bibliothèque Python pour le traitement du langage naturel qui inclut des fonctionnalités d'analyse de sentiment. Il utilise une approche basée sur des lexiques pour attribuer des polarités (positives, négatives ou neutres) aux mots et calcule ensuite la polarité globale du texte. Python : textblob.sentiments.

Stanford CoreNLP : Il s'agit d'une suite d'outils de traitement du langage naturel développée par Stanford University. Elle comprend un module d'analyse de sentiment capable de classifier les phrases en positif, négatif ou neutre. Java : edu.stanford.nlp.

FastText : FastText est une bibliothèque open source de Facebook pour le traitement du langage naturel et l'apprentissage de vecteurs de mots. Il inclut des fonctionnalités d'analyse de sentiment par classification de texte. Python : fasttext.

Scikit-learn : Scikit-learn est une bibliothèque Python pour l'apprentissage automatique. Bien qu'elle ne fournisse pas de modèles pré-entraînés pour l'analyse de sentiment, elle propose des outils et des algorithmes pour construire des modèles personnalisés d'analyse de sentiment en utilisant des techniques telles que la classification naïve bayésienne, les machines à vecteurs de support (SVM), etc.

RoBERTa: BERT (Bidirectional Encoder Representations from Transformers) : BERT est un modèle de langage profond développé par Google. Bien qu'il soit principalement utilisé pour des tâches de compréhension de texte, il peut également être adapté à l'analyse de sentiment en finetunant le modèle sur des données d'analyse de sentiment. Implémentations disponibles en Python : Hugging Face Transformers, TensorFlow, PyTorch. 
Choix : RoBERTa est une amélioration de la stratégie de masquage de langage de BERT et modifie certains hyperparamètres clés de BERT, notamment en supprimant l'objectif de pré-entraînement de la phrase suivante de BERT, et en s'entraînant avec des mini-lots et des taux d'apprentissage beaucoup plus grands. RoBERTa a également été entraîné sur un ordre de grandeur de données plus important que BERT, pendant une période plus longue. Cela permet aux représentations de RoBERTa de généraliser encore mieux aux tâches aval que BERT.

Nous avons utilisé la variante EmoRoBERTa adapté à la classification des émotions.
