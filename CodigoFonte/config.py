import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'MySchool.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/MySchool'


SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'teste-teste-teste'