from behaviour import Behaviour
from typing import Optional

class Memory:

    def __init__(self):
        self.__last_behaviour = None

    def get_last_behaviour(self) -> Optional[Behaviour]:
        return self.__last_behaviour

    def set_last_behaviour(self, new_behaviour: Behaviour) -> None:
        self.__last_behaviour = new_behaviour