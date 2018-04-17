# https://learn.adafruit.com/selfieblock/introduction
# https://learn.adafruit.com/pages/11582/elements/2982628/download

from picamera import PiCamera
from gpiozero import Button
from time import sleep
import time, os
button = Button(14, pull_up=False,)
while True:
    button.wait_for_press()
    name = (time.strftime("%y-%b-%d_%H:%M:%S"))
    fname = "/home/pi/Desktop/mcselfie/" + "Selfie " + name + ".jpg"
    cmd = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Desktop/mcselfie " + "/Selfie_" + name
    command = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload" + fname + "/mcselfie"

    with PiCamera() as camera:
        camera.resolution = (1500,1080)
        camera.start_preview()
        sleep(3)
        camera.stop_preview()
        camera.capture(fname)
        sleep(1)
        os.system(cmd)
