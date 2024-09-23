from environment import Environment
from entities.prey import Prey
from entities.predator import Predator
from entities.plant import Plant
from entity_generator import EntityGenerator
from memory import Memory
from pygame.math import Vector2
import random
from typing import Tuple
import math
from movement import Movement
from vision import Vision
from genome import Genome
from energy import Energy

class EnvironmentSetup:
    
    def __init__(self, map_dimensions: Tuple[int, int], num_prey: int, num_predators: int, num_plants: int):
        self._map_dimensions = map_dimensions
        self._num_prey = num_prey
        self._num_predators = num_predators
        self._num_plants = num_plants
        self._entity_generator = EntityGenerator(map_dimensions)

    def initialize(self) -> Environment:
        prey_list = []
        predator_list = []
        plant_list = []

        for i in range(self._num_prey):
            prey_position = self._entity_generator.generate_random_pos()
            prey_movement = Movement(
                map_dimensions = self._map_dimensions,
                position=prey_position,
                velocity=Vector2(0, 0),  
                mass=1.0,
                max_force=.04,
                max_speed=2.0
            )
            prey_vision = Vision (
                orientation=0,
                vision_range=150,
                fov=3*math.pi/4
            )
            prey_genome = Genome (
                wander_initial_angle_range = math.pi/2,
                wander_angle_range = math.pi/6
            )
            prey_energy = Energy (
                max_energy=100,
                move_energy_lost=.01,
                eat_energy_gained=1
            )
            prey = Prey(
                movement=prey_movement,
                vision=prey_vision,
                memory=Memory(), 
                genome=prey_genome,
                energy=prey_energy,
                radius=5.0,
                color=(255, 0, 0)  
            )
            prey_list.append(prey)

        for i in range(self._num_plants):
            plant_position = Vector2(random.uniform(0, self._map_dimensions[0]),
                              random.uniform(0, self._map_dimensions[1]))
            plant = Plant(
                position=plant_position,
                radius=5,
                color=(0, 255, 0) 
            )
            plant_list.append(plant)

        return Environment(self._map_dimensions, prey_list, predator_list, plant_list)