# -*- coding: utf-8 -*-
from pygame.locals import *

SCREEN_RECT = Rect(0, 0, 640, 480)

DIRECTION_UP = 0
DIRECTION_DOWN = 1
DIRECTION_LEFT = 2
DIRECTION_RIGHT = 3

K_DIRECT = { 
    K_RIGHT: DIRECTION_RIGHT,
    K_LEFT: DIRECTION_LEFT,
    K_UP: DIRECTION_UP,
    K_DOWN: DIRECTION_DOWN
}

K_NEXT_POS = {
    K_RIGHT: lambda x: (x, 0),
    K_LEFT: lambda x: (-x, 0),
    K_UP: lambda x: (0, -x),
    K_DOWN: lambda x: (0, x)
}

DIRECT_NEXT_POS = {
    DIRECTION_RIGHT: lambda x: (x, 0),
    DIRECTION_LEFT: lambda x: (-x, 0),
    DIRECTION_UP: lambda x: (0, -x),
    DIRECTION_DOWN: lambda x: (0, x)
}

