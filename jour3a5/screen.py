import pygame
import sys

class Screen:
    def __init__(self, largeur, hauteur):
        pygame.init()

        self.largeur = largeur
        self.hauteur = hauteur

        self.screen = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("My AppStore")

        self.clock = pygame.time.Clock()

 

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))  

    

            pygame.display.flip()
            self.clock.tick(60) 

        pygame.quit()
        sys.exit()
