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

    def direction(self):
        return self.direction

    def fire_pos(self):
        if self.direction == constants.DIRECTION_UP:
            return (self.rect.centerx, self.rect.top)
        elif self.direction == constants.DIRECTION_DOWN:
            return (self.rect.centerx, self.rect.bottom) 
        elif self.direction == constants.DIRECTION_LEFT:
            return (self.rect.left, self.rect.centery)
        elif self.direction == constants.DIRECTION_RIGHT:
            return (self.rect.right, self.rect.centery)


class Shot(pygame.sprite.Sprite):
    speed = 20
    next_pos = {
            constants.DIRECTION_RIGHT: lambda x: (x, 0),
            constants.DIRECTION_LEFT: lambda x: (-x, 0),
            constants.DIRECTION_UP: lambda x: (0, -x),
            constants.DIRECTION_DOWN: lambda x: (0, x),
    }

    def __init__(self, direction, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.load_images()
        self.image = self.images[direction]
        if direction == constants.DIRECTION_UP:
            self.rect = self.image.get_rect(midbottom=pos)
        elif direction == constants.DIRECTION_DOWN:
            self.rect = self.image.get_rect(midtop=pos)
        elif direction == constants.DIRECTION_LEFT:
            self.rect = self.image.get_rect(midright=pos)
        elif direction == constants.DIRECTION_RIGHT:
            self.rect = self.image.get_rect(midleft=pos)
        self.direction = direction

    def update(self):
        new_pos = self.next_pos[self.direction](self.speed)
        self.rect.move_ip(new_pos)
        if not constants.SCREEN_RECT.contains(self.rect):
            self.kill()

    def load_images(self):
        self.images = {
                constants.DIRECTION_UP: utils.load_image('bullet_1_up.png'),
                constants.DIRECTION_DOWN: utils.load_image('bullet_1_down.png'),
                constants.DIRECTION_LEFT: utils.load_image('bullet_1_left.png'),
                constants.DIRECTION_RIGHT: utils.load_image('bullet_1_right.png')
            }

