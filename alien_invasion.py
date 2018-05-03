import pygame

from pygame.locals import *
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    #初始化pygame,設置和屏幕對象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #創建一艏飛船
    ship = Ship(screen)


    #開始遊戲的主循環
    while True:
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)







run_game()

