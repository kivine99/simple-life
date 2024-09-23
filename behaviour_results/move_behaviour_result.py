from behaviour_results.behaviour_result import BehaviourResult
from environment import Environment
from pygame.math import Vector2
from entities.animal import Animal
import math
from behaviours.behaviour import Behaviour

class MoveBehaviourResult(BehaviourResult):

    def __init__(self, animal: Animal, behaviour: Behaviour, steering_force: Vector2, energy_lost: float):
        self._animal = animal
        self._behaviour = behaviour
        self._steering_force = steering_force
        self._energy_lost = energy_lost

    #Decrease the animal's energy
    #If animal is out of energy remove it from the environment
    #Apply steering force to the animal
    #Inverse the animal's direction and previous force if it goes out of bounds
    #Set the animal's orientation based on its velocity
    #Set the animal's last behaviour in its memory
    #Set the animal's previous steering force in its memory
    def apply_result(self, environment: Environment):
        self._animal.get_energy().decrease_energy(self._energy_lost)   

        if(self._animal.is_dead()):
            environment.remove_animal(self._animal)
            return

        self._animal.get_movement().apply_force(self._steering_force)

        #Invert the animal's velocity and force if it goes out of bounds.
        animal_position = self._animal.get_movement().get_position()
        if environment.out_of_bounds_x(animal_position):
            self._animal.get_movement().inverse_x_vel()
            self._animal.get_memory().inverse_previous_steering_force_x()
            self._animal.get_memory().inverse_previous_steering_force_y()
        if environment.out_of_bounds_y(animal_position):
            self._animal.get_movement().inverse_y_vel()
            self._animal.get_memory().inverse_previous_steering_force_y()
            self._animal.get_memory().inverse_previous_steering_force_x()

        #Set the animal's orientation based on its current velocity.
        animal_velocity = self._animal.get_movement().get_velocity()
        animal_orientation = math.atan2(animal_velocity.y, animal_velocity.x)
        self._animal.get_vision().set_orientation(animal_orientation)

        self._animal.get_memory().set_previous_steering_force(self._steering_force) #TODO: move this into results
        self._animal.get_memory().set_last_behaviour(self._behaviour)

        