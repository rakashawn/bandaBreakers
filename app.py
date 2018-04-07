# app.py
# https://medium.com/@petehouston/apply-image-effect-to-raspberry-pi-camera

import picamera
from time import sleep

effects = ['none', 'negative', 'sketch', 'denoise', 'emboss', 'oilpaint', 'hatch', 'gpen',  'pastel', 'watercolor',  'film', 'blur', 'saturation']

camera = picamera.PiCamera()

camera.resolution = (1280, 720)

camera.start_preview()

sleep(2)

for s in effects:
  print("Effect: " + s)
  camera.image_effect = s
  camera.capture('snapshot_' + s + '.jpg')
camera.stop_preview()
