#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import pygame
from pygame.locals import *

import sprite
import utils
import constants


def game_loop(screen, background):
    # use clock to limit frame update rate
    clock = pygame.time.Clock() 

    all = pygame.sprite.RenderUpdates()
    sprite.Tank.containers = all

    player1 = sprite.Tank()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # refresh screen with changes
        all.clear(screen, background)
        all.update()

        # 
        keystate = pygame.key.get_pressed()
        player1.take_direction(keystate)

        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # set fps up to 40
        clock.tick(40)


def main():
    # Initialize pygame
    pygame.init()

    # Initialize sound subsystem
    
    # Set the display mode 
    win_style = 0 # 1 - fullscreen
    depth = pygame.display.mode_ok(constants.SCREEN_RECT.size, win_style, 32)
    screen = pygame.display.set_mode(constants.SCREEN_RECT.size, win_style, depth)

    # Set icon and title
    icon = pygame.transform.scale(utils.load_image('icon.png'), (24, 24))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('War of Tank')

    # disable cursor 
    pygame.mouse.set_visible(0)

    # create background, solid color with blue
    background = pygame.Surface(constants.SCREEN_RECT.size)
    background.fill(Color(255, 255, 255, 0))
    screen.blit(background, (0,0))
    pygame.display.flip()

    game_loop(screen, background)


if __name__ == "__main__":
    main()
