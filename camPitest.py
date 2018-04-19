#from https://github.com/themagpimag/essentials-camera/blob/master/Chapter%2006%20-%20Stop-motion%20and%20selfies/ch6listing1.py
# https://github.com/waveform80/picamera/issues/146
#importing the necessary modules
from datetime import datetime
from gpiozero import Button
import picamera
import time

b=Button(25)
pc=picamera.PiCamera()
running = True
#pc.resolution = (1024, 768)
#use this to set the resolution if you dislike the default values
timestamp=datetime.now()
def picture():
	pc.resolution = (1296,972)
	pc.framerate = 42
	pc.brightness = 60
	# force camera mode to 1296 x 972, capturing full FOV
	pc.crop = (0,0,0.3,0.2)
	pc.capture('pic'+str(timestamp)+'.jpg') #taking the picture

pc.start_preview() #running the preview
b.when_pressed=picture
try:
	while running:
		print('Active')#displaying 'active' to the shell
		time.sleep(1)
#we detect Ctrl-C then quit the program
except KeyboardInterrupt:
	pc.stop_preview()
	running = False
