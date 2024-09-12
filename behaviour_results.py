from abc import ABC, abstractmethod
from environment import Environment
from plant import Plant

class BehaviourResult(ABC):
    @abstractmethod
    def apply_to_environment(self, environment: Environment) -> None:
        pass

class EatPlantBehaviourResult(BehaviourResult):
    def __init__(self, eaten_plant: Plant):
        """
        Args:
            eaten_plant (Plant): The plant that has been eaten by a prey.
        """
        self.__eaten_plant = eaten_plant

    def apply_to_environment(self, environment: Environment) -> None:
        """
        Remove the eaten plant from the environment.

        Args:
            environment (Environment): The environment from which the eaten plant will be removed.
        """
        environment.remove_plant(self.__eaten_plant)

class NoEffectBehaviourResult(BehaviourResult):
    def __init__(self):
        pass

    def apply_to_environment(self, environment: Environment) -> None:
        """
        No effect on environment.

        Args:
            environment (Environment): Environment on which no changes will be applied.
        """
        pass
