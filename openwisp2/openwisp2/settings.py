import os
from decimal import Decimal

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'G/*gegLQMtc23%)eKnDoHSx45EPvy]w(2XdVe+0I_oFCys7ngI'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '68.183.94.131',
    '68.183.94.131',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    # openwisp2 admin theme
    # (must be loaded here)
    'openwisp_utils.admin_theme',
    # all-auth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_extensions',
    # openwisp2 modules
    'openwisp_users',
    'openwisp_controller.pki',
    'openwisp_controller.config',
    'openwisp_controller.geo',
    # admin
    'django.contrib.admin',
    'django.forms',
    # other dependencies
    'sortedm2m',
    'reversion',
    'leaflet',
    'rest_framework',
    'rest_framework_gis',
    'channels',
    'raven.contrib.django.raven_compat',
]

EXTENDED_APPS = [
    'django_netjsonconfig',
    'django_x509',
    'django_loci',
]

AUTH_USER_MODEL = 'openwisp_users.User'
SITE_ID = 1
LOGIN_REDIRECT_URL = 'admin:index'
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'openwisp_utils.staticfiles.DependencyFinder',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
MIDDLEWARE = MIDDLEWARE_CLASSES

ROOT_URLCONF = 'openwisp2.urls'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_redis.RedisChannelLayer',
        'CONFIG': {'hosts': [('localhost', 6379)]},
        'ROUTING': 'openwisp_controller.geo.channels.routing.channel_routing',
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'openwisp_utils.loaders.DependencyLoader'
                ]),
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# FOR DJANGO REDIS

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

WSGI_APPLICATION = 'openwisp2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'openwisp2',
        'USER': 'openwisp2',
        'PASSWORD': 'oxyow2pg123456',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = '%s/static' % BASE_DIR
MEDIA_ROOT = '%s/media' % BASE_DIR
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# django x509 settings
DJANGO_X509_DEFAULT_CERT_VALIDITY = 1825
DJANGO_X509_DEFAULT_CA_VALIDITY = 3650

LEAFLET_CONFIG = {
    "DEFAULT_CENTER": [
        12.972442,
        77.580643
    ],
    "DEFAULT_ZOOM": 6,
    "TILES": [
        [
            "Map",
            "https://api.mapbox.com/styles/v1/nemesisdesign/cjazqqm1vbt6w2smqpkd8ayjo/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoibmVtZXNpc2Rlc2lnbiIsImEiOiJ4Mk1aLVRjIn0.iaXdEbuL7Nmy78L94TPjBA",
            "&copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors | Imagery by <a href=\"http://www.mapbox.com/\" target=\"_blank\">Mapbox</a>"
        ],
        [
            "Satellite",
            "https://api.mapbox.com/styles/v1/nemesisdesign/cjazqvg6ibtg92rn74hfbowkr/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoibmVtZXNpc2Rlc2lnbiIsImEiOiJ4Mk1aLVRjIn0.iaXdEbuL7Nmy78L94TPjBA",
            "&copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors | Imagery by <a href=\"http://www.mapbox.com/\" target=\"_blank\">Mapbox</a>"
        ]
    ]
}

# Set default email
DEFAULT_FROM_EMAIL = 'ox@oxynetz.com'
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
        'verbose': {
            'format': '\n\n[%(levelname)s %(asctime)s] module: %(module)s, process: %(process)d, thread: %(thread)d\n%(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'main_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'log/error.log'),
            'maxBytes': 5242880.0,
            'backupCount': 3,
            'formatter': 'verbose'
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': [
            'main_log',
            'console',
            'mail_admins',
        ]
    }
}

INFLUXDB_USER = 'root'
INFLUXDB_PASSWORD = 'root'
DJANGO_FREERADIUS_API_TOKEN = '165f9a790787fc38e5cc12c1640db2300648d9a2'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'run_checks': {
        'task': 'openwisp_monitoring.check.tasks.run_checks',
        'schedule': timedelta(minutes=5),
        'args': None,
        'relative': True
    },
}

for app in ['openwisp_monitoring.check',
            'openwisp_monitoring.device',
            'openwisp_monitoring.monitoring',
            'notifications']:
    INSTALLED_APPS.insert(INSTALLED_APPS.index('openwisp_controller.geo',) + 1, app)

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

TEMPLATES[0]['OPTIONS']['loaders'].insert(0, 'apptemplates.Loader')
if 'djcelery_email' not in INSTALLED_APPS:
    INSTALLED_APPS.append('djcelery_email')
    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/3'
