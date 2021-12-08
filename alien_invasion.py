import pygame
import control
from ship import Ship
from pygame.sprite import Group
from stats import Stats


def run():

    pygame.init()
    screen = pygame.display.set_mode((500, 650))
    pygame.display.set_caption("alien_invasoin")
    bg_color = (230, 230, 230)
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    control.create_army(screen, aliens)
    stats = Stats()

    while True:
        control.events(screen, ship, bullets)
        ship.update_ship()
        control.update(bg_color, screen, ship, aliens, bullets)
        control.update_bullets(screen, bullets, aliens)
        control.update_aliens(stats, screen, ship, aliens, bullets)

run()