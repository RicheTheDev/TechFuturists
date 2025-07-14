import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')

    # Récupération sécurisée et correction du schéma DATABASE_URL
    db_uri = os.getenv('DATABASE_URL', 'sqlite:///techfuturists.db')
    if db_uri.startswith("postgres://"):
        db_uri = db_uri.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = db_uri

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuration Email
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_SENDER = os.getenv('MAIL_SENDER')
