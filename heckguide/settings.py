from pathlib import Path
import os
import environ
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = ROOT_DIR

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool("DJANGO_DEBUG", False)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["heckguide.com"])


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.discord',
    'invitations',
	'home',
    'blog',
	'django_summernote',
    'allies',
    'world',
    'mathfilters',
	'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
]

SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGIN_REDIRECT_URL = "homepage"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_ADAPTER = 'invitations.models.InvitationsAdapter'
INVITATIONS_INVITATION_ONLY = True
INVITATIONS_ACCEPT_INVITE_AFTER_SIGNUP = True

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}


#Tokens
HECKFIRE_API_TOKEN = env("TOKEN")
STAY_ALIVE_TOKEN = env("STAY_TOKEN")
TOKEN_128 = env("TOKEN_128")
TOKEN_23 = env("TOKEN_23")
TOKEN_10 = env("TOKEN_10")
TOKEN_129 = env("TOKEN_129")
TITANHOOK_10 = env("TITANHOOK_10")
TITANHOOK_128 = env("TITANHOOK_128")
TITANHOOK_129 = env("TITANHOOK_129")
TITANHOOK_23 = env("TITANHOOK_23")


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

if not DEBUG:
	INSTALLED_APPS.append('whitenoise.runserver_nostatic')
	MIDDLEWARE.append ('whitenoise.middleware.WhiteNoiseMiddleware')

ROOT_URLCONF = 'heckguide.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, 'templates/'), os.path.join(BASE_DIR, 'templates', 'allauth')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'heckguide.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": env.db("DATABASE_URL", default="postgres://postgres:postgres@localhost:5432/heckguide")
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/' 
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')

if DEBUG:
	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if not DEBUG:
	STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
	SECURE_HSTS_SECONDS = 31536000
	SECURE_SSL_REDIRECT = True
	SESSION_COOKIE_SECURE = True
	CSRF_COOKIE_SECURE = True
	SECURE_HSTS_INCLUDE_SUBDOMAINS = True
	SECURE_HSTS_PRELOAD = True
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	EMAIL_HOST = env("EMAIL_HOST")
	EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
	EMAIL_HOST_USER = env('EMAIL_HOST_USER')
	EMAIL_USE_TLS = True
	EMAIL_PORT = 25
	SERVER_EMAIL = EMAIL_HOST_USER
	DEFAULT_FROM_EMAIL = SERVER_EMAIL
	
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}
	
# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Ally Prices
PRICES_1 = ["102428","107549","112926","118572","130725","137261","144124","151330","166840","175182","183941","193138","212933","223579","234757","246494","271758","285345","299612","314592","346837","364178","382386","401505","442659","464791","488030","512431","564954","593201","622861","654004","721039","757090","794944","834691","920246","966258"]

PRICES_2 = ["1014570","1065298","1174490","1233214","1294874","1359617","1498976","1573924","1652620","1735251","1913113","2008768","2109206","2214666","2441668","2563751","2691938","2826534","3116253","3272065","3435668","3607451","3977214","4176074","4384877","4604120","5076042","5329844","5596336","5876152","6478456","6802378","7142496","7499620","8268331","8681747","9115834","10552716","11080351","11634368","12216086","13468234","14141645","14848727","15591163","17189257","18048719","18951154","19898711"]

PRICES_3 = ["21938328","23035244","24187006","25396356","27999481","29399455","30869427","32412898","35735219","37521979","39398077","41367980","45608197","47888606","50283036","52797187","58208898","61119342","64175309","67384074","74290940","78005487","81905761","86001049","94816156","99556963"]

PRICES_4 = ["104534811","109761551","115249628","121012109","133415849","140086641","147090973","154445521","170276186","178789995","187729494","197115968","217320354","228186371","239595689","251575473","277361958","291230055","305791557","321081134","337135190","353991949","371691546","390276123","406789929","430279425","451793396","474383065","498102218","523007328","549157694","576615578","605446356","635718673","667504606","700879836","735923827","772720018","811356018","851923818","894520008","939246008","986208308","996009477"]

PRICES_5 = ["1035518723","1087294659","1141659391","1198742360","1258679478","1321613451","1457078829","1529932770","1606429408","1686450878","1771088421","1859642842","1952624984","2050256233","2152769044","2260407496","2373427870","2492099263","2616704226","2747539437","2884916408","3029162228","3180620339","3339651355","3506633922","3681965618","3866063898"]