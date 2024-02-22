import os
import orm.manage


def setup():
    os.environ['PYTHONPATH'] = os.getcwd()
    print(os.environ['PYTHONPATH'])


setup()
