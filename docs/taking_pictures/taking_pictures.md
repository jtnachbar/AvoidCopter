# Taking Pictures tutorial
In order to generate training data for any decision making models,
we created a script to take pictures using the fisheye cameras
mounted to the front of the drone.

[The script to take pictures](../takeTwoPics.py) is located in this repo.
For more information on how it works, view the file itself.

### Running the picture taking script on start up
To avoid the inconvenience of SSHing or plugging input devices into the Odroid,
you can make the picture taking script run automatically, whenver the Odroid is turned on.
Follow these steps in a terminal on the Odroid:
1. run `crontab -e`
2. A text editor will appear. Add a line to the end of the file:
```bash
@reboot python /home/odroid/avoidcopter/takeTwoPics.py 2> /home/odroid/image_error.log`
```

If your local AvoidCopter repo is stored in a different path, you should point to that one instead.

The purpose of the `2> /home/odroid/image_error.log` is to be able to see any errors that might be occuring.

By default, the script will take a 100 pairs of pictures with a 5 second pause in between each pair.
You can customize this by running the script with command line arguments, like so:
```bash
@reboot python /home/odroid/avoidcopter/takeTwoPics.py 200 1 # 200 pairs with 1 second pauses 
```
