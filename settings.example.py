# Django settings for ecosite project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'database.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3oo%sb1j8tv&rk*tk9rzo9+gv3(9hih(l$y^z0k+p%6o#kzt)p'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'ecosite.urls'

TEMPLATE_DIRS = (
	(os.path.join(SITE_ROOT, 'templates'),)
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.syndication',
	'django.contrib.comments',
	'lettuce.django',
	'ecosite.blog',
	'ecosite.tags',
	'ecosite.contact',
)

#Contact
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[ecofriend]'
