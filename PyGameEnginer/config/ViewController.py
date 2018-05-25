import pygame
from Singleton import cSingleton

class cViewController(object):
    # instance
    __metaclass__ = cSingleton

    __myView = None


    def create_View(self, cView, **kwargs):
        try:
            cViewController.__myView = cView
            cViewController.__myView.create(**kwargs)
        except Exception as exc:
            raise Exception(exc)


    def update_View(self):
        cViewController.__myView.update()


    def render_View(self):
        pass


    def destroy_View(self):
        cViewController.__myView.destroy()


    def change_View(self, cView):
        cViewController.__myView = cView