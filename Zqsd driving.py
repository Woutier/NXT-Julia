import nxt
import nxt.locator
from nxt.motor import Motor, Port
import threading
import msvcrt  

brick = nxt.locator.find()
print("Connected to:", brick.get_device_info()[0])

left = Motor(brick, Port.B)   
right = Motor(brick, Port.C)  

def control_loop():
    print("Use ZQSD to move, X to stop. Press ESC to quit.")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()

            if key == 'z':
                left.run(80)
                right.run(80)
                print("Forward")
            elif key == 's':
                left.run(-80)
                right.run(-80)
                print("Backward")
            elif key == 'q':
                left.run(80)
                right.run(-80)
                print("Left")
            elif key == 'd':
                left.run(-80)
                right.run(80)
                print("Right")
            elif key == 'x':
                left.brake()
                right.brake()
                print("Stop")
            elif ord(key) == 27:  
                break

try:
    control_thread = threading.Thread(target=control_loop)
    control_thread.start()
    control_thread.join()
except KeyboardInterrupt:
    left.brake()
    right.brake()
    print("\nStopped by user.")