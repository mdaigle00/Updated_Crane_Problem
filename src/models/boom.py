import math;

class Boom:
    """This class represents the boom of the crane which rotates around the base pivot."""

    def __init__(self, length: float, angle: float):
        """Initialize the boom with a given length and angle."""

        self.length = length #Store the length of the boom
        self.angle = math.radians(angle) #Store and convert the angle in degrees to radians

    def get_end_position(self, base_x: float, base_y: float) -> tuple:
        """Calculate the end position of the boom based on its rotation.
           base_x: x-coordinate of the base of the crane
           base_y: y-coordinate of the base of the crane
        """ 

        end_x = base_x + self.length * math.cos(self.angle) #Calculate 
        end_y = base_y + self.length * math.sin(self.angle) #Calculate

        return end_x, end_y 

        """
        Return the calculations of the tuple of the x and y coordinates of
        the boom's end point
        """

    pass
