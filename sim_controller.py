from environment import Environment
from behaviour_results import *
from behaviours.prey_behaviours import *
from prey import Prey
from prey_behaviour_manager import PreyBehaviourManager
from pygame.math import Vector2

class SimController:
    def __init__(self, environment):
        self._environment = environment
        self._prey_behaviour_manager = PreyBehaviourManager()

    def update_state(self) -> None:
        prey = self._environment.get_prey()
        for p in prey:
            chosen_behaviour = self._prey_behaviour_manager.choose_behaviour(p, self._environment)
            behaviour_result = chosen_behaviour.execute()
            if behaviour_result:
                behaviour_result.apply_to_environment(self._environment)