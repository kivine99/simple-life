from prey import Prey
from predator import Predator
from plant import Plant
from typing import Tuple

class Environment:
    def __init__(self, 
    prey: List[Prey], 
    predators: List[Predators],
    plants: List[Plant]):
        """
        Args:
            prey (List[Prey]): List of prey.
            predators (List[Predators]): List of predators.
            plants (List[Plant]): List of plants.
        """
        self.__prey = prey
        self.__predators = predators
        self.__plants = plants

    def get_prey(self) -> Tuple[Prey, ...]:
        """
        Returns:
            tuple[Prey]: A tuple of prey.
        """
        return tuple(self.__prey)

    def get_predators(self) -> Tuple[Predator, ...]:
        """
        Returns:
            tuple[Predators]: A tuple of predators.
        """
        return tuple(self.__predators)

    def get_plants(self) -> Tuple[Plant, ...]:
        """
        Returns:
            tuple[Plant]: A tuple of plants.
        """
        return tuple(self.__plants)

    def add_prey(self, prey_to_add: Prey) -> None:
        """
        Add new prey to the environment

        Args:
            prey_to_add (Prey): Prey to add to the prey list.
        """
        self.__prey.append(prey_to_add)

    def add_predator(self, predator_to_add: Predator) -> None:
        """
        Add new predator to the environment

        Args:
            predator_to_add (Predator): predator to add to the predator list.
        """
        self.__predator.append(predator_to_add)