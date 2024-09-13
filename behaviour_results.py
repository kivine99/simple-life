from abc import ABC, abstractmethod
from environment import Environment
from plant import Plant

class BehaviourResult(ABC):
    @abstractmethod
    def apply_to_environment(self, environment: Environment) -> None:
        pass

class EatPlantBehaviourResult(BehaviourResult):
    def __init__(self, eaten_plant: Plant):
        self.__eaten_plant = eaten_plant

    def apply_to_environment(self, environment: Environment) -> None:
        environment.remove_plant(self.__eaten_plant)

class NoEffectBehaviourResult(BehaviourResult):
    def __init__(self):
        pass

    def apply_to_environment(self, environment: Environment) -> None:
        pass
