print("local")
SECRET_KEY = 'drc^l83u=ae3^)s%ai7+!q3dcg9#cmbn$%za1xd7ob#&8+6g=)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# Application definition


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'component_showcase',
        'USER': 'root',
        'PASSWORD': 'hbdev',
        'HOST': 'localhost',
        'DB_PORT': '3344',
    }
}
