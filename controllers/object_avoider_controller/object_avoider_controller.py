"""object_avoider_controller controller."""
from controller import Robot, Motor, DistanceSensor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64

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

right_motor.setVelocity(1.0)
left_motor.setVelocity(1.0)

# Main loop:
while robot.step(timestep) != -1:
    pass