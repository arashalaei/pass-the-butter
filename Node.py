""" 
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since 5/5/2021
"""

class Node:
    __state:tuple
    __parent:any
    __previous_action:str
    __cost:int
    __fn:int

    def __init__(self, state, parent = None, previous_action = None, cost = 0, fn = 0) -> None:
        self.__state = state
        self.__parent = parent
        self.__previous_action = previous_action
        self.__cost = cost
        self.__fn = fn

    def get_state(self) -> tuple:
        return self.__state

    def get_parent(self) -> any:
        return self.__parent

    def get_previous_action(self) -> str:
        return self.__previous_action

    def get_cost(self) -> int:
        return self.__cost

    def get_fn(self) -> int:
        return self.__fn