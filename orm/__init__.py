import os

import pymysql

pymysql.install_as_MySQLdb()

os.environ['CONF'] = '{"db_host": "110.41.145.76", "db_port": "3306", "db_user": "root",' \
                     ' "db_password": "mysql@2024", "db_name": "mixed"}'
