from prey import Prey
from predator import Predator
from plant import Plant
from typing import Tuple
from animal import Animal
from entity_generator import EntityGenerator
import random

class Environment:
    
    def __init__(self, 
    map_dimensions: tuple,
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

    def update_animal_energy(self, animal: Animal, energy_amount: float) -> None:
        animal.update_energy(energy_amount)

    def remove_animal(self, animal_to_remove: Animal) -> None:
        try: #TODO: consider refactoring this
            if isinstance(animal_to_remove, Prey):
                self._prey.remove(animal_to_remove)
            elif isinstance(animal_to_remove, Predator):
                self._predators.remove(animal_to_remove)
        except ValueError:
            pass 

    def move_animal(self, animal_to_move, velocity):
        position = animal_to_move.get_position()

        last_behaviour = animal_to_move.get_memory().get_last_behaviour()

        if last_behaviour and (position[0] < 0 or position[0] > self._map_dimensions[0] or
                            position[1] < 0 or position[1] > self._map_dimensions[1]):
            last_behaviour.invert_previous_force_angle()

        if position[0] < 0:
            position[0] = 0 
            velocity.x = -velocity.x 

        elif position[0] > self._map_dimensions[0]:
            position[0] = self._map_dimensions[0]
            velocity.x = -velocity.x

        if position[1] < 0:
            position[1] = 0
            velocity.y = -velocity.y 

        elif position[1] > self._map_dimensions[1]:
            position[1] = self._map_dimensions[1]
            velocity.y = -velocity.y

        animal_to_move.set_velocity(velocity)
        animal_to_move.update_position()
