import pygame
from time import *
import struct
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
print 'Initialized Joystick : %s' % j.get_name()
is_finish = True
def float2int(f):
    """
    Converts a float to a 32bit integer representation following IEEE-754
    >>> float2int(-0.8)
    -1085485875
    """
    return struct.unpack("=i", struct.pack("=f",f) )[0]

def int2float(i):
    """
    Converts a IEEE-54 32bit int representation of a float back to a float
    TODO: the reverse fails... maube just normal float rounding issues?
    >>> int2float(-1085485875)
    -0.800000011920929
    but should be
    -0.8
    """
    return struct.unpack("=f", struct.pack("=i",i) )[0]

def is_ok():
    return is_finish

def get_buttons():
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    it = 0 #iterator
    try:
        pygame.event.pump()
    except:
        pygame.init()
        k = pygame.joystick.Joystick(0)
        k.init()
    for i in range(0, j.get_numbuttons()):
        out[it] = j.get_button(i)
        it+=1
    is_finish = True
    return out
def get_axis():
    is_finish = False
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    it = 0 #iterator
    try:
        pygame.event.pump()
    except:
        pygame.init()
        k = pygame.joystick.Joystick(0)
        k.init()
    #Read input from the two joysticks
    for i in range(0, j.get_numaxes()):
        left = False
        right = False
        out[it] = j.get_axis(i)
        if out[it] == 0:
            it+=1
            continue
        out[it]=float2int(out[it])
        temp = str(out[it])
        if i == 3:
            if temp[0] == "-":
                out[it] = int(temp[:3])
            else:
                out[it] = int(temp[:2])
            it += 1
            continue
        a = float(-1207959552) - float(out[it])
        if temp[0] == "-":
            a = float(a) / 12582912
            left = True
        else:
            a = float(a) / (-227331225.6)
            right = True

        out[it] = float(a) / 10
        if out[it] > 1:
            out[it] = 1.0
        elif out[it] < -1:
            out[it] = -1.0
        if (len(str(out[it])) > 4):
            out[it] = out[it] / 2
            if left:
                if (out[it] >= -0.41):
                    out[it] = -0.1
                    break
                temp = str(out[it])
                temp = "-0."+temp[4]
                out[it] = float(temp)
            elif right:
                if (out[it] <= 0.490):
                    out[it] = 0.1
                    break
                temp = str(out[it])
                temp = "0."+temp[4]
                out[it] = float(temp)
        it+=1
    out1 = [0.0,0.0,0.0]
    out1 = [out[0],out[1],out[2]]
    return out1
def get():
    is_finish = False
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    it = 0 #iterator
    try:
        pygame.event.pump()
    except:
        pygame.init()
        k = pygame.joystick.Joystick(0)
        k.init()
    #Read input from the two joysticks
    for i in range(0, j.get_numaxes()):
        left = False
        right = False
        out[it] = j.get_axis(i)
        if out[it] == 0:
            it+=1
            continue
        out[it]=float2int(out[it])
        temp = str(out[it])
        if i == 3:
            if temp[0] == "-":
                out[it] = int(temp[:3])
            else:
                out[it] = int(temp[:2])
            it += 1
            continue
        a = float(-1207959552) - float(out[it])
        if temp[0] == "-":
            a = float(a) / 12582912
            left = True
        else:
            a = float(a) / (-227331225.6)
            right = True

        out[it] = float(a) / 10
        if out[it] > 1:
            out[it] = 1.0
        elif out[it] < -1:
            out[it] = -1.0
        if (len(str(out[it])) > 4):
            out[it] = out[it] / 2
            if left:
                if (out[it] >= -0.41):
                    out[it] = -0.1
                    break
                temp = str(out[it])
                temp = "-0."+temp[4]
                out[it] = float(temp)
            elif right:
                if (out[it] <= 0.490):
                    out[it] = 0.1
                    break
                temp = str(out[it])
                temp = "0."+temp[4]
                out[it] = float(temp)
        it+=1
    return out
    #Read input from buttons
    #for i in range(0, j.get_numbuttons()):
    for i in range(0, j.get_numbuttons()):
        out[it] = j.get_button(i)
        it+=1
    is_finish = True
    return out

def test():
    while True:
        print get()
        sleep(2)
