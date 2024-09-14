from behaviours.behaviour import Behaviour
import random
import math
from behaviour_results.no_effect_behaviour_result import NoEffectBehaviourResult
from prey import Prey
from pygame.math import Vector2
from environment import Environment
from animal import Animal


class WanderBehaviour(Behaviour):
    def get_priority(prey: Prey, environment: Environment):
        return 100 #TODO: actually do something here

    def __init__(self, animal: Animal, environment:Environment):
        super().__init__(animal, environment)
        self._previous_force_direction = None
        self._previous_force_magnitude = None

    def execute(self) -> NoEffectBehaviourResult:
        prey_position = self._animal.get_position()
        prey_orientation = self._animal.get_orientation()
        #TODO: this should be part of the genome
        circle_radius = 20
        circle_distance_from_animal = 3
        magnitude = .2
        wander_angle = 2

        circle_position = Vector2(prey_position[0] + math.cos(prey_orientation)*(circle_radius+circle_distance_from_animal), prey_position[1] - math.sin(prey_orientation)*(circle_radius+circle_distance_from_animal))
        if self._previous_force_direction and self._previous_force_magnitude:
            self._previous_force_direction = self._previous_force_direction.rotate_rad(random.uniform(0, wander_angle))
        else:
            theta = random.uniform(0, 2*math.pi)
            random_point_x = circle_position[0] + math.cos(theta)*circle_radius
            random_point_y = circle_position[1] + math.sin(theta)*circle_radius
            random_point = Vector2(random_point_x, random_point_y)
            self._previous_force_direction = prey_position.angle_to(random_point)

        self._animal.apply_force(Vector2(math.cos(self._previous_force_direction)*magnitude,
                                       math.sin(self._previous_force_direction)*magnitude))