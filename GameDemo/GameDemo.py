import sys

sys.path.append('../PyGameEnginer/config')

from game import cGame
from ManagementState import cManagementState
from State import cState
from StateLogo import *

class GameDemo(cGame):
    def __init__(self):
        cGame.__init__(self)


    def _Init(self):
        print "gamedemo __Init"

    def _Destroy(self):
        print "gamedemo __Destroy"

GameDemo()
cManagementState()
cManagementState.get_Instance().swith_State(cStateLogo())
GameDemo.get_Instance().Run()




