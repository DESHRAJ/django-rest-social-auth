"""
Django settings for example_project project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5i830%k0$u*+@0290eq&lb!c%h3cxknj01ygyck-@el-5__y4y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'social.apps.django_app.default',
    'rest_social_auth',

    'users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',  # django 1.6
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.security.SecurityMiddleware',  # django 1.7
)


ROOT_URLCONF = 'config.urls'


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

AUTH_USER_MODEL = 'users.CustomUser'

# DRF settings

# social auth settings
# valid redirect domain for all apps: http://restsocialexample.com:8000/
SOCIAL_AUTH_FACEBOOK_KEY = '295137440610143'
SOCIAL_AUTH_FACEBOOK_SECRET = '4b4aef291799a7b9aaf016689339e97f'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', ]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '976099811367-ihbmg1pfnniln9qgfacleiu41bhl3fqn.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'JaiLLvY1BK97TSy5_xcGWDhp'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', ]

SOCIAL_AUTH_TWITTER_KEY = 'gCrpEpNxpWkAE6Cul98OzAWTk'
SOCIAL_AUTH_TWITTER_SECRET = '7SYSRpYY4amW5kiNXUAxUDdWS7G3nHytRIGHbDVTByzBfsqDJl'


AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',  # OAuth1.0
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'users.social_pipeline.auto_logout',  # custom action
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'users.social_pipeline.save_avatar',  # custom action
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'rest_social_auth': {
            'handlers': ['console', ],
            'level': "DEBUG",
        },
    }
}
