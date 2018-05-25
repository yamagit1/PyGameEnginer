import sys

sys.path.append('../PyGameEnginer/config')

from game import cGame
from ManagementState import cManagementState
from State import cState
from FPSController import cFPSController
from ViewController import cViewController
from  ViewPyGame import cViewPyGame
from StateLogo import *

class GameDemo(cGame):
    def __init__(self):
        cGame.__init__(self)


    def _Init(self):
        print "gamedemo __Init"
        cManagementState().swith_State(cStateLogo())
        cFPSController().config_FPS_Limit(1)
        cViewController().create_View(cViewPyGame())

    def _Destroy(self):
        print "gamedemo __Destroy"


GameDemo().Run()




