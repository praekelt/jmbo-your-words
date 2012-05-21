import os

# Django settings for yal project.

PROJECT_PATH = os.path.realpath(\
               os.path.join(os.path.dirname(__file__), '..', 'jmboyourwords'))


DEBUG = True
TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'your_words.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Africa/Johannesburg'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'static', 'media')
MEDIA_URL = '/static/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static', 'files')
STATIC_URL = '/static/files/'

ADMIN_MEDIA_PREFIX = '/static/files/admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static', 'base'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
SECRET_KEY = '@4v$g819k=!!zakin+r(+77wid514nxy_ez)@bq#k(uve77$e$'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'jmboyourwords.urls'


TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'jmboyourwords',
    'south',
    'ckeditor',
    'django_nose',
    'category',
)

# CKEDITOR
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'Link', 'Unlink', 'Anchor',
              #'-', 'Format',
              #'-', 'SpellChecker', 'Scayt',
              #'-', 'Maximize',
            ],
            ['HorizontalRule',
              #'-', 'Table',
              '-', 'BulletedList', 'NumberedList',
              '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
              #'-', 'SpecialChar',
              '-', 'Source',
              #'-', 'About',
            ]
        ],
        'width': 620,
        'height': 300,
        'toolbarCanCollapse': False,
    }
}

# South Migration settings
SOUTH_TESTS_MIGRATE = False

# Use Nose as our test suite runner
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
