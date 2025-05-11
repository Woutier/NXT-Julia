import time
import nxt.locator
from nxt.motor import Motor, Port, SynchronizedMotors

brick = nxt.locator.find()
print("Connected to:", brick.get_device_info()[0])

left = Motor(brick, Port.B)
right = Motor(brick, Port.C)

sync = SynchronizedMotors(left, right, 0)  

sync.run(100)
time.sleep(1)
sync.idle()

print("Program finished")
