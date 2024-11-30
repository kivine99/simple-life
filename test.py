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

prey_position = Vector2(500, 500)#self._entity_generator.generate_random_pos()
prey_movement = Movement(
    map_dimensions = (1000, 1000),
    position=prey_position,
    velocity=Vector2(0, 0),  
    mass=1.0,
    max_force=.04,
    max_speed=2.0
)
prey_vision = Vision (
    orientation=0,
    vision_range=100,
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

print(prey.get_vision().is_within_view(prey.get_movement().get_position(), Vector2(601, 500)))