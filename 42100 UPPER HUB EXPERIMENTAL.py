#THIS IS AN EXPERIMENTAL VERSION!
#I DON'T HAVE THIS SET. I CAN NOT TEST THIS CODE PROPERLY!

#INSTALLATION:
#Install this on the hub in the upper part. Connect one remote to it
#Install the code for the lower hub on the lower hub. Connect another remote.

#USAGE
#Change "mode" with red buttons on remote (A+B = left mode, C+D = right mode)

from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.tools import wait

Motor1 = Motor(Port.A)
Motor2 = Motor(Port.B)
Motor3 = Motor(Port.C)
Motor4 = Motor(Port.D)
remoteControl = Remote()
mode = 0
#main loop
while True:
    #update pressed buttons information
    pressed = remoteControl.buttons.pressed()

    if Button.LEFT in pressed:
        mode = 0
    elif Button.RIGHT in pressed:
        mode = 1

    #commands to drive forwards or backwards
    if mode == 0:
        Motor3.dc(0)
        Motor4.dc(0)
        if Button.LEFT_PLUS in pressed:
            Motor1.dc(100)
        elif Button.LEFT_MINUS in pressed:
            Motor1.dc(-100)
        else: 
            Motor1.dc(0)
        
        if Button.RIGHT_PLUS in pressed:
            Motor2.dc(100)
        elif Button.RIGHT_MINUS in pressed:
            Motor2.dc(-100)
        else:
            Motor2.dc(0)

    else:
        Motor1.dc(0)
        Motor2.dc(0)
        if Button.LEFT_PLUS in pressed:
            Motor3.dc(100)
        elif Button.LEFT_MINUS in pressed:
            Motor3.dc(-100)
        else:
            Motor3.dc(0)

        if Button.RIGHT_PLUS in pressed:
            Motor4.dc(100)
        elif Button.RIGHT_MINUS in pressed:
            Motor4.dc(-100)
        else:
            Motor4.dc(0)

    wait(100)