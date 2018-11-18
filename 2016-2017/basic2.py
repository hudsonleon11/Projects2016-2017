'''
'''
import pygame

#A
class TestGame:
	
	#B
	def __init__(self,title): #C
		self.ballX = 200
		self.ballY = 200
		self.caption = title
	
	def run(self):
		self.running = True
		
		pygame.display.set_caption(self.caption) 
		screen = pygame.display.get_surface()

		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False  
				elif event.type != pygame.MOUSEBUTTONDOWN:
					self.ballX = pygame.mouse.get_pos()[0]
					self.ballY = pygame.mouse.get_pos()[1]
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.ballX -= 10
			screen.fill((255, 255, 255)) #E
			pygame.draw.circle(screen, (255, 0, 0), (self.ballX, self.ballY), 30)
			pygame.display.flip()

#F
def main():
	pygame.init()
	pygame.display.set_mode((600,400))
	game = TestGame("My basic Pygame") # G
	game.run()	

	mygame = TestGame("me") # G
	mygame.run() # H

#I
if __name__ == '__main__':
	main()
			
