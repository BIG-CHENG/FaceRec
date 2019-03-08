# -*- coding: utf-8 -*-
# Frapi example, compare the similarity of two face-image.
# each face-image is turned to 128 dim features vector (normalized to 1)
# then get the similairty by simply inner produciton.

# BIG CHENG, init 2019/03/07

import numpy as np
import frapi
import frapi.cli2srv as cli2srv
import frapi.img_util as img_util
import frapi.math_helper as math_helper

def fname2fes(fname):
  if True: ## mnet1
    cli2srv._env.server = "127.0.0.1:8600"
    cli2srv._env.model = "mnet1"
  img = img_util.file2img(fname)
  return cli2srv.img2fes(img)

# convert images to feature vectors
fes_c1 = fname2fes("coco1.png")
fes_c7 = fname2fes("coco7.png")
fes_n1 = fname2fes("nicole1.png")
fes_n7 = fname2fes("nicole7.png")

# show distance
print()
"""
print ("coco vs coco: %f" % np.inner(fes_c1, fes_c7))  # show be larger (>0.6)
print ("coco vs nicole: %f" % np.inner(fes_c1, fes_n1))  # show be smaller (<0.5)
print ("nicole vs nicole: %f" % np.inner(fes_n1, fes_n7))  # show be larger (>0.6)
"""
print ("coco vs coco: %f" % math_helper.fes2sim(fes_c1, fes_c7))  # show be larger (>0.6)
print ("coco vs nicole: %f" % math_helper.fes2sim(fes_c1, fes_n1))  # show be smaller (<0.5)
print ("nicole vs nicole: %f" % math_helper.fes2sim(fes_n1, fes_n7))  # show be larger (>0.6)

