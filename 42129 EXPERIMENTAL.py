#THIS IS AN EXPERIMENTAL VERSION!
#I DON'T HAVE THIS SET. I CAN NOT TEST THIS CODE PROPERLY!

#USAGE
#Change difflock with red buttons on remote

#SPECIAL THANKS to Profinerd for providing the port configuration

from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.tools import wait

steering = Motor(Port.D)
driving = Motor(Port.B)
driving2 = Motor(Port.A)
diffLock = DCMotor(Port.C)
remoteControl = Remote()

#steering calibration sequence
steering.run_until_stalled(500)
steering.reset_angle(0)
steering.run_until_stalled(-500)
maxAngle = steering.angle()
steering.run_target(500, (maxAngle/2)+10)
steering.reset_angle(0)

#difflock calibration sequence
diffLock.dc(70)
wait(500)
diffLock.brake()

diffLockPosition = 0

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
    
    if (Button.LEFT in pressed) and (diffLockPosition == 1):
        diffLock.dc(70)
        wait(500)
        diffLock.brake()
        diffLockPosition = 0
    
    if (Button.RIGHT in pressed) and (diffLockPosition == 0):
        diffLock.dc(-70)
        wait(500)
        diffLock.brake()
        diffLockPosition = 1

    #commands to steer
    if Button.RIGHT_PLUS in pressed:
        steering.run_target(1200, (maxAngle/2)-5, Stop.HOLD,False)
    elif Button.RIGHT_MINUS in pressed:
        steering.run_target(1200, -((maxAngle/2)-5), Stop.HOLD,False)
    else:
        steering.run_target(1200, 0, Stop.HOLD, False)

    wait(100)