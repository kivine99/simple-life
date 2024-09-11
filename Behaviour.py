from abc import ABC, abstractmethod

class Behaviour(ABC):
    @abstractmethod
    def execute(self, animal):
        """
        Execute the behavior for the given animal.

        Args:
            animal (Animal): The animal performing the behavior.
        """
        pass