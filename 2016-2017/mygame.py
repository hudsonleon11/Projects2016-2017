# My game.py

#imports
import pygame 
from Hero import Hero 

#functions NADA

#main code
pygame.init()
screen = pygame.display.set_mode((600,400))

pygame.display.get_surface

adam = Hero(200,100,"adam.png")
noey = Hero(-100,100,"noey.png") 
meni = Hero(400,100,"meni.png")

drawlist = [adam,noey,meni]

for hero in drawlist:
	screen.blit(pygame.image.load(hero.imgname),(hero.xcord,hero.ycord))

adam.eatFood()
print (adam.health)
pygame.display.flip() 

keepgoing = True
while keepgoing:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keepgoing = False 
