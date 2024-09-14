from plant import Plant
from environment import Environment
from behaviour_results.behaviour_result import BehaviourResult

class EatPlantBehaviourResult(BehaviourResult):
    def __init__(self, eaten_plant: Plant):
        self._eaten_plant = eaten_plant

    def apply_to_environment(self, environment: Environment) -> None:
        environment.remove_plant(self._eaten_plant)