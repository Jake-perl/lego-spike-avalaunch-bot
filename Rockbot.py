import motion_sensor
import motor
import runloop
from hub import port

front_sensor = motion_sensor.distance(port.B)
left_wheel = motor.dc_motor(port.A)
right_wheel = motor.dc_motor(port.D)
flag_motor = motor.servo_motor(port.C)

def spin_flag():
    while True:
        flag_motor.run(50)
        runloop.pause(1)

runloop.execute(spin_flag)

while True:
    distance = front_sensor.get_distance_cm()

    if distance <= 10:
        left_wheel.start(50)
        right_wheel.start(50)
    else:
        left_wheel.stop()
        right_wheel.stop()

    runloop.pause(0.1)
