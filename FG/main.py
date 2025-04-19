import pygame
import sys
import math
import random

pygame.init()
pygame.font.init

screen = pygame.display.set_mode((1280, 720)) ## creates a value for the screen/application
pygame.display.set_caption('Aim Practice')

circle_pos = (1280/2, 720/2) # sets the x and y coordinate for the center of the circle at the start of the game
font = pygame.font.SysFont('Arial', 30) ## sets the font, pygame.font is the base function, forward you must describe what font is next wether it comes with pygame or it is a sysfont, after that you must select the font desired.

score = 0
misclick = 0
cr = 50 # circle radius
def check_circle_collison() -> bool:
    mouse_pos = pygame.mouse.get_pos()

    if math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - circle_pos[1])**2) <= 50:
        return True
    return False

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if check_circle_collison():
                    score += 1
                    circle_pos = (random.randint(cr, 1280 - cr), random.randint(cr, 720 - cr))
                else:
                    misclick += 1
 
                

    score_surface = font.render(f'Score: {score} ', True, "black") ## Prints the score on the screen
    misclick_surface = font.render(f'Misclicks: {misclick} ', True, "black") ## Prints the misclicks on the screen
    screen.fill('lightblue')
    pygame.draw.circle(screen, "red", circle_pos, 50)
    screen.blit(score_surface, (50,50))
    screen.blit(misclick_surface, (50,80))

    pygame.display.update()