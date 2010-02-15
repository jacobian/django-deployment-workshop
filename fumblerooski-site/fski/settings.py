from unipath import FSPath as Path

DEBUG = True

MANAGERS = ADMINS = []

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'fumblerooski'
DATABASE_USER = 'fumblerooski'
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

# Some setup for relative paths below
ROOT = Path(__file__).parent
BUILDOUT_ROOT = ROOT.parent

MEDIA_ROOT = ROOT.child('media')
MEDIA_URL = '/m/'
ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 'd8i0we+qjkwf*xt&fxl^$)x1pa-c%=$ib(^vrcy2z3y8!w_sua'
USE_I18N = False

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'fumblerooski.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'googlecharts',
    'fumblerooski.college',
    'fumblerooski.blog',
    'fumblerooski.rankings',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    ROOT.child('templates'),
    BUILDOUT_ROOT.child('parts', 'fumblerooski', 'templates'),
)


# Fumblerooski settings
SITE_ID = 2
CURRENT_SEASON = 2010
