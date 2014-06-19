#Copyright (c) 2013 Nectarios Efstathiou
#Controler for AR Drone
#Import the class and create new object (drone = ArDroneController.Drone())
#Conect the AR Drone (drone.connect()) default ip is 192.168.1.1
#!!!IMPORTANT!!! before takeoff the drone you must make calibrate RUN this (drone.flat_trims())
#drone.takeoff() takeoff
#drone.land() land
#drone.hover() hover
#drone.move(roll, pitch, gaz, yaw) do just one move
#drone.moves(roll, pitch, gaz, yaw, second) move for second(Variable)
######################################################################################
#    roll: left/right tilt [-1..1] (negative: left, positive: right)                 #
#    pitch: forwards/backwards tilt [-1..1] (negative: frontward, positive: backward)#
#    gaz: vertical speed [-1..1] (negative: down, positive: up)                      #
#    yaw: angular speed [-1..1] (negative: spin left, positive: spin right)          #
######################################################################################

import socket
import struct
import pprint
import time

class ArDrone(object):

    cmd_port = 5556

############
#INITIALIZE#
############

    def __init__(self, drone_ip=None, local_ip=None):
        self._sequence = 0
        self.drone_ip = drone_ip or '192.168.1.1'
        self.local_ip = local_ip or '192.168.1.2'
        self.cmd_socket = None

######################
#CONNECT & DISCONNECT#
######################

    def connect(self):
        s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        s.connect( (self.drone_ip, self.cmd_port))
        s.settimeout(5);
        self.cmd_socket = s

    def disconnect(self):
        self.cmd_socket.close()
        self.cmd_socket = None

#############
#AT COMMANDS#
#############

    def send(self, method, params=None):
        self.raw_send(self.build_raw_command(method, params))

    def send_many(self, commands):
        for data in self.build_raw_commands(commands):
            self.raw_send(data)

    def raw_send(self, data):
        '''
        sends the raw data to the drone
        '''
        if not self.cmd_socket:
            raise Exception("Not connected yet!")
        print "sending..."
        print data
        self.cmd_socket.send(data)

    def build_raw_commands(self, commands):
        '''
        TODO: logic to prevent UDP Packets that are larger than 1024 characters
        '''
        r = []
        for command in commands:
            r.append(self.build_raw_command(*command))#build_command
        return [''.join(r)]

    def build_raw_command(self, method, params=None):
        '''
        construct the low level AT command and add the squence number
        '''
        if not params:
            params = []
        params2 = []
        for param in params:
            if type(param) == float:
                 params2.append(str(float2int(param)))
            else:
                params2.append(str(param))
        params_str = ','.join([str(self.sequence())] + params2)
        return 'AT*' + method + '=' + params_str + '\r'

    def sequence(self):
        self._sequence += 1
        return self._sequence

#####################
#PROGRAMING COMMANDS#
#####################
    def takeoff(self):
        """
        If no other command is supplied, the drone enters a hovering mode and
        stays still at approximately 1 meter above ground.
        """
        self.flat_trims()
        self.send('REF', ('290718208',))

    def land(self):
        """
        The drone lands and turns off its motors.
        """
        self.send('REF', ('290717696',))

    def hover(self):
        """
        Tells the drone to hold its position
        """
        self.send_many([
        ('COMWDG',),
        # the first value means move. 0 would mean "hover"
        ('PCMD', (0, 0, 0, 0, 0)),
        ])

    def move(self, roll, pitch, gaz, yaw):
        if ((not bool(roll)) and (not bool(pitch)) and (not bool(gaz)) and (not bool(yaw))):
            #if they are all 0, then this is actually a hover command
            self.hover()
            return
        self.send_many([
            ('COMWDG',),
            # the first value means move. 0 would mean "hover"
            ('PCMD', (1, float(roll), float(pitch), float(gaz), float(yaw))),
        ])

    def flat_trims(self):
        self.send('FTRIM',)

    def moves(self, roll, pitch, gaz, yaw , second):
        if (second == 0):
            return
        if ((not bool(roll)) and (not bool(pitch)) and (not bool(gaz)) and (not bool(yaw))):
            #if they are all 0, then this is actually a hover command
            self.hover()
            return
        endtime = time.time() + second
        while time.time() < endtime:
            self.move(roll,pitch,gaz,yaw)

##############################################################################

def float2int(f):
    """
    Converts a float to a 32bit integer representation following IEEE-754
    >>> float2int(-0.8)
    -1085485875
    """
    return struct.unpack("=i", struct.pack("=f",f) )[0]

def int2float(i):
    """
    Converts a IEEE-754 32bit int representation of a float back to a float
    TODO: the reverse fails... maube just normal float rounding issues?
    >>> int2float(-1085485875)
    -0.800000011920929
    but should be
    -0.8
    """
    return struct.unpack("=f", struct.pack("=i",i) )[0]

##############################################################################
