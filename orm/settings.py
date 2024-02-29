from pathlib import Path

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"
TIME_ZONE = 'Asia/Shanghai'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# BASE_DIR = Path(__file__).parent
BASE_DIR = '/opt/dolphinscheduler/data/root/sgDW/resource/'

# DATABASES = {
#     'default': {
#         'engine': 'sqlite',
#         # 'name': BASE_DIR/'batch.models',
#         'name': BASE_DIR + 'sg_erp.models',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rmflogwj',
        'USER': 'rmflogwj',
        'PASSWORD': 'tl8ZUzUzra3krWnAeXSsSwRktHHdo5bK',
        'HOST': 'tiny.db.elephantsql.com',
        'PORT': '5432',
        # 数据库使用的字符集
        'CHARSET': 'utf8',
        # 数据库时区设定
        'TIME_ZONE': 'Asia/Shanghai',
    }

}

INSTALLED_APPS = (
    "Bili.models",
    "Bili.db",
)
