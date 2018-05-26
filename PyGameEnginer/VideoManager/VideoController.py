"""

"""
import sys
sys.path.append('../UtilManager')

from Singleton import cSingleton

class cVideoController(object):
    # instance
    __metaclass__ = cSingleton

    __videoDriver = None


    def create_View(self, cView, **kwargs):
        try:
            cVideoController.__videoDriver = cView
            cVideoController.__videoDriver.create(**kwargs)
        except Exception as exc:
            raise Exception(exc)


    def update(self):
        cVideoController.__videoDriver.update()


    def render(self):
        pass


    def destroy(self):
        cVideoController.__videoDriver.destroy()


    def change_Driver(self, driver):
        cVideoController.__videoDriver = driver