from environment import Environment
from behaviour_results import *
from search_for_plant_behaviour import SearchForPlantBehaviour
from prey import Prey

class SimController:
    def __init__(self, environment):
        self.__environment = environment

    def update_state(self) -> None:
        prey = self.__environment.get_prey()
        for p in prey:
            test = SearchForPlantBehaviour(p, self.__environment.get_plants())
            behaviour_result = test.execute()