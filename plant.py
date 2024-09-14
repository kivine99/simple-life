from pygame.math import Vector2
from typing import Tuple
class Plant:
    def __init__(self, position: Vector2, color: Tuple[int, int, int], size: float):
        self._position = position
        self._color = color
        self._size = size

    def get_size(self) -> float:
        return self._size

    def get_position(self) -> Vector2:
        return self._position

    def get_color(self) -> Tuple[int, int, int]:
        return self._color 
