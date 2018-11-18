#!/usr/bin/python
import pygame
import os
import random
import codecs
#from gi.repository import Gtk

class TextMatchGame:

	def write_file(self, file_path):
		pass

	def read_file(self, file_path):
		pass

	def __init__(self):
		#starting variables
		#self.rect = self.image.get_rect()
		self.hole = 0
		self.birdX = 30
		self.birdY = 625
		#self.bird = pygame.Rect(self.birdX,self.birdY,20,20)
		#self.hole1 = pygame.Rect(0,0,1200,900)
		self.flag = 0	
		self.keyinit = 0
		self.keytest = 0
		self.leftmove = 10	

	def run(self):
		#sound loads
		self.angle = 0
		self.center_x = 0
		self.center_y = 0
		self.sound = True
		self.clock = pygame.time.Clock()	
		self.speed2 = 0
		self.speed = 0
		gravity = 0.1
		button = pygame.image.load("button.png")
		imgRect = button.get_rect()
		imgRect.x = 550
		imgRect.y = 600
		

		opener1 = pygame.image.load("opener.png")
		opener = pygame.transform.scale(opener1, (1200,900))
		bird = pygame.sprite.Sprite()
		bird.image = pygame.image.load("flaps.png")
		bird.transform = pygame.transform.scale(bird.image, (20,20))
		bird.rect = bird.transform.get_rect()
		#gameDisplay = pygame.display.set_mode((1200,900))
		gameDisplay = pygame.display.get_surface()
		land1 = pygame.image.load("land1.0.png")
		land2 = pygame.transform.scale(land1, (1200,900))		
		try:
			pygame.mixer.init()
		except err:
			self.sound = False
			print ('error with sound') 

		self.info = pygame.display.Info()

		self.screen = pygame.display.get_surface()
		
		pygame.display.set_caption("Flappy Golf")
		
		#self.move = pygame.mixer.Sound(" ")
		#self.die = pygame.mixer.Sound(" ")
		#self.win = pygame.mixer.Sound(" ")
		#self.background = pygame.mixer.Sound(" ")
		keeprunning = True
		flg = False	
		#for i in range(1):	
		gameDisplay.blit(opener,(0,0))
		gameDisplay.blit(button,imgRect)
			#pygame.display.update()
		
		while keeprunning:	
			#self.clock.tick(60)
			#while Gtk.events_pending():
				#Gtk.main_iteration()	
			
			self.clock.tick(60)	
			#gameDisplay.blit(opener,(0,0))
			#gameDisplay.blit(button,imgRect)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					keeprunning = False
				
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pos()[0] > 550 and pygame.mouse.get_pos()[1] > 600:
						
						gameDisplay.blit(land2, (0,0))
						flg = True
						#gameDisplay.blit(bird.transform, (self.birdX, self.birdY))
							
						
				elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_LEFT:
							pygame.display.update()	
							if self.birdX >= 260 and self.birdX <= 420 and self.birdY > 750:
								self.speed = 0
								self.birdX = 30
								self.birdY = 625
							if self.birdX >= 761 and self.birdX <= 1010 and self.birdY > 570:
								self.speed = 0
								self.birdX += 5
								self.birdY = 570
							if self.birdY < 600:
								self.birdX -= 30
							if self.birdX >= 100 and self.birdX <= 200 and self.birdY >= 575:
								self.speed = 0
							#gameDisplay.blit(land2, (0,0))	
							#gameDisplay.blit(bird.transform, (self.birdX,self.birdY))
							if self.birdY > 600:
								self.birdX *= 0.8
								#if self.birdX <  200:
									#self.birdX = self.birdX *  0.2
							self.birdY -= 60
							#self.birdY = self.birdY - self.speed 
							#self.speed = self.speed + gravity
							#if self.birdY > 600:
								#self.speed = 0
							gameDisplay.blit(land2, (0,0))	
							#gameDisplay.blit(bird.transform, (self.birdX,self.birdY))
							#pygame.draw.rect(gameDisplay, (0,0,0),(25,658,100,242))
							
							#pygame.display.update()	
									
						elif event.key == pygame.K_RIGHT:
							#pygame.display.update()
							if self.birdX >= 260 and self.birdX <= 420 and self.birdY > 750:
								self.speed = 0
								self.birdX = 30
								self.birdY = 625
							if self.birdX >= 761 and self.birdX <= 1010 and self.birdY > 570:
								self.speed = 0
								self.birdX += 5
								self.birdY = 569	
							self.birdX += 30
							self.birdY -= 60	
							gameDisplay.blit(land2, (0,0))	
							#gameDisplay.blit(bird.transform, (self.birdX,self.birdY))
							#if self.birdX < 600:
								#self.birdX *= 1.5
							#self.birdY -= 60	
			if self.birdY <= 10:
				self.birdY = 30
			elif self.birdX <= 10:
				self.birdX = 50
			elif self.birdX >= 1190:
				self.birdX = 1160
			#pygame.draw.rect(gameDisplay, (0,0,0),(25,658,100,242))
			#gameDisplay.blit(opener, (0,0))
			#gameDisplay.blit(button,imgRect)
			
			#gameDisplay.blit(land2, (0,0))
			#gameDisplay.blit(bird.transform, (self.birdX, self.birdY))
			#gameDisplay.blit(opener, (0,0))
			#gameDisplay.blit(button,imgRect)
			
			self.birdY = self.birdY + self.speed
			self.speed = self.speed + gravity
			if self.birdX >= 20 and self.birdX <= 120 and self.birdY > 625:
				self.speed = 0
			if self.birdX >= 120 and self.birdX <= 250 and self.birdY >= 585:
				self.speed = 0
			if self.birdX >= 260 and self.birdX <= 420 and self.birdY > 750:
				self.speed = 0
			if self.birdX >= 430 and self.birdX <= 575 and self.birdY >= 655:
				self.speed = 0
			if self.birdX >= 580 and self.birdX <= 760  and self.birdY >= 720:
				self.speed = 0
			if self.birdX >= 761 and self.birdX <= 1012 and self.birdY > 570:
				self.speed = 0
			if self.birdX >= 1013 and self.birdX <= 1100 and self.birdY >= 560:
				self.speed = 0
			if self.birdX >= 1100 and self.birdX <= 1200 and self.birdY >= 480:
				self.speed = 0
			
			#if self.birdY > 625:
				#self.speed = 0
			
			#if self.birdY > 625:
				#self.speed = 0
			#gameDisplay.blit(land2, (0,0))		
			if flg == True:
				gameDisplay.blit(land2, (0,0))			
			#pygame.display.flip()
			self.clock.tick(60)
			#gameDisplay.blit(land2, (0,0))		
			gameDisplay.blit(bird.transform, (self.birdX, self.birdY))
			pygame.display.update()
def main():
        pygame.init()
	pygame.display.set_mode((0,0),pygame.RESIZABLE)
	game = TextMatchGame()
	game.run()

if __name__ == '__main__':
	main()
