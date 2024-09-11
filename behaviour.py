from abc import ABC, abstractmethod
from animal import Animal

class Behaviour(ABC):
    @abstractmethod
    def execute(self, animal: Animal):
        """
        Execute the behavior for the given animal.

        Args:
            animal (Animal): The animal performing the behavior.
        """
        pass
