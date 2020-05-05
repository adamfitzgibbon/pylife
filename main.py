import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_TITLE = "The Game of Life"
SCREEN_ICON = "bacteria.png"

# init and create screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
icon = pygame.image.load("bacteria.png")
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  