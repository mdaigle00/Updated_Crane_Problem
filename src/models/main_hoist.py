from typing import Tuple
from src.utils.calc_helpers import calculate_unit_vector_float

class MainHoist:
    """
    Represents the main hoist mechanism of the crane.

    The hoist moves between a start and end position in 3D space and
    calculates the unit vector representing its direction.
    """

    def __init__(self, start_location: Tuple[float, float, float], end_location: Tuple[float, float, float]) -> None:
        """
        Initializes the MainHoist class and calculates the unit vector from 
        the start_location to the end_location.

        Args:
            start_location (Tuple[float, float, float]): The starting position of the hoist in (x, y, z) coordinates.
            end_location (Tuple[float, float, float]): The target position of the hoist in (x, y, z) coordinates.
        """
        self.unit_vector = calculate_unit_vector_float(
            start_location[0], start_location[1], start_location[2],
            end_location[0], end_location[1], end_location[2]
        )

    def get_unit_vector(self) -> tuple[float, float, float]:
        """
        Returns the unit vector for the hoist, ensuring NumPy types are converted to standard Python floats.
        """
        return float(self.unit_vector[0]), float(self.unit_vector[1]), float(self.unit_vector[2])
