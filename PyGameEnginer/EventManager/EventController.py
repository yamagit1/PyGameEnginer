"""

"""

import sys
sys.path.append('../UtilManager')
import pygame
import time

from Singleton import cSingleton
from EventPyGameDriver import cEventPyGameDriver

# EVEN_RAW_TYPE
EVEN_RAW_KEY_UP         =   pygame.KEYUP
EVEN_RAW_KEY_DOWN       =   pygame.KEYDOWN
EVEN_RAW_MOUSE_MOVE     =   pygame.MOUSEMOTION
EVEN_RAW_MOUSE_UP       =   pygame.MOUSEBUTTONUP
EVEN_RAW_MOUSE_DOWN     =   pygame.MOUSEBUTTONDOWN

# EVENT_GROUP
EVENT_GROUP_KEYBOARD  = "EVENT_GROUP_KEYBOARD"
EVENT_GROUP_MOUSE     = "EVENT_GROUP_MOUSE"
EVENT_GROUP_JOYTICK   = "EVENT_GROUP_JOYTICK"

# KEY_STATUS
KS_NONE     = "KS_NONE"
KS_PRESSED  = "KS_PRESSED"
KS_HOLD     = "KS_HOLD"
KS_RELEASED = "KS_RELEASED"

# MOUSE_STATUS
MS_NONE     = "MS_NONE"
MS_MOVE     = "MS_MOVE"
MS_DRAGGED  = "MS_DRAGGED"
MS_RELEASED = "MS_RELEASED"

# MOUSE_KEY
MKS_NONE     = "MKS_NONE"
MKS_CLICK    = "MKS_CLICK"
MKS_DOUCLICK = "MKS_DOUCLICK"
MKS_HOLD     = "MKS_HOLD"
MKS_RELEASED = "MKS_RELEASED"

MK_LEFT_NONE    = "MK_LEFT_NONE"
MK_LEFT_CLICK   = "MK_LEFT_CLICK"
MK_LEFT_DOUCLICK= "MK_LEFT_DOUCLICK"
MK_LEFT_RELEASE = "MK_LEFT_RELEASE"

MK_RIGHT_NONE       = "MK_RIGHT_NONE"
MK_RIGHT_CLICK      = "MK_RIGHT_CLICK"
MK_RIGHT_DOUCLICK   = "MK_RIGHT_DOUCLICK"
MK_RIGHT_RELEASE    = "MK_RIGHT_RELEASE"

MK_MID_1_NONE       = "MK_MID_1_NONE"
MK_MID_1_CLICK      = "MK_MID_1_CLICK"
MK_MID_1_DOUCLICK   = "MK_MID_1_DOUCLICK"
MK_MID_1_RELEASE    = "MK_MID_1_RELEASE"



KEY_TIME_SWITH_HOLD = 2
MOUSE_TIME_SWITH_DOUCLICK = 2
class cEventController(object):
    # instance
    __metaclass__ = cSingleton

    __eventDriver = None
    __eventStore = {}
    __mousePos ={
        "X"     : 0,
        "Y"     : 0,
        "rel_X" : 0,
        "rel_Y" : 0
    }

    def get_Event(self):
        event = None
        if (cEventController.__eventDriver != None):
            event = cEventController.__eventDriver.get()
            cEventController.__eventDriver.clear()
        # self.__eventDriver().clear()
        return event


    def set_Driver(self, driver):
        cEventController.__eventDriver = driver


    def update(self, events):
        for event in events:
            if (event.type == EVEN_RAW_KEY_DOWN):
                try:
                    checkAvalible = cEventController.__eventStore[event.key]
                except:
                    cEventController.__eventStore[event.key] = \
                        {
                            "group"     : EVENT_GROUP_KEYBOARD,
                            "status"    : KS_PRESSED,
                            "timedow"   : time.time() * 1000,
                            "timehold"  : 0.0
                        }

            elif (event.type == EVEN_RAW_KEY_UP):
                del cEventController.__eventStore[event.key]

            elif (event.type == EVEN_RAW_MOUSE_MOVE):
                x, y = event.pos
                rel_x, rel_y = event.rel
                if (cEventController.__mousePos["X"] != x or cEventController.__mousePos["Y"] != y):
                    cEventController.__mousePos["X"]     = x
                    cEventController.__mousePos["Y"]     = y
                    cEventController.__mousePos["rel_X"] = rel_x
                    cEventController.__mousePos["rel_Y"] = rel_y

            elif (event.type == EVEN_RAW_MOUSE_DOWN):
                x,y = event.pos
                try:
                    checkAvalible = cEventController.__eventStore[event.button]
                    timecheck = time.time() * 1000
                    timeLastDown = cEventController.__eventStore[event.button]["timedow"]

                    cEventController.__eventStore[event.button]["status"]   = MKS_CLICK
                    cEventController.__eventStore[event.button]["timedow"]  = time.time() * 1000
                    cEventController.__eventStore[event.button]["timehold"] = 0.0
                    cEventController.__eventStore[event.button]["X"]        = x
                    cEventController.__eventStore[event.button]["Y"]        = y

                    if ((timecheck - timeLastDown ) < MOUSE_TIME_SWITH_DOUCLICK ):
                        checkAvalible = cEventController.__eventStore[event.button]["status"] = MKS_DOUCLICK

                except:
                    cEventController.__eventStore[event.button] = \
                        {
                            "group"     : EVENT_GROUP_MOUSE,
                            "status"    : MKS_CLICK,
                            "timedow"   : time.time() * 1000,
                            "timehold"  : 0.0,
                            "X"         : x,
                            "Y"         : y
                        }

            elif (event.type == EVEN_RAW_MOUSE_UP):
                cEventController.__eventStore[event.button]["status"] = MKS_RELEASED

        timecheck = time.time() * 1000
        for key,value in cEventController.__eventStore.items():
            if (value["group"] == EVENT_GROUP_KEYBOARD):
                if (value["status"] == KS_PRESSED and (timecheck - value["timedow"]) > KEY_TIME_SWITH_HOLD):
                    cEventController.__eventStore[key]["status"] = KS_HOLD
                if (value["status"] == KS_HOLD):
                    cEventController.__eventStore[key]["timehold"] = timecheck - cEventController.__eventStore[key]["timedow"]

            if (value["group"] == EVENT_GROUP_MOUSE):
                if (value["status"] == MKS_CLICK and (timecheck - value["timedow"]) > KEY_TIME_SWITH_HOLD):
                    cEventController.__eventStore[key]["status"] = KS_HOLD
                if (value["status"] == MKS_HOLD):
                    cEventController.__eventStore[key]["timehold"] = timecheck - cEventController.__eventStore[key]["timedow"]


    def get_Key_Infor(self, keyID):
        keyInfor = None

        try:
            keyInfor = cEventController.__eventStore[keyID]
        except:
            pass

        return keyInfor


    def get_Mouse_position(self):
        position = None
        try:
            position = cEventController.__mousePos
        except:
            pass

        return position

