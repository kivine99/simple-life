from abc import ABC, abstractmethod
from environment import Environment

class BehaviourResult(ABC):
    @abstractmethod
    def apply_to_environment(self, environment: Environment) -> None:
        pass