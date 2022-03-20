import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = 'postgresql://qghnjfezobqyue:4e774335da07e432e38ef9a6266ec0eb40a790f950d6aaf4fe8129f43b230e7f@ec2-44-195-191-252.compute-1.amazonaws.com:5432/d6n3i1h9t17jbh'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER=os.environ.get('UPLOAD_FOLDER','./uploads')