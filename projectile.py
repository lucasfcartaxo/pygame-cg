import pygame
import os

from pygame import mixer

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 12
        self.image = pygame.image.load(os.path.join('assets','projectile.png'))
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 150
        self.rect.y = self.player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.demage(self.player.attack)

        if self.rect.x > 1000:
            self.remove()
