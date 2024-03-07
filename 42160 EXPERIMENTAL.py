from pybricks.hubs import TechnicHub
from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.tools import wait

hub = TechnicHub()
hub.light.on(Color.ORANGE)
steering = Motor(Port.D)
driving = Motor(Port.B)
driving2 = Motor(Port.A)
remoteControl = Remote()
hub.light.on(Color.YELLOW)

#steering calibration sequence
steering.run_until_stalled(500)
steering.reset_angle(0)
steering.run_until_stalled(-500)
maxAngle = steering.angle()
steering.run_target(500, (maxAngle/2)+10)
steering.reset_angle(0)
hub.light.on(Color.GREEN)

#main loop
while True:
    #update pressed buttons information
    pressed = remoteControl.buttons.pressed()

    #commands to drive forwards or backwards
    if Button.LEFT_PLUS in pressed:
        driving.dc(100)
        driving2.dc(100)
    elif Button.LEFT_MINUS in pressed:
        driving.dc(-100)
        driving2.dc(-100)
    else: 
        driving.brake()
        driving2.brake()

    #commands to steer
    if Button.RIGHT_PLUS in pressed:
        steering.track_target((maxAngle/2)-5)
    elif Button.RIGHT_MINUS in pressed:
        steering.track_target(-((maxAngle/2)-5))
    else:
        steering.track_target(0)

    wait(100)