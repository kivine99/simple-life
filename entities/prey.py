from entities.animal import Animal
from memory import Memory
from genome import Genome
from pygame.math import Vector2
from entities.plant import Plant
import math
from movement import Movement
from vision import Vision
from energy import Energy

class Prey(Animal):
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

    #TODO: move this method somewhere else
    def nearest_plant(self, plants: list[Plant]) -> Plant:
        nearest_plant = None
        min_distance = math.inf

        for plant in plants:
            plant_position = plant.get_position()
            distance_to_plant = self._movement.get_position().distance_to(plant_position)
            if distance_to_plant < min_distance:
                min_distance = distance_to_plant
                nearest_plant = plant

        return nearest_plant