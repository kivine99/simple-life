import math
from pygame.math import Vector2

class Vision:
    def __init__(self, 
    orientation: float,
    vision_range: float, 
    fov: float):
        self._orientation = orientation
        self._vision_range = vision_range
        self._fov = fov
        
    def get_orientation(self) -> float:
        return self._orientation

    def get_vision_range(self) -> float:
        return self._vision_range

    def get_fov(self) -> float:
        return self._fov

    def set_orientation(self, orientation: float) -> None:
        self._orientation = orientation%(2*math.pi)

    def is_within_view(self, self_position: Vector2, target_position: Vector2) -> bool:
        distance_to_target = self_position.distance_to(target_position)
        
        if distance_to_target > self._vision_range:
            return False

        angle_to_target = math.atan2(target_position.y - self_position.y, target_position.x - self_position.x)
        
        # Normalize the angle difference to the range [-pi, pi]
        angle_difference = angle_to_target - self._orientation
        angle_difference = math.atan2(math.sin(angle_difference), math.cos(angle_difference))  # Normalize between -pi and pi

        return abs(angle_difference) <= (self._fov / 2)