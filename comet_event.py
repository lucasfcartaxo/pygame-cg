import pygame
import os

from comet import Comet
from pygame import mixer

class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 30
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_fill_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def metor_fall(self):
        
        for i in range(20):
            self.all_comets.add(Comet(self))      
            mixer.Sound(os.path.join('assets', 'sounds', 'meteorite.ogg')).play()  

    def attemp_fall(self):

        if self.is_fill_loaded() and len(self.game.all_monsters) == 0:            
            self.metor_fall()
            self.reset_percent()
            self.fall_mode = True

    def update_bar(self, surface):
        
        self.add_percent()

        pygame.draw.rect(surface, (0,0,0), [
            0, # 1 eixo de x
            surface.get_height() - 20, # 1 eixo de y
            surface.get_width(), # largura da barra
            10 # espessura da barra
        ])

        pygame.draw.rect(surface, (187,11,11), [
            0, # 1 eixo de x
            surface.get_height() - 20, # 1 eixo de y
            (surface.get_width() / 100) * self.percent, # largura da barra
            10 # espessura da barra
        ])