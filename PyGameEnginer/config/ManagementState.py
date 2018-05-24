
class cManagementState(object):
    __currentState = None
    __nextState = None
    __instance = None


    def __init__(self):
        if cManagementState.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            cManagementState.__instance = self

        __currentState = None
        __nextState = None


    @staticmethod
    def get_Instance():
        """ Static access method. """
        if cManagementState.__instance == None:
            cManagementState()
        return cManagementState.__instance


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