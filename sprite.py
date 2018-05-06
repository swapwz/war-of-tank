# -*- coding: utf-8 -*-

import os
import pygame
from pygame.locals import *

import constants
import utils 


class Tank(pygame.sprite.Sprite):
    hit_point = 100
    speed = 10
    direct_map = { 
            K_RIGHT: constants.DIRECTION_RIGHT,
            K_LEFT: constants.DIRECTION_LEFT,
            K_UP: constants.DIRECTION_UP,
            K_DOWN: constants.DIRECTION_DOWN
        }
    next_pos = {
            K_RIGHT: lambda x: (x, 0),
            K_LEFT: lambda x: (-x, 0),
            K_UP: lambda x: (0, -x),
            K_DOWN: lambda x: (0, x),
        }
    
    def __init__(self, direction=constants.DIRECTION_UP, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.load_images()
        self.image = self.images[direction]
        self.rect = self.image.get_rect()
        self.direction  = constants.DIRECTION_UP

    def load_images(self):
        self.images = {
                constants.DIRECTION_UP: utils.load_image('tank_1_up.png'),
                constants.DIRECTION_DOWN: utils.load_image('tank_1_down.png'),
                constants.DIRECTION_LEFT: utils.load_image('tank_1_left.png'),
                constants.DIRECTION_RIGHT: utils.load_image('tank_1_right.png')
            }

    def take_direction(self, keystate):
        for key in (K_RIGHT, K_LEFT, K_UP, K_DOWN):
            # if it is the first time to change direction 
            # we just change the direction image
            if keystate[key]:
                next_direct = self.direct_map[key]
                if self.direction != next_direct:
                    self.direction = next_direct
                    self.image = self.images[next_direct]
                else: 
                    pos = self.next_pos[key](self.speed)
                    self.rect.move_ip(pos)            
                    self.rect = self.rect.clamp(constants.SCREEN_RECT)
                break


class Shot(pygame.sprite.Sprite):
    speed = -11
    images = []
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()



