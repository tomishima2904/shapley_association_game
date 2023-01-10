from .settings_common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# メール処理で使うバックエンドを定義
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'game': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        },
    },

    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    }
}

