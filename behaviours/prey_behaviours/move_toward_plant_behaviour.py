from behaviours.behaviour import Behaviour
from prey import Prey
from plant import Plant
from typing import Tuple
import math
from pygame.math import Vector2
from environment import Environment
from behaviour_results.eat_plant_behaviour_result import EatPlantBehaviourResult

class MoveTowardPlantBehaviour(Behaviour):
    def get_priority(prey: Prey, environment: Environment):
        for plant in environment.get_plants():
            if prey.is_within_view(plant.get_position()):
                return 200
        return 20

    def __init__(self, prey: Prey, environment: Environment):
        super().__init__(prey, environment)

    def execute(self) -> EatPlantBehaviourResult:
        nearest_plant = self.find_nearest_plant()
        target_position = nearest_plant.get_position()
        prey_position = self._animal.get_position()
        
        if self._animal.get_position().distance_to(nearest_plant.get_position()) < 2:
            return EatPlantBehaviourResult(nearest_plant)
        
        desired_direction = target_position - prey_position
        
        if desired_direction.length() != 0:
            desired_direction = desired_direction.normalize()
        
        desired_velocity = desired_direction * self._animal.get_max_speed()
        
        steering_force = desired_velocity - self._animal.get_velocity()
        
        self._animal.apply_force(steering_force)

    #TODO: remove this
    def find_nearest_plant(self) -> Plant:
        nearest_plant = None
        min_distance = math.inf#float('inf') 

        for plant in self._environment.get_plants():
            plant_position = plant.get_position()
            distance = self._animal.get_position().distance_to(plant_position)

            if distance < min_distance:
                min_distance = distance
                nearest_plant = plant

        return nearest_plant
        
