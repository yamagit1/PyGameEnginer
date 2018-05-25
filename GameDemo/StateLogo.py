"""

"""
import sys
sys.path.append('../PyGameEnginer/config')
from ManagementState import cManagementState

from StateMain import *

class cStateLogo(object):

    __count = 0
    def __init__(self):
        self.__count = 5


    def _init_State(self, *args):
        print "__initState logo"


    def Update(self):
        print "Update logo " + str(self.__count)
        self.__count -= 1
        if (self.__count == 0):
            cManagementState().swith_State(cStateMain())


    def Render(self):
        print "Render logo"



    def _destroy_State(self):
        print "_Destroy logo"