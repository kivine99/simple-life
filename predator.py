from animal import Animal
from memory import Memory
from genome import Genome

class Predator(Animal):
    def __init__(self, 
    position: tuple,
    direction: float, 
    vision_range: float, 
    fov: float, 
    max_speed: float, 
    curr_speed: float, 
    memory: Memory, 
    genome: Genome, 
    radius: float, 
    color: tuple):
        """
        Args:
            position (tuple): The initial (x, y) position of the animal.
            direction (float): The initial direction in radians, normalized between 0 and 2π.
            vision_range (float): The vision range of the animal.
            fov (float): The field of view of the animal in radians.
            max_speed (float): The maximum speed the animal.
            curr_speed (float): The current speed of the animal.
            memory (Memory): Memory of the animal.
            genome (Genome): Genetic information about the animal.
            radius (float): The radius of the animal.
            color (tuple): The RGB color of the animal.
        """
        super().__init__(position, direction, vision_range, fov, max_speed, curr_speed, memory, genome, radius, color)