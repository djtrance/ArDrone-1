ArDrone
=======

### References 
Reference for the ([ArDrone 1.0](http://en.wikipedia.org/wiki/Parrot_AR.Drone)).

###class

######ArDroneController 
Provide the methods to control the Ar Drone

```python
from ArDroneController import ArDrone()

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
