import math
from abc import ABC, abstractmethod
from memory import Memory
from genome import Genome
from pygame.math import Vector2

class Animal(ABC):

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
        self._position = position
        self._velocity = velocity
        self._mass = mass
        self._max_force = max_force
        self._max_speed = max_speed
        self._orientation = orientation
        self._vision_range = vision_range
        self._fov = fov
        self._memory = memory
        self._genome = genome
        self._radius = radius
        self._color = color

    def get_position(self) -> Vector2:
        return self._position

    def get_orientation(self) -> float:
        return self._orientation

    def get_vision_range(self) -> float:
        return self._vision_range

    def get_fov(self) -> float:
        return self._fov

    def get_memory(self) -> Memory:
        return self._memory

    def get_max_speed(self) -> float:
        return self._max_speed

    def get_velocity(self) -> Vector2:
        return self._velocity

    def get_radius(self) -> float:
        return self._radius

    def get_color(self) -> tuple:
        return self._color

    def set_orientation(self, orientation: float) -> None:
        self._orientation = orientation%(2*math.pi)

    def apply_force(self, force: Vector2) -> None:
        if force.length() != 0:
            force = force.clamp_magnitude(self._max_force)
        acceleration = force / self._mass

        self._velocity += acceleration
        if self._velocity.length() != 0:
            self._velocity = self._velocity.clamp_magnitude(self._max_speed)

        self._position += self._velocity
        self._orientation = math.atan2(self._velocity.y, self._velocity.x)%(math.pi*2) 

    def is_within_view(self, target_position: Vector2) -> bool:
        to_target = target_position - self._position
        distance_to_target = (target_position - self._position).length()

        if distance_to_target > self._vision_range:
            return False

        angle_to_target = math.atan2(to_target.y, to_target.x)%(2*math.pi)
        angle_difference = abs(angle_to_target - self._orientation)

        angle_difference = min(angle_difference, 2*math.pi - angle_difference)

        return angle_difference <= (self._fov / 2)
