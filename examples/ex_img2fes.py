# -*- coding: utf-8 -*-
# Frapi example, compare the similarity of two face-image.
# each face-image is turned to 128 dim features vector (normalized to 1)
# then get the similairty by simply inner produciton.

# BIG CHENG, init 2019/03/07

import numpy as np
import frapi

import frapi.cli2srv as cli2srv
import frapi.img_util as img_util
import frapi.file_util as file_util

## show basic info
print (frapi.__version__)
print(cli2srv._env.server)
#frapi.frapi_client.FLAGS.server = "127.0.0.1:8500"

## load image
path_img = file_util.fname2path("../imgs", "coco1.png")
print (path_img)

## load image
img1 = img_util.file2img(path_img)
print (img1.shape)

## image to features
fes1 = cli2srv.img2fes(img1)
print (fes1)



