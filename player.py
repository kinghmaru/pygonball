import pygame
import os

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkRight = [pygame.image.load(os.path.join('images/',"R1.png")), pygame.image.load(os.path.join('images/','R2.png')), pygame.image.load(os.path.join('images/','R3.png')),
             pygame.image.load(os.path.join('images/','R4.png')), pygame.image.load(os.path.join('images/','R5.png')), pygame.image.load(os.path.join('images/','R6.png')),
             pygame.image.load(os.path.join('images/','R7.png')), pygame.image.load(os.path.join('images/','R8.png')), pygame.image.load(os.path.join('images/','R9.png'))]

        self.walkLeft = [pygame.image.load(os.path.join('images/','L1.png')), pygame.image.load(os.path.join('images/','L2.png')), pygame.image.load(os.path.join('images/','L3.png')),
             pygame.image.load(os.path.join('images/','L4.png')), pygame.image.load(os.path.join('images/','L5.png')), pygame.image.load(os.path.join('images/','L6.png')),
             pygame.image.load(os.path.join('images/','L7.png')), pygame.image.load(os.path.join('images/','L8.png')), pygame.image.load(os.path.join('images/','L9.png'))]
        
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        
    def draw(self, window):       
        if self.walkCount + 1 >= 27:
           self.walkCount = 0
           
        if self.left:
            window.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        

    def hit(self, window):
        self.walkCount = 0
        font = pygame.font.SysFont('comicsans', 100)
        text = font.render('-1', 1, (255, 0, 0))
        window.blit(text, (250 - (text.get_width() / 2), 200))
        
        i = 0
        while i < 300:
            #pygame.time.delay(1)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
            
