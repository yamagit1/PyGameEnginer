"""

"""

import time

from ManagementState import cManagementState
import config

class cGame(object):
    # instance
    __isAlive = None
    __isRuning = None
    __instance = None

    def __init__(self):
        if cGame.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            cGame.__instance = self

        cGame.__isAlive = True
        cGame.__isRuning = True


    @staticmethod
    def get_Instance():
        """ Static access method. """
        if cGame.__instance == None:
            cGame()
        return cGame.__instance


    def is_Alive(self):
        return cGame.__isAlive


    def is_Running(self):
        return cGame.__isRuning


    def Run(self):

        self._Init()

        while(self.is_Alive()):
            if (self.is_Running()):
                cManagementState.get_Instance().Update(True)
                print "game_lib Run"
            else:
                print "game_lib pause"
                cManagementState.get_Instance().Update(False)
            time.sleep(float(1)/float(5))

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





