"""object_avoider_controller controller."""
from controller import Robot, Motor, DistanceSensor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64

MAX_SPEED = 6.28
MIN_DIST = 0.3

right_motor = robot.getDevice("motor_1")
left_motor = robot.getDevice("motor_2")

front_sensor = robot.getDevice("ds1")
front_left_sensor = robot.getDevice("ds2")
front_right_sensor = robot.getDevice("ds3")
down_sensor = robot.getDevice("ds4")
left_sensor = robot.getDevice("ds5")
right_sensor = robot.getDevice("ds6")

front_sensor.enable(1)
front_left_sensor.enable(1)
front_right_sensor.enable(1)
down_sensor.enable(1)
left_sensor.enable(1)
right_sensor.enable(1)

right_motor.setPosition(float('inf'))
left_motor.setPosition(float('inf'))

right_motor.setVelocity(MAX_SPEED)
left_motor.setVelocity(MAX_SPEED)

def turn_left():
    right_motor.setVelocity(-MAX_SPEED / 2)
    left_motor.setVelocity(MAX_SPEED / 2)
   
def turn_right():
    right_motor.setVelocity(MAX_SPEED / 2)
    left_motor.setVelocity(-MAX_SPEED / 2)
    
def go_straight():
    right_motor.setVelocity(MAX_SPEED)
    left_motor.setVelocity(MAX_SPEED)

# Main loop:
while robot.step(timestep) != -1:
    fl_value = front_left_sensor.getValue() / 1000
    fr_value = front_right_sensor.getValue() / 1000
    f_value = front_sensor.getValue() / 1000
    d_value = down_sensor.getValue() / 1000
    l_value = left_sensor.getValue() / 1000
    r_value = right_sensor.getValue() / 1000
    
    sensor_values = [fl_value, fr_value, f_value, l_value, r_value]
  
    # obstacle avoidance
    for value in sensor_values:
        if value < MIN_DIST or d_value > 0.35:
            turn_right()
            break
            
    # drive straight
    else:
        go_straight()
