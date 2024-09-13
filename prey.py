from animal import Animal
from memory import Memory
from genome import Genome
from pygame.math import Vector2

class Predator(Animal):
    def __init__(self, 
    position: Vector2, 
    velocity: Vector2,
    mass: float,
    max_force: float,
    max_speed: float,
    orientation: float,
    vision_range: float, 
    fov: float, 
    memory: Memory, 
    genome: Genome, 
    radius: float, 
    color: tuple):
        super().__init__(
        position,
        velocity,
        mass,
        max_force,
        max_speed,
        orientation,
        vision_range,
        fov,
        memory,
        genome,
        radius,
        color)