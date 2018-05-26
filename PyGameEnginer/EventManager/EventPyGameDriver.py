"""

"""

import pygame
from EventBase import cEventBase

class cEventPyGameDriver(cEventBase):

    def get(self):
        return pygame.event.get()


    def clear(self):
        pygame.event.clear()

