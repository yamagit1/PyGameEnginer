"""

"""

import sys
sys.path.append('../UtilManager')

from Singleton import cSingleton

class cVideoBase(object):
    # instance
    __metaclass__ = cSingleton

    _myTitle       = None  # The content title bar in mode window
    _fullScreen    = None  # The run in mode full screen
    _maxWidth      = None  # The maximum screen width
    _maxHight      = None  # The maximum screen height
    _minWidth      = None  # The minimum screen width
    _minHight      = None  # The minimum screen height
    _currWidth     = None  # The current screen width
    _currHight     = None  # The current screen height
    _posTop        = None  # The position top window
    _posLeft       = None  # The position left window

    def create(self, **kwargs):
        cVideoBase._myTitle     = "Game Python Enginer"
        cVideoBase._fullScreen  = False
        cVideoBase._maxWidth    = 300
        cVideoBase._maxHight    = 300
        cVideoBase._minWidth    = 100
        cVideoBase._minHight    = 100
        cVideoBase._width   = 100
        cVideoBase._hight   = 100
        cVideoBase._posTop      = 0
        cVideoBase._posLeft     = 0

        if ("title" in kwargs.keys()):
            cVideoBase._myTitle =  kwargs["title"]

        if ("fullScreen" in kwargs.keys()):
            cVideoBase._fullScreen = kwargs["fullScreen"]

        if ("maxWidth" in kwargs.keys()):
            cVideoBase._maxWidth = kwargs["maxWidth"]

        if ("maxHight" in kwargs.keys()):
            cVideoBase._maxHight = kwargs["maxHight"]

        if ("minWidth" in kwargs.keys()):
            cVideoBase._minWidth = kwargs["minWidth"]

        if ("minHight" in kwargs.keys()):
            cVideoBase._minHight = kwargs["minHight"]

        if ("width" in kwargs.keys()):
            cVideoBase._width = kwargs["width"]

        if ("hight" in kwargs.keys()):
            cVideoBase._hight = kwargs["hight"]

        if ("posTop" in kwargs.keys()):
            cVideoBase._posTop = kwargs["posTop"]

        if ("posLeft" in kwargs.keys()):
            cVideoBase._posLeft = kwargs["posLeft"]


    def update(self):
        pass


    def render(self):
        pass


    def destroy(self):
        pass
