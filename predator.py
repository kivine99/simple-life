from animal import Animal
from memory import Memory
from genome import Genome
from pygame.math import Vector2

class Predator(Animal):

    _eat_plant_energy_gained = 0
    _move_energy_lost = 0

    @classmethod
    def get_move_energy_lost(cls) -> float:
        return cls._move_energy_lost

    @classmethod
    def get_eat_energy_gained(cls) -> float:
        return cls._eat_plant_energy_gained

    @classmethod
    def set_move_energy_lost(cls, amount_lost: float) -> None:
        cls._move_energy_lost = amount_lost 

    @classmethod
    def set_eat_energy_gained(cls, amount_gained: float) -> None:
        cls._eat_plant_energy_gained = amount_gained

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
    energy: float,
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
        energy,
        radius,
        color)