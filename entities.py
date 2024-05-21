import pygame


class Cone:
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = list(pos)
        self.velocity = 8

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.pos[0] -= self.velocity
        if keys[pygame.K_d]:
            self.pos[0] += self.velocity

        if keys[pygame.K_a]:
            self.pos[0] = self.pos[0]
        if keys[pygame.K_d]:
            self.pos[0] = self.pos[0]

        if self.pos[0] > self.game.screen.get_width():
            self.pos[0] = self.game.screen.get_width() - 30

        if self.pos[0] < self.game.screen.get_width():
            self.pos[0] = -self.game.screen.get_width() + 30

    def render(self, surf):
        surf.blit(self.game.assets['cone'], self.pos)


class Cream:
    def __init__(self):
        print('hi')