import os

from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5ic#bgjm9y4^z4l%^9i5rsb*7kp+p(m*)b5*n1*==k-t*e*7ct'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'mysite.com',
    'localhost',
    '127.0.0.1',
    'e2fb692c.ngrok.io',
]


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'images.apps.ImagesConfig',
    'sorl.thumbnail',
    'actions.apps.ActionsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookmarks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmarks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


# Login
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


#authenticate
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    #custom
    'account.authentication.EmailAuthBackend',

    #facebook
    'social_core.backends.facebook.FacebookOAuth2',

    #twitter
    'social_core.backends.twitter.TwitterOAuth',

    #google
    'social_core.backends.google.GoogleOAuth2',
]


# Facebook auth
SOCIAL_AUTH_FACEBOOK_KEY = '245279936202832'
SOCIAL_AUTH_FACEBOOK_SECRET = '1b19a73b0ab8acb44a331acec6e198f1'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Twitter auth
SOCIAL_AUTH_TWITTER_KEY = 'QdbTTVtiPhP89RufxbbCp4741'
SOCIAL_AUTH_TWITTER_SECRET = 'Jj5pzG5zywi3npMYPAuc2gKVhAB5EE6Vmy42n4Ooh1CN33Isu2'

# Google auth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '450325457331-pcqkq7g6dp47nfvb6b88241h490frg4p.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '2FH_rYEJ84qaD6547-5AHzeu'


# Users url
ABSOLUTE_URL_OVERRIDES = {
    'auth.user':lambda u: reverse_lazy('user_detail', args=[u.username])
}


# Redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0





















