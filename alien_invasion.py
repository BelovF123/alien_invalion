import pygame
import control
from ship import Ship



def run():

    pygame.init()
    screen = pygame.display.set_mode((500, 650))
    pygame.display.set_caption("alien_invasoin")
    bg_color = (230, 230, 230)
    ship = Ship(screen)

    while True:
        control.events(ship)
        screen.fill(bg_color)
        ship.update_ship()
        ship.output()

        pygame.display.flip()

run()