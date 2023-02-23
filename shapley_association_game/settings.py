from .settings_common import *


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'game.apps.GameConfig',
    'accounts.apps.AccountsConfig',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django_ses',
]

# 本番運用環境用にセキュリティキーを生成し環境変数から読み込む
SECRET_KEY = os.environ['SECRET_KEY']


# 本番運用では必ずFalse
DEBUG = False

# 許可するホスト名のリスト
ALLOWED_HOSTS = [os.environ['ALLOWED_HOSTS']]

# 静的ファイルを配置する場所
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

# Amazon SES関連設定
AWS_SES_ACCESS_KEY_ID = os.environ['AWS_SES_ACCESS_KEY_ID']
AWS_SES_SECRET_ACCESS_KEY = os.environ['AWS_SES_SECRET_ACCESS_KEY']
EMAIL_BACKEND = 'django_ses.SESBackend'

# ロギング
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
            'level': 'INFO',
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D', # ログローテーション（新しいファイルへの切り替え）間隔の単位（D=日）
            'interval': 1, # ログローテンション間隔（1日単位）
            'backupCount': 7, # 保存しておくログファイル数
        },
    },

    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    }
}

