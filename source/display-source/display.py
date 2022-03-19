import sys
import time
import traceback
import numpy as np
import cv2
import imagezmq
import simplejpeg
from   imutils.video import FPS

try:
    with imagezmq.ImageHub() as image_hub:
        print("Streaming O.K.")
        while True:                    # receive images until Ctrl-C is pressed
            sent_from, jpg_buffer = image_hub.recv_jpg()
            image                 = simplejpeg.decode_jpeg( jpg_buffer, 
                                                            colorspace='BGR')
            # Resize image
            scale_percent = 200
            width = int(image.shape[1]*scale_percent/100)
            height = int(image.shape[0]*scale_percent/100)
            dim = (width, height)
            image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
            cv2.imshow(sent_from, image)  # display images 1 window per sent_from
            cv2.waitKey(1)
            image_hub.send_reply(b'OK')   # REP reply
except (KeyboardInterrupt, SystemExit):
    pass                                  # Ctrl-C was pressed to end program
except Exception as ex:
    print('Python error with no Exception handler:')
    print('Traceback error:', ex)
    traceback.print_exc()
finally:
    print("\nStream stopped.")
    cv2.destroyAllWindows()         # closes the windows opened by cv2.imshow()
    sys.exit()
