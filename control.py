import pygame
import sys
from bullet import Bullet
from alien import Alien

def events(screen, ship, bullets):
    """управление кораблём"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.mright = True
            if event.key == pygame.K_a:
                ship.mleft = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.mright = False
            if event.key == pygame.K_a:
                ship.mleft = False

def update(bg_color, screen, ship, aliens, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.output()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

def update_aliens(aliens):
    aliens.update()

def create_army(screen, aliens):

    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_hight = alien.rect.height

    number_alien_x = int((500 - 2 * alien_width) / alien_width)
    number_alien_y = 3
    for row_number in range(number_alien_y ):
        for alien_number in range (number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_number
            alien.y = alien_hight + alien_hight * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            aliens.add(alien)


