from behaviour_manager import BehaviourManager
from behaviours.prey_behaviours.wander_behaviour import WanderBehaviour
from behaviours.prey_behaviours.move_toward_plant_behaviour import MoveTowardPlantBehaviour
from behaviours.behaviour import Behaviour
from prey import Prey
from typing import Type
from environment import Environment

class PreyBehaviourManager(BehaviourManager):
    def __init__(self):
        super().__init__()
        self._behaviours.append(WanderBehaviour)
        self._behaviours.append(MoveTowardPlantBehaviour)

    def choose_behaviour(self, prey: Prey, environment: Environment) -> Behaviour:
        highest_priority = -float('inf')
        chosen_behaviour = None
        for behaviour in self._behaviours:
            behaviour_priority = behaviour.get_priority(prey, environment)
            if behaviour_priority > highest_priority:
                highest_priority = behaviour_priority
                chosen_behaviour = behaviour
        
        if chosen_behaviour is type(prey.get_memory().get_last_behaviour()):
            return prey.get_memory().get_last_behaviour()

        return chosen_behaviour(prey, environment)




        
    