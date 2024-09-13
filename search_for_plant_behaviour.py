from behaviour import Behaviour
from prey import Prey
from plant import Plant
from typing import Tuple

class SearchForPlantBehaviour(Behaviour):
    def __init__(self, prey: Prey, plants: Tuple[Plant, ...]):
        self.__prey = prey
        self.__plants = plants

    def execute(self):
        self.__prey.set_position(self.__prey.calculate_next_position())