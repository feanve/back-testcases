from .base import *
# import dj_database_url

# from dotenv import load_dotenv


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# load_dotenv()

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'final_ing',
        'USER': 'user_ing',
        'PASSWORD': 'KqoJKnSI8oPP',
        'HOST': 'localhost',
        'PORT':'5432',
    }
}