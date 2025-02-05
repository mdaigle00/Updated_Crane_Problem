import numpy as np

from .util import calculate_distance_between_float


def calculate_unit_vector_float(
    node_i_x: float,
    node_i_y: float,
    node_i_z: float,
    node_j_x: float,
    node_j_y: float,
    node_j_z: float,
) -> tuple[float, float, float]:
    """
    Calculate the unit vector that points from the start location to the end location.

    Args:
        node_i_x: The x component of the starting location.
        node_i_y: The y component of the starting location.
        node_i_z: The z component of the starting location.
        node_j_x: The x component of the ending location.
        node_j_y: The y component of the ending location.
        node_j_z: The z component of the ending location.

    Returns:
        The unit vector from the start location to the end location.
    """
    distance = calculate_distance_between_float(
        node_i_x,
        node_i_y,
        node_i_z,
        node_j_x,
        node_j_y,
        node_j_z,
    )

    i = (node_j_x - node_i_x) / distance
    j = (node_j_y - node_i_y) / distance
    k = (node_j_z - node_i_z) / distance

    return i, j, k


def calculate_moment_about_arbitrary_axis(
    axis_uv: tuple[float, float, float],
    radius_vector: tuple[float, float, float],
    force_vector: tuple[float, float, float],
) -> float:
    """
    Calculates the moment about an arbitrary axis.

    Args:
        axis_uv: The unit vector of the arbitrary axis as a tuple.
        radius_vector: The distance from the arbitrary axis to the force vector as a tuple.
        force_vector: The force vector as a tuple.
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
    radius_vector: tuple[float, float, float],
) -> float:
    """
    Calculates the counteracting force applied by a suspension element  based on the moment about an arbitrary axis.

    Args:
        axis_uv: The unit vector of the arbitrary axis that the moment is about as a tuple.
        moment_about_axis: The moment about the above axis:
        suspension_uv: The unit vector of the suspension that the force acts in.
        radius_vector: The distance from the arbitrary axis to the force vector as a tuple.

    """

    return moment_about_axis / (
        (-suspension_uv[1] * radius_vector[2] + suspension_uv[2] * radius_vector[1])
        * axis_uv[0]
        + (suspension_uv[0] * radius_vector[2] - suspension_uv[2] * radius_vector[0])
        * axis_uv[1]
        + (-suspension_uv[0] * radius_vector[1] + suspension_uv[1] * radius_vector[0])
        * axis_uv[2]
    )


def calculate_minimum_stand_off_point(
    boom_foot_pin_x: float,
    boom_foot_pin_y: float,
    boom_half_width: float,
    building_top_corner_x: float,
    building_top_corner_y: float,
) -> tuple[float, float]:
    """
    Calculates the minimum stand-off from a building to the centerline of the cranes boom. This is similar to the dimensions to point A in the example problems.

    Args:
        boom_foot_pin_x (float): The x-coordinate of the boom foot pin.
        boom_foot_pin_y (float): The y-coordinate of the boom foot pin.
        boom_half_width (float): Half of the width of the cranes boom.
        building_top_corner_x (float): The x-coordinate of the building corner.
        building_top_corner_y (float): The y-coordinate of the building corner.


    Returns:
        A tuple containing the  x and y global location of the correct offset from the building to the centerline of the boom.
    """

    # calculate the distance from the boom foot pin to the corner of the building
    boom_foot_pin_to_point_of_impact = calculate_distance_between_float(
        boom_foot_pin_x,
        boom_foot_pin_y,
        0,
        building_top_corner_x,
        building_top_corner_y,
        0,
    )

    # calculate the angle from the vector boom_foot_pin_to_point_of_impact to the horizontal
    point_of_impact_to_horizontal_angle = np.arctan(
        (building_top_corner_y - boom_foot_pin_y)
        / (building_top_corner_x - boom_foot_pin_x)
    )

    # calculate the angle from the vector boom_foot_pin_to_point_of_impact to the centerline of the boom
    centerline_of_boom_to_point_of_impact_angle = np.arctan(
        (boom_half_width) / (boom_foot_pin_to_point_of_impact)
    )

    # calculate the angle from the centerline of the boom to the horizontal
    centerline_of_boom_to_horizontal_angle = (
        point_of_impact_to_horizontal_angle
        + centerline_of_boom_to_point_of_impact_angle
    )

    # us the pythagorean theorem to solve for the length down the centerline of the boom where impact occurs.
    impact_length_down_boom = np.sqrt(
        boom_foot_pin_to_point_of_impact**2 + boom_half_width**2
    )

    # solve for minimum_standoff_point given:
    standoff_offset_x = impact_length_down_boom * np.cos(
        centerline_of_boom_to_horizontal_angle
    )

    standoff_offset_y = impact_length_down_boom * np.sin(
        centerline_of_boom_to_horizontal_angle
    )

    return (standoff_offset_x+boom_foot_pin_x, standoff_offset_y+boom_foot_pin_y)
