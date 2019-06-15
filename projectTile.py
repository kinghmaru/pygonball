import pygame
import os

class ProjectTile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 6 * facing

    def draw(self, window):
        ball = pygame.image.load(os.path.join('images/','ball.png'))
        window.blit(ball, (self.x, self.y))
        
    
