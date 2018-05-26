"""

"""
import sys
import sys
sys.path.append('../PyGameEnginer/StateManager')

from StateManager import cStateManager


class cStateMain(object):

    __count = 0

    def _init_State(self, *args):
        print "__initState cStateMain"


    def Update(self):
        self.__count += 1
        print "Update cStateMain " + str(self.__count)


    def Render(self):
        print "Render cStateMain"


    def _destroy_State(self):
        print "_Destroy cStateMain"

    def on_Controll_Event(self, event):
        print event