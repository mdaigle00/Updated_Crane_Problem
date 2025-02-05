class BaseCrane:
    """
    Represents the fixed base of the crane."""

    def __init__(self, x: float, y: float):
        """
        Initialize the base crane with a fixed position.
        The x-coordinate represents the horizontal position of the base.
        The y-coordinate represents the vertical position of the base.
        
        """
        self.x = x #Store the base's X-coordinate
        self.y = y #Store the base's Y-coordinate

    def get_position(self) -> tuple:
        """Returns the base of the crane as a tuple(x,y)."""
        return self.x, self.y
