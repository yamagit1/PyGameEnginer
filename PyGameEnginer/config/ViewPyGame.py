from Singleton import cSingleton
import pygame
from game import cGame


class cViewPyGame(object):
    # instance
    __metaclass__ = cSingleton

    __myView = None


    def create(self, **kwargs):
        pygame.init()
        gameDisplay = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('A bit Racey')


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cGame().Exit()
        pygame.display.update()


    def render(self):
        pass


    def destroy(self):
        pass

