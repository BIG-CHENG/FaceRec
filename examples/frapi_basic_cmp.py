# -*- coding: utf-8 -*-
# Frapi example, compare the similarity of two face-image.
# each face-image is turned to 128 dim features vector (normalized to 1)
# then get the similairty by simply inner produciton.

# BIG CHENG, init 2019/03/07

import numpy as np
import frapi
import frapi.frapi_client

def fname2fes(fname):
  if True: ## mnet1
    frapi.frapi_client._env.server = "127.0.0.1:8600"
    frapi.frapi_client._env.model = "mnet1"
  img = frapi.frapi_image.file2img(fname)
  return frapi.frapi_client.img2fes(img)

# convert images to feature vectors
fes_c1 = fname2fes("coco1.png")
fes_c7 = fname2fes("coco7.png")
fes_n1 = fname2fes("nicole1.png")
fes_n7 = fname2fes("nicole7.png")

# show distance
print()
print ("coco vs coco: %f" % np.inner(fes_c1, fes_c7))  # show be larger (>0.6)
print ("coco vs nicole: %f" % np.inner(fes_c1, fes_n1))  # show be smaller (<0.5)
print ("nicole vs nicole: %f" % np.inner(fes_n1, fes_n7))  # show be larger (>0.6)


