"""object_avoider_controller controller."""
from controller import Robot, Motor, DistanceSensor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64

MAX_SPEED = 6.28

right_motor = robot.getDevice("motor_1")
left_motor = robot.getDevice("motor_2")

front_sensor = robot.getDevice("ds1")
front_left_sensor = robot.getDevice("ds2")
front_right_sensor = robot.getDevice("ds3")

front_sensor.enable(1)
front_left_sensor.enable(1)
front_right_sensor.enable(1)

right_motor.setPosition(float('inf'))
left_motor.setPosition(float('inf'))

right_motor.setVelocity(MAX_SPEED)
left_motor.setVelocity(MAX_SPEED)

def turn_left():
    right_motor.setVelocity(MAX_SPEED / 2)
    left_motor.setVelocity(-MAX_SPEED / 2)
   
def turn_right():
    right_motor.setVelocity(-MAX_SPEED / 2)
    left_motor.setVelocity(MAX_SPEED / 2)
    
def go_straight():
    right_motor.setVelocity(MAX_SPEED)
    left_motor.setVelocity(MAX_SPEED)

# Main loop:
while robot.step(timestep) != -1:
    fl_value = front_left_sensor.getValue() / 1000
    fr_value = front_right_sensor.getValue() / 1000
    f_value = front_sensor.getValue() / 1000

    # obstacle avoidance
    if f_value < 1 or fl_value < 1 or fr_value < 1:
        if fr_value < fl_value:
            turn_right()
        else:
            turn_left()
            
    # drive straight
    else:
        go_straight()
