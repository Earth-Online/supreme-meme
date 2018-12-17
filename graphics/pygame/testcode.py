import pygame
from pygame.locals import *

from setting import*
from constant import *
import widget

class Mygui:
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode(SCREEN_SIZE, 0)
		self.running = True
		self.layers = []
		self.widgets = {}
	
	def main(self):
		rect = widget.Widget((100,100,300,200))
		self.widgets['rect'] = rect
		self.layers.append(rect)

	def one_event(self):
		for e in pygame.event.get():
			if e.type == QUIT:
				self.exit()
			elif e.type == MOUSEMOTION:
				print(self.widgets['rect'].is_over(e.pos))
			print(e)

	def update(self):
		self.screen.fill(grass)
		for layer in self.layers:
			layer.render(self.screen)
		pygame.display.update()

	def mainloop(self):
		self.main()
		while self.running:
			self.update()
			self.clock.tick(FPS)
			self.one_event()

	def exit(self):
		self.running = False
		pygame.quit()

if __name__ == '__main__':
	mygui = Mygui()
	mygui.mainloop()