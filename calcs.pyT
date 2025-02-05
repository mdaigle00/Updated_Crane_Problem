from ..models.crane import Crane
from ..utils.calc_helpers import calculate_minimum_stand_off_point, calculate_moment_about_arbitrary_axis, calculate_the_countering_force_to_a_moment


def calculate_load_displacement_above_building(
    crane: Crane, distance_from_building: float, building_height: float
):
    stand_off_x, stand_off_y = calculate_minimum_stand_off_point(
        crane,base_crane.x,
        crane.base_crane.y,
        crane.boom.length / 2,
        distance_from_bjuilding,
        building_height,
        
        # Get parameters from the Crane object or derive them from the building hight and the crane object.
    )
    return stand_off_x, stand_off_y

    # Calculate the load displacement above the building using the minimum stand-off point
    pass

def calculate_main_hoist_tension(
    crane: Crane, hook_load: float,
)-> float:

boom_tip_x, boom_tip_y = crane.boom.get_end_position(crane.base_crane.x, crane.base_crane.y)
    # calculate the hook load moment about the boom foot pin
    moment = calculate_moment_about_arbitrary_axis(
        (0,0,1), #since this example is 2D
        (boom_tip_x - crane.base_Crane.x, boom_tip_y - crane.base_crane.y,0), # the radius vector is an tuple that consists of the x, y, and z (0 since this is 2D) distances from the boom foot pin to the boom tip
        (0, -hook_load, 0), # the force vector is an tuple that consists of the x, y, and z (0 since this is 2D) components of the hook load force acting on the boom tip, hint down is negative y.
    
    suspension_uv = (0,-1,0)
    
    )

    # Calculate the load displacement above the building using the minimum stand-off point
    return calculate_the_countering_force_to_a_moment(
        (0,0,1), #since this example is 2D
        moment,
        suspension_uv,
        (boom_tip_x) - crane.base_crane.x, boom_tip_y - crane.base_crane.y, 0),
        # the rest should be derived from the crane object 
        )
        
