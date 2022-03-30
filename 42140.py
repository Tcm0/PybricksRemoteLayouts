from pybricks.hubs import TechnicHub
from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.tools import wait

#Thanks to unbrickme for supplying the port configuration
#Thanks to profinerd for testing

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
    if hubOrientation == Side.BOTTOM:
        hub.light.on(Color.ORANGE)
        remoteControl.light.on(Color.ORANGE)
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

    elif hubOrientation == Side.TOP:
        hub.light.on(Color.BLUE)
        remoteControl.light.on(Color.BLUE)
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
    
    #Continue to drive if buttons are still pressed (to complete rolling over)
    #but stop the motors otherwise
    else:
        if (Button.LEFT_PLUS not in pressed) and (Button.LEFT_MINUS not in pressed) and (Button.RIGHT_PLUS not in pressed) and (Button.RIGHT_MINUS not in pressed):
            motor1.brake()
            motor2.brake()

    #Turn the hub off. Shamelessly copied from profinerd
    if (Button.CENTER in pressed):
        hub.system.shutdown()

    wait(100)
