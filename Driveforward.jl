using PyCall

nxt = pyimport("nxt")
nxt_locator = pyimport("nxt.locator")
nxt_motor = pyimport("nxt.motor")

try
    brick = nxt_locator.find()
    info = brick[:get_device_info]()
    println("Connected to: ", info[1])  

    left_motor = nxt_motor.Motor(brick, nxt_motor.Port.B)
    right_motor = nxt_motor.Motor(brick, nxt_motor.Port.C)

    sync = nxt_motor.SynchronizedMotors(left_motor, right_motor, 0)

    println("Program started")
    sync[:run](80)   
    sleep(2.0)

    sync[:idle]()
    println("Program stopped")

    if haskey(brick, :sock)
        brick[:sock][:close]()
        println("Connection closed.")
    end

catch e
    println("Error:", e)
end
