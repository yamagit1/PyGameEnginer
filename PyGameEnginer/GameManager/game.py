"""

"""
import sys
sys.path.append('../VideoManager')
sys.path.append('../UtilManager')
sys.path.append('../StateManager')
sys.path.append('../EventManager')

from StateManager import cStateManager
from FPSController import cFPSController
from VideoController import cVideoController
from EventController import cEventController
from Singleton import cSingleton
import pygame

class cGame(object):
    __metaclass__ = cSingleton

    # private attribute
    __isAlive = None
    __isRuning = None


    def __init__(self):
        """
        """
        cGame.__isAlive     = True
        cGame.__isRuning    = True


    def is_Alive(self):
        """
        :return
        """
        return cGame.__isAlive


    def is_Running(self):
        """

        :return:
        """
        return cGame.__isRuning


    def Run(self):
        """

        :return:
        """
        self._Init()

        while(self.is_Alive()):
            # start fps counter
            cFPSController().begin_Count()

            # start get event
            self._check_Event()

            # update game
            if (self.is_Running()):
                cStateManager().Update(True)
                print "game_lib Run"
            else:
                print "game_lib pause"
                cStateManager().Update(False)

            # update view
            cVideoController().update()
            # render view
            cVideoController().render()
            # fps time wait
            cFPSController().end_Count()

        self._Destroy()


    def Pause(self):
        """

        :return:
        """
        cGame.__isRuning = False


    def Resume(self):
        """

        :return:
        """
        cGame.__isRuning = True


    def Exit(self):
        """

        :return:
        """
        cGame.__isAlive = False


    def _Init(self):
        """

        :return:
        """
        print "gamelib _Init"


    def _Destroy(self):
        """

        :return:
        """
        print "gamelib _Destroy"


    def _check_Event(self):
        event = cEventController().get_Event()
        self._on_Controll_Event(event)
        cStateManager().forward_Event(event)
        cEventController().update(event)

    def _on_Controll_Event(self, event):
        pass