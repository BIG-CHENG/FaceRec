# -*- coding: utf-8 -*-
# Frapi example, compare the similarity of two face-image.
# each face-image is turned to 128 dim features vector (normalized to 1)
# then get the similairty by simply inner produciton.

# BIG CHENG, init 2019/03/07

import numpy as np
import frapi
#import face_recognition.api as face_recognition

print (frapi.__version__)

print (dir(frapi))

import frapi.frapi_client

print(frapi.frapi_client._env.server)
#frapi.frapi_client.FLAGS.server = "127.0.0.1:8500"

img1 = frapi.frapi_image.file2img(["coco1.png"])
print (img1)
#print (frapi.frapi_client.img2fes())

exit()
# convert images to feature vectors
fes1 = frapi.frapi_client.img2fes("obama.jpg")
fes2 = frapi.frapi_client.img2fes("biden.jpg")
fesq = frapi.frapi_client.img2fes("obama2.jpg")

# show fes
print (np.inner(fes1, fesq))  # show be larger (>0.6)
print (np.inner(fes2, fesq))  # show be smaller (<0.5)


