import pygame

class Ship:

    def __init__(self, screen):
        self.screen = screen

        # Load The ships image
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start new ships at bottom of screen

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
