import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'insecure-local-development-key-change-before-deploy')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() == 'true'
ALLOWED_HOSTS = [h.strip() for h in os.environ.get('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost,testserver').split(',') if h.strip()]
INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','dealership']
MIDDLEWARE = ['config.cors_middleware.LocalFrontendCorsMiddleware','django.middleware.security.SecurityMiddleware','whitenoise.middleware.WhiteNoiseMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF = 'config.urls'
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'dealership'/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'config.wsgi.application'
DATABASES = {'default': {'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
AUTH_PASSWORD_VALIDATORS = [] if DEBUG else [{'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},{'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},{'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE='en-us'
TIME_ZONE='Asia/Kolkata'
USE_I18N=True
USE_TZ=True
STATIC_URL='static/'
STATICFILES_DIRS=[BASE_DIR/'frontend'/'static']
STATIC_ROOT=BASE_DIR/'staticfiles'
STORAGES={'default': {'BACKEND':'django.core.files.storage.FileSystemStorage'}, 'staticfiles': {'BACKEND':'whitenoise.storage.CompressedManifestStaticFilesStorage'}}
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
SESSION_COOKIE_HTTPONLY=True
X_FRAME_OPTIONS='DENY'
if not DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF=True
    SESSION_COOKIE_SECURE=True
    CSRF_COOKIE_SECURE=True
