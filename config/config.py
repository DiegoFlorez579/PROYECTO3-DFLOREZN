import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL").replace("mysql://", "mysql+pymysql://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False