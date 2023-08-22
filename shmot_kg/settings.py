from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-utdaokkb9r(1x#hqa7l=4vwuw*888f=s6)o9-ims=aiz7n$y)9'
DEBUG = True
ALLOWED_HOSTS = ['8459-5-8-11-254.ngrok-free.app','5.8.11.254','819f-212-112-100-242.ngrok-free.app','0632-46-251-195-48.ngrok-free.app', '1f32-46-251-221-50.ngrok-free.app', 'd370-212-112-100-242.ngrok-free.app', 'c5f1-212-112-100-242.ngrok-free.app',
                 'abaa-212-112-100-242.ngrok-free.app', '20c9-212-112-100-242.ngrok-free.app', '4977-212-112-100-242.ngrok-free.app', '127.0.0.1:8000', '127.0.0.1', '127.0.0.1:3000', 'a204-212-112-100-242.ngrok-free.app']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'rest_framework',
    'corsheaders',
    'colorfield',
]   

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:6900',
    'http://127.0.0.1:5500',
    'http://localhost:3000',
    'http://127.0.0.1:3001',
    'http://localhost:3001',
)

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'shmot_kg.urls'

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

WSGI_APPLICATION = 'shmot_kg.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_dev'),
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
