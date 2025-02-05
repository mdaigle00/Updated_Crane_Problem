from ..models.crane import Crane
from ..utils.calc_helpers import (
    calculate_minimum_stand_off_point,
    calculate_moment_about_arbitrary_axis,
    calculate_the_countering_force_to_a_moment
)

def calculate_load_displacement_above_building(
    crane: Crane, distance_from_building: float, building_height: float
) -> tuple[float, float]:
    """
    Calculates the load displacement above the building using the crane's base position.
    
    Args:
        crane (Crane): The crane object.
        distance_from_building (float): The horizontal distance from the building.
        building_height (float): The height of the building.
    
    Returns:
        tuple[float, float]: The stand-off point (x, y) coordinates.
    """
    stand_off_x, stand_off_y = calculate_minimum_stand_off_point(
        crane.base_crane.x,
        crane.base_crane.y,
        crane.boom.length / 2,
        distance_from_building,
        building_height
    )
    return stand_off_x, stand_off_y

def calculate_main_hoist_tension(
    crane: Crane, hook_load: float,
) -> float:
    """
    Calculates the main hoist tension required to counteract the hook load moment.
    
    Args:
        crane (Crane): The crane object.
        hook_load (float): The load applied by the hook in Newtons.
    
    Returns:
        float: The calculated tension force in the main hoist.
    """
    # Determine the boom tip position
    boom_tip_x, boom_tip_y = crane.boom.get_end_position(crane.base_crane.x, crane.base_crane.y)
    
    # Calculate the hook load moment about the boom foot pin
    moment = calculate_moment_about_arbitrary_axis(
        (0, 0, 1),  # Axis unit vector (z-axis for 2D)
        (
            boom_tip_x - crane.base_crane.x,  # X-component of radius vector
            boom_tip_y - crane.base_crane.y,  # Y-component of radius vector
            0  # Z-component is zero in 2D
        ),
        (
            0, -hook_load, 0  # Force vector, with negative Y direction for downward force
        )
    )
    
    # Define the suspension unit vector (acting vertically downward)
    suspension_uv = (0, -1, 0)
    
    # Calculate and return the countering force to balance the moment
    return calculate_the_countering_force_to_a_moment(
        (0, 0, 1),  # Axis unit vector (z-axis for 2D)
        moment,
        suspension_uv,
        (
            boom_tip_x - crane.base_crane.x,
            boom_tip_y - crane.base_crane.y,
            0  # Z-component is zero in 2D
        )
    )
