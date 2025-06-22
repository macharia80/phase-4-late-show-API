import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://macharia:NewPass1234@localhost/late_show_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False