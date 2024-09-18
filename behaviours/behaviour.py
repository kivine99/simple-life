from abc import ABC, abstractmethod

class Behaviour(ABC):
    
    def __init__(self, environment):
        self._environment = environment

    @staticmethod
    @abstractmethod
    def get_priority(animal):
        pass

    @abstractmethod
    def execute(self):
        pass
