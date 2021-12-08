import pygame.font
from ship import Ship
from pygame.sprite import Group

class Scores():

    def __init__(self, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = 0, 0, 0
        self.font = pygame.font.SysFont(None, 40)
        self.image_score()
        self.image_hscore()
        self.image_lifes()

    def image_hscore(self):

        self.hscore_img = self.font.render(str(self.stats.hscore), True, self.text_color, (230, 230, 230))
        self.hscore_rect = self.hscore_img.get_rect()
        self.hscore_rect.centerx = self.screen_rect.centerx
        self.hscore_rect.top = 10

    def image_score(self):
        """отрисовка счёта"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (230, 230, 230))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 20

    def image_lifes(self):
        self.ships = Group()
        for ship_num in range(self.stats.lifes):
            ship = Ship(self.screen)
            ship.rect.x = 15 + ship_num * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hscore_img, self.hscore_rect)
        self.ships.draw(self.screen)