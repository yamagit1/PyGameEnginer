"""

"""

import config
import time

from Singleton import cSingleton


DEFAULT_FPS_LIMIT = 10

class cFPSController(object):
    # instance
    __metaclass__ = cSingleton

    __fpsLimit          = 0.0
    __fpsTimeFrame      = 0.0
    __fpsTimeFrameReal  = 0.0
    __fpsTimeStart      = 0.0

    def __init__(self, fpsLimit=1.0):
        cFPSController.__fpsLimit = float(fpsLimit)
        cFPSController.__fpsTimeFrame = float(1) / float(fpsLimit)
        cFPSController.__fpsTimeFrameReal = 0.0
        cFPSController.__fpsTimeStart = 0.0


    def get_FPS_Limit(self):
        return cFPSController.__fpsLimit


    def get_FPS_Time_Frame(self):
        return cFPSController.__fpsTimeFrame


    def get_FPS_Real_Time_Frame(self):
        return cFPSController.__fpsTimeFrameReal


    def config_FPS_Limit(self, fpsLimit):
        cFPSController.__fpsLimit           = float(fpsLimit)
        cFPSController.__fpsTimeFrame       = float(1)/float(fpsLimit)
        cFPSController.__fpsTimeFrameReal   = 0.0
        cFPSController.__fpsTimeStart       = 0.0

    def begin_Count(self):
        cFPSController.__fpsTimeStart = time.time()


    def end_Count(self):
        fpsTimeUpdate = time.time() - cFPSController.__fpsTimeStart

        if (fpsTimeUpdate < cFPSController.__fpsTimeFrame):
            cFPSController.__fpsTimeFrameReal = fpsTimeUpdate
            time.sleep(cFPSController.__fpsTimeFrame - fpsTimeUpdate)
        else:
            cFPSController.__fpsTimeFrameReal = cFPSController.__fpsTimeFrame
            time.sleep(0)