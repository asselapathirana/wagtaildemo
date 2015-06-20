from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
        'INDEX': 'wagtaildemo'
    }
}



# BASE_URL required for notification emails
BASE_URL = 'http://localhost:8000'

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY=os.getenv('DJANGO_SECRET_KEY','')

DATABASES = {
    'default':
        {'HOST': 'localhost', 'USER': os.getenv('DATABASE_USER',''), 'PASSWORD': os.getenv('DATABASE_PASSWORD',''), 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'PORT': '', 'NAME': os.getenv('DATABASE_NAME','')}
}

