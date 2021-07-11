#Make sure to connect the motor to port A of the hub after uploading

from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.tools import wait

Motor1 = Motor(Port.A)
remoteControl = Remote()
speed = 0
maxSpeed = 15   #max speed = 1500rpm
firstLoop = 1

#main loop
while True:
    #update pressed buttons information
    pressed = remoteControl.buttons.pressed()
    #Make sure that lastPressed is initialized
    #(lastPressed is used to not increase val while button is hold)
    if firstLoop == 1:
        lastPressed = pressed
        firstLoop = 0

    #increase/decrease speed variable between -15 and 15
    if Button.LEFT_PLUS in pressed and not (Button.LEFT_PLUS in lastPressed):
        if speed < maxSpeed:
            speed = speed + 1

    if Button.LEFT_MINUS in pressed and not (Button.LEFT_MINUS in lastPressed):
        if speed > -maxSpeed:
            speed = speed - 1
    
    #emergency stop
    if Button.LEFT in pressed:
        speed = 0

    #make the motor move with the speed (speed val * 100 = rpm)
    Motor1.run(speed*100)

    lastPressed = pressed
    wait(100)