# -*- coding: utf-8 -*-
# Frapi example, calculation confusion matrix from images.

# BIG CHENG, init 2019/03/07

import numpy as np
import frapi.fr_facade as fr

fr1 = fr.fr_facade()

## register images & names
fname_imgs = ["coco1.png", "nicole1.png"]
names = ["coco"] + ["nicole"]
fr1.files2reg(fname_imgs, names)

## query image to check which face similar
print(fr1.file2inf("coco7.png"))
print(fr1.file2inf("nicole7.png"))


