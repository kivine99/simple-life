from prey import Prey
from predator import Predator
from plant import Plant
from typing import Tuple

class Environment:
    def __init__(self, 
    prey: list[Prey], 
    predators: list[Predator],
    plants: list[Plant]):
        self._prey = prey
        self._predators = predators
        self._plants = plants

    def get_prey(self) -> Tuple[Prey, ...]:
        return tuple(self._prey)

    def get_predators(self) -> Tuple[Predator, ...]:
        return tuple(self._predators)

    def get_plants(self) -> Tuple[Plant, ...]:
        return tuple(self._plants)

    def add_prey(self, prey_to_add: Prey) -> None:
        self._prey.append(prey_to_add)

    def add_predator(self, predator_to_add: Predator) -> None:
        self._predator.append(predator_to_add)

    def remove_plant(self, plant_to_remove: Plant) -> None:
        self._plants.remove(plant_to_remove)