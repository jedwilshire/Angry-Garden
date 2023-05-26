import pygame
from colors import *
pygame.font.init()

class Writer:
    def __init__(self, screen, font = 'Arial', size = 12, color = (0, 0, 0)):
        self.screen = screen
        self.font = font
        self.size = size
        self.color = color
        self.text = ''
        self.writer = pygame.font.SysFont(self.font, self.size)
        
    def writeText(self, x, y):
        img = self.writer.render(self.text, True, self.color)
        self.screen.blit(img, (x, y))
        
    def setText(self, text):
        self.text = text
    
    def getText(self):
        return self.text
    
    def setSize(self, size):
        self.size = size
        self.writer = pygame.font.SysFont(self.font, self.size)
    
    def setFont(self, fontName):
        self.font = font
        self.writer = pygame.font.SysFont(self.font, self.size)
    