from behaviours.behaviour import Behaviour
from prey import Prey
from environment import Environment
from behaviour_results.eat_plant_behaviour_result import EatPlantBehaviourResult
import math

class EatPlantBehaviour(Behaviour):

    @staticmethod
    def get_priority(prey: Prey, environment: Environment):
        #TODO: optimize this
        nearest_plant = prey.nearest_plant(environment.get_plants())
        distance_to_plant = math.dist(prey.get_position(), nearest_plant.get_position())#prey.get_position().distance_to(nearest_plant.get_position())
        if distance_to_plant < 3:
            return 100000 #TODO: maybe it shouldn't always be eaten?
        return 0

    def __init__(self, prey: Prey, environment:Environment):
        super().__init__(environment)
        self._prey = prey

    def execute(self) -> EatPlantBehaviourResult:
        nearest_plant = self._prey.nearest_plant(self._environment.get_plants())
        distance_to_plant = math.dist(self._prey.get_position(), nearest_plant.get_position())#self._prey.get_position().distance_to(nearest_plant.get_position())

        return EatPlantBehaviourResult(self._prey, nearest_plant, self._prey.get_eat_energy_gained()) #TODO: should I check if it's close enough?