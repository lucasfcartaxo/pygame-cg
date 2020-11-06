import pygame
import os

from pygame import mixer
from player import Player
from monster import Monster
from comet_event import CometFallEvent


class Game:

	def __init__(self):
		self.all_players = pygame.sprite.Group()
		self.all_monsters = pygame.sprite.Group()
		self.player = Player(self)		
		self.all_players.add(self.player)
		self.comet_event = CometFallEvent(self)
		self.pressed = {}
		self.is_playing = False
				
	def game_over(self):
		
		mixer.Sound(os.path.join('assets', 'sounds', 'game_over.ogg')).play()

		self.all_monsters = pygame.sprite.Group()
		self.comet_event.all_comets = pygame.sprite.Group()

		self.player.health = self.player.max_health
		self.is_playing = False

	def update(self, screen):
		screen.blit(self.player.image, self.player.rect)

		self.player.update_health_bar(screen)

		#atualiza a barra de eventos
		self.comet_event.update_bar(screen)

		for projectile in self.player.all_projectiles:
			projectile.move()

		for monter in self.all_monsters:
			monter.forward()
			monter.update_health_bar(screen)

		for comet in self.comet_event.all_comets:
			comet.fall()
					
		self.player.all_projectiles.draw(screen)
		self.all_monsters.draw(screen)
		self.comet_event.all_comets.draw(screen)

		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
			self.player.move_right()
		
		elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
			self.player.move_left()


	def check_collision(self, sprit, group):
		# 3o param checks if the entity dies with the collision 
		return pygame.sprite.spritecollide(sprit, group, False, pygame.sprite.collide_mask)

	def generate_monster(self, x=5):

		for i in range(x):
			self.all_monsters.add(Monster(self))