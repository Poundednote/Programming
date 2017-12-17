import pygame
from settings import Settings
import entitys as en
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_length))
    pygame.display.set_caption('Alien Invasion')
    ship = en.Ship(screen)  # Creates ship
    alien = en.Alien(screen)

    # Main loop for game
    while True:
        gf.check_events(ship)  # Watch for keyboard and mouse events
        gf.update_screen(alien, ai_settings, screen, ship)

run_game()
