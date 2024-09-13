from abc import ABC, abstractmethod

class Behaviour(ABC):
    @abstractmethod
    def execute(self):
        pass
