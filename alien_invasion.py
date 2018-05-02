
import sys

import pygame

def run_game():
    #初始化遊戲並創建一個屏幕對象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Alien Invasion')

    #開始遊戲的主循環
    while True:

        #監視鍵盤和鼠標事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    #讓最近繪制的屏幕可見
        pygame.display.flip()

run_game()

