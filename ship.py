import pygame

class Ship():

    def __init__(self,screen):
        '''初始化飛船並設置其初始化位置'''
        self.screen = screen

        #加載飛船圖像並獲取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #將每艏飛船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitem(self):
        '''指定位置繪製飛船'''
        self.screen.blit(self.image,self.rect)