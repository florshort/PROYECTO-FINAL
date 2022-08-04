from .base import *

DEBUG = False
# No subir en true porque puede mostrar la ruta exacta del archivo de configuración

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), #ponemos los datos de nuestra base de datos para conectar
        'USER': ''
    }
}