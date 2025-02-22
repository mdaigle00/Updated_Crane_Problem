import sys
from src.utils.calcs import calculate_load_displacement_above_building, calculate_main_hoist_tension
from src.models.crane import Crane
import numpy as np

def main():
    """
    Main function to initialize a crane, perform calculations, and display results.
    """
    # Define crane and boom parameters
    crane_length = 32.791666666666667  # 32ft 9.5in
    boom_foot_pin_x = 6.458333333333333  # 6ft 5.5in
    boom_foot_pin_y = 9.9375  # 9ft 11.25in
    boom_length = 100.0  # 100ft
    boom_width = 2.8333333333333335  # 2ft 10in
    main_suspension_point_x = 20.6875  # 20ft 8.25in
    main_suspension_point_y = 10.416666666666666  # 10ft 5in

    hook_load = 50000.0 # Load force in lbf
    boom_angle = 45  # Boom angle in degrees

    # Initialize the crane object
    crane = Crane(boom_foot_pin_x, boom_foot_pin_y, boom_length, boom_angle)

    # Define building parameters
    building_height = 50.0  # 50ft
    distance_from_building = 10.0  # 10ft

    # Calculate load displacement above the building
    A = distance_from_building
    B = calculate_load_displacement_above_building(crane, A, building_height)
    print(f'Load displacement above building: {B} ft')

    # Calculate the main hoist tension required to support the hook load
    main_hoist_tension = calculate_main_hoist_tension(crane, hook_load)
    print(f'Main hoist tension: {main_hoist_tension} lbf')

    # Display crane status
    crane.display_status()

    return 0

if __name__ == "__main__":
    sys.exit(main())