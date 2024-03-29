import numpy as np
import cv2
from datetime import datetime
import time

from src import functions

startTime = time.time()

data = np.load('src/Data/hw1.npy', allow_pickle=True)

img = functions.render(
    data[()]['verts2d'],
    data[()]['faces'],
    data[()]['vcolors'],
    data[()]['depth'],
    'gouraud'
)

cv2.imwrite(
    'images/img-gouraud-' + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg',
    cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
)

print("--- %s seconds ---" % (time.time() - startTime))