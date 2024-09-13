from prey import Prey
from predator import Predator
from plant import Plant
from typing import Tuple

class Environment:
    def __init__(self, 
    prey: list[Prey], 
    predators: list[Predator],
    plants: list[Plant]):
        self.__prey = prey
        self.__predators = predators
        self.__plants = plants

    def get_prey(self) -> Tuple[Prey, ...]:
        return tuple(self.__prey)

    def get_predators(self) -> Tuple[Predator, ...]:
        return tuple(self.__predators)

    def get_plants(self) -> Tuple[Plant, ...]:
        return tuple(self.__plants)

    def add_prey(self, prey_to_add: Prey) -> None:
        self.__prey.append(prey_to_add)

    def add_predator(self, predator_to_add: Predator) -> None:
        self.__predator.append(predator_to_add)