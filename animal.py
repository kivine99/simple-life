import math
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, position, direction, vision_range, fov, max_speed, curr_speed, memory, genome, radius, color):
        """
        Constructor.

        Args:
            position (tuple): The initial (x, y) position of the animal.
            direction (float): The initial direction in radians, normalized between 0 and 2π.
            vision_range (float): The vision range of the animal.
            fov (float): The field of view of the animal in radians.
            max_speed (float): The maximum speed the animal.
            curr_speed (float): The current speed of the animal.
            memory (Memory): Memory of the animal.
            genome (Genome): Genetic information about the animal.
            radius (float): The radius of the animal.
            color (tuple): The RGB color of the animal.
        """
        self.__position = position
        self.__direction = direction % (2*math.pi)
        self.__vision_range = vision_range
        self.__fov = fov
        self.__max_speed = max_speed
        self.__curr_speed = curr_speed
        self.__memory = memory
        self.__genome = genome
        self.__radius = radius
        self.__color = color

    def get_position(self):
        """
        Returns:
            tuple: The (x, y) position of the animal.
        """
        return self.__position

    def get_direction(self):
        """
        Returns:
            float: The direction of the animal in radians.
        """
        return self.__direction

    def get_vision_range(self):
        """
        Returns:
            float: The vision range of the animal.
        """
        return self.__vision_range

    def get_fov(self):
        """
        Returns:
            float: The field of view of the animal in radians.
        """
        return self.__fov

    def get_max_speed(self):
        """
        Returns:
            float: The max speed of the animal.
        """
        return self.__max_speed

    def get_curr_speed(self):
        """
        Returns:
            float: The current speed of the animal.
        """
        return self.__curr_speed

    @abstractmethod
    def get_memory(self):
        pass

    @abstractmethod
    def get_genome(self):
        pass

    def get_radius(self):
        """
        Returns:
            float: The radius of the animal.
        """
        return self.__radius

    def get_color(self):
        """
        Returns:
            tuple: (R, G, B) of the animal.
        """
        return self.__color

    def calculate_next_position(self):
        """
        Returns the animal's next position based on its current speed and direction. Does not modify the position.

        Returns:
            tuple: The new x, y position.
        """
        x = self.__position[0] + math.cos(self.__direction) * self.__curr_speed
        y = self.__position[1] + math.sin(self.__direction) * self.__curr_speed
        return (x, y)

    def set_direction(self, direction):
        """
        Sets the direction of the animal. Normalized between 0 and 2π.
        
        Args:
            direction (float): The new direction in radians.
        """
        self.__direction = direction%(2*math.pi)

    def set_curr_speed(self, new_speed):
        """
        Sets the current speed of the animal, ensuring it's between 0 and max_speed.
        
        Args:
            new_speed (float): The new speed of the animal.
        """
        self.__curr_speed = max(0, min(new_speed, self.__max_speed))

    def set_position(self, new_position):
        """
        Sets the new position of the animal. Does not check if new position is within proper bounds.

        Args:
            new_position (tuple): The new (x, y) position of the animal.
        """
        if len(new_position) != 2:
            raise ValueError("Position must be a tuple of length 2.")
        self.__position = new_position