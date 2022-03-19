# ME 499 Independent Study: Raspberyy Pi Home Security System

For this independent study, I explored the application of a linux based controller 
to a couple of different engineering disciplines: motor control, computer vision, and controller networking. 
To weave all three of these disciplines together, I propose to design a motion(face) detection home security
system using Raspberry Pi’s. A perfect product would feature one controller mounted near a gate or entrance outside,
and one controller located indoors in an office. The exterior-mounted controller controls a camera mounted on a pan-tilt 
base; the interior controller is connected to an HD display. As a person approaches the home, the camera outside detects 
and tracks them, alerts the controller indoors, an if armed - shines a spotlight on the intruder.

For this independent study, I achieved all the above except the spotlight feature (was not able to procure one). I was able
program one Raspberry Pi with a Pi-camera V2 and a Pan-Tilt hat to track human faces and track them with a simple computer vision 
control algorithm. This raspberry pi also transmitted the camera images over wifi using the ZeroMQ protocol to the second raspberry pi located indoors. This 
Raspberry Pi then displays these images on a monitor.

## Components

The following components were used in this project:
- Raspberry Pi 3 Model B V1.2 (x2)
- Pi Camera Module 2
- Pimoroni Pan-Tilt HAT
- HDMI Display (any display works)

## Installation

Begin by installing the latest version of Raspbian onto each Raspberry Pi using the Raspberry Pi Imager tool. Enable ssh on both Raspberry Pi's.
Designate one Pi as the camera Pi, and the other Pi as the display Pi. Make sure both can connect to the correct network.

Now, install the following packages on both Pis. No virtual environment was used in this project, but it is highly recommended.
- opencv-python
	- follow the instructions at this link: [pip install OpenCV](https://pyimagesearch.com/2018/09/19/pip-install-opencv/)
- numpy 
	- make sure to force it to upgrade - necessary to work with opencv
- imutils
- pantilthat
	- follow the instructions at this link : [Pimoroni Pan-Tilt HAT python package](https://github.com/pimoroni/pantilt-hat)
- imagezmq

Next, within the `source` folder are two folders:
- `camera-source`
- `display-source`

Using a computer terminal, secure copy the folders above into the directory of your choice in the corresponding Raspberry Pi.

Installation is now complete!.

## Running the Project

In order to run the project, simply ssh into each Raspberry Pi and navigate to the directory where you copied the folders above.
Once in the `camera-source` and `display-source` directories, simply run these commands in the following order (on their respective Raspberyy Pi's):
1. `python display.pi`
2. `python camera.pi`

It is necessary that the display software be run first in order for images to begin streaming.

## Results

See the `images` folder in this repository for a demonstration.