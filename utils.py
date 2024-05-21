import os
import pygame


def load_image(filename):
    img = pygame.image.load(filename).convert()
    img.set_colorkey((0, 0, 0))
    return img
