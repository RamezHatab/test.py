import random
#width, height
WIDTH = 1600
HEIGHT = 900

IMG_WIDTH = 100
IMG_HEIGHT = 100

FPS = 30

PLAYER_GRAVITY = 0.8
PLAYER_ACC = 0.9
PLAYER_FRICTION = -0.12

GROUND_PLATFORM = (0.0, (HEIGHT - 20), WIDTH, 40)
def CREATE_PLATFORMS():
    return [(0, HEIGHT / 2, 200, 50), (random.randint(200, 500), HEIGHT - random.randint(300, 500), random.randint(100, 200), 50), (random.randint(800, 1000), HEIGHT - random.randint(200, 400), random.randint(100, 200), 50), (1400, HEIGHT - 200, random.randint(100, 200), 50)]
    
PLATFORM_LIST = CREATE_PLATFORMS()
#PLATFORM_LIST_TWO = [(0, HEIGHT / 2, 200, 50), (400, HEIGHT - 400, 200, 50), (900, HEIGHT - 100, 200, 50), (1350, HEIGHT - 119, 200, 50)]
#PLATFORM_DICT = {1 : PLATFORM_LIST_ONE, 2 : PLATFORM_LIST_TWO}

#colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 255)
RED = (255, 0, 0)