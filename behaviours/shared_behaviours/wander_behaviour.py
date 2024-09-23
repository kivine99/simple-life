from behaviours.behaviour import Behaviour
import random
import math
from behaviour_results.move_behaviour_result import MoveBehaviourResult
from entities.prey import Prey
from pygame.math import Vector2
from environment import Environment
from entities.animal import Animal
from energy import Energy

class WanderBehaviour(Behaviour):

    @staticmethod
    def get_priority(animal: Animal, environment: Environment):
        return 100 #TODO: actually do something here

    def __init__(self, animal: Animal, environment:Environment):
        super().__init__(environment)
        self._animal = animal

    def execute(self) -> MoveBehaviourResult:
        animal_velocity = self._animal.get_movement().get_velocity()
        animal_direction = math.atan2(animal_velocity.y, animal_velocity.x)
        animal_max_force = self._animal.get_movement().get_max_force()
        animal_memory = self._animal.get_memory()

        #If the previous behaviour was not WanderBehaviour
        if not isinstance(animal_memory.get_last_behaviour(), WanderBehaviour):
            initial_angle_range = self._animal.get_genome().get_wander_initial_angle_range()
            steering_force_direction = animal_direction + random.uniform(-initial_angle_range, initial_angle_range)
        else: 
            angle_range = self._animal.get_genome().get_wander_angle_range()
            previous_steering_force = animal_memory.get_previous_steering_force()
            previous_steering_force_direction = math.atan2(previous_steering_force.y, previous_steering_force.x)
            steering_force_direction = previous_steering_force_direction + random.uniform(-angle_range, angle_range)

        steering_force_x = math.cos(steering_force_direction) * animal_max_force
        steering_force_y = math.sin(steering_force_direction) * animal_max_force
        steering_force = Vector2(steering_force_x, steering_force_y)

        return MoveBehaviourResult(self._animal, self, steering_force, self._animal.get_energy().get_move_energy_lost())