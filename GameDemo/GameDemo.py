import sys
sys.path.append('../PyGameEnginer/GameManager')
sys.path.append('../PyGameEnginer/VideoManager')
sys.path.append('../PyGameEnginer/StateManager')
sys.path.append('../PyGameEnginer/UtilManager')
sys.path.append('../PyGameEnginer/EventManager')

import pygame
from game import cGame
from FPSController import cFPSController
from StateManager import cStateManager
from VideoController import cVideoController
from VideoPyGameDriver import cVideoPyGameDriver
from EventController import cEventController
from EventPyGameDriver import cEventPyGameDriver
from StateLogo import *

class GameDemo(cGame):

    def _Init(self):
        print "gamedemo __Init"
        pygame.init()
        cStateManager().swith_State(cStateLogo())
        cFPSController().config_FPS_Limit(1)
        cVideoController().create_View(cVideoPyGameDriver(), title="Game python", fullScreen=False, width=500, hight=500)
        cEventController().set_Driver(cEventPyGameDriver())


    def _Destroy(self):
        print "gamedemo __Destroy"


    def _on_Controll_Event(self, events):
        for event in events:
            if (event.type == pygame.QUIT):
                cGame().Exit()

GameDemo().Run()




