ArDrone
=======

### References 
Reference for the ([ArDrone 1.0](http://en.wikipedia.org/wiki/Parrot_AR.Drone)).

###Wifi network and connection

The ArDrone can be controlled from any client device supporting the Wifi ad-hoc mode. The ArDrone creates a WIFI network with an ESSID usually called adrone_xxx and self allocates a free, odd IP address. The user connects the client device to this ESSID network.

###class

######ArDroneController 
Provide the methods to control the Ar Drone

```python
from ArDroneController import ArDrone()

drone = ArDrone()

drone.connect() #Connect socket with Drone
drone.disconnect() #Disconnect socket with Drone

drone.takeoff() #Take off the Drone
drone.land() #Land the Drone
drone.hover() #Hover the Drone, actually the drone balancing on the air 
drone.move(Roll, Pitch, Gaz, Yaw) #Do just one move
drone.moves(Roll, Pitch, Gaz, Yaw, second) #Move for second(Variable)
```
Basic moves
```
Roll: left/right tilt [-1..1] (negative: left, positive: right)                 
Pitch: forwards/backwards tilt [-1..1] (negative: frontward, positive: backward)                  
Gaz: vertical speed [-1..1] (negative: down, positive: up)                      
Yaw: angular speed [-1..1] (negative: spin left, positive: spin right) 
```
######ArDroneVideo 
Provide the methods for the Ar Drone Video Streaming.
requirements 
([pygame](http://pygame.org/news.html)).
([psyco](http://psyco.sourceforge.net/)).

```python
import ArDroneVideo

vdrone = ArDroneVideo.ArVideo()

vdrone.connect() #Connect socket with Drone
cdrone.disconnect() #Disconnect socket with Drone

vdrone.video(size) #Initialize video streaming, for original size give 0, to double the size give 1
vdrone.capture(size) #Save the photo, for original size give 0, to double the size give 1
```
