"""

"""

import pygame
from VideoBase import cVideoBase

class cVideoPyGameDriver(cVideoBase):
    # instance
    def __init__(self):
        print "__init__"

    def create(self, **kwargs):
        super(cVideoPyGameDriver, self).create(**kwargs)

        videoInfor =  pygame.display.Info()

        pygame.display.set_caption(self._myTitle)

        if (self._fullScreen == True):
            pygame.display.set_mode((videoInfor.current_w, videoInfor.current_h), pygame.FULLSCREEN)
        else:
            pygame.display.set_mode((self._width, self._hight))


    def update(self):
        pygame.display.update()
