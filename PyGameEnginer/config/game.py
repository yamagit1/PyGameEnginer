"""

"""

import time

import config
from Singleton import cSingleton
from ManagementState import cManagementState
from FPSController import cFPSController
from ViewController import cViewController

class cGame(object):
    __metaclass__ = cSingleton

    __isAlive = None
    __isRuning = None


    def __init__(self):
        cGame.__isAlive     = True
        cGame.__isRuning    = True


    def is_Alive(self):
        return cGame.__isAlive


    def is_Running(self):
        return cGame.__isRuning


    def Run(self):

        self._Init()

        while(self.is_Alive()):
            cFPSController().begin_Count()
            if (self.is_Running()):
                cManagementState().Update(True)
                print "game_lib Run"
            else:
                print "game_lib pause"
                cManagementState().Update(False)

            cViewController().update_View()
            cViewController().render_View()
            cFPSController().end_Count()

        self._Destroy()


    def Pause(self):
        cGame.__isRuning = False


    def Resume(self):
        cGame.__isRuning = True


    def Exit(self):
        cGame.__isAlive = False


    def _Init(self):
        print "gamelib _Init"


    def _Destroy(self):
        print "gamelib _Destroy"





