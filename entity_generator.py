from typing import List
from plant import Plant
import random

class EntityGenerator:

    def __init__(self, map_dimensions: List[int]):
        self._map_dimensions = map_dimensions

    def generate_random_plant(self) -> Plant:
        red = random.randint(0, 50) 
        green = random.randint(100, 255)
        blue = random.randint(0, 50)

        plant = Plant(
            position=self.generate_random_pos(),
            radius=5,
            color=(red, green, blue) 
        )
        
        return plant

    def generate_random_pos(self) -> List[int]:
        return [random.uniform(0, self._map_dimensions[0]), random.uniform(0, self._map_dimensions[1])]

