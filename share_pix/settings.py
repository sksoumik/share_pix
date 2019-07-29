
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ze134*o@h%ubp-c!2dphdh02(!#6qmc(75p2)(-di%738nh#fg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'share_pix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'share_pix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
# MEDIA_URL is the base URL to serve the media files uploaded by users
MEDIA_URL = '/media/'
# MEDIA_ROOT is the local path where they reside
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# For sending password reset link using email in case the user forgets the password.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = [
'django.contrib.auth.backends.ModelBackend',
'account.authentication.EmailAuthBackend',
'social_core.backends.facebook.FacebookOAuth2',
'social_core.backends.twitter.TwitterOAuth',
'social_core.backends.google.GoogleOAuth2',
]

# social auth settings
SOCIAL_AUTH_FACEBOOK_KEY = '429952364258636' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '6e89ba97e745e59625a960e3a77b26af' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = '0Ke4vaFEM1upy24psCRLIgOk0' # Twitter Consumer Key
SOCIAL_AUTH_TWITTER_SECRET = 's4fpJ9xw6zWIU7lNTFRC93fXmtmwjbpdrpS8lzsFL6zKv3b1I7 ' # Twitter Consumer Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '759453334070-esokajlphs7om7bv159qbj71ocei6vlr.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'UtzjVFwqzrCoG5ydt2UopT9D'