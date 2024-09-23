from entities.animal import Animal
from memory import Memory
from genome import Genome
from pygame.math import Vector2
from movement import Movement
from vision import Vision
from energy import Energy

class Predator(Animal):
    def __init__(self, 
    movement: Movement,
    vision: Vision, 
    memory: Memory, 
    genome: Genome, 
    energy: Energy,
    radius: float, 
    color: tuple):
        super().__init__(
        movement,
        vision,
        memory,
        genome,
        energy,
        radius,
        color)