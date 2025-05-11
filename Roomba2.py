import time
import random
import nxt.locator
import nxt.motor
import nxt.sensor
import nxt.sensor.generic
from nxt.motor import SynchronizedMotors

with nxt.locator.find() as brick:
    print("Connected to:", brick.get_device_info()[0])

    left_motor = nxt.motor.Motor(brick, nxt.motor.Port.B)
    right_motor = nxt.motor.Motor(brick, nxt.motor.Port.C)
    sync_motors = SynchronizedMotors(left_motor, right_motor, 0)

    touch = brick.get_sensor(nxt.sensor.Port.S4, nxt.sensor.generic.Touch)

    def drive_forward():
        sync_motors.run(80)

    def stop():
        sync_motors.idle()

    def reverse(duration=1.0):
        print("Reversing")
        sync_motors.run(-80)
        time.sleep(duration)
        stop()

    def random_turn():
        direction = random.choice(['left', 'right'])
        degrees = random.randint(90, 360)
        power = 80
        print(f"Turning {direction} for {degrees}°")

        # Turn time calculation
        turn_time = degrees / 180.0

        if direction == 'left':
            left_motor.run(power)
            right_motor.run(-power)
        else:
            left_motor.run(-power)
            right_motor.run(power)

        time.sleep(turn_time)
        stop()

    print("Program started")
    try:
        while True:
            drive_forward()
            if touch.get_sample() == 1:
                print("Collision")
                stop()
                reverse()
                random_turn()
            time.sleep(0.05)

    except KeyboardInterrupt:
        stop()
        print("Program stopped")
