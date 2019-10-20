

import pygame
from pygame.locals import K_LEFT, K_RIGHT

pygame.init()

size = [700, 500]
white = 236, 240, 241
red = 231, 76, 60

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

circle_startx, circle_starty = 350, 250
circle_speed = circle_dx, circle_dy = 5, 5
rect_x, rect_y = 350, 480
shift = 20
max_lives = 3

myfont = pygame.font.SysFont("monospace", 15)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                rect_x += shift
            elif event.key == K_LEFT:
                rect_x += -shift
        elif event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                rect_move = 0
            elif event.key == K_LEFT:
                rect_move == 0

    screen.fill(white)

    # ball
    pygame.draw.circle(screen, red, [circle_startx, circle_starty], 10, 0)
    # bar
    pygame.draw.rect(screen, red, [rect_x, rect_y, 100, 10])

    circle_startx += circle_dx
    circle_starty += circle_dy

    # render text
    lives = myfont.render("Lives: " + str(max_lives), 5, (149, 165, 166))
    screen.blit(lives, (10, 10))

    # Collision with boundaries
    if circle_startx > 680 or circle_startx < 20:
        circle_dx = circle_dx * -1
    if circle_starty < 20:
        circle_dy = circle_dy * -1
    if circle_starty > 500:
        circle_startx, circle_starty = 350, 250
        max_lives = max_lives - 1

    # condition for game over
    if max_lives == 0:
        exit()

    # Collision with the bar
    if circle_starty >= rect_y:
        if circle_startx >= rect_x - 5 and circle_startx <= rect_x + 95:
            circle_dy = circle_dy * -1

    clock.tick(20)  # limits frames per second
    pygame.display.flip()  # updates the screen

pygame.quit()