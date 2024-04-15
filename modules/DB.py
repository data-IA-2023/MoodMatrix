"""
=========================================
classe :
    DB
methode :
    connectBd() => sortie : return dict_connection ou print error
    set_bd ( dict_new_data, session ) => entrée : dict, fonction : ajout dans la bd
    get_bd ( value, session, engine ) => sortie : return df ou print error, fonction : réccupaire dans la bd
=========================================
"""

# =========================================
# classe :
#     ORM
# methode :
#     createsession() => return dict { engine, session } 
# =========================================
# classe :
#     Historiques => __tablename__ = "historiques"
# attribus :
#     idTexte = Column(Integer, primary_key=True, autoincrement=True)
#     texte = Column(VARCHAR())
#     sentiment = Column(VARCHAR())
#     resultat = Column(VARCHAR())
#     feedBack = Column(Boolean)
#     idMonitoring = Column(Integer, ForeignKey('dbo.monitoring.idMonitoring'))
# =========================================
# classe :
#     Monitoring => __tablename__ = "monitoring"
# attribus :
#     idMonitoring = Column(Integer, primary_key=True, autoincrement=True)
#     statusAnalys = Column(String(50))
#     codeErrorAnalys = Column(String(500))
#     statusChatBot = Column(String(50))
#     codeErrorChatBot = Column(String(500))
#     statusResult = Column(String(50))
#     codeErrorResult = Column(String(500))
# =========================================
from ORM import createsession, Historiques, Monitoring

# =========================================
# importation :
# =========================================
import os
import pandas as pd

# =========================================
# classe et méthode :
# ========================================= 

# =======================    connection à la base de données    =======================

def connectBd():
    try:
        dict_connection = createsession ()  # dict { engine, session }
        return dict_connection
    except Exception as e :
        print("error :", e)

# teste :
# dict = createsession ()
# print (dict)
    
# =======================    ajout à la base de données    =======================

def set_bd ( dict_new_data, session ) :
    """
    dict_new_data = { texte : "", sentiment : "", resultat : "", feedBack : "", 
                     statusAnalys : "", codeErrorAnalys : "", statusChatBot : "", 
                     codeErrorChatBot : "", statusResult : "", codeErrorResult : "" }
    """

    # ========== traitement du monitoring ==========
    
    monitoring = Monitoring(
        statusAnalys = dict_new_data['statusAnalys'],
        codeErrorAnalys = dict_new_data['codeErrorAnalys'],
        statusChatBot = dict_new_data['statusChatBot'],
        codeErrorChatBot = dict_new_data['codeErrorChatBot'],
        statusResult = dict_new_data['statusResult'],
        codeErrorResult = dict_new_data['codeErrorResult']
    )

    # Ajout du monitoring à la session
    session.add(monitoring)
    session.commit()

    # ========== traitement de l'historiques ==========
    id_monitoring = monitoring.idMonitoring

    historiques = Historiques(
        texte = dict_new_data['texte'],
        sentiment = dict_new_data['sentiment'],
        resultat = dict_new_data['resultat'],
        feedBack = dict_new_data['feedBack'],
        idMonitoring = id_monitoring
    )

    # Ajout de l'historiques à la session
    session.add(historiques)
    session.commit()


# =======================    réccupère la base de données    =======================

def get_bd ( value, session, engine ) :

    if value == "monitoring" :
        df_query = session.query(Monitoring)
        
        df = pd.read_sql( sql=df_query.statement, con=engine )

        return df
    
    elif value == "historique" :
        df_query = session.query(Historiques)
        
        df = pd.read_sql( sql=df_query.statement, con=engine )

        return df
    
    else :
        print("error : la requette n'ai pas valide")
