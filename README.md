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
control algorithm. This raspberry pi also transmitted the camera images over wifi to the second raspberry pi located indoors. This 
Raspberry Pi then displays these images on a monitor.

## Components
The following components were used in this project:
- Raspberry Pi 3 Model B V1.2 (x2)
- Pi Camera Module 2
- Pimoroni Pan-Tilt HAT
- HDMI Display (any display works)

![display-pi](https://github.com/jrroches/ME-499-object-tracking-raspis/images/display-pi.jpg?raw=true)

## Installation
To use the source included in this repo, the following 