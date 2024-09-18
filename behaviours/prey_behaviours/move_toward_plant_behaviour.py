from behaviours.behaviour import Behaviour
from prey import Prey
from plant import Plant
from typing import Tuple
import math
from pygame.math import Vector2
from environment import Environment
from behaviour_results.move_behaviour_result import MoveBehaviourResult

class MoveTowardPlantBehaviour(Behaviour):
    
    @staticmethod
    def get_priority(prey: Prey, environment: Environment):
        for plant in environment.get_plants():
            if prey.is_within_view(plant.get_position()):
                return 200
        return 20

    def __init__(self, prey: Prey, environment: Environment):
        super().__init__(environment)
        self._prey = prey

    def execute(self) -> MoveBehaviourResult:
        energy_cost = 0 

        nearest_plant = self._prey.nearest_plant(self._environment.get_plants())
        target_position = nearest_plant.get_position()
        prey_position = self._prey.get_position()
        
        desired_direction = target_position - prey_position
        
        if desired_direction.length() != 0:
            desired_direction = desired_direction.normalize()
        
        desired_velocity = desired_direction * self._prey.get_max_speed()
        
        steering_force = desired_velocity - self._prey.get_velocity()
        
        new_velocity = self._prey.calculate_new_velocity(steering_force)
        return MoveBehaviourResult(self._prey, new_velocity, self._prey.get_move_energy_lost())
        # self._animal.apply_force(steering_force)