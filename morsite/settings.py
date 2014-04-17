import os

# Django settings for morsite project.

LOCAL_DIR = r"c:\morsite"
IS_LOCAL = os.path.isdir(LOCAL_DIR)
if IS_LOCAL:
    PROJECT_DIR = LOCAL_DIR
    # BASE_URL = "http://127.0.0.1:8000/"
else:
    PROJECT_DIR = r"/home/ordercak/public_html/sweetsamuel.co.il/"
    # BASE_URL = "http://www.morsite.ordercakeinhaifa.com/"
    


def relToAbs(path):
    return os.path.join(PROJECT_DIR, path).replace('\\','/')

def dec(st):
    ret = ''
    key = '\xab\x67\xa4\x5c\xbb' * 10
    for i in xrange(len(st)):
        ret += chr( ord(st[i]) ^ ord(key[i]) )
    
    return ret
    
def assign(name , value):
    
    attr_name = dec(name)
    attr_value = dec(value)
    globals()[attr_name] = attr_value
    
    
    
DEBUG = False
TEMPLATE_DEBUG = DEBUG


ADMINS = [
    ('Mor' , 'SamuelCakes@gmail.com') ,         
    # ('Your Name', 'your_emai@example.com'),
]

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'morsite.db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Tel_Aviv'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'he'#'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


MEDIA_ROOT =  relToAbs('media')
MEDIA_URL = '/media/'

STATIC_ROOT =  relToAbs('static')
STATIC_URL = '/static/'
MY_STATIC_ROOT = relToAbs('static_files')

# Additional locations of static files
STATICFILES_DIRS = (
    MY_STATIC_ROOT,
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'f3oda#81rs%yu+*-bc%_5@*nmmf0!yiyw23d(!34awfexfc+j-'

# List of callables that know how to import templates from various sources.
if IS_LOCAL:
    TEMPLATE_LOADERS = ( 
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
else:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    #     'django.template.loaders.eggs.Loader',
    )    

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'morsite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'morsite.wsgi.application'

TEMPLATE_DIRS = (
    relToAbs('templates') , 
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'Prices' ,
    'orderedmodel',
    'django.contrib.comments',
    'tagging',
    'mptt',
    'zinnia',
    'menu' ,
    'Gallery',
    'contact_form',
    'my_comment_app',
    'tinymce',
    
)

COMMENTS_APP = 'my_comment_app'

#Zinnia stuff
TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  'zinnia.context_processors.version',
  "django.core.context_processors.debug",
  "django.contrib.messages.context_processors.messages",
  ) # Optional

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


TINYMCE_DEFAULT_CONFIG = {
    'theme_advanced_buttons1' : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect",
}


# assign('\xee*\xe5\x15\xf7\xf4/\xeb\x0f\xef\xf47\xe5\x0f\xe8\xfc(\xf6\x18' , '\x9aU\x97h\x8e\x9dP\xdd')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cakesnmore1010@gmail.com'
assign('\xee*\xe5\x15\xf7\xf4/\xeb\x0f\xef\xf47\xe5\x0f\xe8\xfc(\xf6\x18' , '\xd1\x00\xce2\xd5\xc7\x08\xd1-\xcc\xde\x11\xd32\xcf\xc1')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_RECIPIAENTS_LIST = [EMAIL_HOST_USER ]

    
    
EMAIL_RECIPIAENTS_LIST = ['cakesnmore1010@gmail.com' , 'SamuelCakes@gmail.com']