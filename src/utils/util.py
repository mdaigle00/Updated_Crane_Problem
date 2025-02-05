import numpy as np

def calculate_distance_between_float(
    node_i_x: float, node_i_y: float, node_i_z: float,
    node_j_x: float, node_j_y: float, node_j_z: float
) -> float:
    """
    Calculate the Euclidean distance between two points in 3D space.

    Args:
        node_i_x (float): The x coordinate of the first point.
        node_i_y (float): The y coordinate of the first point.
        node_i_z (float): The z coordinate of the first point.
        node_j_x (float): The x coordinate of the second point.
        node_j_y (float): The y coordinate of the second point.
        node_j_z (float): The z coordinate of the second point.

    Returns:
        float: The Euclidean distance between the two points.
    """
    return np.sqrt(
        (node_j_x - node_i_x) ** 2 +
        (node_j_y - node_i_y) ** 2 +
        (node_j_z - node_i_z) ** 2
    )


def format_ft(d: float) -> str:
    """
    Converts a measurement in inches to a feet-and-inches format.

    Args:
        d (float): The total measurement in inches.

    Returns:
        str: The formatted string representing feet and inches.

    Example:
        >>> format_ft(74)
        '6ft 2in'
    """
    if d < 0:
        return "Invalid input"  # Handle negative distances

    ft: int = int(d // 12)  # Extract whole feet
    inches: int = round(d % 12)  # Extract remaining inches
    return f"{ft}ft {inches}in"
