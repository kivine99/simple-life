from behaviour_results.behaviour_result import BehaviourResult
from environment import Environment
from pygame.math import Vector2
from animal import Animal

class MoveBehaviourResult(BehaviourResult):

    def __init__(self, animal: Animal, new_velocity: Vector2, energy_lost: float):
        self._animal = animal
        self._new_velocity = new_velocity
        self._energy_lost = energy_lost

    def apply_result(self, environment: Environment):
        environment.update_animal_energy(self._animal, self._energy_lost)
        if(self._animal.get_energy() < 0):
            environment.remove_animal(self._animal)
            return

        environment.move_animal(self._animal, self._new_velocity)

        