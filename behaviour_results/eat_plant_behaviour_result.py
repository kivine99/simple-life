from entities.plant import Plant
from environment import Environment
from behaviour_results.behaviour_result import BehaviourResult
from entities.prey import Prey

class EatPlantBehaviourResult(BehaviourResult):

    def __init__(self, prey: Prey, eaten_plant: Plant, energy_gained: float):
        self._prey = prey
        self._eaten_plant = eaten_plant
        self._energy_gained = energy_gained

    def apply_result(self, environment: Environment) -> None:
        environment.remove_plant(self._eaten_plant)
        self._prey.get_energy().increase_energy(self._energy_gained)
