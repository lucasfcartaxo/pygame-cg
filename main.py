import pygame 
import sys
import os

from pygame import mixer
from pygame.locals import *
from game import Game

pygame.init()


if __name__ == '__main__':

	fps = 60
	frame = pygame.time.Clock()
	pygame.display.set_caption('Jogo Computação Gráfica')
	screen = pygame.display.set_mode((1080,720))
	background = pygame.image.load(os.path.join('assets', 'bg.jpg'))
	banner = pygame.image.load(os.path.join('assets', 'banner.png'))
	banner = pygame.transform.scale(banner, (500, 500))
	banner_rec = banner.get_rect()
	banner_rec.x = screen.get_width() / 4

	play_button = pygame.image.load(os.path.join('assets', 'button.png'))
	play_button = pygame.transform.scale(play_button, (400,150))
	play_button_rec = play_button.get_rect()
	play_button_rec.x = screen.get_width() / 3.33 # 33%
	play_button_rec.y = screen.get_height() / 2

	game = Game()

	while True:
		
		screen.blit(background, (0, -200))
		
		if game.is_playing:
			game.update(screen)

		else:
			screen.blit(play_button, play_button_rec)
			screen.blit(banner, banner_rec)

		pygame.display.flip()

		for event in pygame.event.get():
			
			if event.type == QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				game.pressed[event.key] = True

				if event.key == K_SPACE:
					mixer.Sound(os.path.join('assets', 'sounds', 'tir.ogg')).play()
					game.player.launch_projectile()
					game.player.animate()

			elif event.type == KEYUP:
				game.pressed[event.key] = False

				if event.key == K_SPACE: 
					mixer.Sound(os.path.join('assets', 'sounds', 'tir.ogg')).play()
					game.player.launch_projectile()
					game.player.animate()

			elif event.type == MOUSEBUTTONDOWN:

				if play_button_rec.collidepoint(event.pos):
					mixer.Sound(os.path.join('assets', 'sounds', 'click.ogg')).play()
					game.is_playing = True
					game.generate_monster(2)

		pygame.display.update()
		frame.tick(fps)
