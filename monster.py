import pygame
import os

from random import randint

class Monster(pygame.sprite.Sprite):

	def __init__(self, game):
		super().__init__()
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attck = 0.5
		self.image = pygame.image.load(os.path.join('assets', 'mummy.png')) 
		self.rect = self.image.get_rect()
		self.rect.x = 1000 + randint(0, 400)
		self.rect.y = 540
		self.velocity = randint(5, 8)
		self.current_image = 0
		self.animate_images = self.get_images()

	def animate(self):
				
		self.current_image += 0.2
		if self.current_image >= len(self.animate_images):
			self.current_image = 0
		self.image = self.animate_images[int(self.current_image)]

	def get_images(self):

		images = []
		for image in os.listdir(os.path.join('assets', 'mummy')):
			images.append(pygame.image.load(os.path.join('assets', 'mummy', image)))
		
		return images

	def demage(self, amount):
		self.health -= amount

		if self.health <= 0:
			self.rect.x = 1080 + randint(0, 400)
			self.health = self.max_health
			self.velocity = randint(1,3)

			if self.game.comet_event.is_fill_loaded():
				self.game.all_monsters.remove(self)
				self.game.comet_event.attemp_fall()

	def update_health_bar(self, surface):
		bar_color = (111, 210, 46)
		back_bar_color = (60, 63, 60)
		bar_position = [self.rect.x + 10, self.rect.y - 15, self.health, 5] # x, y, width, height
		back_bar_position = [self.rect.x + 10, self.rect.y - 15, self.max_health, 5] # x, y, width, height
		
		pygame.draw.rect(surface, back_bar_color, back_bar_position)
		pygame.draw.rect(surface, bar_color, bar_position)

	def forward(self):
		
		self.animate()
		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity
		else:
			self.game.player.demage(self.attck)