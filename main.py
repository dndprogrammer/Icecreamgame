import pygame
import sys
from pygame.locals import *
from entities import Cone
from utils import load_image


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Ice Cream Game")
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.display = pygame.Surface((self.screen.get_height() * 0.2, self.screen.get_width() * 0.09))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'cone': load_image('ice_cream_cone.png'),
            'cream': load_image('ice_cream.png')
        }

        self.player = Cone(self, (50, 150), (64, 64))

    def run(self):
        while True:
            self.display.fill((255, 255, 255))

            self.player.update()
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()
