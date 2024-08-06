import json
from pathlib import Path
import os

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = True

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

# 读取系统环境变量 `ENV`
env = os.environ['CONF']
print("env: ", env, "--end----")
print("DBENV", os.environ['DBENV'])

if not env:
    exit()

env = json.loads(env)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env['db_name'],
        'USER': env['db_user'],
        'PASSWORD': env['db_password'],
        'HOST': env['db_host'],
        'PORT': env['db_port'],
        # 数据库使用的字符集
        'CHARSET': 'utf8',
        'timezone': 'Asia/Shanghai'
    },
    'debug': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rmflogwj',
        'USER': 'rmflogwj',
        'PASSWORD': 'tl8ZUzUzra3krWnAeXSsSwRktHHdo5bK',
        'HOST': 'tiny.db.elephantsql.com',
        'PORT': '5432',
        # 数据库使用的字符集
        'CHARSET': 'utf8',
    }

}

INSTALLED_APPS = (
    "Bili.models",
    "Bili.db",
    # "stock.entity",
)
