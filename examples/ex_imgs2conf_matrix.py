# -*- coding: utf-8 -*-
# Frapi example, calculation confusion matrix from images.

# BIG CHENG, init 2019/03/07

import numpy as np
import frapi

import frapi.cli2srv as cli2srv
import frapi.img_util as img_util
import frapi.math_helper as math_helper

## load images
fname_imgs = ["coco1.png", "coco7.png", "nicole1.png", "nicole7.png"]
imgs = img_util.files2imgs(fname_imgs)
print (imgs.shape)

## image to features
fess = cli2srv.imgs2fess(imgs)

## calculate confusion matrix
cm = math_helper.fess2confusion(fess)
print (cm)

