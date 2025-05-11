
import time
import nxt.locator
import nxt.sensor
import nxt.sensor.generic  

with nxt.locator.find() as b:
    print("Connected to:", b.get_device_info()[0])

    sensor = b.get_sensor(nxt.sensor.Port.S4, nxt.sensor.generic.Touch)

    print("Program started")
    while True:
        val = sensor.get_sample()  
        print("Touch Sensor:", "Pressed" if val else "Not pressed")
        time.sleep(0.5)
