from behaviours.behaviour import Behaviour
import random
import math
from behaviour_results.move_behaviour_result import MoveBehaviourResult
from prey import Prey
from pygame.math import Vector2
from environment import Environment
from animal import Animal
from trig_utils import TrigUtils


class WanderBehaviour(Behaviour):

    @staticmethod
    def get_priority(prey: Prey, environment: Environment):
        return 100 #TODO: actually do something here

    def __init__(self, animal: Animal, environment:Environment):
        super().__init__(environment)
        self._animal = animal
        self._previous_force_angle = None
        self._previous_force_magnitude = None


    def execute(self) -> MoveBehaviourResult:
        animal_position = self._animal.get_position()
        animal_orientation = self._animal.get_orientation()

        #TODO: this should be part of the genome
        circle_radius = 20
        circle_distance_from_animal = 3
        circle_position = [animal_position[0] + math.cos(animal_orientation)*(circle_radius+circle_distance_from_animal), animal_position[1] - 
        math.sin(animal_orientation)*(circle_radius+circle_distance_from_animal)]

        magnitude = .2
        wander_angle = .1

        #If wander was the previous behaviour
        if isinstance(self._animal.get_memory().get_last_behaviour(), WanderBehaviour):
            direction_vector = Vector2(math.cos(self._previous_force_angle), math.sin(self._previous_force_angle))
            direction_vector = direction_vector.rotate_rad(random.uniform(-wander_angle, wander_angle))
            self._previous_force_angle = math.atan2(direction_vector.y, direction_vector.x)
        else:
            self._animal.get_memory().set_last_behaviour(self)
            theta = random.uniform(0, 2*math.pi)
            random_point_x = circle_position[0] + math.cos(theta)*circle_radius
            random_point_y = circle_position[1] + math.sin(theta)*circle_radius
            random_point = Vector2(random_point_x, random_point_y)

            self._previous_force_angle = TrigUtils.angle_from(animal_position, random_point)
            self._previous_force_magnitude = .1

        new_velocity = self._animal.calculate_new_velocity(Vector2(math.cos(self._previous_force_angle)*self._previous_force_magnitude, math.sin(self._previous_force_angle)*self._previous_force_magnitude))
        return MoveBehaviourResult(self._animal, new_velocity, self._animal.get_move_energy_lost())

    def invert_previous_force_angle(self):
        self._previous_force_angle += math.pi