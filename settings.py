import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DBENGINE'),
        'HOST': os.getenv('DBHOST'),
        'PORT': os.getenv('DBPORT'),
        'NAME': os.getenv('DBNAME'),
        'USER': os.getenv('DBUSER'),
        'PASSWORD': os.getenv('DBPASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
