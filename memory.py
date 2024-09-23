from behaviours.behaviour import Behaviour
from typing import Optional
from pygame.math import Vector2

class Memory:
    
    def __init__(self):
        self._last_behaviour = None
        self._previous_steering_force = None

    def get_last_behaviour(self) -> Optional[Behaviour]:
        return self._last_behaviour

    def set_last_behaviour(self, new_behaviour: Behaviour) -> None:
        self._last_behaviour = new_behaviour

    def get_previous_steering_force(self) -> Vector2:
        return self._previous_steering_force

    def set_previous_steering_force(self, new_force: Vector2) -> None:
        self._previous_steering_force = new_force

    def inverse_previous_steering_force_x(self) -> None:
        if self._previous_steering_force:
            self._previous_steering_force.x *= -1

    def inverse_previous_steering_force_y(self) -> None:
        if self._previous_steering_force:
            self._previous_steering_force.y *= -1