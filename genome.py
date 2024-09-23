from abc import ABC
import math

class Genome(ABC):
    
    def __init__(self, wander_initial_angle_range: float, wander_angle_range: float):
        self._wander_initial_angle_range = wander_initial_angle_range%(math.pi)
        self._wander_angle_range = wander_angle_range

    def set_wander_initial_angle_range(self, range: float) -> None:
        self._wander_initial_angle_range = range%(math.pi)

    def set_wander_angle_range(self, range: float) -> None:
        self._wander_angle_range = range%(math.pi)
    def get_wander_initial_angle_range(self):
        return self._wander_initial_angle_range

    def get_wander_angle_range(self):
        return self._wander_angle_range