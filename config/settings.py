import sys

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIRS = BASE_DIR / 'apps'
sys.path.append(str(APP_DIRS))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ygpj0e$o3-$f0*+vazv(h7osm*=v51($n-e&&&yc!reqs+(b26'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DJANGO_EXTENSIONS = [
    'django_extensions',
    'widget_tweaks',
]

MY_APPS = [f'{dir_apps.name}.apps.{dir_apps.name.title()}Config' for dir_apps in APP_DIRS.iterdir()]
INSTALLED_APPS = MY_APPS + DJANGO_APPS + DJANGO_EXTENSIONS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'apps' / 'core' /'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'libraries': {
                'core_tags': 'core.templatetags.core_tags',
                'get_mp': 'forum.templatetags.forum_tags',
            },
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'forum.context_processors.boards_urls',
                'forum.context_processors.get_search_forms',
                'core.context_processors.get_theme_user',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'apps' / 'core' /'static',
]

# account
LOGOUT_REDIRECT_URL = 'forum:index'
LOGIN_REDIRECT_URL = 'forum:index'
LOGIN_URL = 'registration:login'

# email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_HOST_USER = '9650522bb15611'
# EMAIL_HOST_PASSWORD = '9dfe19de3b6fc4'
# EMAIL_PORT = '2525'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
