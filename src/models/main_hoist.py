from typing import Tuple
from src.utils.calc_helpers import calculate_unit_vector_float


class MainHoist:
    
    def __init__(self, start_location: Tuple[float,float, float] , end_location: Tuple[float,float, float]) -> None:

        """Initializes the MainHoist class and calculates the unit
        vector from the start_location to end_location. """
        

        self.unit_vector = calculate_unit_vector_float(
            start_location[0],
            start_location[1],
            start_location[2],
            end_location[0],
            end_location[1],
            end_location[2],
            )

    def get_unit_vector(self) ->  Tuple[float,float, float]:
        """
        Returns the unit vector for the hoist.
        """
        return self.unit_vector
    