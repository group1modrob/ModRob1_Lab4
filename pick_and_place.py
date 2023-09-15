# Import the necessary libraries to create the PincherX 100 Robot object and use the pi constant later in the code
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np

# All the code that will be run when this file is ran as a script will be in this function
def main():
    # Create the robot object
    bot = InterbotixManipulatorXS(
        robot_model='px100',
        group_name='arm',
        gripper_name='gripper'
    )
    
    # Go to HOME position before doing anything to ensure that we always start from the same spot!
    bot.arm.go_to_home_pose()

    # We instruct the robot to move (not rotate!) 16 cm DOWN in the Z axis 
    bot.arm.set_ee_cartesian_trajectory(z=-0.16)
   
    # The open gripper is now in front of the object to be picked up. Close the gripper, and wait 1 second before proceeding to the next action.    
    bot.gripper.grasp(1.0)

    # Tell the gripper to grasp the object with 50% pressure
    bot.gripper.set_pressure(0.50)

    # After having picked up the object, move 10 cm UP in the Z axis 
    bot.arm.set_ee_cartesian_trajectory(z=0.1)
    
    # Tell the WAIST joint to ROTATE -90 degrees
    bot.arm.set_single_joint_position(joint_name='waist', position=-np.pi/2.0)
    
    # Tell the robot to move down 10 cm in the z position to place the block on the ground
    bot.arm.set_ee_cartesian_trajectory(z=-0.1)
    
    # Once on the ground, release the block and then wait 2 seconds   
    bot.gripper.release(2.0)
    
    # Move back up 10 cm
    bot.arm.set_ee_cartesian_trajectory(z=0.1)
    
    # The pick and place task is done. Go to the home position!
    bot.arm.go_to_home_pose()
    
    # Go to the sleep position
    bot.arm.go_to_sleep_pose()

    # Shutdown the robot
    bot.shutdown()

if __name__ == '__main__':
    main()
