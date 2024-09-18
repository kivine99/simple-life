from abc import ABC, abstractmethod
from animal import Animal

class BehaviourManager(ABC):

    def __init__(self):
        self._behaviours = []
        
    @abstractmethod
    def choose_behaviour(animal: Animal):
        pass
