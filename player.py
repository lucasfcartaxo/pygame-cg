import pygame
import os
from time import sleep

from projectile import Projectile

class Player(pygame.sprite.Sprite):

	def __init__(self, game):
		super().__init__()
		self.game			 = game
		self.health 		 = 100
		self.max_health 	 = 100
		self.attack 		 = 20
		self.velocity 		 = 10
		self.all_projectiles = pygame.sprite.Group()
		self.image 			 = pygame.image.load(os.path.join('assets', 'player.png'))
		self.origin_image 	 = self.image
		
		self.rect			 = self.image.get_rect()
		self.rect.x			 = 400
		self.rect.y			 = 500
	
		self.current_image = 0
		self.animate_images	 = self.get_images()

	def animate(self):
				
		self.current_image += 1
		if self.current_image >= len(self.animate_images):
			self.current_image = 0
		self.image = self.animate_images[int(self.current_image)]

	def get_images(self):

		images = []
		for image in os.listdir(os.path.join('assets', 'player')):
			images.append(pygame.image.load(os.path.join('assets', 'player', image)))
		
		return images

	def demage(self, amount):

		if self.health > 0:
			self.health -= amount 

			if self.health <= 0: self.game.game_over()

		else:
			self.game.game_over()

	def update_health_bar(self, surface):
		bar_color = (111, 210, 46)
		back_bar_color = (60, 63, 60)
		bar_position = [self.rect.x + 50, self.rect.y + 15, self.health, 8] # x, y, width, height
		back_bar_position = [self.rect.x + 50, self.rect.y + 15, self.max_health, 8] # x, y, width, height
		
		pygame.draw.rect(surface, back_bar_color, back_bar_position)
		pygame.draw.rect(surface, bar_color, bar_position)

	def launch_projectile(self):
		self.all_projectiles.add(Projectile(self))		

	def move_right(self):

		if not self.game.check_collision(self, self.game.all_monsters):
			self.rect.x += self.velocity

	def move_left(self):
		self.rect.x -= self.velocity