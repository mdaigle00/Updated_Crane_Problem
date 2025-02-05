import math
import unittest

class Boom:
    """
    This class represents the boom of the crane which rotates around the base pivot.
    The boom has a fixed length and an adjustable angle of rotation.
    """

    def __init__(self, length: float, angle: float):
        """Initialize the boom with a given length and angle.

        Arguments: 
            length (float): The length of the boom.
            angle (float): The angle of the boom in degrees - 
                           converted to radians for calculations.
        """
        self.length = length  # Store the length of the boom
        self.angle = math.radians(angle)  # Convert and store the angle in radians

    def get_end_position(self, base_x: float, base_y: float) -> tuple:
        """Calculate the end position of the boom based on its length and angle.

        The end position is calculated using trigonometric functions:
        - The x-coordinate is calculated using cosine.
        - The y-coordinate is calculated using sine.

        Arguments:
            base_x (float): x-coordinate of the crane base.
            base_y (float): y-coordinate of the crane base.

        Returns:
            tuple: A tuple (x, y) representing the boom's endpoint coordinates.
        """
        end_x = base_x + self.length * math.cos(self.angle)  # Calculate x-coordinate
        end_y = base_y + self.length * math.sin(self.angle)  # Calculate y-coordinate

        return end_x, end_y  # Return calculated endpoint


# Unit tests should be outside the class definition
class TestBoom(unittest.TestCase):
    def test_initialization(self):
        """Test if Boom initializes with the correct length and angle."""
        boom = Boom(15.0, 45.0)
        self.assertEqual(boom.length, 15.0)
        self.assertAlmostEqual(boom.angle, math.radians(45.0), places=5)

    def test_get_end_position(self):
        """Test if get_end_position() correctly calculates coordinates 
        based on base position and boom properties.
        """
        boom = Boom(10.0, 0.0)  # Horizontal boom
        self.assertAlmostEqual(boom.get_end_position(5.0, 5.0)[0], 15.0, places=5)
        self.assertAlmostEqual(boom.get_end_position(5.0, 5.0)[1], 5.0, places=5)

        boom = Boom(10.0, 90.0)  # Vertical boom
        self.assertAlmostEqual(boom.get_end_position(5.0, 5.0)[0], 5.0, places=5)
        self.assertAlmostEqual(boom.get_end_position(5.0, 5.0)[1], 15.0, places=5)


if __name__ == "__main__":
    unittest.main()
