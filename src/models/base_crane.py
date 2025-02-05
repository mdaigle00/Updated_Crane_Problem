import unittest

class BaseCrane:
    """
    Represents the fixed base of the crane.

    The base is initialized with a fixed (x, y) position, which determines its location in a coordinate system.
    """

    def __init__(self, x: float, y: float):
        """
        Initialize the base crane with a fixed position.

        Arguments:
        x (float): The x-coordinate represents the horizontal position of the base.
        y (float): The y-coordinate represents the vertical position of the base.
        """
        self.x = x  # Store the base's X-coordinate
        self.y = y  # Store the base's Y-coordinate

    def get_position(self) -> tuple:
        """
        Get the current position of the base of the crane.

        Returns:
            tuple: The (x, y) coordinates of the base.
        """
        return self.x, self.y


# Unit tests should be outside the class definition
class TestBaseCrane(unittest.TestCase):
    def test_initialization(self):
        """Test if BaseCrane initializes with correct coordinates."""
        base = BaseCrane(10.5, 20.0)
        self.assertEqual(base.x, 10.5)
        self.assertEqual(base.y, 20.0)

    def test_get_position(self):
        """Test if get_position() returns the correct coordinates."""
        base = BaseCrane(-5.2, 15.8)
        self.assertEqual(base.get_position(), (-5.2, 15.8))


if __name__ == "__main__":
    unittest.main()
