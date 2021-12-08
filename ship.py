import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, screen):
        """расположение корабля"""
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """вывод изображения"""
        self.screen.blit(self.image, self.rect)

    def update_ship(self):
        if self.mright == True and self.rect.right < self.screen_rect.right:
            self.center += 0.5
        if self.mleft == True and self.rect.left > 0:
            self.center -= 0.5

        self.rect.centerx = self.center

    def create_ship(self):

        self.center = self.screen_rect.centerx
