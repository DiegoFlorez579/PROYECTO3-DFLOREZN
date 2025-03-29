import os

#class Config:
#    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL").replace("mysql://", "mysql+pymysql://")
#    SQLALCHEMY_TRACK_MODIFICATIONS = False

DATABASE_URL = os.getenv("DATABASE_URL", "")
if DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("mysql://", "mysql+pymysql://")
else:
    print("❌ ERROR: No se encontró DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False