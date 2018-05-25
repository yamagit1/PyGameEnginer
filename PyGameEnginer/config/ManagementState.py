"""

"""
from Singleton import cSingleton

class cManagementState(object):
    __metaclass__ = cSingleton

    __currentState = None
    __nextState = None


    def __init__(self):
        __currentState = None
        __nextState = None


    def Update(self, isRun):
        if (self.__currentState != self.__nextState):
            if (self.__currentState != None):
                self.__currentState._destroy_State()

            if (self.__nextState != None):
                self.__nextState._init_State()

            self.__currentState = self.__nextState

        if (self.__currentState != None):
            if (isRun == True):
                self.__currentState.Update()

            self.__currentState.Render()


    def swith_State(self, nextState):
        self.__nextState = nextState