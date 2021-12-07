import pygame

class Ship():

    def __init__(self, screen):
        """расположение корабля"""

        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """вывод изображения"""
        self.screen.blit(self.image, self.rect)

    def update_ship(self):
        if self.mright == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.mleft == True and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1