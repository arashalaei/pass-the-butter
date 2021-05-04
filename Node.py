""" 
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since 5/5/2021
"""

class Node:
    __state:tuple
    __parent:any
    __previous_action:str

    def __init__(self, state, parent = None, previous_action = None) -> None:
        self.__state = state
        self.__parent = parent
        self.__previous_action = previous_action

    def get_state(self) -> tuple:
        return self.__state

    def get_parent(self) -> any:
        return self.__parent

    def get_previous_action(self) -> str:
        return self.__previous_action
