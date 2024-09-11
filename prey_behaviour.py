from abc import abstractmethod
from behaviour import Behaviour


class PreyBehaviour(Behaviour):
    @abstractmethod
    def execute(self, prey):
        """
        Execute the behavior for the given prey.

        Args:
            prey (Prey): The prey performing the behavior.
        """
        pass