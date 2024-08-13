import sys
from pathlib import Path


def init():
    BASE_DIR = Path(__file__).parent.parent
    sys.path.append(str(BASE_DIR))
