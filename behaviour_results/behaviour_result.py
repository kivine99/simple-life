from abc import ABC, abstractmethod
from environment import Environment

class BehaviourResult(ABC):
    
    @abstractmethod
    def apply_result(self, environment: Environment) -> None:
        pass