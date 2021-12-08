import pygame
import control
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from scores import Scores

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
    sc = Scores(screen, stats)

    while True:
        control.events(screen, ship, bullets)
        if stats.run_game ==True:
            ship.update_ship()
            control.update(bg_color, screen, stats, sc, ship, aliens, bullets)
            control.update_bullets(screen, stats, sc, bullets, aliens)
            control.update_aliens(stats, sc, screen, ship, aliens, bullets)

run()