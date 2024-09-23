from behaviours.behaviour import Behaviour
from entities.prey import Prey
from entities.plant import Plant
from typing import Tuple
import math
from pygame.math import Vector2
from environment import Environment
from behaviour_results.move_behaviour_result import MoveBehaviourResult

class MoveTowardPlantBehaviour(Behaviour):
    
    @staticmethod
    def get_priority(prey: Prey, environment: Environment):
        for plant in environment.get_plants():
            if prey.get_vision().is_within_view(prey.get_movement().get_position(), plant.get_position()):
                return 200
        return 20

    def __init__(self, prey: Prey, environment: Environment):
        super().__init__(environment)
        self._prey = prey

    from pygame.math import Vector2

    def execute(self) -> MoveBehaviourResult:
        nearest_plant = self._prey.nearest_plant(self._environment.get_plants())

        #Do nothing if there is no plant 
        if nearest_plant is None:
            return

        target_position = nearest_plant.get_position()

        prey_position = self._prey.get_movement().get_position()
        prey_max_speed = self._prey.get_movement().get_max_speed()
        prey_velocity = self._prey.get_movement().get_velocity()
        prey_energy_lost = self._prey.get_energy().get_move_energy_lost()
        
        desired_direction = Vector2(target_position.x - prey_position.x, target_position.y - prey_position.y)

        if desired_direction.length() != 0:
            desired_direction = desired_direction.normalize()
        
        desired_velocity = desired_direction * prey_max_speed

        steering_force = desired_velocity - prey_velocity
        
        return MoveBehaviourResult(self._prey, self, steering_force, prey_energy_lost)