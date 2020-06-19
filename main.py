import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_TITLE = "The Game of Life"
SCREEN_ICON = "images/bacteria.png"

# init and create screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
icon = pygame.image.load(SCREEN_ICON)
pygame.display.set_icon(icon)

# entity
entityImg = pygame.image.load(SCREEN_ICON)
entityX, entityY = 370, 480
entityXChange, entityYChange = 0, 0


def entity(x, y):
    screen.blit(entityImg, (x, y))


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                entityXChange = -.3
            if event.key == pygame.K_RIGHT:
                entityXChange = .3
            if event.key == pygame.K_UP:
                entityYChange = -.3
            if event.key == pygame.K_DOWN:
                entityYChange = .3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                entityXChange = .3
            if event.key == pygame.K_RIGHT:
                entityXChange = -.3
            if event.key == pygame.K_UP:
                entityYChange = .3
            if event.key == pygame.K_DOWN:
                entityYChange = -.3

    screen.fill((100, 150, 50))
    entityX += entityXChange
    entityY += entityYChange

    if entityX <= 0:
        entityX = 0
    if entityX >= SCREEN_WIDTH - 32:
        entityX = SCREEN_WIDTH - 32
    if entityY <= 0:
        entityY = 0
    if entityY >= SCREEN_HEIGHT - 32:
        entityY = SCREEN_HEIGHT - 32

    entity(entityX, entityY)
    pygame.display.update()
