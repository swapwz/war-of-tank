# -*- coding: utf-8 -*-

import os
import random
import math
import pygame

RESOURCES_DIR = './resources'


def load_image(img_path):
    file = os.path.join(RESOURCES_DIR, img_path)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image %s: %s' % (file, pygame.get_error()))
    return surface

def random_direction():
    return math.floor(random.random() * 4)
    
