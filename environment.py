from prey import Prey
from predator import Predator
from typing import Tuple

class Environment:
    def __init__(self, 
    prey: List[Prey], 
    predators: List[Predators]):
        """
        Args:
            prey (List[Prey]): List of prey.
            predators (List[Predators]): List of predators.
        """
        self.__prey = prey
        self.__predators = predators

    def get_prey(self) -> Tuple[Prey, ...]:
        """
        Returns:
            tuple[Prey]: An immutable tuple of prey.
        """
        return tuple(self.__prey)

    def get_predators(self) -> Tuple[Predator, ...]:
        """
        Returns:
            tuple[Predators]: An immutable tuple of predators.
        """
        return tuple(self.__predators)

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