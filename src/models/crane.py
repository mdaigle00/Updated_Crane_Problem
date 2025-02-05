from .main_hoist import MainHoist
from .boom import Boom
from .base_crane import BaseCrane

class Crane: 
    """Represents the Crane object, which consists of:
    -BaseCrane: The fixed based of the crane.
    -Boom: The rotating arm extending from the base.
    -MainHoist: The lifting mecehanism attached to the boom.
    """

    def __init__(self, base_x: float,base_y: float,boom_length: float, boom_angle: float) -> None:
        """Initializes the Crane object with its components.
        """
        self.base_crane = BaseCrane(base_x,base_y) #Create the X and Y coordinate of the crane base.
        self.boom = Boom(boom_length, boom_angle) #Create the Boom Length and Boom Angle.

        #Initialize the main hoist at the boom's end position.
        boom_end_x, boom_end_y = self.boom.get_end_position(self.base_crane.x, self.base_crane.y) #Calculate the boom's end position on its rotation and length.
        self.main_hoist = MainHoist((boom_end_x, boom_end_y,0), (boom_end_x,boom_end_y, 10))

    def display_status(self):
        """
        Print statements to display the base, boom, and hoist vector.
        """
    
        print("Crane is operating with the following components: ")
        print(f"Base Position: {self.base_crane.get_position()}")
        print(f"Boom End Position: {self.boom.get_end_position(self.base_crane.x, self.base_crane.y)}")
        print(f"Main Hoist Unit Vector: {self.main_hoist.get_unit_vector()}")
        
        pass #Placeholder for future functions.
    

