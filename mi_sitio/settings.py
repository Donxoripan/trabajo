"""
Django settings for mi_sitio project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*(uz4gctkt10wa@s(!lydohne0&8#rj3vo5$d2a+h!vnn%xh^)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Nuestras aplicaciones
    'usuarios',
    'inicio',
    'comentarios',
    'videos',
]

MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 #Middleware de seguridad
 'django.contrib.sessions.middleware.SessionMiddleware',
 #para sesiones
 'django.middleware.common.CommonMiddleware',
 #Middleware común, necesario para el funcionamiento de Django
 'django.middleware.csrf.CsrfViewMiddleware', 
 #Middleware para protección contra ataques CSRF
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 #Middleware para autenticación de usuarios
 'django.contrib.messages.middleware.MessageMiddleware',
 #Middleware para mensajes
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
#Middleware para protección contra ataques de clickjacking
]


ROOT_URLCONF = 'mi_sitio.urls'

import os
TEMPLATES = [
    {
 'BACKEND': 'django.template.backends.django.DjangoTemplates',
 'DIRS': [os.path.join(BASE_DIR, 'templates')], # Directorio global de templates
 'APP_DIRS': True, # Habilita la búsqueda de templates dentro de las apps
 'OPTIONS': 
        {
        'context_processors': 
            [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',# Necesario para que los templates accedan al objeto request
            'django.contrib.auth.context_processors.auth', # Proporciona el usuario en los templates
            'django.template.context_processors.csrf', #Para protección CSRF
            'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'mi_sitio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

from decouple import config
import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.mysql',
 'NAME': config('DB_NAME'),
 'USER': config('DB_USER'),
 'PASSWORD': config('DB_PASSWORD'),
 'HOST': 'localhost',
 'PORT': '3306',
 }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # Directorio donde colocaremos archivos estáticos globales
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Directorio para almacenar archivos subidos por el usuario


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
