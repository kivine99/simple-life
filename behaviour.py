from abc import ABC, abstractmethod

class Behaviour(ABC):
    @abstractmethod
    def execute(self):
        """
        Execute the behavior for the given animal.
        """
        pass
