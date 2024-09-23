from pygame.math import Vector2
from typing import Tuple

class Movement:
    def __init__(self, 
    map_dimensions: Tuple[int, int],
    position: Vector2, 
    velocity: Vector2,
    mass: float,
    max_force: float,
    max_speed: float,
    ):
        self._map_dimensions = map_dimensions
        self._position = position
        self._velocity = velocity
        self._mass = mass
        self._max_force = max_force
        self._max_speed = max_speed

    def get_position(self) -> Vector2:
        return self._position

    def get_max_speed(self) -> float:
        return self._max_speed

    def get_velocity(self) -> Vector2:
        return self._velocity

    def get_max_force(self) -> float:
        return self._max_force

    def set_velocity(self, new_velocity: float) -> None:
        self._velocity = new_velocity
    
    def apply_force(self, steering_force: Vector2):
        if steering_force.length() > self._max_force:
            steering_force = steering_force.normalize() * self._max_force

        acceleration = steering_force /self._mass

        new_velocity = self._velocity + acceleration

        if new_velocity.length() > self._max_speed:
            new_velocity = new_velocity.normalize() * self._max_speed

        self._velocity = new_velocity
        self._position += self._velocity

        if self.inverse_x_vel():
            
            self._velocity.x = -self._velocity.x
        if self.inverse_y_vel():
            self._velocity.y = -self._velocity.y

    def inverse_x_vel(self) -> bool:
        if self._position[0] < 0 or self._position[0] > self._map_dimensions[0]:
            return True

    def inverse_y_vel(self) -> bool:
        if self._position[1] < 0 or self._position[1] > self._map_dimensions[1]:
            return True

    # def calculate_new_velocity(self, force: Vector2):
    #     new_velocity = self._velocity

    #     if force.length() != 0:
    #         force = force.clamp_magnitude(self._max_force)
    #     acceleration = force / self._mass

    #     new_velocity += acceleration
    #     if new_velocity.length() != 0:
    #         new_velocity = new_velocity.clamp_magnitude(self._max_speed)

    #     return new_velocity