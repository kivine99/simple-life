from entities.plant import Plant
from entities.prey import Prey
from entities.predator import Predator
from entities.animal import Animal
from typing import Tuple
from entity_generator import EntityGenerator
import random
from pygame.math import Vector2

class Environment:
    
    def __init__(self, 
    map_dimensions: tuple[int, int],
    prey: list[Prey], 
    predators: list[Predator],
    plants: list[Plant]):
        self._map_dimensions = map_dimensions
        self._prey = prey
        self._predators = predators
        self._plants = plants
        self._entity_generator = EntityGenerator(map_dimensions)

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

    def add_random_plant(self) -> None:
        self._plants.append(self._entity_generator.generate_random_plant())

    def remove_plant(self, plant_to_remove: Plant) -> None:
        self._plants.remove(plant_to_remove)
        self.add_random_plant()

    def remove_animal(self, animal_to_remove: Animal) -> None:
        try: #TODO: consider refactoring this
            if isinstance(animal_to_remove, Prey):
                self._prey.remove(animal_to_remove)
            elif isinstance(animal_to_remove, Predator):
                self._predators.remove(animal_to_remove)
        except ValueError:
            pass 

    def out_of_bounds_x(self, pos: Vector2) -> bool:
        return (pos.x < 0 or pos.x > self._map_dimensions[0])

    def out_of_bounds_y(self, pos: Vector2) -> bool:
        return (pos.y < 0 or pos.y > self._map_dimensions[1])