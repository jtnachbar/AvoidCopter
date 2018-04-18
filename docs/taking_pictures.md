# Taking Pictures tutorial
In order to generate training data for any decision making models,
we created a script to take pictures using the fisheye cameras
mounted to the front of the drone.

[The script to take pictures](../takeTwoPics.py) is located in this repo. 

If you want the program to run at start up, follow these steps on the Odroid:
1. run `crontab -e`
2. add a line `@reboot ....`
