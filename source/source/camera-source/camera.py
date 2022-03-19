from imutils.video import VideoStream
from pathlib import Path
import os
import sys
import traceback
import cv2
import time
import socket
import pantilthat as pht
import imagezmq
import simplejpeg


# Set idle timeout
pht.idle_timeout(0.5)

# Set Default Camera position
cam_pan = 90
cam_tilt = 60

# Set up cascade classifier for facial recognition
currPath = Path(os.getcwd())
cascPath = os.path.join(currPath, 'data/lbpcascade_frontalface_improved.xml')
faceCascade = cv2.CascadeClassifier(cascPath)

# Start and set up video capture object
rpi_name     = socket.gethostname() # send RPi hostname with each image
picam        = VideoStream(usePiCamera=True).start()
time.sleep(2.0)                     # allow camera sensor to warm up
jpeg_quality = 25                    # 0 to 100, higher is better quality

# Turn camera on and move to the start position
pht.pan(cam_pan-90)
pht.tilt(cam_tilt-90)

print("Tracking Starting in 5sec")
time.sleep(5)
print("Tracking now.")

try:
    with imagezmq.ImageSender(connect_to='tcp://bertpi-2:5555') as sender:
        while True:                 # send images as a stream until Ctrl-C

            # Capture video
            frame = picam.read()

	    # Get image dimensions
            (FRAME_H, FRAME_W) = frame.shape[:2]

	    # Invert the video
            frame = cv2.flip(frame, 0)

            # Convert images to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)

            # Perform face detection
            faces = faceCascade.detectMultiScale(gray, 1.1, 3, 0, (10, 10))

            # Perform tracking
            for (x, y, w, h) in faces:

                # draw rectangle around original image
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 4)

                # Get the center of the face
                x = x + (w/2)
                y = y + (h/2)

		# Correct relative to center of image
                turn_x = float(x - (FRAME_W/2))
                turn_y = float(y - (FRAME_H/2))

		# Convert to percentage
                turn_x /= float(FRAME_W)
                turn_y /= float(FRAME_H)

                # Scale the offset to degrees
                scale_factor_pan = 30
                scale_factor_tilt = 30
                turn_x *= scale_factor_pan
                turn_y *= scale_factor_tilt
                cam_pan += turn_x
                cam_tilt += turn_y

                # print(cam_pan-90, cam_tilt-90)

                # Clamp Pan/Tilt to 0 to 180 degrees
                cam_pan = max(0, min(180, cam_pan))
                cam_tilt = max(0, min(180, cam_tilt))

                # Update the Servos
                pht.pan(int(cam_pan-90))
                pht.tilt(int(cam_tilt-90))

                # limit to first face
                break

            jpg_buffer     = simplejpeg.encode_jpeg(frame, quality=jpeg_quality, colorspace='BGR')
            reply_from_mac = sender.send_jpg(rpi_name, jpg_buffer)
except (KeyboardInterrupt, SystemExit):
    pass                            # Ctrl-C was pressed to end program
except Exception as ex:
    print('Python error with no Exception handler:')
    print('Traceback error:', ex)
    traceback.print_exc()
finally:
    print("\nStream stopped.")
    picam.stop()                    # stop the camera thread
    sys.exit()
