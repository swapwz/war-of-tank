# -*- coding: utf-8 -*-

import os
import random
import math

import pygame
from pygame.locals import *

import constants
import utils 


class Monster(pygame.sprite.Sprite):
    hit_point = 100     
    speed = 1 

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.load_images()
        self.direction = utils.random_direction()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        new_pos = math.floor(random.random() * 40), math.floor(random.random() * 80)
        self.rect.move_ip(new_pos)

    def load_images(self):
        self.images = {
                constants.DIRECTION_UP: utils.load_image('enemy_1_up.png'),    
                constants.DIRECTION_DOWN: utils.load_image('enemy_1_down.png'),    
                constants.DIRECTION_RIGHT: utils.load_image('enemy_1_right.png'),    
                constants.DIRECTION_LEFT: utils.load_image('enemy_1_left.png')    
            }

    def update(self):
        self.direction = utils.random_direction()
        new_pos = constants.DIRECT_NEXT_POS[self.direction](self.speed)
        self.rect.move_ip(new_pos)
        if not constants.SCREEN_RECT.contains(self.rect):
            self.kill()

       
        

class Tank(pygame.sprite.Sprite):
    hit_point = 100
    speed = 3 
        
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
                next_direct = constants.K_DIRECT[key]
                if self.direction != next_direct:
                    self.direction = next_direct
                    self.image = self.images[next_direct]
                else: 
                    pos = constants.K_NEXT_POS[key](self.speed)
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
        new_pos = constants.DIRECT_NEXT_POS[self.direction](self.speed)
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

