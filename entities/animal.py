import math
from abc import ABC, abstractmethod
from memory import Memory
from genome import Genome
from pygame.math import Vector2
from typing import List
from movement import Movement
from vision import Vision
from energy import Energy

class Animal(ABC):

    def __init__(self, 
    movement: Movement,
    vision: Vision, 
    memory: Memory, 
    genome: Genome, 
    energy: Energy,
    radius: float, 
    color: tuple):
        self._movement = movement
        self._vision = vision
        self._memory = memory
        self._genome = genome
        self._energy = energy
        self._radius = radius
        self._color = color

    def is_dead(self) -> bool:
        return self._energy.get_curr_energy() <= 0

    def get_movement(self) -> Movement:
        return self._movement

    def get_vision(self) -> Vision:
        return self._vision

    def get_energy(self) -> Energy:
        return self._energy

    def get_memory(self) -> Memory:
        return self._memory

    def get_radius(self) -> float:
        return self._radius

    def get_color(self) -> tuple:
        return self._color

    def get_genome(self) -> Genome:
        return self._genome