# openwisp-radius, registration, CORS & social login
INSTALLED_APPS += [
  'corsheaders',
  'django_filters',
  'rest_framework.authtoken',
  'rest_auth',
  'rest_auth.registration',
  'allauth.socialaccount.providers.facebook',
  'allauth.socialaccount.providers.google',
  'openwisp_radius',
]
EXTENDED_APPS.append('django_freeradius')
DJANGO_FREERADIUS_RADIUSREPLY_MODEL = 'openwisp_radius.RadiusReply'
DJANGO_FREERADIUS_RADIUSGROUPREPLY_MODEL = 'openwisp_radius.RadiusGroupReply'
DJANGO_FREERADIUS_RADIUSCHECK_MODEL = 'openwisp_radius.RadiusCheck'
DJANGO_FREERADIUS_RADIUSGROUPCHECK_MODEL = 'openwisp_radius.RadiusGroupCheck'
DJANGO_FREERADIUS_RADIUSACCOUNTING_MODEL = 'openwisp_radius.RadiusAccounting'
DJANGO_FREERADIUS_NAS_MODEL = 'openwisp_radius.Nas'
DJANGO_FREERADIUS_RADIUSUSERGROUP_MODEL = 'openwisp_radius.RadiusUserGroup'
DJANGO_FREERADIUS_RADIUSPOSTAUTH_MODEL = 'openwisp_radius.RadiusPostAuth'
DJANGO_FREERADIUS_RADIUSBATCH_MODEL = 'openwisp_radius.RadiusBatch'
DJANGO_FREERADIUS_RADIUSGROUP_MODEL = 'openwisp_radius.RadiusGroup'
# CORS
MIDDLEWARE.insert(
    MIDDLEWARE.index('django.middleware.common.CommonMiddleware'),
    'corsheaders.middleware.CorsMiddleware'
)
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = ('POST',)
# social login
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
        ],
        'VERIFIED_EMAIL': True,
    },
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# these should be moved to ansible-openwisp2
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# firmware upgrade
INSTALLED_APPS += [
    'openwisp_controller.connection',
    'openwisp_firmware_upgrader',
]
OPENWISP_CUSTOM_OPENWRT_IMAGES = (
    ('oxwap1200-squashfs-sysupgrade.bin', {
        'label': 'OX WAP-1200',
        'boards': ('OXWAP1200',)
    }),
    ('oxwapc200-squashfs-sysupgrade.bin', {
        'label': 'OX WAP-1200',
        'boards': ('OXWAPC200',)
    }),
)

# radius subscriptions
INSTALLED_APPS += [  # noqa
    'openwisp_radius.subscriptions',
    'ordered_model',
    'plans',
    'payments',
]
MIGRATION_MODULES = {
    'plans': 'openwisp_radius.subscriptions.plans_migrations'
}
PAYMENT_HOST = 'oxwisp.oxynetz.com:4431'
PAYMENT_USES_SSL = True
PAYMENT_MODEL = 'plans.Payment'
PAYMENT_VARIANTS = {
    'default': ('payments.paypal.PaypalProvider', {
        'client_id': 'ASWGFeaCOCrZkGWU1Ow7r16OqLy3m1yxPhMkv3ocz_LDn1N4dzqxKK6abgJ4fRKxbQv1ealdkUIK1stR',
        'secret': 'ED_cPh9F7L9XqSJO1ALN1WHpHWxNA9JykM0DLCu22Y_vc-EpK59bv4PKCxuTNO70UhHqGVXP4jMjfjHg',
        'endpoint': 'https://api.sandbox.paypal.com',
        'capture': True
    })
}
PAYMENT_SUCCESS_URL = 'https://oxwisp.oxynetz.com:4431/loginpage/success.html'
PAYMENT_RENEW_SUCESS_URL = 'https://oxwisp.oxynetz.com:4431/loginpage/success.html?renew=1'
PAYMENT_FAILURE_URL = 'https://oxwisp.oxynetz.com:4431/loginpage/failure.html'
PLANS_APP_VERBOSE_NAME = 'Subscriptions'
PLANS_INVOICE_COUNTER_RESET = 3
PLANS_INVOICE_ISSUER = {
    'issuer_name': 'Oxynet Solutions',
    'issuer_street': '#G04 A-Block, King Space Meadows, ' \
                     'Sy No 85/3, Thanisandra Main Road',
    'issuer_zipcode': '560077',
    'issuer_city': 'Bangalore',
    'issuer_country': 'IN',
    'issuer_tax_number': '',
}
PLANS_INVOICE_TEMPLATE = 'invoice.html'
PLANS_TAX = Decimal('18.0')
PLANS_CURRENCY = 'USD'
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'openwisp_radius.subscriptions.serializers.RegisterSerializer',
}
REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'openwisp_radius.subscriptions.serializers.TokenSerializer',
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 4000
PAYMENT_ADMIN_EDITABLE = True
