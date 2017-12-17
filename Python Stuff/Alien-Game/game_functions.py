import pygame
import sys


def check_events(ship):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 10
            if event.key == pygame.K_LEFT:
                ship.rect.centerx -= 10


# Redraw the screen during each pass through the loop.
def update_screen(ai_settings, screen, ship, alien):
    screen.fill(ai_settings.bg_colour)
    ship.blitme()  # Draws the ships pixels to a position
    pygame.display.flip()  # Make the most recently drawn screen visible.


