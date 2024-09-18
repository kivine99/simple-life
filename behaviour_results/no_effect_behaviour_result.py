from environment import Environment
from behaviour_results.behaviour_result import BehaviourResult

class NoEffectBehaviourResult(BehaviourResult):
    
    def __init__(self):
        pass

    def apply_result(self, environment: Environment) -> None:
        pass