import ArDroneController
import time
import msvcrt
cdrone = ArDroneController.ArDrone()

cdrone.connect()

try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

while 1:
    c = getch()
    c = c.lower()
    if c == 'q':
        print 'shutdown!!'
        break
    if c == 'a':
        cdrone.move(-1,0,0,0)
    if c == 'd':
        cdrone.move(1,0,0,0)
    if c == 'w':
        cdrone.move(0,-1,0,0)
    if c == 's':
        cdrone.move(0,1,0,0)
    if c == 'l':
        cdrone.move(0,0,0,1)
    if c == 'k':
        cdrone.move(0,0,0,-1)
    if c == 'p':
        cdrone.move(0,0,1,0)
    if c == 'o':
        cdrone.move(0,0,-1,0)
    if c == 'm':
        cdrone.takeoff()
    if c == ' ':
        cdrone.land()
    if c == 'q':
        break

 

