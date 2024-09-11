class Memory(ABC):

    def __init__(self):
        self.__last_behaviour = None

    def get_last_behaviour(self):
        """
        Returns:
            Behaviour or None: The animal's previous behaviour, or None if there is no previous behaviour.
        """
        return self.__last_behaviour

    def set_last_behaviour(self, new_behaviour):
        """
        Sets the previous behaviour of the animal.
        
        Args:
            new_behaviour (Behaviour): The new behaviour of the animal.
        """
        self.__last_behaviour = new_behaviour