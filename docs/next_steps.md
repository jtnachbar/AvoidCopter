# Next steps

We planned on making the quadcopter avoid obstacles autonomously, but we never completed
this part of the project. In its current state, avoidcopter could be extended to achieve
our original goal or any number of other applications.

## Our original plan

We hoped to train [a neural network](http://neuralnetworksanddeeplearning.com/) to output
a safe direction of travel given a pair of images from the onboard cameras. We would
generate training data by flying the quadcopter manually through an obstacle course and
recording the direction of travel for each image pair using an accelerometer. We had not
determined the exact architecture of the network, but we would almost certainly use
[convolutional layers](https://colah.github.io/posts/2014-07-Conv-Nets-Modular/).

## Alternative plans

The combination of quadcopter + [dronekit](../autonomous_flight/dronekit.md) can be used
to make a lot of cool things. Instead of navigating obstacles, you could make it deliver
small items or go around taking pictures of people.
