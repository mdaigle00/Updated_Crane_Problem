import numpy as np


def calculate_distance_between_float(
    node_i_x: float,
    node_i_y: float,
    node_i_z: float,
    node_j_x: float,
    node_j_y: float,
    node_j_z: float,
) -> float:
    """
    Calculate the distance between two locations, most commonly nodes.

    Args:
        node_i_x: The x component of the starting location.
        node_i_y: The y component of the starting location.
        node_i_z: The z component of the starting location.
        node_j_x: The x component of the ending location.
        node_j_y: The y component of the ending location.
        node_j_z: The z component of the ending location.

    Returns:
        The distance between the start and the end location.
    """

    return np.sqrt(
        (node_j_x - node_i_x) ** 2
        + (node_j_y - node_i_y) ** 2
        + (node_j_z - node_i_z) ** 2
    )


def format_ft(d: float) -> str:
    ft: int = int(d // 12)
    inches: round = d % 12
    return f'{ft:d}ft {inches:d}in'
