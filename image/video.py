#!/bin/env python3
import glob
import numpy as np
from scipy.misc import imsave, imread

THRESHOLD_LOWER = np.array([210, 190, 5])
THRESHOLD_UPPER = np.array([255, 250, 70])


def filter_image(image):
    return np.all(np.logical_and(THRESHOLD_LOWER < image, image < THRESHOLD_UPPER), axis=2)


def find_ball(image_filtered):
    ball_pixels = np.where(image_filtered)
    if not len(ball_pixels):
        return (float('nan'), float('nan'))
    here_it_is = np.median(ball_pixels[0]), np.median(ball_pixels[1])
    return here_it_is


for fname in glob.glob('*.jpg'):
    image = imread(fname)

    image_filtered = filter_image(image)
    here_it_is = find_ball(image_filtered)

    #or_here = np.array((here_it_is[1], here_it_is[0]))

    pixel_size = 20
    out = np.zeros(image.shape)
    if any(np.isnan(here_it_is)):
        continue
    out[int(here_it_is[0] - pixel_size):int(here_it_is[0] + pixel_size),
        int(here_it_is[1] - pixel_size):int(here_it_is[1] + pixel_size), 0] = 1
    out[:, :, 1] = image_filtered.astype(int)
    imsave("{}_filtered.jpg".format(*fname.split('.')), out)

    # imshow(image)
    # plot(*or_here, 'ro')
