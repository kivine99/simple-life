from environment import Environment
from prey import Prey
from predator import Predator
from plant import Plant
from memory import Memory
from pygame.math import Vector2
import random
from typing import Tuple
import math

class EnvironmentSetup:
    
    def __init__(self, map_size: Tuple[int, int], num_prey: int, num_predators: int, num_plants: int):
        self._map_size = map_size
        self._num_prey = num_prey
        self._num_predators = num_predators
        self._num_plants = num_plants

    def initialize(self) -> Environment:
        prey_list = []
        predator_list = []
        plant_list = []

        for i in range(self._num_prey):
            prey_position = self._random_position()
            prey = Prey(
                position=prey_position,
                velocity=Vector2(0, 0),  
                mass=1.0,
                max_force=.04,
                max_speed=2.0,
                orientation=0.0,
                vision_range=150.0,
                fov=3*math.pi/4,
                memory=Memory(), 
                genome=None,
                energy=100,
                radius=5.0,
                color=(255, 0, 0)  
            )
            prey_list.append(prey)

        for i in range(self._num_plants):
            plant_position = [random.uniform(0, self._map_size[0]),
                              random.uniform(0, self._map_size[1])]
            plant = Plant(
                position=plant_position,
                radius=5,
                color=(0, 255, 0) 
            )
            plant_list.append(plant)

        return Environment(self._map_size, prey_list, predator_list, plant_list)

    def _random_position(self) -> Vector2:
        return Vector2(
            random.uniform(0, self._map_size[0]),
            random.uniform(0, self._map_size[1])   
        )