# Django settings for cromongo project.

# Django settings for bookabed project.
import sys, os
import django

###########################################################################
# FILE PATHS

FILEROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# The base directory of this project
PROJECT_DIR = os.path.join(FILEROOT, 'cromongo')

#adding our lib folder here for .py files and __init__()ed modules
sys.path.insert(0, os.path.join(PROJECT_DIR, "lib"))

#South (for migrations) lives in /lib/south/south 
sys.path.insert(0, os.path.join(PROJECT_DIR, "lib", "south"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Tom', 'tom@throwingbeans.org'),
    ('Steve', 'steve@somefantastic.co.uk'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db/cromongo.sqlite',           # Or path to database file if using sqlite3.
        'USER': '',                             # Not used with sqlite3.
        'PASSWORD': '',                         # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/usr/local/django/cromongo/static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://127.0.0.1:8000/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xg94=c29ut9tamvd*w8oetpu_oj^b2yp9$s8dooy!k=2la+n^+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",    
)

MESSSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

ROOT_URLCONF = 'cromongo.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'), #base dir
    os.path.join(PROJECT_DIR, 'templates', 'crm'), #crm app, natch
    #os.path.join(PROJECT_DIR, 'templates', 'registration'), #login/out stuff, overriding bundled contrib.auth stuff
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'crm',
    'south'
)

try:
    from local_settings import *
except ImportError:
    import sys
    print "Please create a local_settings file containing your local configuration (e.g. database and email conf)"
    sys.exit(1)