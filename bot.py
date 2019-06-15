import pygame
import os

class Bot():
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.vel = 6
        self.walkCount = 0
        self.walkRight = [pygame.image.load(os.path.join('images/',"R1E.png")), pygame.image.load(os.path.join('images/','R2E.png')), pygame.image.load(os.path.join('images/','R3E.png')),
             pygame.image.load(os.path.join('images/','R4E.png')), pygame.image.load(os.path.join('images/','R5E.png')), pygame.image.load(os.path.join('images/','R6E.png')),
             pygame.image.load(os.path.join('images/','R7E.png')), pygame.image.load(os.path.join('images/','R8E.png')), pygame.image.load(os.path.join('images/','R9E.png')),
                          pygame.image.load(os.path.join('images/','R10E.png')), pygame.image.load(os.path.join('images/','R11E.png'))]

        self.walkLeft = [pygame.image.load(os.path.join('images/',"L1E.png")), pygame.image.load(os.path.join('images/','L2E.png')), pygame.image.load(os.path.join('images/','L3E.png')),
             pygame.image.load(os.path.join('images/','L4E.png')), pygame.image.load(os.path.join('images/','L5E.png')), pygame.image.load(os.path.join('images/','L6E.png')),
             pygame.image.load(os.path.join('images/','L7E.png')), pygame.image.load(os.path.join('images/','L8E.png')), pygame.image.load(os.path.join('images/','L9E.png')),
                         pygame.image.load(os.path.join('images/','L10E.png')), pygame.image.load(os.path.join('images/','L11E.png'))]      
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        
    def draw(self, window):       
        self.move()
        if self.visible:  
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 2, 2)
            
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 0.2
        else:
            self.visible = False
            self.x = 900
            self.y = 900
            pygame.display.update()

        
        
            
