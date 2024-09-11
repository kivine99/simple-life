from abc import abstractmethod
from behaviour import Behaviour
from prey import Prey

class PreyBehaviour(Behaviour):
    @abstractmethod
    def execute(self, prey: Prey) -> None:
        """
        Execute the behavior for the given prey.

        Args:
            prey (Prey): The prey performing the behavior.
        """
        pass