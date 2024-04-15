"""
=========================================
classe :
    main
methode :
    
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
#     get_bd ( value, session, engine ) => sortie : return df ou print error, fonction : réccupaire dans la bd
# =========================================
from DB import connectBd, set_bd, get_bd

# =========================================
# classe :
#     Sentiment_analysis
# methode :
#     
# =========================================
from Sentiment_analysis import *

# =========================================
# classe :
#     Text_generator
# methode :
#     
# =========================================
from Text_generator import *

# =========================================
# importation :
# =========================================



# =========================================
# classe et méthode :
# =========================================  

# =======================    connection à la base de données    =======================
engine_session = connectBd()

engine = engine_session ['engine']
session = engine_session ['session']

# =======================    initialisation du dictionnaire de resultat     =======================
dict_resultat = { "texte" : "", "sentiment" : "", "resultat" : "", "feedBack" : False, 
                 "statusAnalys" : "", "codeErrorAnalys" : "", "statusChatBot" : "", 
                 "codeErrorChatBot" : "", "statusResult" : "", "codeErrorResult" : "" }

# =======================    ourve streamlit et obtien texte de l'utilisateur     =======================



# =======================    appelle l'API d'analise de texte     =======================



# =======================    appelle l'API de chatBot     =======================



# =======================    envoit le resultat à la page streamlit     =======================



# =======================    enregistre le resultat à la base de donnée     =======================

"""
dict_resultat = { texte : "", sentiment : "", resultat : "", feedBack : "", 
                 statusAnalys : "", codeErrorAnalys : "", statusChatBot : "", 
                 codeErrorChatBot : "", statusResult : "", codeErrorResult : "" }
"""
# set_bd ( dict_resultat, session)

# =======================    réccupère infos de la base de donnée     =======================
df_historique = get_bd ( "historique", session, engine )
print('df_historique :', df_historique)
df_monitoring = get_bd ( "monitoring", session, engine )
print('df_monitoring :', df_monitoring)