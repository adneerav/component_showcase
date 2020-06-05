SECRET_KEY = 'drc^l83u=ae3^)s%ai7+!q3dcg9#cmbn$%za1xd7ob#&8+6g=)'
print("production")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['192.168.34.184', '127.0.0.1']
# Application definition
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hbcomponent',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'DB_PORT': '3306',
    }
}
