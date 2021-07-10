from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.tools import wait

steering = Motor(Port.B)
driving = Motor(Port.D)
remoteControl = Remote()

#steering calibration sequence
steering.run_until_stalled(500)
steering.reset_angle(0)
steering.run_until_stalled(-500)
maxAngle = steering.angle()
steering.run_target(500, (maxAngle/2)+10)
steering.reset_angle(0)

#main loop
while True:
    #update pressed buttons information
    pressed = remoteControl.buttons.pressed()

    #commands to drive forwards or backwards
    if Button.LEFT_PLUS in pressed:
        driving.dc(100)
    elif Button.LEFT_MINUS in pressed:
        driving.dc(-100)
    else: 
        driving.brake()

    #commands to steer
    if Button.RIGHT_PLUS in pressed:
        steering.run_target(1200, (maxAngle/2)-5, Stop.HOLD,False)
    elif Button.RIGHT_MINUS in pressed:
        steering.run_target(1200, -((maxAngle/2)-5), Stop.HOLD,False)
    else:
        steering.run_target(1200, 0, Stop.HOLD, False)

    wait(100)