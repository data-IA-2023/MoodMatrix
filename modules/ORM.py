"""
=========================================
classe :
    ORM
methode :
    createsession() => return dict { engine, session } 
=========================================
classe :
    Historiques => __tablename__ = "historiques"
attribus :
    idTexte = Column(Integer, primary_key=True, autoincrement=True)
    texte = Column(VARCHAR())
    sentiment = Column(VARCHAR())
    resultat = Column(VARCHAR())
    feedBack = Column(Boolean)
    idMonitoring = Column(Integer, ForeignKey('dbo.monitoring.idMonitoring'))
=========================================
classe :
    Monitoring => __tablename__ = "monitoring"
attribus :
    idMonitoring = Column(Integer, primary_key=True, autoincrement=True)
    statusAnalys = Column(String(50))
    codeErrorAnalys = Column(String(500))
    statusChatBot = Column(String(50))
    codeErrorChatBot = Column(String(500))
    statusResult = Column(String(50))
    codeErrorResult = Column(String(500))
=========================================
"""

# =========================================
# importation :
# =========================================

from sqlalchemy import ForeignKey, Column, Integer, VARCHAR, Boolean, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import os

# =========================================
# classe et méthode :
# =========================================  

# création de l'engine et la session
def createsession():
    # Trouve le chemein du fichier .env et l'ouvre par dotenv
    repertoir_fichier = os.path.dirname(__file__)
    bd_path = f'{repertoir_fichier}/DataBase.sql'

    # connection à la base de données et engine
    engine = create_engine(f"sqlite:///{bd_path}")
    Base.metadata.create_all(engine)

    # Création de la session en utilisant l'engine passé en paramètre
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()
    session.autocommit = True

    return { "engine" : engine, "session" : session}

# déclaraction de la classe de basse de sqlalchimy
# tous les modèles en hérite
Base = declarative_base()


# =======================    classe des classe de la base de données    =======================

# clase pour la table historiques
class Historiques ( Base ):
    __tablename__ = "historiques"
    __table_args__ = {'schema': 'dbo'}

    idTexte = Column(Integer, primary_key=True, autoincrement=True)
    texte = Column(VARCHAR())
    sentiment = Column(VARCHAR())
    resultat = Column(VARCHAR())
    feedBack = Column(Boolean)
    idMonitoring = Column(Integer, ForeignKey('dbo.monitoring.idMonitoring'))  # Spécification du schéma

    # Définir la relation avec la table "Monitoring"
    monitoring = relationship("Monitoring", back_populates="historiques")

# clase pour la table monitoring
class Monitoring ( Base ):
    __tablename__ = "monitoring"
    __table_args__ = {'schema': 'dbo'}

    idMonitoring = Column(Integer, primary_key=True, autoincrement=True)
    statusAnalys = Column(String(50))
    codeErrorAnalys = Column(String(500))
    statusChatBot = Column(String(50))
    codeErrorChatBot = Column(String(500))
    statusResult = Column(String(50))
    codeErrorResult = Column(String(500))

    # Définir la relation avec la table "Historiques"
    historiques = relationship("Historiques", back_populates="monitoring")