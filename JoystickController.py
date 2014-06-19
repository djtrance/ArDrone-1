import gamepad
import ArDroneController
import Capture
from time import sleep

cdrone = ArDroneController.ArDrone()

cdrone.connect()
takeoff = True
land = False
is_capture = False
capture = Capture.Capture()

while 1:
    while (not gamepad.is_ok()):
        print "whait"
    axis = gamepad.get_axis()
    if (axis[0] == -0.1) or (axis[0] == 0.1):
        axis[0] = 0.0
    if (axis[1] == -0.1) or (axis[1] == 0.1):
        axis[1] = 0.0
    button = gamepad.get_buttons()

    try:
        if button[4] == 1:
            cdrone.land()
            cdrone.disconnect()
            print "Drone Landing"
            print 'shutdown!!'
            break
        if button[27] == 1 and takeoff:
            takeoff = False
            land = True
            cdrone.takeoff()
        if button[28] == 1 and land:
            takeoff = True
            land = False
            cdrone.land()
        if not takeoff:
            if axis[2] == 1 or axis[2] == -1:
                cdrone.move(0,0,-axis[2],0)
            if button[0] == 1:
                if axis[0] != 0:
                    cdrone.move(0,0,0,axis[0])
                if axis[1] != 0:
                    cdrone.move(0,0,axis[1],0)
            else:
                if axis[0] != 0:
                    cdrone.move(axis[0],0,0,0)
                if axis[1] != 0:
                    cdrone.move(0,axis[1],0,0)
            if button[1] == 1 and not is_capture:
                is_capture = True
                execfile("Capture.py")
                print"capture"
        else:
            if button[1] == 1 and not is_capture:
                is_capture = True
                execfile("Capture.py")
                print"capture"
    except:
        cdrone.land()
        cdrone.disconnect()
        print "Drone Landing"
