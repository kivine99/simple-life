from pygame.math import Vector2
from typing import Tuple, List
class Plant:
    
    def __init__(self, position: list[int], color: Tuple[int, int, int], radius: float):
        self._position = position
        self._color = color
        self._radius = radius

    def get_radius(self) -> float:
        return self._radius

    def get_position(self) -> List[int]:
        return self._position

    def get_color(self) -> Tuple[int, int, int]:
        return self._color 
