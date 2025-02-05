from .main_hoist import MainHoist
from .boom import Boom
from .base_crane import BaseCrane

class Crane:
    """
    Represents the Crane object, which consists of:
    - BaseCrane: The fixed base of the crane.
    - Boom: The rotating arm extending from the base.
    - MainHoist: The lifting mechanism attached to the boom.
    """

    def __init__(self, base_x: float, base_y: float, boom_length: float, boom_angle: float) -> None:
        """
        Initializes the Crane object with its components.

        Arguments:
            base_x (float): The x-coordinate of the crane base.
            base_y (float): The y-coordinate of the crane base.
            boom_length (float): The length of the crane's boom.
            boom_angle (float): The initial angle of the boom in degrees.
        """
        self.base_crane = BaseCrane(base_x, base_y)  # Initialize the base coordinates.
        self.boom = Boom(boom_length, boom_angle)  # Initialize the boom's length and angle.

        # Calculate the boom's end position based on its rotation and length.
        boom_end_x, boom_end_y = self.boom.get_end_position(self.base_crane.x, self.base_crane.y)

        # Initialize the main hoist at the boom's endpoint with a starting and target position.
        self.main_hoist = MainHoist((boom_end_x, boom_end_y, 0), (boom_end_x, boom_end_y, 10))

    def display_status(self) -> None:
        """
        Displays the crane's status, including the base position, boom endpoint, 
        and main hoist unit vector.
        """
        print("Crane is operating with the following components:")
        print(f"Base Position: {self.base_crane.get_position()}")
        print(f"Boom End Position: {self.boom.get_end_position(self.base_crane.x, self.base_crane.y)}")
        print(f"Main Hoist Unit Vector: {self.main_hoist.get_unit_vector()}")


