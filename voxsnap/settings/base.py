"""
Django settings for voxsnap project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import datetime
import os

from django.conf.global_settings import STATICFILES_FINDERS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_NAME = 'voxsnap'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cs+m4g23a*-#0ew@z3s(6+t-&6r-^=4&0m8x=v1hoi2uippy50'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ROOT_HOSTCONF = 'voxsnap.hosts'
DEFAULT_HOST = 'website'
PARENT_HOST = 'voxsnap.com'
ROOT_URLCONF = 'voxsnap.urls'
HOST_SCHEME = 'https'

DEFAULT_FROM_EMAIL = 'order@voxsnap.com'

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'apps.users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.postgres',
    'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    'storages',
    'django_hosts',
    'django_ses',
    'custom_user',
    'allauth',
    'allauth.account',
    #'allauth.socialaccount',
    'easy_thumbnails',
    'compressor',
    'webpack_loader',
    'rest_framework',
    'rest_auth',
    'colorfield',
    'ordered_model',
    'django_filters',
    'djstripe',

    # project apps list
    'apps.narrations.apps.NarrationsConfig',
    'apps.sales.apps.SalesConfig',
    'apps.leads.apps.LeadsConfig',
    'apps.analytics.apps.AnalyticsConfig',
    'apps.blog.apps.BlogConfig',
    'apps.podcasts.apps.PodcastsConfig',
    'apps.uploader.apps.UploaderConfig',
    'apps.articles.apps.ArticlesConfig',
    'apps.embedded.apps.EmbeddedConfig',
    'apps.voice.apps.VoiceConfig',
]

# Django Debug Toolbar doesn't like S3BotoStorage
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

LOGIN_REDIRECT_URL = '/'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_SIGNUP_FORM_CLASS = 'apps.users.forms.CustomSignupForm'

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    # django-hosts must be first
    'voxsnap.cors_middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_plotly_dash.middleware.BaseMiddleware',
    # django-hosts must be last
    'django_hosts.middleware.HostsResponseMiddleware'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'voxsnap.context_processors.head_body_settings',
                'voxsnap.context_processors.stripe_keys',
            ],
            'builtins': [
                'django_hosts.templatetags.hosts_override',
            ]
        },
    },
]

WSGI_APPLICATION = 'voxsnap.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASE_ROUTERS = ['voxsnap.dbrouter.AnalyticsRouter']

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False

# LANGUAGES = (
#     ('ru', 'Russian'),
#     ('ua', 'Ukrainian'),
#     ('en', 'English'),
# )
#
# LOCALE_PATHS = (
#     os.path.join(BASE_DIR, 'locale'),
# ))

# fix boto so that we can use dns name buckets with dots
AWS_S3_CALLING_FORMAT = 'boto.s3.connection.OrdinaryCallingFormat'
AWS_DEFAULT_ACL = 'public-read'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

COMPRESS_ROOT = 'static'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

PUBLIC_ROOT = os.path.join(BASE_DIR, '../', 'public')
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')
FRONTEND_ROOT = os.path.join(BASE_DIR, '../', 'frontend')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, '../', 'assets/build'),
    os.path.join(FRONTEND_ROOT, 'bundles'),
)

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_plotly_dash.finders.DashAssetFinder',
    'django_plotly_dash.finders.DashComponentFinder',
    'django_plotly_dash.finders.DashAppDirectoryFinder',
)

PLOTLY_COMPONENTS = [

    # Common components
    'dash_core_components',
    'dash_html_components',
    'dash_renderer',

    # django-plotly-dash components
    'dpd_components',

    # Other components, as needed
    #'dash_bootstrap_components',
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    # ('text/x-scss', 'django_pyscss.compressor.DjangoScssFilter'),
    # ('text/x-scss', 'sass --style compressed {infile} {outfile}'),
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME':
        '',
        'STATS_FILE':
        os.path.abspath(
            os.path.join(FRONTEND_ROOT, 'webpack/webpack-stats.json')),
    }
}

FILE_UPLOAD_PERMISSIONS = 0o644

NEW_USERS_CONFIRMATION_ENABLED = False

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':
    20,
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework_jwt.authentication.JSONWebTokenAuthentication',
     'rest_framework.authentication.SessionAuthentication',
     'rest_framework.authentication.BasicAuthentication'),
    'DEFAULT_FILTER_BACKENDS':
    ('django_filters.rest_framework.DjangoFilterBackend', ),
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer', )
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER':
    'apps.users.serializers.UserBasicSerializer',
    'PASSWORD_RESET_SERIALIZER':
    'apps.users.serializers.AllAuthPasswordResetSerializer',
}
REST_USE_JWT = True

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA':
    datetime.timedelta(days=7),  # 7 days for token expiration
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'voxsnap.utils.auth.jwt_response_payload_handler',
}

PLAYS_STATS_PERIOD = 3  # default period (in hours) for plays statistics data aggregation

THUMBNAIL_DEFAULT_STORAGE = 'voxsnap.utils.custom_storages.MediaStorage'
