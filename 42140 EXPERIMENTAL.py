
from pybricks.hubs import TechnicHub
from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.tools import wait

hub = TechnicHub()
motor1 = Motor(Port.B)
motor2 = Motor(Port.A)
remoteControl = Remote()


#main loop
while True:
    #update pressed buttons information
    pressed = remoteControl.buttons.pressed()
    #update orientation of the hub
    hubOrientation = hub.imu.up()

    #commands to drive forwards or backwards
    #they depend on the orientation of the hub
    #for one side, motors are reversed and switched
    if hubOrientation == Side.TOP:
        hub.light.on(Color.RED)
        if Button.LEFT_PLUS in pressed:
            motor2.dc(100)
        elif Button.LEFT_MINUS in pressed:
            motor2.dc(-100)
        else: 
            motor2.brake()
        
        if Button.RIGHT_PLUS in pressed:
            motor1.dc(-100)
        elif Button.RIGHT_MINUS in pressed:
            motor1.dc(100)
        else:
            motor1.brake()

    elif hubOrientation == Side.BOTTOM:
        hub.light.on(Color.GREEN)
        if Button.LEFT_PLUS in pressed:
            motor1.dc(100)
        elif Button.LEFT_MINUS in pressed:
            motor1.dc(-100)
        else: 
            motor1.brake()
        
        if Button.RIGHT_PLUS in pressed:
            motor2.dc(-100)
        elif Button.RIGHT_MINUS in pressed:
            motor2.dc(100)
        else:
            motor2.brake()
        
    else:
        hub.light.on(Color.YELLOW)
        motor1.brake()
        motor2.brake()

    wait(100)