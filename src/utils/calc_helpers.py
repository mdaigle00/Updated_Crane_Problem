import numpy as np
from .util import calculate_distance_between_float

def calculate_unit_vector_float(
    node_i_x: float, node_i_y: float, node_i_z: float,
    node_j_x: float, node_j_y: float, node_j_z: float
) -> tuple[float, float, float]:
    """
    Calculate the unit vector that points from the start location to the end location.

    Args:
        node_i_x (float): The x component of the starting location.
        node_i_y (float): The y component of the starting location.
        node_i_z (float): The z component of the starting location.
        node_j_x (float): The x component of the ending location.
        node_j_y (float): The y component of the ending location.
        node_j_z (float): The z component of the ending location.

    Returns:
        tuple[float, float, float]: The unit vector from the start location to the end location.
                                    Returns (0.0, 0.0, 0.0) if the start and end points are identical.
    """
    distance = calculate_distance_between_float(
        node_i_x, node_i_y, node_i_z,
        node_j_x, node_j_y, node_j_z
    )

    if distance == 0:
        return 0.0, 0.0, 0.0  # Avoid ZeroDivisionError

    i = (node_j_x - node_i_x) / distance
    j = (node_j_y - node_i_y) / distance
    k = (node_j_z - node_i_z) / distance

    return i, j, k


def calculate_moment_about_arbitrary_axis(
    axis_uv: tuple[float, float, float],
    radius_vector: tuple[float, float, float],
    force_vector: tuple[float, float, float]
) -> float:
    """
    Calculates the moment about an arbitrary axis.

    Args:
        axis_uv (tuple[float, float, float]): The unit vector of the arbitrary axis.
        radius_vector (tuple[float, float, float]): The distance from the arbitrary axis to the force vector.
        force_vector (tuple[float, float, float]): The force vector.

    Returns:
        float: The calculated moment about the given axis.
    """
    axis_uv_np = np.array(axis_uv)
    radius_vector_np = np.array(radius_vector)
    force_vector_np = np.array(force_vector)

    overall_moment = np.cross(radius_vector_np, force_vector_np)

    return float(np.dot(axis_uv_np, overall_moment))


def calculate_the_countering_force_to_a_moment(
    axis_uv: tuple[float, float, float],
    moment_about_axis: float,
    suspension_uv: tuple[float, float, float],
    radius_vector: tuple[float, float, float]
) -> float:
    """
    Calculates the counteracting force applied by a suspension element based on the moment about an arbitrary axis.

    Args:
        axis_uv (tuple[float, float, float]): The unit vector of the arbitrary axis that the moment is about.
        moment_about_axis (float): The moment about the above axis.
        suspension_uv (tuple[float, float, float]): The unit vector of the suspension that the force acts in.
        radius_vector (tuple[float, float, float]): The distance from the arbitrary axis to the force vector.

    Returns:
        float: The calculated counteracting force.
    """
    numerator = moment_about_axis
    denominator = (
        (-suspension_uv[1] * radius_vector[2] + suspension_uv[2] * radius_vector[1]) * axis_uv[0]
        + (suspension_uv[0] * radius_vector[2] - suspension_uv[2] * radius_vector[0]) * axis_uv[1]
        + (-suspension_uv[0] * radius_vector[1] + suspension_uv[1] * radius_vector[0]) * axis_uv[2]
    )

    if denominator == 0:
        raise ValueError("Division by zero encountered in countering force calculation.")

    return numerator / denominator


def calculate_minimum_stand_off_point(
    base_x: float, base_y: float, boom_half_length: float, 
    distance_from_building: float, building_height: float
) -> tuple[float, float]:
    """
    Calculates the minimum stand-off point where the crane can place a load 
    without touching the building.

    Args:
        base_x (float): X-coordinate of the crane base.
        base_y (float): Y-coordinate of the crane base.
        boom_half_length (float): Half of the crane boom length.
        distance_from_building (float): Distance from the building to the crane.
        building_height (float): Height of the building.

    Returns:
        tuple[float, float]: The (x, y) coordinates of the minimum stand-off point.
    """
    # Calculate the stand-off point based on crane and building geometry
    stand_off_x = base_x + boom_half_length + distance_from_building
    stand_off_y = max(base_y, building_height)  # Ensure the crane clears the building height

    return stand_off_x, stand_off_y
