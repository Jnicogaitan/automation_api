import os
from enum import Enum

class DevelopmentEnvironments(Enum):
    DEV1 = os.environ['DEV1']
    DEV3 = os.environ['DEV3']


