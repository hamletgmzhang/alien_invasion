import sys

import pygame

def check_events():
    '''響應按鍵和鼠標事件'''
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    '''更新屏幕上的圖像，並切換到新屏幕'''
    #每次循環時都重繪屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitem()

    # 讓最近繪制的屏幕可見
    pygame.display.flip()