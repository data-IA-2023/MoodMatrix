"""
=========================================
classe :
    main
methode :
    text_analyse_et_generation ( texte, idConversation, dateHistorique ) => return : dict = {'reponce': '', 'emotion': '', 'emoticon': ''}
=========================================
"""

import sys
sys.path.append('modules')

# =========================================
# classe :
#     DB
# methode :
#     connectBd() => sortie : return dict_connection ou print error
#     set_bd ( dict_new_data, session ) => entrée : dict, fonction : ajout dans la bd
#     get_bd_monitoring ( session, engine ) => sortie : return df 
#     get_bd_historique ( value, session, engine ) => sortie : return df 
# =========================================
from DB import connectBd, set_bd, get_bd_monitoring, get_bd_historique

# =========================================
# methode :
#     translate_to_en(text="") => return {'langue': langue, 'textTraduie':translated_text}
#     translate_and_analyse(text) => return {'text':text,'traduction':trad['textTraduie'], "emotion" : emo, "langue" : trad["langue"], 'emoticon':sentiment_to_emoticon(emo)}
#     sentiment_to_emoticon(sentiment) => return emoticon_dict.get(sentiment.lower(), None)
# =========================================
from Sentiment_analysis import translate_and_analyse

# =========================================
# classe :
#     Text_generator
# methode :
#     reponce_generator ( dict_analyse ) => return : assistant_response
# =========================================
from Text_generator import reponce_generator

# =========================================
# importation :
# =========================================
import datetime

# =========================================
# classe et méthode :
# =========================================  

# =======================    connection à la base de données    =======================
engine_session = connectBd()

engine = engine_session ['engine']
session = engine_session ['session']

# =======================    méthode pour généré réponce adapté à un text     =======================
def text_analyse_et_generation ( texte, idConversation, dateHistorique ) :
    """
    analyse le texte en entrée pour en tirer le sence et un sentiment général, pour générer une réponse adapté.

    arg :
        texte (str) : issus de l'input du chat

    return :
        dict : un dictionnaire contenant le texte généré, l'émotion détectée et une émogi
            'text': "c'est incroiyable."
            {'reponce': "qu'est ce qui est incroiyable ?", 'emotion': 'admiration', 'emoticon': '😍'}
              
    """
    
    # =======================    initialisation du dictionnaire de resultat     =======================
    dict_resultat = { "texte" : "", "sentiment" : "", "resultat" : "", "feedBack" : None, "idConversation" : idConversation, 
                     "dateHistorique" : dateHistorique, "statusAnalys" : "", "codeErrorAnalys" : "", "statusChatBot" : "", 
                    "codeErrorChatBot" : "", "statusResult" : "", "codeErrorResult" : "" }
    
    # =======================    appelle l'API d'analise de texte     =======================
    try :
        dict_analyse = translate_and_analyse ( texte )
        # {'text':text,'traduction':trad['textTraduie'], "emotion" : emo, "langue" : trad["langue"], 'emoticon':sentiment_to_emoticon(emo)}

        dict_resultat['texte'] = dict_analyse['text']
        dict_resultat['sentiment'] = dict_analyse['emotion']
        dict_resultat['statusAnalys'] = "success"
    
    except Exception as e :
        dict_resultat['statusAnalys'] = "error"
        dict_resultat['codeErrorAnalys'] = f'{e}'

    # =======================    appelle l'API de chatBot     =======================
    try :
        text_generator = reponce_generator ( dict_analyse )
        dict_resultat['resultat'] = text_generator
        dict_resultat['statusChatBot'] = "success"
    except Exception as e :
        dict_resultat['statusChatBot'] = "error"
        dict_resultat['codeErrorChatBot'] = f'{e}'

    # =======================    enregistre le resultat à la base de donnée     =======================
    set_bd ( dict_resultat, session)

    # =======================    return     =======================
    return { "resultat" : text_generator, "sentiment" : dict_analyse['emotion'], "emoticon" : dict_analyse['emoticon'] }


# test :

# idConversation = 1
# dateHistorique = datetime.datetime.today()
# texte = "Aujourd'hui , je stress, j'ai un entretien à 14h."
# text_analyse_et_generation ( texte, idConversation, dateHistorique ) 

# =======================    réccupère infos de la base de donnée     =======================

def get_df_bd_monitoring () :
    """
    arg : none
    return : dataframe
    """
    df_monitoring = get_bd_monitoring ( session, engine )
    return df_monitoring

def get_df_bd_historique ( id_conversation ) :
    """
    arg : id_conversation (int)
    return : dataframe
    """
    df_historique = get_bd_historique ( id_conversation, session, engine )
    return df_historique

# test
# df_historique = None
# df_historique = get_bd ( "historique", session, engine )
# print('df_historique :', df_historique)

# df_monitoring = None
# df_monitoring = get_bd ( "monitoring", session, engine )
# print('df_monitoring :', df_monitoring)