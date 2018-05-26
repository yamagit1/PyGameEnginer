"""

"""

import sys
sys.path.append('../UtilManager')

from Singleton import cSingleton

class cEventBase(object):
    # instance
    __metaclass__ = cSingleton

    def get(self):
        pass

    def clear(self):
        pass