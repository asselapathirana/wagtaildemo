from .base import *

DEBUG = False



WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
        'URLS': [os.getenv('WAGTAILSEARCH_URL','')],
        'INDEX': os.getenv('WAGTAILSEARCH_INDEX',''),
        'TIMEOUT' : 5,

    }
}


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'KEY_PREFIX': 'wagtaildemo',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}

# Use the cached template loader
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)


try:
	from .local import *
except ImportError:
	pass


SECRET_KEY=os.getenv('DJANGO_SECRET_KEY','')

DATABASES = {
    'default':
        {'HOST': 'localhost', 'USER': os.getenv('DATABASE_USER',''), 'PASSWORD': os.getenv('DATABASE_PASSWORD',''), 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'PORT': '', 'NAME': os.getenv('DATABASE_NAME','')}
}
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../static'))

ALLOWED_HOSTS=[ os.getenv('HOSTS1'), os.getenv('HOSTS2') ]
