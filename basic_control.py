import dronekit
from time import sleep
drone=dronekit.connect("/dev/ttyUSB0")
drone.groundspeed=1 #m/s
condition_yaw(0)
print("sending ned")
dronekit.send_ned_velocity(.2,0,0) #Coordinates are north, east, down (so south, west, up are negative)
print("finished sending ned")
#sleep(10)
#dronekit.send_ned_velocity(0,0,0)
#vehicle.mode = VehicleMode("LAND")
