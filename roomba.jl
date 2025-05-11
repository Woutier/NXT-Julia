using PyCall
using Random
using Dates

nxt = pyimport("nxt")
nxt_locator = pyimport("nxt.locator")
nxt_motor = pyimport("nxt.motor")
nxt_sensor = pyimport("nxt.sensor")
nxt_generic = pyimport("nxt.sensor.generic")

brick = nxt_locator.find()
info = brick[:get_device_info]()  
println("Connected to: ", info[1])  

left_motor = nxt_motor.Motor(brick, nxt_motor.Port.B)
right_motor = nxt_motor.Motor(brick, nxt_motor.Port.C)

touch = brick.get_sensor(nxt_sensor.Port.S4, nxt_generic.Touch)

function drive_forward()
    left_motor[:run](80)
    right_motor[:run](80)
end

function stop()
    left_motor[:brake]()
    right_motor[:brake]()
end

function reverse(duration::Float64=1.0)
    println("Reversing")
    left_motor[:run](-80)
    right_motor[:run](-80)
    sleep(1)
    stop()
end

function random_turn()
    direction = rand(["left", "right"])
    degrees = rand(90:360)
    power = 80
    println("Turning $direction for $(degrees)°")  

    turn_time = degrees / 180.0  # Turn formula

    if direction == "left"
        left_motor[:run](power)
        right_motor[:run](-power)
    else
        left_motor[:run](-power)
        right_motor[:run](power)
    end

    sleep(turn_time)
    stop()
end

println("Program started")
try
    while true
        drive_forward()
        is_pressed = touch[:get_sample]() == 1
        if is_pressed
            println("Collision")
            stop()
            reverse()
            random_turn()
        end
        sleep(0.05)
    end
catch e
    stop()
    println("Program stopped")
    println(e)
end
