"""

"""
import sys
sys.path.append('../PyGameEnginer/StateManager')

from StateManager import cStateManager

from StateMain import *
import pygame

class cStateLogo(object):

    __count = 0
    def __init__(self):
        self.__count = 100


    def _init_State(self, *args):
        print "__initState logo"


    def Update(self):
        print "Update logo " + str(self.__count)
        self.__count -= 1
        if (self.__count == 0):
            cStateManager().swith_State(cStateMain())


    def Render(self):
        print "Render logo"



    def _destroy_State(self):
        print "_Destroy logo"


    def on_Controll_Event(self, events):
        for event in events:
            if (event.type == pygame.KEYDOWN):
                print event.key