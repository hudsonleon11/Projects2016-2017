'''
A?
'''

#imports
import pygame

#functions

#main code
pygame.init() #e
pygame.display.set_mode((600,400)) #F?
screen = pygame.display.get_surface() #G

#H?
ballX = 200
ballY = 200

keeprunning = True #I
while keeprunning: #J
	keys = pygame.key.get_pressed()
	
	for event in pygame.event.get():
				
		if event.type == pygame.QUIT: #L
			keeprunning = False #m
		elif event.key == pygame.K_LEFT: #O
				ballX = ballX - 20 # P
		elif event.key == pygame.K_RIGHT: #O
				ballX = ballX + 20 # P
		elif event.key == pygame.K_UP: #O
				ballY = ballY - 20
			elif event.key == pygame.K_DOWN: #O
				ballY = ballY + 20 # P
			elif event.key == pygame.K_ESCAPE:
				keeprunning = False 
	
	
	pygame.Surface.fill(screen,(0,0,0))		
			
	pygame.draw.circle(screen, (220,230,100), (ballX, ballY), 30) #q
	pygame.display.flip() #r

